---
name: completion-validation
description: Use when about to claim work is complete, fixed, passing, or ready to commit/PR — requires running verification commands and reading fresh output before any success claim. Evidence before assertions, always.
user-invocable: false
---

# Completion Validation

## Overview

Claiming work is complete without verification is dishonesty, not efficiency.

**Core principle:** Evidence before claims, always.

**Violating the letter of this rule is violating the spirit of this rule.** Paraphrases, hedges, and implications of success are all bound by it.

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command in this message, you cannot claim it passes. Previous runs do not count — code may have changed since.

## The Gate Function

Before claiming any status, expressing satisfaction, committing, or moving on:

1. **IDENTIFY** — What command proves this claim?
2. **RUN** — Execute the FULL command (fresh, complete — no `--bail`, no partial scope)
3. **READ** — Full output. Check exit code. Count failures.
4. **VERIFY** — Does the output confirm the claim?
   - If NO: state actual status with evidence
   - If YES: state claim WITH evidence (paste the proof)
5. **ONLY THEN** — Make the claim

Skipping any step = lying, not verifying.

> 🗣 Say: "Running verification… [paste output] — N/N pass, exit 0. Confirmed."

## Common Failures

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Test original symptom: passes | Code changed, assumed fixed |
| Regression test works | Red-green cycle verified | Test passes once |
| Agent completed | VCS diff shows changes | Agent reports "success" |
| Requirements met | Line-by-line checklist | Tests passing |
| Skill works | Pressure test under load | Skill reads correctly |

## Red Flags — STOP

- Using "should", "probably", "seems to", "I think it works"
- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!", "✅")
- About to commit / push / open PR without verification
- Trusting agent success reports without checking diff
- Relying on partial verification (one test file ≠ suite)
- Thinking "just this once"
- Tired and wanting the work over with
- **ANY wording implying success without having run verification this turn**

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Linter passed" | Linter ≠ compiler ≠ tests |
| "Agent said success" | Verify independently via diff |
| "I'm tired" | Exhaustion ≠ excuse |
| "Partial check is enough" | Partial proves nothing about the rest |
| "Different words so rule doesn't apply" | Spirit over letter |
| "Type-check passed, tests will too" | Type-check ≠ runtime behavior |
| "I changed one line, full suite is overkill" | Run it anyway |
| "I lowered [Confidence: 0.7] so I don't need to verify" | Confidence score ≠ evidence. Score reflects certainty about *verified* claims, not a license to skip the run |
| "PM2 process is running, so tests are passing" | Running ≠ done. Read `pm2 logs --nostream` AND exit code |
| "I wrote the User Action doc, the task is done" | Writing instructions ≠ executing them. Status is "pending user action", not "complete" |

## Key Patterns

**Tests:**
```
✅ [Run test command] → [See: 34/34 pass, exit 0] → "All tests pass"
❌ "Should pass now" / "Looks correct" / "Tests passed earlier"
```

**Regression tests (TDD Red-Green):**
```
✅ Write test → Run (pass) → Revert fix → Run (MUST FAIL) → Restore fix → Run (pass)
❌ "I've written a regression test" (without red-green verification — test may pass for unrelated reasons)
```

**Build:**
```
✅ [Run build] → [See: exit 0] → "Build passes"
❌ "Linter passed" (linter doesn't check compilation or runtime)
```

**Requirements (Full mode features):**
```
✅ Re-read requirements.md → Create line-by-line checklist → Verify each → Report gaps OR completion
❌ "Tests pass, phase complete"
```

**Agent delegation:**
```
✅ Agent reports success → Check `git diff` / `git status` → Read changed files → Report actual state
❌ Trust agent report verbatim
```

**UI/frontend changes:**
```
✅ Start dev server → Open browser → Exercise the feature → Check golden path + edge cases
❌ "Type-check passed, frontend works"
```

## Kisune-Specific Patterns

