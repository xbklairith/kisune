---
name: spec-driven-implementation
description: MANDATORY implementation methodology — breaks design into TDD tasks in docx/features/ tasks.md with Red-Green-Refactor cycle. MUST activate when implementing features that have completed spec-driven-planning.
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
    Linked Requirements: REQ-###, REQ-###
```

**Traceability Rules:**
- Every task must list the requirement IDs it satisfies (use IDs from requirements.md).
- Maintain coverage by ensuring all requirements appear in at least one task.
- If a requirement spans multiple tasks, repeat the ID across those tasks for clarity.

**Task Sizing Guidelines:**
- Each task should take 30-60 minutes
- If longer, break into subtasks
- Each task must be independently testable
- Each task produces working, tested code

**UltraThink Before Task Breakdown:**
Before breaking design into tasks, activate deep thinking if:
- Design involves complex algorithms or data structures
- Integration points between components are unclear
- Multiple implementation strategies are possible
- Edge cases and error handling are non-trivial

> 🗣 Say: "Let me ultrathink the implementation strategy before breaking this into tasks."

**Questions to ultrathink:**
- What's the simplest implementation that satisfies requirements?
- Which parts are most likely to change?
- Where are the hidden complexities?
- What assumptions might break during implementation?
- How will we test each component in isolation?
- What could we build incrementally vs. all at once?

**After UltraThink:** Create focused, testable tasks that validate assumptions early.

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

   **Use Edit tool** on `docx/features/[NN-feature-name]/tasks.md`:

   - Find the task header: `[ ] Task N: [description]`
   - Replace with: `[→] Task N: [description]`
   - Also mark the RED phase checkbox as `[→]`

   **Example Edit call:**
   ```
   Edit tool:
     file: docx/features/01-user-auth/tasks.md
     old_string: "[ ] Task 3: Implement JWT validation"
     new_string: "[→] Task 3: Implement JWT validation"
   ```

2. **RED Phase**

   - Write failing test for the specific functionality
   - Run test suite to verify failure (test MUST fail)
   - **Use Edit tool** to check off RED phase: `[ ] RED: ...` → `[x] RED: ...`
   - Commit: `test: Add test for [functionality]`

3. **GREEN Phase**

   - Write minimal implementation to make test pass
   - Run tests until passing (all tests MUST pass)
   - Don't optimize yet (just make it work)
   - **Use Edit tool** to check off GREEN phase: `[ ] GREEN: ...` → `[x] GREEN: ...`
   - Commit: `feat: Implement [functionality]`

4. **REFACTOR Phase**

   - Clean up code (remove duplication, improve naming)
   - Run tests to ensure still passing
   - **Use Edit tool** to check off REFACTOR phase: `[ ] REFACTOR: ...` → `[x] REFACTOR: ...`
   - Commit: `refactor: Optimize [component]`

5. **Mark Task Complete**

   **Use Edit tool** on `docx/features/[NN-feature-name]/tasks.md`:

   - Change task header: `[→] Task N: ...` → `[x] Task N: ...`
   - Verify all acceptance criteria are checked: `[x]`
   - Update Progress Summary section (see instructions below)

### Task Tracking Protocol

**CRITICAL: Use Edit tool to update tasks.md - don't just announce progress.**

#### Workflow Summary

```
Start Phase 5
    ↓
Edit: Status "Not Started" → "In Progress"
    ↓
For each task:
    ↓
    Edit: [ ] Task N → [→] Task N
    Edit: [ ] RED → [→] RED
    ↓
    Write failing test
    ↓
    Edit: [→] RED → [x] RED
    Edit: [ ] GREEN → [→] GREEN
    ↓
    Implement code
    ↓
    Edit: [→] GREEN → [x] GREEN
    Edit: [ ] REFACTOR → [→] REFACTOR
    ↓
    Refactor code
    ↓
    Edit: [→] REFACTOR → [x] REFACTOR
    Edit: [→] Task N → [x] Task N
    Edit: Update Progress Summary
    ↓
Next task or finish
    ↓
Edit: Status "In Progress" → "Complete"
```

#### Edit Tool Usage Pattern

**Always follow this pattern for every task:**

1. **Before starting any task:**
   ```
   Use Edit tool to change [ ] → [→] in tasks.md
   ```

2. **After completing each phase (RED/GREEN/REFACTOR):**
   ```
   Use Edit tool to change [→] → [x] for that phase
   Use Edit tool to change [ ] → [→] for next phase
   ```

3. **After completing full task:**
   ```
   Use Edit tool to change [→] → [x] for task header
   Use Edit tool to update Progress Summary counts
   ```

4. **Don't skip these Edit calls** - they're not optional suggestions, they're required operations.

#### Announcing vs. Modifying

**Wrong (Just Announcing):**
```
✅ Task 1 complete
Moving to Task 2...
```

**Right (Actually Modifying + Announcing):**
```
[Using Edit tool to mark Task 1 complete: [→] → [x]]
[Using Edit tool to update Progress Summary: Completed 1/10]
✅ Task 1 complete

