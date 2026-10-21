---
type: regex
pattern: '^#+[^\n]*\bInvoices?\b[^\n]*\n[\s\S]*^#+[^\n]*\bInvoices?\b'
flags: m
match: not_contains
target: {source: file, path: docx/glossary.md}
arm: both
---
