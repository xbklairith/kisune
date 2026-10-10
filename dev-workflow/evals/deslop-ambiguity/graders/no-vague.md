---
type: regex
pattern: '(^|[.!?]\s+)It can take|\bYou should set\b'
flags: m
match: not_contains
target: {source: file, path: docs/upgrade.md}
arm: both
---
