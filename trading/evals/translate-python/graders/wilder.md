---
type: regex
pattern: 'alpha\s*=\s*1\s*/|com\s*=\s*\w+\s*-\s*1|\*\s*\(\s*\w+\s*-\s*1\s*\)\s*\+|wilder'
flags: i
target: {source: file, path: strategy.py}
arm: both
---
