---
# No TBD/TODO or unfilled template brackets anywhere. Vague words (etc., as
# needed, appropriate, handle errors) count only on a requirement line
# ("- [REQ-001] ...", "- **REQ-001:** ...") or an acceptance checkbox
# ("- [ ] ..."), so research notes such as "csv.writer quotes fields as
# needed" pass.
type: regex
pattern: '\bTBD\b|\bTODO\b|\[(?:trigger|condition|response|system state|optional feature)[^\]\n]*\]|^[ \t]*[-*][ \t]*(?:(?:\*\*|\[)?REQ-\d+|\[[ xX]\])[^\n]*?(?:\betc\.|\bas needed\b|\bappropriate(?:ly)?\b|\bhandle (?:all )?errors\b)'
flags: im
match: not_contains
target: {source: file, path: textkit/docx/features/01-csv-export/requirements.md}
arm: both
---
