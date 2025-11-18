---
name: spec-driven-implementation
description: Break down technical design into TDD tasks with Red-Green-Refactor cycles and execute implementation with checkbox tracking. Activates when design is complete and user is ready to implement, or mentions tasks, execution, TDD, or implementation.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, TodoWrite
---

# Spec-Driven Implementation Skill

## Purpose

Guide feature implementation through two structured phases: Task Breakdown (TDD) → Execution. This systematic approach ensures test-driven development, quality gates, and tracked progress from design to working code.

## Activation Triggers

Activate this skill when:
- User says "implement this feature" or "let's code this"
- User mentions "tasks", "TDD", or "execution"
- User uses `/dev-workflow:spec` command with implementation options (tasks, execute)
- User is ready to start implementation after design approval
- User says "break this down into tasks"
- Design phase is complete and approved

## Prerequisites

This skill requires completed planning from `spec-driven-planning` skill:
- [ ] Feature directory exists: `docx/features/[NN-feature-name]/`
- [ ] `requirements.md` is complete with EARS requirements
- [ ] `design.md` is complete and approved

**If prerequisites are missing:**
> "Implementation requires completed planning. Run `/dev-workflow:spec` and complete options 1-3 first (Feature Creation, Requirements, Design)."

---

## Two-Phase Implementation Workflow

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
```

**Task Sizing Guidelines:**
- Each task should take 30-60 minutes
- If longer, break into subtasks
- Each task must be independently testable
- Each task produces working, tested code

**Task Categories:**

1. **Component Tasks**
   - Implement individual components
   - One component per task or split if large

2. **Integration Tasks**
   - Connect components
   - Test component interactions
   - Verify data flow

3. **Error Handling Tasks**
   - Implement error scenarios
   - Test edge cases
   - Verify error messages

4. **Documentation Tasks**
   - Write docstrings
   - Update README
   - Create API docs

5. **Final Verification Tasks**
   - Code review
   - Performance testing
   - Security review
   - Manual testing

**Output:**
Update `docx/features/[NN-feature-name]/tasks.md` with:
- Implementation approach summary
- Organized task list with checkboxes
- Acceptance criteria for each task
- Notes section for implementation considerations

**User Confirmation:**
> "Tasks defined with TDD cycle. Ready to begin implementation?"

---

### Phase 5: Execution

**Goal:** Execute tasks systematically with quality gates

**Execution Workflow:**

For each task:

1. **Mark Task as In Progress**
   - Update checkbox from `[ ]` to `[→]` or add comment

2. **RED Phase**
   - Write failing test
   - Run test suite to verify failure
   - Commit: `test: Add test for [functionality]`

3. **GREEN Phase**
   - Write minimal implementation
   - Run tests until passing
   - Don't optimize yet
   - Commit: `feat: Implement [functionality]`

4. **REFACTOR Phase**
   - Clean up code
   - Remove duplication
   - Improve naming
   - Run tests to ensure still passing
   - Commit: `refactor: Optimize [component]`

5. **Mark Task Complete**
   - Update checkbox to `[x]`
   - Update acceptance criteria checkboxes

**Status Checkpoints:**

Every 2-3 completed tasks, provide status update:

```
🔄 Checkpoint Update:
- ✅ Tests: [N/N] passing
- ✅ Type check: No errors
- ✅ Lint: Clean
- 📝 Completed tasks: [X/Y]
- 🎯 Next: [Next task description]

[Confidence: X.X]
```

**Auto-Trigger Code Quality Review:**

Before each commit:
- Auto-activate `code-quality` skill
- Review changes for issues
- Address critical findings before commit

**Integration Points:**

- Activate `test-driven-development` skill for strict TDD guidance
- Use `git-workflow` skill for smart commits
- Use `code-quality` skill for pre-commit reviews

**Completion Criteria:**

Feature is complete when:
- [ ] All tasks checked off
- [ ] All tests passing
- [ ] No linter errors
- [ ] No type errors
- [ ] Code review passed
- [ ] Documentation updated
- [ ] Manual testing complete

**Final Output:**
```
✅ Feature Complete: [Feature Name]

