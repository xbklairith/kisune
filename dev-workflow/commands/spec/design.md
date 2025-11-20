---
description: Generate technical design
---

Activate the `spec-driven-planning` skill to execute Phase 3 (Technical Design).

**Instructions:**

1. Determine target feature:
   - If $ARGUMENTS provided: Use it as feature name/number
   - If $ARGUMENTS empty: Find most recent feature in docx/features/

2. Use the Skill tool to invoke: `dev-workflow:spec-driven-planning`

3. Tell the skill:
   "Execute Phase 3 (Technical Design) for feature [feature-name]:
   - Read requirements from docx/features/[NN-feature-name]/requirements.md
   - Propose 2-3 architectural approaches with trade-offs
   - Recommend best approach with reasoning
   - Update docx/features/[NN-feature-name]/design.md with comprehensive design

   After design is complete, ask if I'm ready to proceed with Phase 4 (Task Breakdown)."

**Expected Outcome:**
- design.md populated with architecture, components, data flow, and API contracts
- User prompted for next phase
