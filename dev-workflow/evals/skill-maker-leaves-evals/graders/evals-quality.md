---
type: llm
focus: files
arm: both
---

Pass only if ALL hold:
1. notes-plugin/evals/ contains at least three separate eval cases for changelog-writer (each a directory with a case.yaml or prompt.md), in the `claude plugin eval` format.
2. At least one case checks that the skill does NOT trigger on an unrelated prompt.
3. notes-plugin/skills/changelog-writer/SKILL.md has a description in third person that says both what the skill does and when to use it, and is at most 1024 characters.
Fail if the evals exist only as prose inside SKILL.md or a notes file.
