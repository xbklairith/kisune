---
type: regex
pattern: 'Outage On|What Happened|The Fix|Looking Ahead'
match: not_contains
target: {source: file, path: docs/cache-outage.md}
arm: both
---
