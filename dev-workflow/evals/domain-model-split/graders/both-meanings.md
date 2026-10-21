---
type: regex
pattern: '^(?=[\s\S]*\b(balance|invoice|credit limit|bill))(?=[\s\S]*\b(password|log ?in|sign[- ]?in|credential))'
flags: i
target: {source: file, path: docx/glossary.md}
arm: both
---
