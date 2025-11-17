# Development Workflow Plugin Design

**Date:** 2025-11-17
**Plugin Name:** `dev-workflow`
**Purpose:** Integrated development lifecycle plugin combining spec-driven development with code quality, git workflow, documentation, and testing

## Overview

A comprehensive Claude Code plugin that integrates spec-driven development methodology with systematic workflows for code quality, git operations, documentation generation, and testing/debugging. Combines existing `/x:spec/*` commands with superpowers patterns and adds professional development capabilities.

## Design Philosophy

- **Minimal Commands** - Only 2 essential slash commands
- **Natural Activation** - Skills auto-activate based on context
- **Integration Focus** - Combines spec-driven + superpowers patterns
- **Quality-First** - Built-in quality gates throughout workflow

## Plugin Structure

```
dev-workflow/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── spec-driven/
│   │   └── SKILL.md
│   ├── code-quality/
│   │   └── SKILL.md
│   ├── git-workflow/
│   │   └── SKILL.md
│   ├── documentation/
│   │   └── SKILL.md
│   └── systematic-testing/
│       └── SKILL.md
├── commands/
│   ├── spec.md
│   └── review.md
└── templates/
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

## Core Skills

### 1. Spec-Driven Development Skill

**File:** `skills/spec-driven/SKILL.md`

**Frontmatter:**
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

**Five-Phase Workflow:**

**Phase 1: Feature Creation**
- Parse feature name from user input
- Check existing features in `docx/features/`
- Create directory: `docx/features/[NN-feature-name]/`
- Generate placeholder files: requirements.md, design.md, tasks.md

**Phase 2: Requirements (EARS Format)**
Interactive elicitation using EARS templates:
- **Event-Driven**: "WHEN [trigger] THEN system SHALL [response]"
- **State-Driven**: "WHILE [state] system SHALL [requirement]"
- **Ubiquitous**: "System SHALL [requirement]"
- **Conditional**: "IF [condition] THEN system SHALL [requirement]"

Systematic questioning:
1. What triggers this feature?
2. What state conditions matter?
3. What always happens?
4. What edge cases exist?

**Phase 3: Technical Design**
- Integrate brainstorming if available
- Propose 2-3 architectural approaches with trade-offs
- Present recommendation with reasoning
- Create comprehensive design.md covering:
  - Architecture overview
  - Component structure
  - Data flow
  - API contracts
  - Error handling
  - Security considerations

**Approval Gate:** "Design complete. Ready for task breakdown?"

**Phase 4: Task Breakdown (TDD Focus)**
Break design into Red-Green-Refactor tasks:
```
[ ] Task 1: Write test for [component]
[ ] Task 2: Implement minimal code to pass test
[ ] Task 3: Refactor and optimize
[ ] Task 4: Write integration tests
```

Each task:
- Small (30-60 min)
- Testable
- Clear acceptance criteria

**Phase 5: Execution**
Execute tasks systematically:
1. Mark task [ ] → [x] as completed
2. Run tests after each task
3. Commit after logical units
4. Status checkpoints every 2-3 tasks
5. Auto-trigger code-quality skill before commits

### 2. Code Quality Skill

**File:** `skills/code-quality/SKILL.md`

**Frontmatter:**
```yaml
---
name: code-quality
description: Perform code reviews, suggest refactorings, enforce best practices, and identify code smells. Activates when reviewing code, before commits, or when user requests refactoring/optimization.
version: 1.0.0
---
```

**Auto-Activation Triggers:**
- Before git commits (pre-commit review)
- User says "review this code"
- User asks "can this be improved?"
- User mentions refactoring or optimization
- After completing a feature

**Review Checklist:**

1. **Code Structure**
   - Single Responsibility Principle
   - DRY violations
   - Function length
   - Naming clarity
   - Magic numbers

2. **Error Handling**
   - All errors caught appropriately
   - No silent failures
   - User-friendly error messages
   - Logging for debugging
   - Edge cases covered

3. **Security**
   - Input validation
   - SQL injection prevention
   - XSS prevention
   - Sensitive data handling
   - Environment variables for secrets

4. **Performance**
   - No N+1 queries
   - Appropriate caching
   - Database indexes
   - Unnecessary computations removed
   - Memory leak prevention

5. **Testing**
   - Tests exist for new functionality
   - Edge cases tested
   - Happy path tested
   - Error conditions tested
   - Tests are maintainable

**Review Output Format:**
```markdown
## Code Review Results

