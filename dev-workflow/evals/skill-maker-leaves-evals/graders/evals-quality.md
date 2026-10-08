---
type: llm
focus: files
arm: both
---

You see only the list of files the agent created or changed.

Pass only if notes-plugin/evals/ contains at least three separate eval case directories for changelog-writer, each with a case.yaml or prompt.md, and at least one graders/*.md file in total. Fail if no such directories exist (for example, if evals were written only as prose inside SKILL.md or a notes file).
