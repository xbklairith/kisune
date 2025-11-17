---
name: spec-driven
description: Guide feature development through structured phases - requirements (EARS format), design, tasks (TDD), and execution. Activates when user mentions feature planning, specs, requirements, or uses /dev-workflow:spec command.
---

# Spec-Driven Development Skill

## Purpose

Guide feature development through five structured phases: Feature Creation → Requirements (EARS) → Design → Tasks (TDD) → Execution. This systematic approach ensures clear requirements, thoughtful design, and test-driven implementation.

## Activation Triggers

Activate this skill when:
- User says "create a new feature"
- User mentions "requirements", "specifications", or "specs"
- User uses `/dev-workflow:spec` command
- User asks to plan a feature
- User says "I need to build [feature]"

## Five-Phase Workflow

### Phase 1: Feature Creation

**Goal:** Establish feature structure and placeholder files

**Process:**
1. Parse feature name from user input
2. Check existing features: `ls docx/features/`
3. Determine next number (NN) for feature directory
4. Create directory: `docx/features/[NN-feature-name]/`
5. Copy templates from plugin to feature directory:
   - requirements.md
   - design.md
   - tasks.md
6. Initialize placeholder content with feature name

**Output:**
```
Created feature: docx/features/[NN-feature-name]/
- requirements.md (from template)
- design.md (from template)
- tasks.md (from template)

Next step: Define requirements using EARS format
```

**User Confirmation:**
> "Feature structure created. Ready to define requirements?"

---

### Phase 2: Requirements Definition (EARS Format)

**Goal:** Capture clear, testable requirements using EARS methodology

**EARS Format Explained:**

EARS (Easy Approach to Requirements Syntax) provides five templates for unambiguous requirements:

1. **Ubiquitous Requirements** - Always true
   - Template: "The system SHALL [requirement]"
   - Example: "The system SHALL validate all user inputs before processing"

2. **Event-Driven Requirements** - Triggered by events
   - Template: "WHEN [trigger] THEN the system SHALL [response]"
   - Example: "WHEN user clicks submit THEN the system SHALL validate form data"

3. **State-Driven Requirements** - Active during specific states
   - Template: "WHILE [state] the system SHALL [requirement]"
   - Example: "WHILE processing payment the system SHALL display loading indicator"

4. **Conditional Requirements** - Based on conditions
   - Template: "IF [condition] THEN the system SHALL [requirement]"
   - Example: "IF user role is admin THEN the system SHALL show management panel"

5. **Optional Requirements** - Feature toggles
   - Template: "WHERE [feature included] the system SHALL [requirement]"
   - Example: "WHERE premium subscription is active the system SHALL enable advanced analytics"

**Systematic Questioning Approach:**

Ask the user these questions to elicit requirements:

1. **Core Functionality**
   - "What is the primary purpose of this feature?"
   - "What problem does it solve?"

2. **Event-Driven Requirements**
   - "What user actions trigger this feature?"
   - "What system events are involved?"

3. **State-Driven Requirements**
   - "Are there different states or modes?"
   - "What should happen during each state?"

4. **Conditional Requirements**
   - "Are there different behaviors for different users/roles?"
   - "What conditions affect functionality?"

5. **Performance Requirements**
   - "Are there response time requirements?"
   - "What's the expected load/scale?"

6. **Security Requirements**
   - "What data needs protection?"
   - "Who should have access?"

7. **Error Handling**
   - "What can go wrong?"
   - "How should errors be handled?"

8. **Edge Cases**
   - "What are the boundary conditions?"
   - "What happens at extremes?"

**Best Practices:**
- Use "SHALL" for mandatory requirements
- Be specific and measurable (avoid "quickly", use "within 2 seconds")
- One requirement per statement
- Avoid ambiguous terms ("appropriate", "reasonable", "user-friendly")
- Use active voice

**Output Format:**
Update `docx/features/[NN-feature-name]/requirements.md` with:
- Overview section
- Functional requirements (organized by EARS type)
- Non-functional requirements (performance, security, usability)
- Constraints
- Acceptance criteria (checkboxes)
- Out of scope items

