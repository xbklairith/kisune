# Dev-Workflow Plugin Implementation Plan

**Plugin:** `dev-workflow`
**Estimated Time:** 6-8 hours
**Prerequisites:** Design document reviewed, existing `/x:spec/*` commands understood

## Phase 1: Plugin Structure Setup

### Task 1.1: Create Plugin Directory
**Estimated Time:** 10 min

```bash
mkdir -p dev-workflow/.claude-plugin
mkdir -p dev-workflow/skills/spec-driven
mkdir -p dev-workflow/skills/code-quality
mkdir -p dev-workflow/skills/git-workflow
mkdir -p dev-workflow/skills/documentation
mkdir -p dev-workflow/skills/systematic-testing
mkdir -p dev-workflow/commands
mkdir -p dev-workflow/templates
```

**Verification:**
- [ ] All directories created
- [ ] Structure matches design doc

### Task 1.2: Create plugin.json
**Estimated Time:** 15 min

**File:** `dev-workflow/.claude-plugin/plugin.json`

```json
{
  "name": "dev-workflow",
  "description": "Integrated development lifecycle combining spec-driven development with code quality, git workflow, documentation, and systematic testing",
  "version": "1.0.0",
  "author": {
    "name": "[Your Name]",
    "email": "[Your Email]"
  },
  "homepage": "[Repository URL]",
  "repository": "[Repository URL]",
  "license": "MIT",
  "keywords": [
    "development",
    "workflow",
    "spec-driven",
    "tdd",
    "code-quality",
    "git",
    "documentation"
  ]
}
```

**Verification:**
- [ ] Valid JSON syntax
- [ ] All required fields present
- [ ] Metadata accurate

---

## Phase 2: Spec-Driven Skill

### Task 2.1: Create Spec-Driven SKILL.md
**Estimated Time:** 90 min

**File:** `dev-workflow/skills/spec-driven/SKILL.md`

**Implementation Steps:**

1. Create frontmatter:
```yaml
---
name: spec-driven
description: Guide feature development through structured phases - requirements (EARS format), design, tasks (TDD), and execution. Activates when user mentions feature planning, specs, requirements, or uses /dev-workflow:spec command.
version: 1.0.0
dependencies:
  - superpowers:brainstorming (if available)
  - superpowers:writing-plans (if available)
---
```

2. Document five-phase workflow:

   **Phase 1: Feature Creation**
   - Parse feature name
   - Check existing features in docx/features/
   - Create directory structure
   - Generate placeholder files

   **Phase 2: Requirements (EARS Format)**
   - EARS template explanations
   - Systematic questioning approach
   - Functional vs non-functional requirements
   - Output format

   **Phase 3: Technical Design**
   - Integration with brainstorming
   - Approach comparison (2-3 options)
   - Design document structure
   - Approval gate

   **Phase 4: Task Breakdown (TDD)**
   - Red-Green-Refactor task structure
   - Task sizing guidelines
   - Acceptance criteria
   - Checkbox tracking

   **Phase 5: Execution**
   - Task execution workflow
   - Testing after each task
   - Commit strategy
   - Status checkpoints

3. Include EARS format examples

4. Add task breakdown examples

**Verification:**
- [ ] All five phases clearly documented
- [ ] EARS format explained with examples
- [ ] Integration points with superpowers noted
- [ ] Activation triggers are specific
- [ ] Examples are comprehensive

---

## Phase 3: Code Quality Skill

### Task 3.1: Create Code Quality SKILL.md
**Estimated Time:** 60 min

**File:** `dev-workflow/skills/code-quality/SKILL.md`

**Implementation Steps:**

1. Create frontmatter:
```yaml
---
name: code-quality
description: Perform code reviews, suggest refactorings, enforce best practices, and identify code smells. Activates when reviewing code, before commits, or when user requests refactoring/optimization.
version: 1.0.0
---
```

2. Define auto-activation triggers:
   - Pre-commit review
   - User requests review
   - User mentions refactoring
   - After feature completion

3. Create comprehensive review checklist:
   - Code structure (SRP, DRY, function length, naming)
   - Error handling (catching errors, no silent failures, logging)
   - Security (input validation, SQL injection, XSS, secrets)
   - Performance (N+1 queries, caching, indexes, memory leaks)
   - Testing (coverage, edge cases, maintainability)

4. Define review output format:
   - Strengths section
   - Issues by priority (High/Medium/Low)
   - Refactoring suggestions with code examples
   - Metrics (complexity, coverage, maintainability)

**Verification:**
- [ ] Activation triggers are clear
- [ ] Checklist is comprehensive
- [ ] Output format is actionable
- [ ] Includes code examples

---

## Phase 4: Git Workflow Skill

