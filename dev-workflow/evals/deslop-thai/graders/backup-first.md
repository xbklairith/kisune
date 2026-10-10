---
type: llm
focus: {source: file, path: docs/deploy-guide.md}
arm: both
---

The document is a Thai deploy guide. Pass if the instruction to back up the database comes before the step that runs `make migrate` (as an earlier step, or a warning placed above the steps). Fail if the backup instruction appears only after that step.
