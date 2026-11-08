#!/usr/bin/env python3
"""Regex eval graders, run against pages written to pass or fail them.

The eval runner grades with JavaScript regexes, so each pattern runs under
node and bun (whichever are installed), not Python's re.

Usage: python3 tools/test_eval_graders.py
"""
import json, re, shutil, subprocess, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "dev-workflow/evals"
RUNTIMES = [r for r in ("node", "bun") if shutil.which(r)]
JS = ("const {pattern, flags, texts} = JSON.parse(require('fs').readFileSync(0, 'utf8'));"
      "const re = new RegExp(pattern, flags);"
      "process.stdout.write(JSON.stringify(texts.map(t => re.test(t))));")


def grader(rel):
    """Pattern, flags and match mode of a regex grader file."""
    text = (EVALS / rel).read_text()
    pattern = re.search(r"^pattern: '((?:[^']|'')*)'$", text, re.M).group(1).replace("''", "'")
    flags = re.search(r"^flags: (\w*)$", text, re.M)
    match = re.search(r"^match: (\S+)$", text, re.M)
    return pattern, flags.group(1) if flags else "", match.group(1) if match else "contains"


def passes(rel, texts):
    """Whether each text passes the grader, per installed runtime."""
    pattern, flags, match = grader(rel)
    out = {}
    for rt in RUNTIMES:
        r = subprocess.run([rt, "-e", JS], input=json.dumps({"pattern": pattern, "flags": flags, "texts": texts}),
                           capture_output=True, text=True, check=True)
        hits = json.loads(r.stdout)
        out[rt] = [not h if match == "not_contains" else h for h in hits]
    return out


def page(head="", body=""):
    return f"<!DOCTYPE html>\n<html>\n<head>\n<title>Order status</title>\n{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n"


MERMAID = "<pre class=\"mermaid\">\nstateDiagram-v2\n  [*] --> pending\n  pending --> paid: pay\n</pre>"
PINNED = "<script src=\"https://cdn.jsdelivr.net/npm/mermaid@11.16.1/dist/mermaid.min.js\"></script>"
SVG = ("<figure><svg viewBox=\"0 0 200 60\" role=\"img\" aria-label=\"pending to paid\">"
       "<rect x=\"4\" y=\"4\" width=\"60\" height=\"30\" fill=\"none\" stroke=\"currentColor\"/></svg>"
       "<figcaption>Read it like a flowchart LR: left to right.</figcaption></figure>\n<p>graph TD would stack it.</p>")


@unittest.skipUnless(RUNTIMES, "needs node or bun")
class DiagramRenders(unittest.TestCase):
    rels = ("explain-diagram/graders/diagram-renders.md", "explain-mermaid/graders/diagram-renders.md")

    def check(self, texts, want):
        for rel in self.rels:
            for rt, got in passes(rel, texts).items():
                self.assertEqual(got, [want] * len(texts), f"{rel} under {rt}")

    def test_mermaid_without_a_loader_fails(self):
        self.check([
            page(body=MERMAID),
            page(body=MERMAID.replace('class="mermaid"', "class='diagram mermaid'")),
            page(body="<pre>\nstateDiagram-v2\n  pending --> paid\n</pre>"),
            page(body="<pre>\n  flowchart LR\n  a --> b\n</pre>"),
        ], False)

    def test_unpinned_or_unlisted_loader_fails(self):
        self.check([
            page(PINNED.replace("@11.16.1", "@11"), MERMAID),
            page(PINNED.replace("mermaid@11.16.1", "mermaid"), MERMAID),
            page("<script src=\"mermaid.min.js\"></script>", MERMAID),
        ], False)

    def test_pinned_loader_passes(self):
        self.check([
            page(PINNED, MERMAID),
            page(body=MERMAID + "\n<script type=\"module\">\nimport mermaid from "
                 "'https://cdn.jsdelivr.net/npm/mermaid@11.16.1/dist/mermaid.esm.min.mjs';\n"
                 "mermaid.initialize({startOnLoad: true});\n</script>"),
            page("<script src=\"https://unpkg.com/mermaid@11.16.1/dist/mermaid.min.js\"></script>", MERMAID),
        ], True)

    def test_inline_svg_passes_even_when_prose_names_a_diagram(self):
        self.check([page(body=SVG), page(body="<table><tr><td>pending</td></tr></table>")], True)


