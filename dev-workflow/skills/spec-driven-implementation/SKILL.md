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

**Goal:** Break design into small, testable tasks following Red-Green-Refactor

**Task Structure:**

Each task follows TDD cycle:
```
[ ] Task N: [Description]
    [ ] RED: Write failing test for [functionality]
    [ ] GREEN: Implement minimal code to pass test
    [ ] REFACTOR: Clean up and optimize

    Acceptance Criteria:
    [ ] [Specific criterion 1]
    [ ] [Specific criterion 2]
    Linked Requirements: REQ-###, REQ-###
```

**Traceability Rules:**
- Every task must list the requirement IDs it satisfies (from requirements.md)
- All requirements must appear in at least one task
- Repeat IDs across tasks if a requirement spans multiple tasks

**Task Sizing:** 30-60 minutes each. If longer, break into subtasks. Each task must be independently testable and produce working, tested code.

**UltraThink Before Task Breakdown:**
Before breaking design into tasks, activate deep thinking if design involves complex algorithms, unclear integration points, multiple strategies, or non-trivial edge cases.

> "Let me ultrathink the implementation strategy before breaking this into tasks."

**Questions to ultrathink:**
- What's the simplest implementation that satisfies requirements?
- Where are the hidden complexities?
- What assumptions might break during implementation?
- How will we test each component in isolation?

**Task Categories:**
1. **Component Tasks** - Individual components implementation
2. **Integration Tasks** - Connect components, test interactions, verify data flow
3. **Error Handling Tasks** - Error scenarios, edge cases, error messages
4. **Documentation Tasks** - Docstrings, README updates, API docs
5. **Final Verification Tasks** - Code review, performance, security, manual testing

**Output:** Update `docx/features/[NN-feature-name]/tasks.md` with implementation approach summary, organized task list with checkboxes, acceptance criteria, and notes.

> "Tasks defined with TDD cycle. Ready to begin implementation?"

---

### Phase 5: Execution (Full Mode TDD)

**Goal:** Execute tasks systematically with quality gates

**For each task:**

1. **Mark Task as In Progress** - Edit `tasks.md`: `[ ] Task N` → `[→] Task N`, mark RED as `[→]`

2. **RED Phase** - Write failing test, verify failure, Edit to check off RED `[x]`, commit: `test: Add test for [functionality]`

3. **GREEN Phase** - Write minimal implementation, all tests must pass, Edit to check off GREEN `[x]`, commit: `feat: Implement [functionality]`

4. **REFACTOR Phase** - Clean up code, tests still passing, Edit to check off REFACTOR `[x]`, commit: `refactor: Optimize [component]`

5. **Mark Task Complete** - Edit: `[→] Task N` → `[x] Task N`, verify acceptance criteria checked, update Progress Summary

### Task Tracking Protocol

**CRITICAL: Use Edit tool to update tasks.md - don't just announce progress.**

```
Start Phase 5
    ↓
Edit: Status "Not Started" → "In Progress"
    ↓
For each task:
    Edit: [ ] Task N → [→] Task N
    Edit: [ ] RED → [→] RED
    Write failing test
    Edit: [→] RED → [x] RED, [ ] GREEN → [→] GREEN
    Implement code
    Edit: [→] GREEN → [x] GREEN, [ ] REFACTOR → [→] REFACTOR
    Refactor code
    Edit: [→] REFACTOR → [x] REFACTOR, [→] Task N → [x] Task N
    Edit: Update Progress Summary
    ↓
Next task or finish
    ↓
Edit: Status "In Progress" → "Complete"
```

**Announcing progress is NOT updating files.** Always use Edit tool to modify tasks.md, then announce.

### Progress Summary Maintenance

Keep the Progress Summary section in tasks.md synchronized after every task:
```markdown
- Total Tasks: 10
- Completed: X/10
- In Progress: Task N - [description]
```

### Status Checkpoints

Every 2-3 completed tasks:
```
Checkpoint Update:
- Tests: [N/N] passing
- Type check: No errors
- Lint: Clean
- Completed tasks: [X/Y]
- Next: [Next task description]
[Confidence: X.X]
```

---

## Auto-Trigger Code Quality Review

Before each commit, invoke `dev-workflow:review` to review changes and address critical findings.

**Integration Skills:**
- `dev-workflow:test-driven-development` - Strict TDD guidance
- `dev-workflow:git-workflow` - Smart commits
- `dev-workflow:review` - Pre-commit reviews

**Completion Criteria:**
- [ ] All tasks checked off
- [ ] All tests passing
- [ ] No linter errors
- [ ] No type errors
- [ ] Code review passed
- [ ] Documentation updated
- [ ] Manual testing complete

**Final Output:**
```
Feature Complete: [Feature Name]

Summary:
- Total tasks: [N]
- Tests added: [N]
- Test coverage: [X%]
- Commits: [N]
- Files changed: [N]

Ready to create PR or merge to main?
```

---

## TDD Principles

### Red-Green-Refactor Cycle

- **RED:** Write a test that describes what the code should do. It MUST fail because the code doesn't exist yet.
- **GREEN:** Write MINIMUM code to make the test pass. Don't optimize, just make it work.
- **REFACTOR:** Improve the code (remove duplication, improve naming, simplify). Run tests after each change.

### TDD Rules

**DO:** Write test before code (always RED first), write smallest test possible, run tests frequently, commit at each phase, keep tests fast and independent.

**DON'T:** Write production code without a failing test, write multiple tests before implementation, skip refactor phase, test implementation details (test behavior), let tests become slow or flaky.

---

## Example: Task Breakdown

**User:** "/dev-workflow:spec tasks"

**Assistant:**
```
Activating Phase 4: Task Breakdown

Found feature: docx/features/01-user-authentication/
Reading design to create TDD tasks...

[ ] Task 1: User model with password hashing
    [ ] RED: Test password hashing on save
    [ ] GREEN: Implement bcrypt hashing
    [ ] REFACTOR: Extract hashing to utility
    Acceptance Criteria:
    [ ] Passwords are hashed before storage
    [ ] Original password is not stored
    Linked Requirements: REQ-001, REQ-002

[...more tasks...]

Tasks defined. Ready to begin implementation?
```

---

## Back to Planning

If during implementation you discover missing requirements, design changes needed, or unclear specifications:

> "Implementation blocked: [issue]. Need to revisit [requirements/design]. Use `/dev-workflow:spec [requirements/design]` to update planning documents."

Invoke `dev-workflow:spec-driven-planning` to update planning documents before continuing.

---

## Critical Reminders

- **NEVER write production code without a failing test first**
- **ALWAYS use Edit tool to update tasks.md checkboxes** - don't just announce progress
- **ALWAYS update Progress Summary** after each task completion
- **Update Status header** when starting/completing implementation
- Follow TDD cycle religiously (RED → GREEN → REFACTOR)
- Provide checkpoint updates every 2-3 tasks
- Stop and return to planning if design issues discovered
