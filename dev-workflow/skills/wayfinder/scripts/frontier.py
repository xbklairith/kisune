#!/usr/bin/env python3
"""Answer "where is this effort, and what is next?" from a wayfinder map.

A map is a directory: map.md plus tickets/NN-slug.md. Each ticket starts with
frontmatter:

    ---
    type: grilling | research | prototype | task
    status: open | closed
    claimed: <who> | (empty)
    blocked_by: [03, 05]        # ticket numbers; may be empty
    ---
    # <Title>

Usage: frontier.py docx/wayfinder/<effort>
Prints closed, claimed, blocked and frontier tickets. The frontier is every
open, unclaimed ticket whose blockers are all closed, in number order.
Exit 1 if the map is malformed: missing fields, a status or type outside the
lists above, unknown blocker numbers, or blockers that form a cycle.
"""
import re, sys

TYPES = {"grilling", "research", "prototype", "task"}
STATUSES = {"open", "closed"}
from pathlib import Path


def parse(p):
    text = p.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError(f"{p.name}: no frontmatter")
    meta = dict(re.findall(r"^(\w+):[ \t]*(.*)$", m.group(1), re.M))
    for k in ("type", "status"):
        if k not in meta:
            raise ValueError(f"{p.name}: missing {k}")
    if meta["type"].strip() not in TYPES:
        raise ValueError(f"{p.name}: type {meta['type'].strip()!r} not one of {sorted(TYPES)}")
    if meta["status"].strip() not in STATUSES:
        raise ValueError(f"{p.name}: status {meta['status'].strip()!r} not one of {sorted(STATUSES)}")
    title = re.search(r"^# (.+)$", text[m.end():], re.M)
    num = re.match(r"(\d+)", p.name)
    if not num:
        raise ValueError(f"{p.name}: filename must start with its number")
    return {
        "num": int(num.group(1)), "file": p.name,
        "title": title.group(1).strip() if title else p.stem,
        "type": meta["type"].strip(), "status": meta["status"].strip(),
        "claimed": meta.get("claimed", "").strip(),
        "blocked_by": [int(x) for x in re.findall(r"\d+", meta.get("blocked_by", ""))],
    }


def find_cycle(by):
    """Return one blocker cycle as a list of ticket numbers, or None."""
    state = {}  # 1 = on the current path, 2 = done

    def visit(n, path):
        state[n] = 1
        for b in by[n]["blocked_by"]:
            if state.get(b) == 1:
                return path[path.index(b):] + [b]
            if b not in state:
                found = visit(b, path + [b])
                if found:
                    return found
        state[n] = 2
        return None

    for n in by:
        if n not in state:
            found = visit(n, [n])
            if found:
                return found
    return None


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1])
    if not (root / "map.md").is_file():
        sys.exit(f"{root}/map.md not found")
    try:
        ts = sorted((parse(p) for p in (root / "tickets").glob("*.md")), key=lambda t: t["num"])
    except ValueError as e:
        print(f"malformed: {e}"); sys.exit(1)
    by = {t["num"]: t for t in ts}
    bad = [(t["num"], b) for t in ts for b in t["blocked_by"] if b not in by]
    if bad:
        print("malformed: unknown blockers " + ", ".join(f"{a}<-{b}" for a, b in bad)); sys.exit(1)
    cycle = find_cycle(by)
    if cycle:
        print("malformed: cycle " + "→".join(f"{n:02}" for n in cycle)); sys.exit(1)
    groups = {"closed": [], "claimed": [], "blocked": [], "frontier": []}
    for t in ts:
        if t["status"] == "closed":
            groups["closed"].append(t)
        elif t["claimed"]:
            groups["claimed"].append(t)
        elif any(by[b]["status"] != "closed" for b in t["blocked_by"]):
            groups["blocked"].append(t)
        else:
            groups["frontier"].append(t)
    for g, items in groups.items():
        print(f"{g} ({len(items)})")
        for t in items:
            extra = f" — {t['claimed']}" if g == "claimed" else (
                f" — waits on {', '.join(str(b) for b in t['blocked_by'] if by[b]['status'] != 'closed')}" if g == "blocked" else "")
            print(f"  {t['num']:02} [{t['type']}] {t['title']}{extra}")
    if groups["frontier"]:
        n = groups["frontier"][0]
        print(f"\nnext: {n['num']:02} {n['title']} ({n['file']})")
    elif not groups["claimed"] and not groups["blocked"]:
        print("\nno open tickets: check map.md 'Not yet specified' for fog to graduate, or the way is clear")


if __name__ == "__main__":
    main()
