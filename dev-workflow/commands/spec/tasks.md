---
description: Break down design into TDD tasks
---

Activate the `spec-driven-implementation` skill to execute Phase 4 (Task Breakdown).

**Instructions:**

1. Determine target feature:
   - If $ARGUMENTS provided: Use it as feature name/number
   - If $ARGUMENTS empty: Find most recent feature in docx/features/

2. Use the Skill tool to invoke: `dev-workflow:spec-driven-implementation`

3. Tell the skill:
   "Execute Phase 4 (Task Breakdown) for feature [feature-name]:
   - Read design from docx/features/[NN-feature-name]/design.md
   - Break down into TDD tasks following Red-Green-Refactor cycle
   - Create checkbox list for tracking progress
   - Update docx/features/[NN-feature-name]/tasks.md

   After tasks are defined, ask if I'm ready to proceed with Phase 5 (Execution)."

**Expected Outcome:**
- tasks.md populated with TDD task breakdown and checkboxes
- User prompted for execution phase
