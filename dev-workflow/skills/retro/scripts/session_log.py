#!/usr/bin/env python3
"""Read Claude Code session logs for ONE project: the current one.

Logs live at ~/.claude/projects/<slug>/<session-id>.jsonl, where <slug> is the
project's absolute path with every non-alphanumeric character replaced by '-'.
This script derives <slug> from --project (default: the git root of cwd, else
cwd) and never lists any other project's directory: those logs are private
chats from unrelated work. It never walks up parent directories, since a
parent such as $HOME can be a different project.

Usage:
  session_log.py list                [--project DIR]
  session_log.py show SESSION_ID     [--project DIR] [--full]
  session_log.py show latest         [--project DIR]

`show` prints the session as a numbered timeline of tool calls, flags failed
tool results, and ends with a summary: files read more than once, commands
run more than once, and the first edit relative to the first command.
"""
import argparse, json, re, subprocess, sys
from collections import Counter
from pathlib import Path


def project_root(project):
    if project:
        return Path(project)
    r = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                       capture_output=True, text=True)
    return Path(r.stdout.strip()) if r.returncode == 0 else Path.cwd()


def log_dir(project):
    slug = re.sub(r"[^A-Za-z0-9]", "-", str(Path(project).resolve()))
    return Path.home() / ".claude" / "projects" / slug


def sessions(d):
    return sorted(d.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)


def records(path):
    for line in path.open():
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def first_prompt(path):
    for r in records(path):
        m = r.get("message", {})
        if m.get("role") == "user":
            c = m.get("content")
            text = c if isinstance(c, str) else next(
                (b.get("text", "") for b in c if b.get("type") == "text"), "")
            if text and not text.startswith("<"):
                return " ".join(text.split())[:90]
    return ""


def brief(name, inp):
    for k in ("command", "file_path", "pattern", "path", "url", "query", "skill"):
        if k in inp:
            return " ".join(str(inp[k]).split())[:140]
    return json.dumps(inp)[:140]


def show(path, full):
    n, first_edit, first_cmd = 0, None, None
    reads, cmds = Counter(), Counter()
    for r in records(path):
        m = r.get("message", {})
        content = m.get("content")
        if not isinstance(content, list):
            continue
        for b in content:
            if m.get("role") == "assistant" and b.get("type") == "tool_use":
                n += 1
                name, inp = b["name"], b.get("input", {})
                arg = brief(name, inp)
                print(f"{n:4} {name:10} {arg}")
                if name == "Read":
                    reads[inp.get("file_path")] += 1
                if name == "Bash":
                    cmds[inp.get("command", "").strip()] += 1
                    first_cmd = first_cmd or n
                if name in ("Edit", "Write", "NotebookEdit"):
                    first_edit = first_edit or n
            elif m.get("role") == "assistant" and b.get("type") == "text" and full:
                print("     » " + " ".join(b["text"].split())[:300])
            elif b.get("type") == "tool_result" and b.get("is_error"):
                c = b.get("content")
                c = c if isinstance(c, str) else json.dumps(c)
                print("     ✗ " + " ".join(c.split())[:200])
    print("\n-- summary --")
    print(f"tool calls: {n}; first Bash at #{first_cmd}; first Edit/Write at #{first_edit}")
    for f, k in reads.items():
        if k > 1:
            print(f"read {k}x: {f}")
    for c, k in cmds.items():
        if k > 1:
            print(f"ran {k}x: {c[:120]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["list", "show"])
    ap.add_argument("session", nargs="?")
    ap.add_argument("--project", help="project root (default: git root of cwd)")
    ap.add_argument("--full", action="store_true", help="include assistant text")
    a = ap.parse_args()
    d = log_dir(project_root(a.project))
    if not d.is_dir():
        sys.exit(f"no session logs for this project at {d}")
    found = sessions(d)
    if a.action == "list":
        for p in found[:30]:
            print(f"{p.stem}  {p.stat().st_size // 1024:6}K  {first_prompt(p)}")
        return
    if not a.session:
        sys.exit("show needs a SESSION_ID or 'latest'")
    if a.session != "latest" and not re.fullmatch(r"[A-Za-z0-9-]+", a.session):
        sys.exit("SESSION_ID is the file stem shown by `list`")
    path = found[0] if a.session == "latest" else d / f"{a.session}.jsonl"
    if not path.is_file():
        sys.exit(f"{path.name} is not a session of this project")
    show(path, a.full)


if __name__ == "__main__":
    main()