### ✅ Strengths
[What's done well]

### ⚠️ Issues Found
**Priority: High** - Critical issues
**Priority: Medium** - Important improvements
**Priority: Low** - Nice-to-have optimizations

### 💡 Refactoring Suggestions
[Specific improvements with examples]

### 📊 Metrics
- Complexity, Test Coverage, Maintainability
```

### 3. Git Workflow Skill

**File:** `skills/git-workflow/SKILL.md`

**Frontmatter:**
```yaml
---
name: git-workflow
description: Manage git operations with best practices - smart commits, branch management, PR creation, and deployment helpers. Activates during git operations or when user mentions commits, branches, or pull requests.
version: 1.0.0
---
```

**Auto-Activation Triggers:**
- User asks to commit code
- User mentions branches or PRs
- Before pushing to remote
- When creating pull requests
- Merge conflicts detected

**Core Capabilities:**

**1. Smart Commits**
Before committing:
1. Run `git status` and `git diff`
2. Analyze changes to understand what was done
3. Generate meaningful commit message:
   - Format: `[type]: [concise description]`
   - Types: feat, fix, refactor, test, docs, chore
   - Present tense, imperative mood
   - One-line, under 72 characters

Examples:
- `feat: Add RSI indicator to market analysis`
- `fix: Handle division by zero in position sizing`
- `refactor: Extract strategy validation into separate function`

**2. Branch Management**
Smart branch naming:
- `feature/[feature-name]`
- `fix/[issue-description]`
- `refactor/[component-name]`
- `experiment/[idea-name]`

Safety features:
- Warn before pushing to main/master
- Suggest creating PR instead of direct merge

**3. PR Creation**
When creating pull request:
1. Analyze all commits in branch
2. Review `git diff main...HEAD`
3. Generate comprehensive PR description:
   - Summary of changes
   - Key modifications
   - Testing checklist
   - Code review checklist
4. Use `gh pr create` with formatted body
5. Return PR URL

**4. Safety Checks**
- Never force push to main/master
- Warn about large commits (>10 files)
- Check for secrets before commit
- Verify tests pass before pushing
- Confirm destructive operations

### 4. Documentation Skill

**File:** `skills/documentation/SKILL.md`

**Frontmatter:**
```yaml
---
name: documentation
description: Generate and maintain documentation - function docs, API specs, architecture diagrams, and code explanations. Activates when user requests documentation, explanations, or mentions docs/README.
version: 1.0.0
---
```

**Auto-Activation Triggers:**
- User says "document this"
- User asks "how does this work?"
- User mentions README, docs, or documentation
- After completing a feature
- When API endpoints are created

**Documentation Types:**

**1. Code Documentation**
Auto-generate comprehensive docstrings:
```python
def function_name(args) -> return_type:
    """
    Brief description.

    Detailed explanation of logic.

    Args:
        arg1: Description
        arg2: Description

    Returns:
        Description of return value

    Example:
        >>> function_name(example_args)
        expected_output

    Raises:
        ErrorType: When this happens
    """
```

**2. API Documentation**
Generate OpenAPI-style documentation:
- Endpoint description
- Request/response schemas
- Example payloads
- Error codes and descriptions

**3. Architecture Documentation**
Create system architecture docs:
- Component overview diagrams (ASCII art)
- Data flow descriptions
- Integration points
- Technology stack

**4. README Generation**
Auto-generate project README:
- Project overview
- Installation instructions
- Usage examples
- API reference
- Contributing guidelines
- License information

**5. Code Explanations**
When explaining code:
- High-level purpose
- Step-by-step logic flow
- Key algorithms/patterns
- Edge cases handled
- Dependencies and integrations
- Performance considerations

### 5. Systematic Testing Skill

**File:** `skills/systematic-testing/SKILL.md`

**Frontmatter:**
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

**Auto-Activation Triggers:**
- User implements new functionality
- Tests fail
- User asks about debugging
- User mentions bugs or errors
- Before marking feature complete

**Core Capabilities:**

**1. Test-Driven Development (RED-GREEN-REFACTOR)**

**Phase 1: RED - Write Failing Test**
1. Understand requirement
2. Write test describing expected behavior
3. Run test - verify it fails for right reason
4. Commit: `test: Add test for [feature]`

**Phase 2: GREEN - Make Test Pass**
1. Write minimal code to pass test
2. Run test - verify it passes
3. Don't optimize yet
4. Commit: `feat: Implement [feature]`

**Phase 3: REFACTOR - Improve Code**
1. Clean up implementation
2. Remove duplication
3. Improve naming
4. Run tests - ensure still passing
5. Commit: `refactor: Optimize [component]`

**2. Test Generation**
Auto-generate test templates for:
- Normal cases (happy path)
- Edge cases (boundary conditions)
- Error cases (invalid inputs)
- Integration cases (component interactions)

**3. Systematic Debugging Framework**

**Phase 1: Root Cause Investigation**
1. Reproduce bug consistently
2. Identify symptoms
3. Gather evidence (logs, errors, stack traces)
4. Form hypothesis

**Phase 2: Pattern Analysis**
1. When does it fail?
2. When does it work?
3. What changed recently?
4. Is it environmental?

**Phase 3: Hypothesis Testing**
1. Create minimal test case
2. Add instrumentation
3. Test hypothesis
4. If wrong, form new hypothesis
5. Repeat until root cause found

**Phase 4: Implementation**
1. Write test that reproduces bug
2. Fix the bug
3. Verify test passes
4. Add regression tests
5. Document why bug occurred

**4. Test Coverage Analysis**
Identify and suggest tests for:
- Functions without tests
- Edge cases not covered
- Error conditions not tested
- Integration paths missing

## Slash Commands

### 1. `/dev-workflow:spec`
**Description:** Launch spec-driven development workflow for features

**Interactive Menu:**
1. Create new feature
2. Define requirements (EARS format)
3. Generate technical design
4. Break down into tasks (TDD)
5. Execute implementation
6. List all features

**Usage:**
- `/dev-workflow:spec` → Show menu
- `/dev-workflow:spec "user authentication"` → Create new feature
- `/dev-workflow:spec requirements` → Define requirements

### 2. `/dev-workflow:review`
**Description:** Trigger comprehensive code review with quality checks

**Process:**
1. Ask what to review
2. Run `git diff` to see changes
3. Perform comprehensive review checklist
4. Generate review report with priorities
5. Suggest refactorings with examples

**Usage:**
- `/dev-workflow:review` → Review current staged changes
- `/dev-workflow:review src/file.py` → Review specific file

## Natural Language Activation

All other capabilities activate naturally:
- "help me refactor this" → code-quality skill
- "document this function" → documentation skill
- User commits code → git-workflow skill
- User debugs → systematic-testing skill

## Integration Points

**Combines:**
1. Existing `/x:spec/*` commands → Integrated into spec-driven skill
2. Superpowers patterns → Brainstorming, systematic approaches
3. Code Quality (A) → code-quality skill
4. Development Workflow (B) → git-workflow skill
5. Documentation (C) → documentation skill
6. Testing & Debugging (D) → systematic-testing skill

## File Structure Convention

```
docx/
├── features/
│   └── [NN-feature-name]/
│       ├── requirements.md
│       ├── design.md
│       ├── tasks.md
│       └── task_*_completed.md
└── plans/
    └── [YYYY-MM-DD]-[topic]-design.md
```

## Dependencies

**Optional (auto-detected):**
- `superpowers:brainstorming` - Enhanced design phase
- `superpowers:writing-plans` - Plan generation
- `superpowers:test-driven-development` - TDD workflow
- `superpowers:systematic-debugging` - Debugging framework

Plugin works standalone without these dependencies.

## Success Metrics

- Faster feature development with clear structure
- Higher code quality through systematic reviews
- Better documentation coverage
- Fewer bugs through TDD and systematic debugging
- Cleaner git history with meaningful commits
- Seamless workflow from idea to production

## Design Principles

1. **Minimal Friction** - Auto-activation reduces manual invocation
2. **Quality Gates** - Built-in reviews at key checkpoints
3. **Systematic Approach** - Structured workflows prevent shortcuts
4. **Integration** - Works with existing tools and workflows
5. **Extensible** - Easy to add new skills as needed
6. **Educational** - Teaches best practices through usage