### Task 4.1: Create Git Workflow SKILL.md
**Estimated Time:** 60 min

**File:** `dev-workflow/skills/git-workflow/SKILL.md`

**Implementation Steps:**

1. Create frontmatter:
```yaml
---
name: git-workflow
description: Manage git operations with best practices - smart commits, branch management, PR creation, and deployment helpers. Activates during git operations or when user mentions commits, branches, or pull requests.
version: 1.0.0
---
```

2. Document smart commits process:
   - Run git status and git diff
   - Analyze changes
   - Generate commit message format
   - Commit message types (feat, fix, refactor, test, docs, chore)
   - Show and confirm
   - Execute and verify

3. Define branch management:
   - Branch naming conventions
   - Branch operations
   - Safety warnings

4. Document PR creation workflow:
   - Analyze all commits
   - Review git diff main...HEAD
   - Generate PR description template
   - Use gh pr create
   - Return PR URL

5. Add safety checks:
   - No force push to main/master
   - Large commit warnings
   - Secrets detection
   - Test verification

**Verification:**
- [ ] Commit message format is clear
- [ ] Branch naming is consistent
- [ ] PR template is comprehensive
- [ ] Safety checks are robust

---

## Phase 5: Documentation Skill

### Task 5.1: Create Documentation SKILL.md
**Estimated Time:** 60 min

**File:** `dev-workflow/skills/documentation/SKILL.md`

**Implementation Steps:**

1. Create frontmatter:
```yaml
---
name: documentation
description: Generate and maintain documentation - function docs, API specs, architecture diagrams, and code explanations. Activates when user requests documentation, explanations, or mentions docs/README.
version: 1.0.0
---
```

2. Define activation triggers:
   - User says "document this"
   - User asks "how does this work?"
   - User mentions docs/README
   - After feature completion
   - API endpoint creation

3. Document documentation types:

   **Code Documentation:**
   - Docstring templates (Python, JS, etc.)
   - Include description, args, returns, examples, raises

   **API Documentation:**
   - Endpoint description
   - Request/response schemas
   - Example payloads
   - Error codes

   **Architecture Documentation:**
   - Component overview diagrams
   - Data flow descriptions
   - Integration points

   **README Generation:**
   - Project overview
   - Installation instructions
   - Usage examples
   - API reference

   **Code Explanations:**
   - High-level purpose
   - Step-by-step logic
   - Key algorithms
   - Edge cases

4. Include templates for each type

**Verification:**
- [ ] All documentation types covered
- [ ] Templates are comprehensive
- [ ] Examples are clear
- [ ] Covers multiple languages

---

## Phase 6: Systematic Testing Skill

### Task 6.1: Create Systematic Testing SKILL.md
**Estimated Time:** 90 min

**File:** `dev-workflow/skills/systematic-testing/SKILL.md`

**Implementation Steps:**

1. Create frontmatter:
```yaml
---
name: systematic-testing
description: Guide test-driven development, generate tests, and provide systematic debugging framework. Activates when writing tests, debugging issues, or investigating failures. Integrates with superpowers TDD and debugging skills if available.
version: 1.0.0
dependencies:
  - superpowers:test-driven-development (if available)
  - superpowers:systematic-debugging (if available)
---
```

2. Document TDD workflow (RED-GREEN-REFACTOR):

   **Phase 1: RED**
   - Understand requirement
   - Write failing test
   - Run and verify failure
   - Commit test

   **Phase 2: GREEN**
   - Write minimal code
   - Run and verify pass
   - Don't optimize yet
   - Commit implementation

   **Phase 3: REFACTOR**
   - Clean up code
   - Remove duplication
   - Improve naming
   - Verify tests still pass
   - Commit refactor

3. Define test generation:
   - Normal cases (happy path)
   - Edge cases (boundary conditions)
   - Error cases (invalid inputs)
   - Integration cases
   - Include code templates

4. Document systematic debugging framework:

   **Phase 1: Root Cause Investigation**
   - Reproduce bug
   - Identify symptoms
   - Gather evidence
   - Form hypothesis

   **Phase 2: Pattern Analysis**
   - When it fails
   - When it works
   - Recent changes
   - Environmental factors

   **Phase 3: Hypothesis Testing**
   - Minimal test case
   - Add instrumentation
   - Test hypothesis
   - Iterate

   **Phase 4: Implementation**
   - Write test for bug
   - Fix bug
   - Verify test passes
   - Add regression tests
   - Document root cause

5. Add test coverage analysis guidelines

**Verification:**
- [ ] TDD cycle is clear
- [ ] Test generation covers all cases
- [ ] Debugging framework is systematic
- [ ] Integrates with superpowers
- [ ] Includes code examples

