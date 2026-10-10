---
type: regex
pattern: '^(?=[\s\S]*Rasch (&|and) Born,? 2013)(?=[\s\S]*Mednick et al\.,? 2003)(?=[\s\S]*\b24\b)(?=[\s\S]*90-minute)(?=[\s\S]*20%)(?=[\s\S]*under 30)'
target: {source: file, path: notes/sleep-memory.md}
arm: both
---
