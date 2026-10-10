---
type: regex
pattern: '^(?:(?!bin/migrate)[\s\S])*back(?:ed)?[ -]?up[\s\S]*bin/migrate'
flags: i
target: {source: file, path: docs/upgrade.md}
arm: both
---