---

## Phase 7: Slash Commands

### Task 7.1: Create /dev-workflow:spec Command
**Estimated Time:** 30 min

**File:** `dev-workflow/commands/spec.md`

```markdown
---
description: Launch spec-driven development workflow for features
---

Activate the spec-driven skill to guide feature development through structured phases.

Present interactive menu:
1. Create new feature
2. Define requirements (EARS format)
3. Generate technical design
4. Break down into tasks (TDD)
5. Execute implementation
6. List all features

If user provides feature name as argument, start directly at that phase.
If user provides phase name (requirements, design, tasks, execute), start at that phase for the most recent feature.

Examples:
- `/dev-workflow:spec` → Show menu
- `/dev-workflow:spec "user authentication"` → Create new feature
- `/dev-workflow:spec requirements` → Define requirements for latest feature
- `/dev-workflow:spec design` → Generate design for latest feature
```

**Verification:**
- [ ] Interactive menu defined
- [ ] Argument handling explained
- [ ] Examples are clear
- [ ] Activates spec-driven skill

### Task 7.2: Create /dev-workflow:review Command
**Estimated Time:** 20 min

**File:** `dev-workflow/commands/review.md`

```markdown
---
description: Trigger comprehensive code review with quality checks
---

Activate the code-quality skill to perform systematic code review.

Process:
1. Ask what to review:
   - Current staged changes (git diff --cached)
   - Current unstaged changes (git diff)
   - Specific file or directory
   - Entire feature

2. Run appropriate git diff command to see changes

3. Perform comprehensive review using checklist:
   - Code structure
   - Error handling
   - Security
   - Performance
   - Testing

4. Generate review report with:
   - Strengths
   - Issues by priority
   - Refactoring suggestions
   - Metrics

5. Suggest refactorings with code examples

If user provides file path as argument, review that specific file directly.

Examples:
- `/dev-workflow:review` → Review current staged changes
- `/dev-workflow:review src/file.py` → Review specific file
- `/dev-workflow:review .` → Review all changes in current directory
```

**Verification:**
- [ ] Clear review process
- [ ] Multiple review scopes supported
- [ ] Output format specified
- [ ] Activates code-quality skill

---

## Phase 8: Templates

### Task 8.1: Create Requirements Template
**Estimated Time:** 20 min

**File:** `dev-workflow/templates/requirements.md`

```markdown
# Requirements: [Feature Name]

**Created:** [Date]
**Status:** Draft

## Overview
[Brief description of what this feature does and why it's needed]

## Functional Requirements

### Event-Driven Requirements
- WHEN [trigger] THEN the system SHALL [response]
- WHEN [trigger] THEN the system SHALL [response]

### State-Driven Requirements
- WHILE [state] the system SHALL [requirement]
- WHILE [state] the system SHALL [requirement]

### Ubiquitous Requirements
- The system SHALL [requirement]
- The system SHALL [requirement]

### Conditional Requirements
- IF [condition] THEN the system SHALL [requirement]
- IF [condition] THEN the system SHALL [requirement]

## Non-Functional Requirements

### Performance
- The system SHALL [performance requirement with specific metrics]

### Security
- The system SHALL [security requirement]

### Usability
- The system SHALL [usability requirement]

### Reliability
- The system SHALL [reliability requirement]

## Constraints
- [Any technical, business, or regulatory constraints]

## Acceptance Criteria
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]
- [ ] [Testable criterion 3]

## Out of Scope
- [Explicitly state what is NOT included in this feature]
```

**Verification:**
- [ ] EARS format clearly structured
- [ ] All requirement types included
- [ ] Non-functional requirements covered
- [ ] Acceptance criteria checkboxes

### Task 8.2: Create Design Template
**Estimated Time:** 20 min

**File:** `dev-workflow/templates/design.md`

```markdown
# Design: [Feature Name]

**Created:** [Date]
**Status:** Draft

## Architecture Overview
[High-level description of how this feature fits into the system]

## Component Structure

### Components
1. **[Component Name]**
   - Responsibility: [What this component does]
   - Dependencies: [What it depends on]
   - Interface: [Public API]

2. **[Component Name]**
   - Responsibility:
   - Dependencies:
   - Interface:

## Data Flow

```
[User/System] → [Component 1] → [Component 2] → [Database/API]
                     ↓
               [Component 3]
