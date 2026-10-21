---
# The backup comes before the step that runs the migration. A step is a list
# item naming bin/migrate or "run ... bin/migrate" in prose, so an intro
# sentence that only mentions the command does not count as running it.
type: regex
pattern: '^(?:(?!\n[ \t]*(?:\d+[.)]|[-*])[ \t][^\n]*bin/migrate|\brun\b[^.\n]{0,20}bin/migrate)[\s\S])*back(?:ed)?[ -]?up[\s\S]*bin/migrate'
flags: i
target: {source: file, path: docs/upgrade.md}
arm: both
---
