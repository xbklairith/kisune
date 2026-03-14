---
name: spec-driven-implementation
description: MANDATORY implementation — breaks design into TDD tasks in docx/features/ tasks.md with Red-Green-Refactor. MUST activate after spec-driven-planning.
---

# Spec-Driven Implementation Skill

## Purpose

Guide feature implementation through two structured phases: Task Breakdown (TDD) → Execution. Ensures test-driven development, quality gates, and tracked progress from design to working code.

## Activation Triggers

Activate this skill when:
- User says "implement this feature" or "let's code this"
- User mentions "tasks", "TDD", or "execution"
- User uses `/dev-workflow:spec` command with implementation options (tasks, execute)
- User is ready to start implementation after design approval
- Design phase is complete and approved

## Prerequisites

Requires completed planning from `spec-driven-planning` skill:
- [ ] Feature directory exists: `docx/features/[NN-feature-name]/`
- [ ] `requirements.md` is complete with EARS requirements
- [ ] `design.md` is complete and approved

**If prerequisites are missing:**
> "Implementation requires completed planning. Run `/dev-workflow:spec` and complete options 1-3 first (Feature Creation, Requirements, Design)."

---

## Phase 4: Task Breakdown (TDD Focus)

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

## Phase 5: Execution

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
