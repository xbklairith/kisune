#!/usr/bin/env python3
"""Fail when a fact kisune keeps in more than one place has drifted.

kisune keeps ~35 facts by hand: version strings across three manifests, skill
counts in four documents, and the using-kisune index. Doc/index drift has
shipped three times. Each check below must be able to fail -- a guard that
cannot fail is decoration -- so prove it with tools/check-selftest.sh.

Usage: python3 tools/check.py        (exit 1 on any failure)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fails = []


def fail(check, msg):
    fails.append((check, msg))


def skills(plugin):
    d = ROOT / plugin / "skills"
    return {p.name for p in d.iterdir() if p.is_dir()} if d.is_dir() else set()


# --- 1. version strings agree across the three manifests ------------------
def check_versions():
    mk = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    market = {p["name"]: p["version"] for p in mk["plugins"]}
    for name in ("dev-workflow", "trading"):
        own = json.loads((ROOT / name / ".claude-plugin/plugin.json").read_text())["version"]
        if name not in market:
            fail("versions", f"{name} missing from marketplace.json")
        elif market[name] != own:
            fail("versions", f"{name}: plugin.json {own} != marketplace.json {market[name]}")


# --- 2. every written count matches the disk ------------------------------
def check_counts():
    dw, tr = len(skills("dev-workflow")), len(skills("trading"))
    total = dw + tr
    # (file, regex with one capture group, expected int, what it counts)
    rules = [
        ("CLAUDE.md", r"skills/\s+# (\d+) skills \(planning", dw, "dev-workflow skill dirs"),
        ("CLAUDE.md", r"### Dev-Workflow Plugin \((\d+) skills", dw, "dev-workflow skill dirs"),
        ("CLAUDE.md", r"- (\d+) skills, 8 agents, 7 commands, 4 templates", dw, "dev-workflow skill dirs"),
        ("CLAUDE.md", r"- (\d+) skills, 8 agents, 7 commands, 7 templates", total, "all skill dirs"),
        ("PLUGINS_INSTALLATION.md", r"skills/ \((\d+)\)\s+# analyze", tr, "trading skill dirs"),
        ("PLUGINS_INSTALLATION.md", r"skills/ \((\d+)\)\s+# All dev-workflow", dw, "dev-workflow skill dirs"),
        ("dev-workflow/README.md", r"includes (\d+) integrated skills", dw, "dev-workflow skill dirs"),
    ]
    for rel, pat, expected, what in rules:
        f = ROOT / rel
        if not f.is_file():
            fail("counts", f"{rel} missing")
            continue
        m = re.search(pat, f.read_text())
        if not m:
            fail("counts", f"{rel}: no count matching /{pat}/ -- pattern or prose changed")
        elif int(m.group(1)) != expected:
            fail("counts", f"{rel}: says {m.group(1)}, {what} on disk = {expected}")


# --- 3. the index row set EQUALS the skill set, failing by name -----------
def check_index():
    idx_file = ROOT / "dev-workflow/skills/using-kisune/SKILL.md"
    text = idx_file.read_text()
    rows = set(re.findall(r"^\| `([a-z][a-z0-9-]*)`", text, re.M))
    # using-kisune is the index itself and is deliberately not a row in it
    disk = skills("dev-workflow") - {"using-kisune"}
    for name in sorted(disk - rows):
        fail("index", f"skill `{name}` exists on disk with no row in using-kisune")
    for name in sorted(rows - disk):
        fail("index", f"using-kisune has a row for `{name}`, which is not on disk")
    m = re.search(r"Kisune Skill Index \((\d+) skills\)", text)
    if not m:
        fail("index", "using-kisune has no 'Kisune Skill Index (N skills)' header")
    elif int(m.group(1)) != len(rows):
        fail("index", f"index header says {m.group(1)}, table has {len(rows)} rows")


# --- 4. no skill references a skill that does not exist -------------------
def check_references():
    known = skills("dev-workflow") | skills("trading")
    for plugin in ("dev-workflow", "trading"):
        for sk in sorted((ROOT / plugin / "skills").glob("*/SKILL.md")):
            for ref in set(re.findall(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+){1,})`", sk.read_text())):
                # only treat it as a skill reference when it names a real sibling
                # shape; unknown hyphenated words are prose, not broken links
                if ref in known or ref == sk.parent.name:
                    continue
                if ref in STALE_SKILL_NAMES:
                    rel = sk.relative_to(ROOT)
                    fail("references", f"{rel} references removed skill `{ref}`")


# --- 5-10. skill-authoring rules (Anthropic skill best-practices guide) ---
# https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
# description <= 1024 is the API limit; Claude Code allows 1536, but a skill
# that should also work on claude.ai / the API must fit the stricter one.
NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
# A "when" clause: "Use when", "Use for", "Use PROACTIVELY for", "Use after"...
WHEN_RE = re.compile(r"\buse\b(?:\s+\w+)?\s+(?:when|whenever|for|after|before)\b", re.I)


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fields = dict(re.findall(r"^([a-z-]+):[ \t]*(.*)$", m.group(1), re.M))
    return {k: v.strip().strip("\"'") for k, v in fields.items()}, text[m.end():]


def check_skill_authoring():
    for plugin in ("dev-workflow", "trading"):
        for sk in sorted((ROOT / plugin / "skills").glob("*/SKILL.md")):
            rel = sk.relative_to(ROOT)
            fm, body = frontmatter(sk.read_text())
            if fm is None:
                fail("name", f"{rel}: no YAML frontmatter")
                continue
            name, desc = fm.get("name", ""), fm.get("description", "")
            if name != sk.parent.name:
                fail("name", f"{rel}: name `{name}` != directory `{sk.parent.name}`")
            if not NAME_RE.fullmatch(name) or len(name) > 64 or re.search("anthropic|claude", name):
                fail("name", f"{rel}: name `{name}` breaks the rules (lowercase-hyphen, <=64, no reserved words)")
            if not desc or len(desc) > 1024:
                fail("description", f"{rel}: description is {len(desc)} chars (want 1-1024)")
            if re.search(r"<[A-Za-z/][^>]*>", desc):
                fail("description", f"{rel}: description contains an XML/HTML tag")
            if fm.get("disable-model-invocation") != "true" and not WHEN_RE.search(desc):
                fail("when", f"{rel}: description says what, not when (add 'Use when ...')")
            if body.count("\n") >= 500:
                fail("length", f"{rel}: body is {body.count(chr(10))} lines (want < 500; move detail to references/)")
            for link in re.findall(r"\]\(([^)#\s]+\.md)\)", body):
                if "\\" in link:
                    fail("links", f"{rel}: link `{link}` uses a backslash path")
                elif link.count("/") > 1:
                    fail("links", f"{rel}: link `{link}` nests deeper than one level")
            for ref in sorted(sk.parent.rglob("*.md")):
                if ref == sk:
                    continue
                text = ref.read_text()
                if text.count("\n") > 100 and not re.search(r"^#+\s*(table of )?contents\b", text, re.I | re.M):
                    fail("toc", f"{ref.relative_to(ROOT)}: over 100 lines with no Contents heading")


# Names that WERE skills and must never be referenced again.
STALE_SKILL_NAMES = {"explain-in", "management-talk"}


if __name__ == "__main__":
    for fn in (check_versions, check_counts, check_index, check_references, check_skill_authoring):
        fn()
    if fails:
        print(f"FAIL ({len(fails)}):")
        for check, msg in fails:
            print(f"  [{check}] {msg}")
        sys.exit(1)
    print("ok: versions, counts, index, references, skill authoring all consistent")
