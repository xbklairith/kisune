---
name: scrutinize
description: Outsider-perspective deep review of a plan, PR, design doc, or code change — questions intent first (should this exist?), then traces the actual code path end-to-end to verify the change does what it claims. Use for serious PR reviews, design audits, or second opinions. Lighter pre-commit checks use `review` instead.
allowed-tools: Read, Bash, Grep
---

# Scrutinize

Stand outside the artifact and ask whether it should exist at all — then verify it actually does what it claims, end-to-end.

## Activation Triggers

Activate this skill when:
- User runs `/scrutinize`
- User says "review this PR", "audit this", "sanity check"
- User asks for a "second opinion" or "does this change do what it says"
- User says "review this design doc" or "validate this design"
- User asks "should we ship this?" before a serious merge

For quick pre-commit quality checks, use `review` instead. `scrutinize` is for deeper review where intent and end-to-end correctness are in question.

## Purpose

Apply an outsider perspective — forget who wrote it and why they believe it is right. Question the goal first, then trace the actual execution path through real code to verify every claim. Output is concise, ordered by severity, and every finding carries its rationale and evidence.

## Operating Stance

- **Outsider.** Read the artifact cold. No benefit of the doubt earned by authorship.
- **End-to-end, not diff-local.** The diff is the entry point, not the scope. Follow the call graph through real code paths, including the unchanged code on either side.
- **Actionable, concise, with rationale.** Every finding states what to change, why it matters, and what evidence led there. No filler, no restating the diff back.

## Workflow

Run these steps in order. Do not skip ahead.

### Step 1: Intent — what is this actually trying to do?

State the goal in one sentence, in your own words. If you cannot, the artifact is underspecified — say so and stop.

Then ask: **is there a simpler, smaller, or more elegant way to achieve the same goal?** Consider:
- Doing nothing — is the problem real and load-bearing?
- Using something that already exists in the codebase instead of adding new surface.
- A smaller change that solves 90% of the goal with 10% of the risk.
- Solving it at a different layer (config vs code, framework vs app, build vs runtime).

If a better alternative exists, name it explicitly with rationale before the line-by-line review. This is often the most valuable output.

### Step 2: Trace — walk the actual code path

For each behavior the change claims, trace the path end-to-end through real code — not just the lines in the diff:

- Entry point → call sites → branches taken → state mutated → exit / return / side effect.
- Include the unchanged code on either side of the diff. Bugs hide at the seams.
- For a plan or design doc: trace the proposed flow against the existing system. Where does it touch reality? What does it assume that is not true?

Note every place the trace surprises you — unexpected branch, dead code reached, state you did not know existed. Surprises are signal.

### Step 3: Verify — does it do what it claims?

For each claim the change or plan makes, answer:

- **Does the traced path actually produce that behavior?** Walk it explicitly: "It claims X. Path: A → B → C. At C, [observation]. Therefore [holds / does not hold]."
- **What inputs or states would break it?** Edge cases, concurrent callers, error paths, partial failures, retries, empty/null/huge inputs, ordering assumptions.
- **What does it silently change?** Performance, error semantics, observability, contracts for other callers, on-disk or on-wire formats.
- **How is it tested?** Do the tests actually exercise the traced path, or do they pass while skipping it — mocks that hide the bug, asserts on intermediate state, happy path only?

### Step 4: Report

Output one tight section per finding. Order by severity: blocker → major → nit. For each finding:

- **Finding** — one sentence, specific. Cite `file:line` when applicable.
- **Why it matters** — the consequence, not the principle.
- **Evidence** — the trace step or input that exposes it.
- **Suggested change** — concrete and minimal.

Close with a one-line verdict:

> **ship** / **fix-then-ship** / **rework** / **reject** — [single biggest reason]

**Example output shape:**

> 🔴 **Blocker** — `auth/token.go:84`: refresh token is written before the DB transaction commits; concurrent requests can read a token that will be rolled back. Suggests a two-phase write or write-after-commit.
>
> 🟡 **Major** — `api/user.go:212`: error path returns HTTP 200 with an error body; callers relying on status code will silently succeed.
>
> 🟢 **Nit** — `handler.go:31`: `ctx` is passed but never threaded into the downstream call; cancellation won't propagate.
>
> **fix-then-ship** — token visibility race is a data-integrity bug under concurrent load.

## Operating Rules

- **No rubber-stamps.** If you genuinely find nothing, say what you traced and what you checked so the reviewer can judge whether coverage matched what they cared about.
- **Cite or it did not happen.** Every claim about the code references a specific path, file, or line. No vague "this might break under load."
- **Distinguish claim from verification.** "The PR says X" and "I traced X and confirmed / refuted it" are different — keep them separate in the output.
- **One simpler-alternative pass is mandatory.** Even on small changes, spend one breath asking if the whole thing is necessary. Skip only if the user explicitly says "don't question scope."
- **Don't pad with style nits when there is a structural problem.** If Step 1 or Step 2 surfaces a real issue, lead with it; defer or drop nits.
- **No flattery, no hedging.** "This is a great PR but…" adds nothing. State the finding.

## Integration Points

- For quick pre-commit quality checks: use `review`
- For security-specific vulnerabilities: use `security-review`
- For spec and requirements validation: use `spec-review`
- For the engineering record of a bug this review uncovers: use `post-mortem`