Summary:
- Total tasks: [N]
- Tests added: [N]
- Test coverage: [X%]
- Commits: [N]
- Files changed: [N]

Ready to create PR or merge to main?
```

---

## Test-Driven Development (TDD) Principles

### The Red-Green-Refactor Cycle

**RED (Write Failing Test):**
```
Write a test that describes what the code should do.
The test MUST fail because the code doesn't exist yet.
This proves the test is actually testing something.
```

**GREEN (Make Test Pass):**
```
Write the MINIMUM code needed to make the test pass.
Don't worry about elegance or optimization.
Just make it work.
```

**REFACTOR (Improve Code):**
```
Now that tests pass, improve the code:
- Remove duplication
- Improve naming
- Simplify logic
- Optimize performance
Run tests after each change to ensure they still pass.
```

### TDD Best Practices

**DO:**
- Write test before production code (always RED first)
- Write smallest test possible
- Run tests frequently
- Commit at each phase (RED, GREEN, REFACTOR)
- Keep tests fast and independent

**DON'T:**
- Write production code without a failing test
- Write multiple tests before implementation
- Skip the refactor phase
- Test implementation details (test behavior)
- Let tests become slow or flaky

---

## Examples

### Example 1: Starting Task Breakdown

**User:** "/dev-workflow:spec tasks"

**Assistant:**
```
Activating spec-driven-implementation skill at Phase 4: Task Breakdown

Found feature: docx/features/01-user-authentication/
✅ requirements.md exists
✅ design.md exists

Reading design to create TDD tasks...

Breaking down into testable tasks:

[ ] Task 1: User model with password hashing
    [ ] RED: Test password hashing on save
    [ ] GREEN: Implement bcrypt hashing
    [ ] REFACTOR: Extract hashing to utility

    Acceptance Criteria:
    [ ] Passwords are hashed before storage
    [ ] Original password is not stored
    [ ] Hash is verifiable

[ ] Task 2: JWT token generation
    [ ] RED: Test token generation with user ID
    [ ] GREEN: Implement JWT signing
    [ ] REFACTOR: Extract to auth service

    Acceptance Criteria:
    [ ] Token contains user ID
    [ ] Token expires in 24 hours
    [ ] Token is properly signed

[...8 more tasks...]

Tasks defined. Ready to begin implementation?
```

### Example 2: Executing Implementation

**User:** "Yes, let's start"

**Assistant:**
```
Activating Phase 5: Execution

Starting Task 1: User model with password hashing

RED Phase: Writing failing test...
[Creates test file with failing test]
Running tests... ❌ 1 failing (expected)

Commit: test: Add test for user password hashing

GREEN Phase: Implementing minimal code...
[Implements password hashing]
Running tests... ✅ All passing

Commit: feat: Implement user password hashing with bcrypt

REFACTOR Phase: Extracting to utility...
[Refactors code]
Running tests... ✅ All passing

Commit: refactor: Extract password hashing to utility module

✅ Task 1 complete

🔄 Checkpoint Update:
- ✅ Tests: 3/3 passing
- ✅ Type check: No errors
- ✅ Lint: Clean
- 📝 Completed tasks: 1/10
- 🎯 Next: Task 2 - JWT token generation

[Confidence: 0.9]

Continue to Task 2?
```

---

## Back to Planning

If during implementation you discover:
- Missing requirements
- Design needs changes
- Unclear specifications

**STOP implementation and return to planning:**
> "Implementation blocked: [issue]. Need to revisit [requirements/design]. Use `/dev-workflow:spec [requirements/design]` to update planning documents."

Then use `spec-driven-planning` skill to update planning documents before continuing implementation.

---

## Notes

- NEVER write production code without a failing test first
- Mark tasks in progress and completed for visibility
- Provide checkpoint updates every 2-3 tasks
- Auto-trigger code-quality before commits
- Use git-workflow skill for smart commit messages
- Follow TDD cycle religiously (RED → GREEN → REFACTOR)
- Stop and return to planning if design issues discovered
