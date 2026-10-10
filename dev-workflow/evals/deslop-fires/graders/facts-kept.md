---
type: regex
pattern: '^(?=[\s\S]*export_csv\(\))(?=[\s\S]*--delimiter)(?=[\s\S]*tests/test_export\.py)(?=[\s\S]*#88)(?=[\s\S]*2 GB)(?=[\s\S]*\b6\b)'
target: {source: file, path: fixture/PR_BODY.md}
arm: both
---
