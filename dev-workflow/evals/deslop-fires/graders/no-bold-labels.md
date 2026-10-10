---
type: regex
pattern: '^- \*\*[^*]+:\*\*'
flags: m
match: not_contains
target: {source: file, path: fixture/PR_BODY.md}
arm: both
---