```

Description:
1. [Step 1 of data flow]
2. [Step 2 of data flow]
3. [Step 3 of data flow]

## API Contracts

### Endpoint/Function: [Name]
**Input:**
```json
{
  "field": "type"
}
```

**Output:**
```json
{
  "result": "type"
}
```

**Errors:**
- [Error condition]: [Error response]

## Error Handling
- [Error scenario 1]: [How it's handled]
- [Error scenario 2]: [How it's handled]

## Security Considerations
- [Security measure 1]
- [Security measure 2]

## Performance Considerations
- [Performance optimization 1]
- [Performance optimization 2]

## Testing Strategy
- Unit tests for: [Components/functions]
- Integration tests for: [Integration points]
- E2E tests for: [User workflows]

## Open Questions
- [ ] [Question or decision that needs resolution]
```

**Verification:**
- [ ] All design sections present
- [ ] Clear structure
- [ ] Includes testing strategy
- [ ] Open questions tracked

### Task 8.3: Create Tasks Template
**Estimated Time:** 15 min

**File:** `dev-workflow/templates/tasks.md`

```markdown
# Tasks: [Feature Name]

**Created:** [Date]
**Status:** Not Started

## Implementation Approach
[Brief description of implementation strategy]

## Tasks (TDD: Red-Green-Refactor)

### Component 1: [Name]

#### Task 1: [Description]
- [ ] RED: Write failing test for [functionality]
- [ ] GREEN: Implement minimal code to pass test
- [ ] REFACTOR: Clean up and optimize

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]

#### Task 2: [Description]
- [ ] RED: Write failing test
- [ ] GREEN: Implement code
- [ ] REFACTOR: Optimize

**Acceptance Criteria:**
- [ ] [Criterion 1]

### Component 2: [Name]

#### Task 3: [Description]
- [ ] RED: Write test
- [ ] GREEN: Implement
- [ ] REFACTOR: Clean up

**Acceptance Criteria:**
- [ ] [Criterion 1]

## Integration Tasks

#### Task N: Integration Testing
- [ ] Write integration tests
- [ ] Verify components work together
- [ ] Test error scenarios

## Final Tasks

#### Task N+1: Documentation
- [ ] Update API documentation
- [ ] Update README
- [ ] Add code comments

#### Task N+2: Code Review
- [ ] Self-review code
- [ ] Run `/dev-workflow:review`
- [ ] Address review findings

#### Task N+3: Verification
- [ ] All tests passing
- [ ] No linter errors
- [ ] No type errors
- [ ] Manual testing complete

## Notes
[Any implementation notes, gotchas, or important considerations]
```

**Verification:**
- [ ] TDD structure clear
- [ ] Checkboxes for tracking
- [ ] Acceptance criteria included
- [ ] Final verification tasks included

---

## Phase 9: Testing & Documentation

### Task 9.1: Create README.md
**Estimated Time:** 45 min

**File:** `dev-workflow/README.md`

Include:
- Plugin overview
- Installation instructions
- Usage guide for each command
- Skill descriptions and activation triggers
- Integration with existing `/x:spec/*` commands
- Example workflows
- Template usage
- Contributing guidelines

**Verification:**
- [ ] Clear installation steps
- [ ] All commands documented
- [ ] All skills explained
- [ ] Examples are actionable
- [ ] Integration points clear

### Task 9.2: Manual Testing
**Estimated Time:** 60 min

Test each component:
- [ ] Install plugin in Claude Code
- [ ] Test `/dev-workflow:spec` menu
- [ ] Test creating a new feature
- [ ] Test requirements phase (EARS format)
- [ ] Test design phase
- [ ] Test tasks phase
- [ ] Test execution phase
- [ ] Test `/dev-workflow:review` command
- [ ] Verify code-quality skill auto-activates
- [ ] Verify git-workflow skill auto-activates
- [ ] Verify documentation skill auto-activates
- [ ] Verify systematic-testing skill auto-activates
- [ ] Test templates are accessible

**Verification:**
- [ ] All commands work
- [ ] Skills activate correctly
- [ ] No syntax errors
- [ ] YAML frontmatter is valid
- [ ] Output quality is high
- [ ] Integration with superpowers works (if available)

---

## Final Checklist

- [ ] All files created with correct structure
- [ ] YAML frontmatter is valid in all SKILL.md files
- [ ] Commands are properly formatted
- [ ] Templates are comprehensive
- [ ] README is complete
- [ ] Plugin tested in Claude Code
- [ ] No errors or warnings
- [ ] Integration with existing `/x:spec/*` verified
- [ ] Integration with superpowers verified (if available)
- [ ] Ready for use

---

## Estimated Total Time: 7-8 hours

**Success Criteria:**
- Plugin installs without errors
- All commands accessible
- Skills activate appropriately at correct triggers
- EARS requirements format works correctly
- TDD workflow is clear and actionable
- Code review output is comprehensive
- Git workflow improves commit quality
- Documentation generation is helpful
- Debugging framework is systematic
- Replaces/enhances existing `/x:spec/*` commands seamlessly
