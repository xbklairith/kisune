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


# Names that WERE skills and must never be referenced again.
STALE_SKILL_NAMES = {"explain-in", "management-talk"}


if __name__ == "__main__":
    for fn in (check_versions, check_counts, check_index, check_references):
        fn()
    if fails:
        print(f"FAIL ({len(fails)}):")
        for check, msg in fails:
            print(f"  [{check}] {msg}")
        sys.exit(1)
    print("ok: versions, counts, index, references all consistent")
