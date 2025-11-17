---
description: Launch spec-driven development workflow for features
---

Activate the `spec-driven` skill to guide feature development through structured phases: requirements (EARS format) → design → tasks (TDD) → execution.

## Interactive Menu

Present this menu to the user:

```
📋 Spec-Driven Development Workflow

Choose an option:

1. Create new feature
2. Define requirements (EARS format)
3. Generate technical design
4. Break down into tasks (TDD)
5. Execute implementation
6. List all features

What would you like to do? (1-6)
```

## Argument Handling

**If user provides feature name as argument:**
```
/dev-workflow:spec "user authentication"
```
→ Start directly at Phase 1 (Feature Creation) with that feature name

**If user provides phase name as argument:**
```
/dev-workflow:spec requirements
/dev-workflow:spec design
/dev-workflow:spec tasks
/dev-workflow:spec execute
```
→ Start at that phase for the most recent feature (highest NN number in docx/features/)

**If user provides "list" as argument:**
```
/dev-workflow:spec list
```
→ Show all features with their current status

## Phase Execution

### Phase 1: Create New Feature
1. Ask user for feature name
2. Check existing features: `ls docx/features/`
3. Determine next number (NN)
4. Create: `docx/features/[NN-feature-name]/`
5. Copy templates:
   - requirements.md
   - design.md
   - tasks.md
6. Confirm creation

### Phase 2: Define Requirements
1. Use EARS format (Event-Driven, State-Driven, Ubiquitous, Conditional)
2. Ask systematic questions to elicit requirements
3. Capture functional and non-functional requirements
4. Update `requirements.md`
5. Request approval before proceeding

### Phase 3: Generate Design
1. If `superpowers:brainstorming` available, activate it
2. Propose 2-3 architectural approaches with trade-offs
3. Present recommendation with reasoning
4. Create comprehensive design.md
5. Request approval before proceeding

### Phase 4: Break Down Tasks
1. Break design into Red-Green-Refactor tasks
2. Each task should be 30-60 minutes
3. Include acceptance criteria
4. Use checkbox format for tracking
5. Update `tasks.md`
6. Request approval before proceeding

### Phase 5: Execute Implementation
1. Follow TDD cycle for each task
2. Mark tasks as complete with checkboxes
3. Auto-trigger `code-quality` skill before commits
4. Use `git-workflow` skill for smart commits
5. Provide status updates every 2-3 tasks
6. Complete when all tasks done and verified

## Examples

**Example 1: Start workflow**
```
User: /dev-workflow:spec

Assistant presents interactive menu.
```

**Example 2: Create specific feature**
```
User: /dev-workflow:spec "user authentication"