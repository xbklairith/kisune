---
name: post-mortem
description: Write the canonical engineering record of a fixed bug — root cause, mechanism, fix, validation, and how it slipped through. Use after a debug session lands a validated fix, before closing the bug.
allowed-tools: Read, Write
---

# Post-mortem

## Activation Triggers

- `/post-mortem`
- "write the post-mortem" / "postmortem" / "RCA" / "root cause analysis"
- "document this fix" / "write up the root cause" / "close out this bug"
- After `systematic-debug` lands a validated fix — proactively offer to draft one.

## Purpose

The canonical engineering record of a bug fix. Written after debugging lands a real fix, for other engineers and future-you who will have forgotten everything in six months. Code identifiers are welcome — this is the artifact that lets the next person recover the mental model fast.

For the leadership-facing version of this content, hand the finished post-mortem to `explain-in`. Post-mortem owns the engineering truth; `explain-in` reframes it for stakeholders.

## When NOT to Use

- **Bug not fixed or fix not validated.** A post-mortem of a hypothesis is misleading. Refuse, list what's missing, and stop.
- **Customer-visible outage or incident.** Those need a separate incident report covering timeline, blast radius, paging history, and comms. This skill is bug-fix scope. Flag and confirm before proceeding.
- **Trivial one-liner fix.** The PR description is the record. Don't manufacture ceremony.

## Required Inputs Gate

Before writing a single line, confirm all four. If any are missing, list them and stop — do not draft:

- [ ] **Reliable repro** — deterministic or high-rate-flake; the next person can run it.
- [ ] **Root cause known** — the mechanism is identified, not a hypothesis.
- [ ] **Fix identified** — PR, commit, or branch pointer exists.
- [ ] **Fix validated** — the original repro now passes; the failing test or workload now succeeds.

`systematic-debug`'s breadcrumb ledger is the raw material for all four. Pull from it.

## Structure

Use these sections in this order. **Summary, Root cause, Fix, and Validation are mandatory.** The rest are conditional but usually present.

### 1. Summary _(mandatory)_

One paragraph. What broke in user or workload terms. What fixed it in one sentence. Issue ID (if any), PR number, owner. A reader who stops here should have the right answer.

### 2. Symptom

What was actually observed — test output, error message, log line, perf number, customer report. Concrete identifiers; don't paraphrase the failure mode.

### 3. Root cause _(mandatory)_

The actual bug mechanism. Code identifiers are expected: function names, file paths, struct fields, branch conditions, commit SHAs. Walk the cause chain end-to-end. This is the most expensive section and the reason the post-mortem exists. Future-you will live or die by how clearly this is written.

### 4. Why it produced the symptom

Link root cause to symptom. Often non-obvious — the bug is in one function but the visible failure surfaces hours later in a different layer. Walk the chain so a reader who only knows the symptom can connect it back to the cause without re-deriving it.

### 5. Fix _(mandatory)_

What changed and why it addresses the root cause rather than hiding the symptom. Link to PR or commit. If a prior fix attempt papered over the symptom, name it and explain what was wrong with it — that history is part of the cause.

### 6. How it was found

Short. The debugging path: what made the repro deterministic, which tools cracked it, hypotheses tried and rejected with a one-line reason each, and the single experiment that confirmed the cause. (Pull from the `systematic-debug` breadcrumb ledger.) Write it for the next debugger — make it learnable.

### 7. Why it slipped through

What allowed this bug to reach the branch, release, or customer. Pick the real reason:

- **CI gap** — no test exercises this path or configuration.
- **Latent code** — correct when written, broken by a later change in a different file.
- **Workload gap** — no real workload reached this code path until now.
- **Incomplete prior fix** — a defensive check hid the symptom; root cause was untouched.
- **Review miss** — the change was reviewable; the implication wasn't.

If the honest answer is "no good reason — this should have been caught," say so. Blameless: describe the gap, not the person.

### 8. Validation _(mandatory)_

How we know the fix works. Concrete: test names, run links, configs tested, perf numbers before and after. If you only validated one configuration, say so explicitly — "validated on X; not retested on other workloads." Don't imply broader coverage than you have.

### 9. Action items

Concrete next steps not already in the fix PR. Each item: what + owner + tracking artifact.

If there are no action items, write: *"None — the fix is sufficient and no class-of-bug follow-up is warranted."* Don't manufacture action items to look thorough.

## Tone

Engineer-to-engineer. Different from `explain-in`:

- **Code identifiers are first-class.** Function names, file paths, commit SHAs, line numbers — keep them. The point is that future engineers can grep their way back to the change.
- **Mechanism over narrative.** Walk the actual cause chain. Don't soften "a synchronization issue" — name which function skipped which event under which gate.
- **Active voice, short paragraphs.** No padding.
- **No hedging.** Drop "we believe" / "appears to" / "may have." State it or don't write it.
- **Blameless.** Describe the bug, the gap, and the fix. Never "X should have caught this."
- **No advocacy.** A post-mortem records what happened and what's next. Arguments for a broader refactor go in a separate proposal — link to it from action items.

## Output Flow

1. Confirm all four required inputs are satisfied. If any are missing, list them and stop.
2. Confirm destination (default: `docx/postmortems/<bug-name>.md`). Other valid targets: issue tracker comment (JIRA, GitHub Issues, Linear), PR description, internal wiki. Shape is the same — only the wrapping changes.
3. Produce the draft as a single block.
4. For issue tracker back-post (JIRA, GitHub Issues, Linear): show the exact payload, wait for explicit "post it" / "go ahead" / "yes," then post. Print-only output needs no approval.
5. Offer the handoff: *"Want a leadership-friendly version? I can hand this to `explain-in`."* Don't do it automatically.

## Worked Example — Partial (JIRA-12345)

> **Summary.** Tada's single-stream fast-path skipped a required cross-stream synchronization, causing kernels to launch before scratch-buffer writes were visible. Triggered reliably by dumbModel on LLM-7B fine-tuning, hanging the workload at every eval step. Fixed by removing the unsafe fast-path and adding a device-side null check. JIRA-12345, PR org/platform#5751, owner Alex (Tada team).
>
> **Root cause.** The single-stream fast-path in `tadaLaunchPrepare` / `tadaLaunchKernel` / `tadaLaunchFinish` (gated on `scheduler->numStreams == 1 && !plan->persistent`) skipped the cross-stream event between `launchStream` and `handle->shared->deviceStream`. dumbModel hits this gate exactly. The kernel launched before IPC publish / scratch-buffer writes on `deviceStream` populated `scratchBuf`. In the kernel: `scratchBuf == NULL` → stray pointer dereference → ring ready-flag read from garbage memory → thread spins forever waiting for a signal that will never arrive.

What the engineering record does that a management summary doesn't: names every code identifier, walks the cause chain to the exact gate, calls out the prior failed fix attempt by PR number, and states validation coverage honestly.

## Rules

- **Refuse to draft without all four required inputs.** A post-mortem of a hypothesis is worse than no post-mortem.
- **Never invent root cause, owner, validation runs, or action items.** If a section's facts aren't there, ask. Don't fill the gap with plausible prose.
- **Never strip code identifiers.** They are the index. Reframing for leadership is `explain-in`'s job.
- **Blameless.** Gaps and bugs, never people.
- **State validation coverage honestly.** Implying broader coverage than you have is the failure mode that breeds repeat regressions.
- **Get sign-off before posting to any issue tracker.** Print-only output needs no approval.
