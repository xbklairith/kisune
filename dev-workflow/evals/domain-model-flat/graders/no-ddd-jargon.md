---
type: regex
pattern: 'bounded context|context map|anti-corruption|subdomain|ubiquitous language'
flags: i
match: not_contains
target: {source: file, path: docx/glossary.md}
arm: both
---
