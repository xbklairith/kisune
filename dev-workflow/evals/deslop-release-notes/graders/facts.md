---
type: regex
pattern: '^(?=[\s\S]*v0\.5\.0)(?=[\s\S]*export_csv)(?=[\s\S]*--delimiter)(?=[\s\S]*3\.8)(?=[\s\S]*#88)'
target: {source: file, path: proj/CHANGELOG.md}
arm: both
---
