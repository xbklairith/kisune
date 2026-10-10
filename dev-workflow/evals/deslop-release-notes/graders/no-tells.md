---
type: regex
pattern: '—|–|seamless|robust|enhanc|leverag|streamlin|comprehensive|significant|delight|empower|ensur|exciting|we.re (thrilled|excited)|^- \*\*(?!Breaking)[^*]+:?\*\*:?'
flags: im
match: not_contains
target: {source: file, path: proj/CHANGELOG.md}
arm: both
---
