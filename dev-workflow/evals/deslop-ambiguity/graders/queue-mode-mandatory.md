---
type: regex
pattern: 'QUEUE_MODE[^\n]*\b(must|required)\b|\b(must|required)\b[^\n]*QUEUE_MODE'
flags: i
target: {source: file, path: docs/upgrade.md}
arm: both
---
