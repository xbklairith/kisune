---
type: regex
pattern: '^(?=[\s\S]*\bTask\b)(?=[\s\S]*\bProject\b)(?=[\s\S]*\bReminder\b)(?=[\s\S]*\barchiv)'
flags: i
target: {source: file, path: docx/glossary.md}
arm: both
---