**Status Reporting block (`🔄 Checkpoint Update`):**
Every line is its own claim and needs its own fresh evidence in the same turn.
```
✅ Tests: 48/48 passing      → ran `npm test` this turn, paste output
✅ Type check: No errors     → ran `tsc --noEmit` this turn
✅ Lint: Clean               → ran lint command this turn
💾 Committed: "..."          → ran `git log -1` this turn
```
A status block built from runs scattered across earlier turns is a fabricated report. Re-run before posting.

**Long-running commands under PM2 / `docx/logs/`:**
Per kisune's command-execution convention, anything >30s runs under PM2 or redirects to `docx/logs/`. The verification workflow:
```
1. pm2 list                              → confirm process exited (status: stopped/online?)
2. pm2 logs <name> --nostream --lines N  → read FULL output, not a tail
3. Check exit code (PM2: `pm2 describe <name>` → exit_code field, OR check the log)
4. ONLY THEN claim pass/fail
```
"Process is still running" is NOT a pass. "PM2 says online" is NOT a pass. Wait for completion, read logs, verify exit code.

**Confidence score (`[Confidence: X.X]`):**
The score reflects how certain you are about claims you've already verified. It is NOT a hedge to bypass verification.
```
✅ "Tests pass [output: 48/48, exit 0] [Confidence: 0.95]"
❌ "Should work [Confidence: 0.6]"   ← unverified, score doesn't redeem it
```
If you haven't verified, the honest report is "not verified yet" — not a lower number.

**Full-mode phase gate (Requirements check):**
Before marking any Full-mode phase complete, write the checklist as an artifact, not in your head:
```
✅ Re-open requirements.md → For each EARS requirement, paste the line +
   evidence (test name / file / output) → If any gap, list it explicitly
❌ "I read it, looks covered, moving on"
```
The written checklist is the verification. Skipping the artifact = skipping the gate.

**User Action Tasks (`docx/UserInstructions/*.md`):**
Writing the instruction document IS NOT completing the underlying task. The doc is a hand-off, not a deliverable for the work it describes.
```
✅ "Created docx/UserInstructions/setup-supabase.md.
    Status: pending user action — Supabase is NOT yet configured."
❌ "Supabase is set up." (when only the doc exists)
```

## When To Apply

**ALWAYS before:**
- ANY variation of success / completion claims
- ANY expression of satisfaction
- ANY positive statement about work state
- Committing, opening PR, marking task complete
- Moving to the next task or phase
- Reporting back after delegating to an agent
- Marking a `- [ ]` checkbox in plan.md or tasks.md as `[x]`

**Rule applies to:**
- Exact success phrases
- Paraphrases and synonyms ("looks good", "all set", "ready", "wrapped up")
- Implications of success
- ANY communication suggesting completion or correctness
- **Silent handoffs**: ending a turn without an explicit "not yet verified" qualifier counts as a claim. If you haven't verified, say so out loud.

## Integration With Other Kisune Skills

- **`spec-driven-implementation`** — Each task's `Verify` step IS this skill in action. Run the exact command, paste the output, only then check the box.
- **`test-driven-development`** — RED phase verification: confirm the test FAILS for the right reason before writing code. GREEN phase: confirm the test passes by running it, not by reading the diff.
- **`git-workflow`** — Before any commit, the working state must be verified. No "commit then run tests".
- **`review`** — Reviewer claims like "no security issues" require evidence (grep output, scan results), not assertion.

## Why This Matters

False completion claims cost more time than verification ever would:
- The user catches the lie → trust broken, work redone under suspicion
- The lie ships → broken code in production, regression in main
- "Tests pass" with stale output → real failures hidden until the next change blames itself
- Agent reports trusted blindly → silent regressions because no one read the diff

Honesty is non-negotiable. A 30-second verification beats an hour of unwinding a false claim.

## The Bottom Line

**No shortcuts for verification.**

Run the command. Read the output. THEN claim the result.

This is non-negotiable.