[Using Edit tool to mark Task 2 in progress: [ ] → [→]]
Starting Task 2: JWT token generation...
```

#### Progress Summary Maintenance

The Progress Summary section must stay synchronized:

**Before any tasks start:**
```markdown
- Total Tasks: 10
- Completed: 0/10
- In Progress: None
```

**After Task 1 starts:**
```markdown
- Total Tasks: 10
- Completed: 0/10
- In Progress: Task 1 - User model with password hashing
```

**After Task 1 completes:**
```markdown
- Total Tasks: 10
- Completed: 1/10
- In Progress: Task 2 - JWT token generation
```

**Use Edit tool** to update these fields after every task completion.

---

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

---

### Quick Reference

**Edit patterns already detailed above. Key reminders:**
- Update Status header when starting/completing implementation
- Use Grep to count tasks if needed: `grep -c "^\- \[x\] Task" tasks.md`
- Update test coverage optionally: Run `npm run test:coverage` and Edit tasks.md

---

**Auto-Trigger Code Quality Review:**

Before each commit:
- Use Skill tool to invoke: `dev-workflow:review`
- Review changes for issues
- Address critical findings before commit

**How to activate:**
```
Use Skill tool: Skill(skill: "dev-workflow:review")
```

**Integration Points:**

- Use Skill tool to invoke: `dev-workflow:test-driven-development` for strict TDD guidance
- Use Skill tool to invoke: `dev-workflow:git-workflow` for smart commits
- Use Skill tool to invoke: `dev-workflow:review` for pre-commit reviews

**How to activate integration skills:**
```
# For TDD enforcement
Use Skill tool: Skill(skill: "dev-workflow:test-driven-development")

# For git operations
Use Skill tool: Skill(skill: "dev-workflow:git-workflow")

# For code review
Use Skill tool: Skill(skill: "dev-workflow:review")
```

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

[Using Edit tool on docx/features/01-user-authentication/tasks.md]
[Changing "**Status:** Not Started" to "**Status:** In Progress"]

[Using Edit tool to mark Task 1 in progress]
[Changing "[ ] Task 1: User model with password hashing" to "[→] Task 1: User model with password hashing"]

[Using Edit tool to mark RED phase in progress]
[Changing "    [ ] RED: Test password hashing on save" to "    [→] RED: Test password hashing on save"]

Starting Task 1: User model with password hashing

RED Phase: Writing failing test...
[Creates test file tests/models/user.test.js with failing test]
Running tests... ❌ 1 failing (expected)

[Using Edit tool to check off RED phase]
[Changing "    [→] RED: Test password hashing on save" to "    [x] RED: Test password hashing on save"]

Commit: test: Add test for user password hashing

[Using Edit tool to mark GREEN phase in progress]
[Changing "    [ ] GREEN: Implement bcrypt hashing" to "    [→] GREEN: Implement bcrypt hashing"]

GREEN Phase: Implementing minimal code...
[Implements password hashing in src/models/user.js]
Running tests... ✅ All passing

[Using Edit tool to check off GREEN phase]
[Changing "    [→] GREEN: Implement bcrypt hashing" to "    [x] GREEN: Implement bcrypt hashing"]

Commit: feat: Implement user password hashing with bcrypt

[Using Edit tool to mark REFACTOR phase in progress]
[Changing "    [ ] REFACTOR: Extract hashing to utility" to "    [→] REFACTOR: Extract hashing to utility"]

REFACTOR Phase: Extracting to utility...
[Refactors code to src/utils/crypto.js]
Running tests... ✅ All passing

[Using Edit tool to check off REFACTOR phase]
[Changing "    [→] REFACTOR: Extract hashing to utility" to "    [x] REFACTOR: Extract hashing to utility"]

Commit: refactor: Extract password hashing to utility module

[Using Edit tool to mark Task 1 complete]
[Changing "[→] Task 1: User model with password hashing" to "[x] Task 1: User model with password hashing"]

[Using Edit tool to update Progress Summary]
[Changing "- Completed: 0/10" to "- Completed: 1/10"]
[Changing "- In Progress: Task 1 - User model with password hashing" to "- In Progress: Task 2 - JWT token generation"]

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

Then use Skill tool to invoke: `dev-workflow:spec-driven-planning` to update planning documents before continuing implementation.

**How to return to planning:**
```
Use Skill tool: Skill(skill: "dev-workflow:spec-driven-planning")
```

---

## Notes

### Critical Requirements

- **NEVER write production code without a failing test first**
- **ALWAYS use Edit tool to update tasks.md checkboxes** - don't just announce progress
- **ALWAYS use Edit tool to update Progress Summary** after each task completion
- **Use Edit tool to update Status header** when starting/completing implementation

### Task Tracking Best Practices

- **Mark in progress:** Use Edit tool to change `[ ]` → `[→]` before starting task
- **Mark complete:** Use Edit tool to change `[→]` → `[x]` after finishing task
- **Update Progress Summary:** Use Edit tool after every task to keep counts accurate
- **File updates are mandatory:** Actually modify tasks.md, don't just announce

### Implementation Guidelines

- Provide checkpoint updates every 2-3 tasks
- Use Skill tool to invoke: `dev-workflow:review` before commits
- Use Skill tool to invoke: `dev-workflow:git-workflow` for smart commit messages
- Follow TDD cycle religiously (RED → GREEN → REFACTOR)
- Stop and return to planning if design issues discovered

### Remember

**Announcing progress ≠ Updating files**

Wrong:
```
✅ Task 1 complete
Moving to Task 2...
```

Right:
```
[Using Edit tool to mark Task 1 complete: [→] → [x]]
[Using Edit tool to update Progress Summary]
✅ Task 1 complete
```
