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
   "Create a new feature called [feature-name]. Execute Phase 1 (Feature Creation):
   - Check existing features in docx/features/
   - Create directory structure: docx/features/[NN-feature-name]/
   - Copy all templates (requirements.md, design.md, tasks.md)
   - Initialize with feature name

   After creating the feature structure, ask if I'm ready to proceed with Phase 2 (Requirements Definition)."

**What Gets Created:**

The following files will be created with comprehensive templates:

1. **requirements.md** (135 lines)
   - EARS format structure (Event, State, Ubiquitous, Conditional, Optional)
   - Non-functional requirements (Performance, Security, Usability)
   - Constraints, acceptance criteria, out-of-scope items
   - Dependencies, risks, and assumptions

2. **design.md** (434 lines)
   - Architecture overview and system context
   - Component structure with interfaces
   - Data flow diagrams and API contracts
   - Error handling, security, and performance strategies
   - Testing strategy and deployment plan

3. **tasks.md** (427 lines)
   - TDD task breakdown (Red-Green-Refactor cycles)
   - Integration, error handling, and performance tasks
   - Documentation and quality assurance tasks
   - Progress tracking with checkboxes

**After creation, show the user:**
```
✅ Created: docx/features/[NN-feature-name]/
   - requirements.md (ready to fill in)
   - design.md (ready to fill in)
   - tasks.md (ready to fill in)

📋 Next: Define requirements using /dev-workflow:spec:requirements
```
