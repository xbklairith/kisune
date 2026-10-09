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
   "Execute implementation for feature [feature-name]: detect the mode from docx/features/[NN-feature-name]/ (plan.md → Quick, tasks.md → Full) and run the matching playbook.
   - Update checkboxes as tasks complete
   - Integrate with review and git-workflow skills
   - Run quality gates before marking tasks complete

   Work through all tasks until feature is complete."

**Expected Outcome:**
- Each task executed and verified for its mode (Full mode: RED-GREEN-REFACTOR)
- Checkboxes updated in plan.md or tasks.md
- Code quality verified
- Feature implementation complete