def call(msg, *names):
    """One trace line: an assistant message carrying the named tool calls."""
    blocks = [{"type": "tool_use", "id": f"toolu_{msg}{i}", "name": n, "input": {}} for i, n in enumerate(names)]
    return json.dumps({"type": "assistant", "message": {"model": "m", "id": f"msg_{msg}", "type": "message",
                                                        "role": "assistant", "content": blocks}},
                      separators=(",", ":"))  # the trace's own compact form


RESULT = json.dumps({"type": "user", "message": {"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": "toolu_x", "content": "done"}]}})


@unittest.skipUnless(RUNTIMES, "needs node or bun")
class AgentsBatched(unittest.TestCase):
    rel = "spawn-three-bugs/graders/agents-batched.md"

    def check(self, traces, want):
        for rt, got in passes(self.rel, ["\n".join(t) + "\n" for t in traces]).items():
            self.assertEqual(got, [want] * len(traces), rt)

    def test_agent_calls_in_one_message_pass(self):
        self.check([
            [call("A1", "Skill"), call("A2", "Agent"), call("A2", "Agent"), call("A2", "Agent"), RESULT],
            [call("A1", "Agent", "Agent")],
            [call("A1", "Read"), RESULT, call("A2", "Task"), call("A2", "Task")],
        ], True)

    def test_agent_calls_across_messages_fail(self):
        self.check([
            [call("A1", "Agent"), RESULT, call("A2", "Agent"), RESULT, call("A3", "Agent")],
            [call("A1", "Agent"), call("A1", "Read")],
            [call("A1", "Read"), call("A1", "Grep")],
        ], False)


@unittest.skipUnless(RUNTIMES, "needs node or bun")
class RootCauses(unittest.TestCase):
    rel = "spawn-three-bugs/graders/root-causes.md"
    ALL = ("1. Billing: `should_retry` checks `attempt < MAX_ATTEMPTS - 1`, so it stops one short.\n"
           "2. Search: `search()` never lowercases the query, so the P is dropped.\n"
           "3. Auth: `ttl_seconds()` returns `SESSION_TTL.seconds // 60`, which is 30, not 1800.")

    def check(self, texts, want):
        for rt, got in passes(self.rel, texts).items():
            self.assertEqual(got, [want] * len(texts), rt)

    def test_all_three_causes_pass(self):
        self.check([self.ALL, self.ALL.upper()], True)

    def test_a_missing_cause_fails(self):
        lines = self.ALL.split("\n")
        self.check(["\n".join(lines[:i] + lines[i + 1:]) for i in range(3)], False)


def forked(skill, text):
    """One trace line: the result a forked skill hands back to the main session."""
    body = (f"<tools-used-before-summary>Agent, Read</tools-used-before-summary>\n"
            f"Skill \"{skill}\" completed (forked execution).\n\nResult:\n{text}")
    return json.dumps({"type": "user", "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "toolu_s", "content": body}]}}, separators=(",", ":"))


def agent(desc):
    """One trace line: an Agent call with a description."""
    return json.dumps({"type": "assistant", "message": {"id": "msg_a", "content": [
        {"type": "tool_use", "id": "toolu_a", "name": "Agent",
         "input": {"description": desc, "prompt": "Review the plan."}}]}}, separators=(",", ":"))


@unittest.skipUnless(RUNTIMES, "needs node or bun")
class SpecReviewReport(unittest.TestCase):
    rel = "spec-review-quick/graders/report.md"
    REPORT = ("# Spec Review: 01-version\n**Mode:** Quick  **Date:** 2026-11-08\n\n## Verdict: PASS ✅\n\n"
              "## 1. Spec Quality [PASS]\n## 2. Completeness [PASS]\n")

    def check(self, traces, want):
        for rt, got in passes(self.rel, ["\n".join(t) + "\n" for t in traces]).items():
            self.assertEqual(got, [want] * len(traces), rt)

    def test_forked_report_passes(self):
        self.check([
            [agent("Spec Quality review"), forked("dev-workflow:spec-review", self.REPORT)],
            [forked("spec-review", self.REPORT.replace("✅", ""))],
        ], True)

    def test_agent_descriptions_alone_fail(self):
        self.check([
            [agent("Spec Quality review"), agent("Completeness review")],
            [forked("dev-workflow:spec-review", "Spec Quality and Completeness reviewed; no report.")],
            [forked("dev-workflow:review", self.REPORT)],
        ], False)


if __name__ == "__main__":
    unittest.main()
