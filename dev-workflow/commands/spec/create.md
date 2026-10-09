---
description: Create new feature specification
---

Activate the `spec-driven-planning` skill to execute Phase 1 (Feature Creation).

**Instructions:**

1. Extract feature name from $ARGUMENTS
   - If $ARGUMENTS provided: Use it as the feature name
   - If $ARGUMENTS empty: Ask user "What feature would you like to create?"

2. Use the Skill tool to invoke: `dev-workflow:spec-driven-planning`

3. Tell the skill:
   "Create a new feature called [feature-name]. Pick Quick or Full mode using your mode-selection rules, create docx/features/[NN-feature-name]/ with that mode's template file(s), then ask whether to continue."

**What Gets Created:**

Quick mode creates one file; Full mode creates three:

- **plan.md** (Quick mode) — goal, architecture, bite-sized tasks with verification steps

1. **requirements.md** (Full mode)
   - EARS format structure (Event, State, Ubiquitous, Conditional, Optional)
   - Non-functional requirements (Performance, Security, Usability)
   - Constraints, acceptance criteria, out-of-scope items
   - Dependencies, risks, and assumptions

2. **design.md** (Full mode)
   - Architecture overview and system context
   - Component structure with interfaces
   - Data flow diagrams and API contracts
   - Error handling, security, and performance strategies
   - Testing strategy and deployment plan

3. **tasks.md** (Full mode)
   - TDD task breakdown (Red-Green-Refactor cycles)
   - Integration, error handling, and performance tasks
   - Documentation and quality assurance tasks
   - Progress tracking with checkboxes

**After creation, show the user one of:**
```
✅ Created: docx/features/[NN-feature-name]/
   - plan.md (Quick mode, ready to fill in)

📋 Next: Implement using /dev-workflow:spec execute
```
```
✅ Created: docx/features/[NN-feature-name]/
   - requirements.md (ready to fill in)
   - design.md (ready to fill in)
   - tasks.md (ready to fill in)

📋 Next: Define requirements using /dev-workflow:spec:requirements
```