**User Confirmation:**
> "Requirements complete. Ready for design phase?"

---

### Phase 3: Technical Design

**Goal:** Create comprehensive technical design with architectural decisions

**Process:**

1. **Brainstorming Integration**
   - If `superpowers:brainstorming` available, activate it
   - Explore 2-3 different architectural approaches
   - Discuss trade-offs for each approach

2. **Approach Comparison**
   Present options with trade-offs:

   **Option A: [Approach Name]**
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Complexity: Low/Medium/High
   - Timeline: [Estimate]

   **Option B: [Approach Name]**
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Complexity: Low/Medium/High
   - Timeline: [Estimate]

3. **Recommendation**
   - State recommended approach
   - Provide clear reasoning
   - Explain why it best fits requirements

4. **Design Document Structure**
   Create comprehensive `design.md` covering:

   **Architecture Overview**
   - How feature fits into system
   - High-level component diagram (ASCII art)

   **Component Structure**
   - List components with responsibilities
   - Define dependencies between components
   - Specify public interfaces

   **Data Flow**
   - Step-by-step data movement
   - Diagram showing flow

   **API Contracts**
   - Input/output schemas
   - Error responses
   - Example requests/responses

   **Error Handling**
   - Error scenarios and handling strategy
   - Fallback behaviors

   **Security Considerations**
   - Authentication/authorization
   - Input validation
   - Data protection

   **Performance Considerations**
   - Optimization strategies
   - Caching approach
   - Database indexing needs

   **Testing Strategy**
   - Unit test areas
   - Integration test scenarios
   - E2E test workflows

**Approval Gate:**
> "Design complete. Ready for task breakdown?"

Wait for explicit user approval before proceeding.

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

- Use `superpowers:test-driven-development` if available for TDD guidance
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

## Examples

### Example 1: Creating User Authentication Feature

**User:** "I need to add user authentication"

**Assistant:**
```
Activating spec-driven skill for feature development.

Let me create the feature structure:

Created feature: docx/features/01-user-authentication/
- requirements.md
- design.md
- tasks.md

Phase 1 Complete. Ready to define requirements?
```

**User:** "Yes"

**Assistant:**
```
Phase 2: Requirements Definition (EARS Format)

Let me ask some questions to capture clear requirements:

1. Core Functionality:
   - What authentication methods should be supported? (email/password, OAuth, etc.)
   - Should there be session management?

2. Events:
   - What happens when user tries to log in?
   - What happens when session expires?

[...continues with systematic questioning...]
```

### Example 2: Resuming at Design Phase

**User:** "/dev-workflow:spec design"

**Assistant:**
```
Activating spec-driven skill at Phase 3: Design

Found latest feature: docx/features/01-user-authentication/

Requirements already defined. Let me propose architectural approaches:

**Option A: JWT-Based Authentication**
Pros: Stateless, scalable, works across services
Cons: Token invalidation complexity, larger payload
Complexity: Medium
Timeline: 3-4 days

**Option B: Session-Based Authentication**
Pros: Simple invalidation, smaller cookies, familiar pattern
Cons: Requires session storage, scaling challenges
Complexity: Low
Timeline: 2-3 days

Recommendation: Option A (JWT-Based)
Reasoning: Better for microservices, future-proof, industry standard

Proceed with JWT-based design?
```

---

## Integration with Existing `/x:spec/*` Commands

This skill replaces and enhances existing commands:
- `/x:spec:create` → Phase 1: Feature Creation
- `/x:spec:requirements` → Phase 2: Requirements (EARS)
- `/x:spec:design` → Phase 3: Technical Design
- `/x:spec:tasks` → Phase 4: Task Breakdown
- `/x:spec:execute` → Phase 5: Execution

## Notes

- Always request explicit approval between phases
- Use EARS format strictly for requirements
- Maintain checkbox tracking throughout
- Integrate with other skills (code-quality, git-workflow, systematic-testing)
- Create clear, actionable tasks
- Follow TDD cycle religiously during execution
