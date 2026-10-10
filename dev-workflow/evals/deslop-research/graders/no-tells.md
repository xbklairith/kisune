---
type: regex
pattern: 'deep dive|ever-evolving|landscape|pivotal|crucial|furthermore|underscor|profound|cornerstone|not just rest|I hope|—'
flags: i
match: not_contains
target: {source: file, path: notes/sleep-memory.md}
arm: both
---
