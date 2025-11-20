---
description: Execute implementation with TDD
---

Activate the `spec-driven-implementation` skill to execute Phase 5 (Execution).

**Instructions:**

1. Determine target feature:
   - If $ARGUMENTS provided: Use it as feature name/number
   - If $ARGUMENTS empty: Find most recent feature in docx/features/

2. Use the Skill tool to invoke: `dev-workflow:spec-driven-implementation`

3. Tell the skill:
   "Execute Phase 5 (Implementation) for feature [feature-name]:
   - Read tasks from docx/features/[NN-feature-name]/tasks.md
   - Execute tasks systematically following TDD (Red-Green-Refactor)
   - Update checkboxes as tasks complete
   - Integrate with code-quality and git-workflow skills
   - Run quality gates before marking tasks complete

   Work through all tasks until feature is complete."

**Expected Outcome:**
- All tasks executed with TDD discipline
- Checkboxes updated in tasks.md
- Code quality verified
- Feature implementation complete
