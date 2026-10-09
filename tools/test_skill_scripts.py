#!/usr/bin/env python3
"""Behavioural checks for the scripts bundled inside skills.

Usage: python3 tools/test_skill_scripts.py
"""
import os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTIER = ROOT / "dev-workflow/skills/wayfinder/scripts/frontier.py"
SESSION_LOG = ROOT / "dev-workflow/skills/retro/scripts/session_log.py"
HOOK_GIT_VARS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
                 "GIT_PREFIX", "GIT_OBJECT_DIRECTORY")
# Run from a pre-commit hook, these point at the real repo; the temp repos below
# must not inherit them.
for _var in HOOK_GIT_VARS:
    os.environ.pop(_var, None)


def ticket(d, name, status="open", type_="grilling", blocked="[]", claimed=""):
    (d / "tickets" / name).write_text(
        f"---\ntype: {type_}\nstatus: {status}\nclaimed: {claimed}\nblocked_by: {blocked}\n---\n# {name}\n")


class Frontier(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        (self.d / "tickets").mkdir()
        (self.d / "map.md").write_text("# map\n")

    def run_it(self):
        return subprocess.run([sys.executable, FRONTIER, self.d], capture_output=True, text=True)

    def test_picks_first_unblocked_unclaimed(self):
        ticket(self.d, "01-a.md", status="closed")
        ticket(self.d, "02-b.md", blocked="[01]")
        ticket(self.d, "03-c.md", blocked="[02]")
        r = self.run_it()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("next: 02", r.stdout)

    def test_cycle_is_malformed(self):
        ticket(self.d, "01-a.md", blocked="[02]")
        ticket(self.d, "02-b.md", blocked="[01]")
        r = self.run_it()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("cycle", r.stdout)

    def test_unknown_status_is_malformed(self):
        ticket(self.d, "01-a.md", status="Closed")
        r = self.run_it()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("status", r.stdout)

    def test_unknown_type_is_malformed(self):
        ticket(self.d, "01-a.md", type_="spike")
        r = self.run_it()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("type", r.stdout)


class SessionLog(unittest.TestCase):
    def setUp(self):
        self.home = Path(tempfile.mkdtemp())
        self.repo = Path(tempfile.mkdtemp()).resolve()
        subprocess.run(["git", "init", "-q", self.repo], check=True)
        (self.repo / "sub" / "deeper").mkdir(parents=True)
        slug = "".join(c if c.isalnum() else "-" for c in str(self.repo))
        logs = self.home / ".claude" / "projects" / slug
        logs.mkdir(parents=True)
        (logs / "abc-123.jsonl").write_text(
            '{"message":{"role":"user","content":"hello there"}}\n')

    def run_it(self, cwd, *args):
        env = dict(os.environ, HOME=str(self.home))
        return subprocess.run([sys.executable, SESSION_LOG, *args], cwd=cwd,
                              capture_output=True, text=True, env=env)

    def test_list_from_repo_root(self):
        r = self.run_it(self.repo, "list")
        self.assertIn("abc-123", r.stdout, r.stderr)

    def test_list_from_subdirectory_uses_git_root(self):
        r = self.run_it(self.repo / "sub" / "deeper", "list")
        self.assertIn("abc-123", r.stdout, r.stderr)

    def test_rejects_traversal(self):
        r = self.run_it(self.repo, "show", "../other/x")
        self.assertNotEqual(r.returncode, 0)


class HookEnvironment(unittest.TestCase):
    """A pre-commit hook run from a worktree exports GIT_DIR; scripts that
    `git init` a temp repo must not write through it to the real repo."""

    def setUp(self):
        base = Path(tempfile.mkdtemp())
        self.main = base / "main"
        subprocess.run(["git", "init", "-q", self.main], check=True)
        subprocess.run(["git", "-C", self.main, "-c", "user.name=t", "-c", "user.email=t@t",
                        "commit", "-q", "--allow-empty", "-m", "x"], check=True)
        self.wt = base / "wt"
        subprocess.run(["git", "-C", self.main, "worktree", "add", "-q", "--detach", self.wt], check=True)
        self.env = dict(os.environ, GIT_DIR=str(self.main / ".git/worktrees/wt"))

    def bare(self):
        return subprocess.run(["git", "--git-dir", self.main / ".git", "config", "core.bare"],
                              capture_output=True, text=True).stdout.strip()

    def test_wizard_selftest_leaves_repo_config_alone(self):
        subprocess.run(["/bin/bash", ROOT / "tools/wizard-selftest.sh"], cwd=self.wt,
                       env=self.env, capture_output=True)
        self.assertEqual(self.bare(), "false")

    def test_session_log_tests_pass_under_hook_env(self):
        r = subprocess.run([sys.executable, __file__, "SessionLog"], cwd=self.wt,
                           env=self.env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr[-500:])
        self.assertEqual(self.bare(), "false")


if __name__ == "__main__":
    unittest.main(verbosity=1)
