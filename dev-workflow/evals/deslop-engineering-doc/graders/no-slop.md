---
type: regex
pattern: 'pivotal|fast-paced|landscape|crucial|seamless|stark reminder|intricate|interplay|not just a bug|fostering|peace of mind|future looks bright|journey|I hope this helps|—'
flags: i
match: not_contains
target: {source: file, path: docs/cache-outage.md}
arm: both
---
