---
name: spec-driven-implementation
description: Execute spec-driven implementation — auto-detects Quick (plan.md) or Full (tasks.md) mode and runs step-by-step with verification. Use when implementing a planned feature or running TDD tasks.
allowed-tools: Read, Write, Edit, Bash
---

# Spec-Driven Implementation Skill

## Purpose

Execute the planning artifacts produced by `spec-driven-planning`. The skill auto-detects which mode the feature is in and runs the matching playbook:

- **Quick mode** (`plan.md` exists) — follow bite-sized steps, run verification commands, commit. **No RED-GREEN-REFACTOR.** Tests welcome but not mandated.
- **Full mode** (`tasks.md` exists) — strict TDD per task: RED → GREEN → REFACTOR, traceability to REQ-### IDs, quality gates between tasks.

## Activation Triggers

- User says "implement this feature", "let's code this", "execute the plan"
- User mentions "tasks", "TDD", or "execution"
- User uses `/dev-workflow:spec` with `tasks` or `execute`
- Planning phase is complete

---

## Mode Detection (DO THIS FIRST)

Before doing anything, find the active feature folder and detect mode:

```
1. ls docx/features/  →  pick most recent or user-named feature
2. Inside docx/features/[NN-name]/, look for:
   - plan.md only                          → QUICK MODE
   - tasks.md only                         → FULL MODE
   - tasks.md + plan.archived.md           → FULL MODE (post-upgrade; archive is informational, ignored for routing)
   - plan.md + tasks.md (no archive)       → STOP AND ASK: ambiguous state.
                                              Likely a hand-conversion in progress.
                                              Ask user which file is authoritative.
                                              Do NOT auto-pick — risk of clobbering.
   - neither                               → ERROR: "No plan/spec found. Run /dev-workflow:spec first."
```

`plan.archived.md` is informational only and never affects mode detection — a clean post-upgrade state has `tasks.md` + `plan.archived.md` and routes to Full.

**Announce the mode:**
> "Detected [Quick/Full] mode from `docx/features/[NN-name]/[plan.md|tasks.md]`. Running [Quick/Full] execution."

Then run the matching section below.

---

## Quick Mode Execution

**Source:** `docx/features/[NN-name]/plan.md`

**Philosophy:** Behavior-based verification, not test-suite-based. The plan already tells you exactly what to do.

### Pre-flight

1. Read `plan.md` end-to-end
2. Review critically — raise concerns BEFORE starting:
   - Are file paths real? (sample-check 1-2 with Read)
   - Do the steps actually solve the Goal?
   - Are there obvious gaps?
3. If concerns: surface them to the user, wait for guidance
4. If clean: proceed

### Per-task loop

For each task in the plan:

1. **Mark task as in-progress** — Edit the Progress section: `- [ ] Task N` → `- [→] Task N`
2. **For each step in the task** (steps are themselves checkboxes `- [ ]` in the template):
   - Execute the action (write code from the plan, run the command, etc.)
   - Run the verification command shown in the plan
   - Compare actual output to "Expected:" — if mismatch, **stop and ask**, don't guess
   - **Edit `plan.md`** to flip the step's `- [ ]` → `- [x]` immediately after completing it
3. **Commit** using the message from the plan (the commit step itself is one of the checkboxed steps)
4. **Mark task complete** — Edit the Progress section: `- [→] Task N` → `- [x] Task N`

### Quick mode rules

- **No RED-GREEN-REFACTOR enforcement.** If the plan lists a test step, do it. If not, don't invent one.
- **Opting into TDD per-task is allowed.** If a specific task warrants a test, the plan author adds an explicit test step (e.g., "1. Write failing test in `tests/foo.test.ts` ... 2. Verify: `npm test foo` → expect FAIL"). Execute it as ordinary verification. No test step in the plan = no test required.
- **Don't expand scope.** The plan is the contract. New ideas → tell the user, don't silently add tasks.
- **Use Edit on `plan.md`**, don't just announce progress. Mark step-level checkboxes (`- [ ]` → `- [x]`) as you complete each numbered step within a task — this preserves resumability if interrupted mid-task.
- **Stop when blocked.** Failing verification, missing file, ambiguous step → ask.
- **No quality gate between tasks** beyond what the plan specifies. (Optionally invoke `dev-workflow:review` before commits if the user requested it.)

