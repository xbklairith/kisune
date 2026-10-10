---
type: regex
pattern: 'pivotal|seamless|robust|testament|leverag|fostering|underscor|I hope this helps|journey|—'
flags: i
match: not_contains
target: {source: file, path: fixture/PR_BODY.md}
arm: both
---
