---
description: Define requirements using EARS format
---

Activate the `spec-driven-planning` skill to execute Phase 2 (Requirements Definition).

**Instructions:**

1. Determine target feature:
   - If $ARGUMENTS provided: Use it as feature name/number
   - If $ARGUMENTS empty: Find most recent feature in docx/features/

2. Use the Skill tool to invoke: `dev-workflow:spec-driven-planning`

3. Tell the skill:
   "Execute Phase 2 (Requirements Definition) for feature [feature-name]:
   - Use EARS format for all requirements
   - Ask systematic questions to elicit clear requirements
   - Update docx/features/[NN-feature-name]/requirements.md

   After requirements are complete, ask if I'm ready to proceed with Phase 3 (Design)."

**Expected Outcome:**
- requirements.md populated with EARS-formatted requirements
- User prompted for next phase