### Quick mode completion

When all tasks are `[x]`:

1. Update `Status:` line in `plan.md` to `Complete`
2. Run any final verification listed in the plan
3. Report:

```
Quick implementation complete: [Feature Name]

- Tasks: N/N
- Commits: M
- Files changed: K

Plan: docx/features/[NN-name]/plan.md
Ready for PR or further work?
```

---

## Full Mode Execution

**Source:** `docx/features/[NN-name]/{requirements.md, design.md, tasks.md}`

### Prerequisites Check

- [ ] `requirements.md` complete (EARS, REQ-### IDs)
- [ ] `design.md` complete and approved
- [ ] `tasks.md` exists (Phase 4 done) OR run Phase 4 below

If `tasks.md` is empty/missing, run Phase 4 first.

---

### Pre-flight Review (before Phase 4)

Before breaking design into tasks or executing existing tasks, critically review the planning artifacts:

1. **Are referenced file paths real?** Sample-check 1-2 paths from `design.md` with Read. Hallucinated paths are a strong signal the design wasn't grounded in the actual codebase.
2. **Do the requirements actually match what the user asked for?** Re-read the original request and check `requirements.md` for drift.
3. **Does the design solve the requirements?** Each REQ-### should map to at least one design component.
4. **Are there obvious gaps?** Missing error handling, undefined interfaces, hand-waved sections.

If concerns: STOP. Surface them to the user BEFORE writing tasks or code. Don't push through hoping it'll work out.

> 🗣 Say: "Pre-flight: [N concerns found / clean — proceeding to Phase 4]."

---

### Phase 4: Task Breakdown (TDD Focus)

Skip if `tasks.md` already has tasks. Otherwise break the design into tasks of 30-60 minutes, each independently testable, shaped like:

```
[ ] Task N: [Description]
    [ ] RED: Write failing test for [functionality]
    [ ] GREEN: Implement minimal code to pass test
    [ ] REFACTOR: Clean up and optimize

    Acceptance Criteria:
    [ ] [Specific, checkable criterion]
    Linked Requirements: REQ-###, REQ-###
```

- Every task lists the REQ-IDs it satisfies; every requirement appears in at least one task.
- Cover components, their integration, error cases, docs, and a final verification task (review, security, performance).
- When the design hides complexity (tricky algorithms, unclear integration points), first ask what the simplest implementation is and where it will break, then size the tasks.

> "Tasks defined with TDD cycle. Ready to begin implementation?"

---

### Phase 5: Execution (Full Mode TDD)

Invoke `dev-workflow:test-driven-development` and follow it for every task. Set `Status:` in `tasks.md` to `In Progress` when you start.

**For each task:**

1. Edit `tasks.md`: `[ ] Task N` → `[→] Task N`.
2. **RED** — write the failing test, run it, and see it fail for the expected reason. Check off RED. Commit: `test: Add test for [functionality]`.
3. **GREEN** — minimal code; the whole suite passes. Check off GREEN. Commit: `feat: Implement [functionality]`.
4. **REFACTOR** — clean up with tests green. Check off REFACTOR. Commit: `refactor: [component]` (skip the commit if nothing changed).
5. Check off the acceptance criteria you verified, mark `[x] Task N`, and update the Progress Summary (`Completed: X/N`).

**Edit the file, then announce.** Saying a box is done is not checking it; a resumed session only sees what is in `tasks.md`.

Every 2-3 tasks, post a checkpoint: tests passing, type check, lint, tasks done, next task.

Before each commit, invoke `dev-workflow:review` and fix critical findings. When all tasks are `[x]`, set `Status:` to `Complete`, confirm tests, lint and type check pass (`dev-workflow:completion-validation`), and report tasks, tests added, commits and files changed.

---

## Back to Planning

If implementation uncovers a missing requirement or a design that cannot work, stop: "Implementation blocked: [issue]. Need to revisit [requirements/design]." Invoke `dev-workflow:spec-driven-planning` to update the documents before continuing.
