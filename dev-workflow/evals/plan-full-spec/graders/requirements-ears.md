---
# At least five requirement lines read "- [REQ-NNN] WHEN|WHILE|IF|WHERE|The
# system ... SHALL ...", and no line that starts with a requirement ID is in
# another form. Bold IDs (**REQ-001:**) count too.
type: regex
pattern: '(?<![\s\S])(?![\s\S]*^[ \t]*[-*][ \t]*(?:\*\*|\[)?REQ-\d+(?!\d|[\]*: \t]*(?:WHEN|WHILE|IF|WHERE|The system)\b[^\n]*\bSHALL\b))(?:[\s\S]*?^[ \t]*[-*][ \t]*(?:\*\*|\[)?REQ-\d+[\]*: \t]*(?:WHEN|WHILE|IF|WHERE|The system)\b[^\n]*\bSHALL\b){5}'
flags: m
target: {source: file, path: textkit/docx/features/01-csv-export/requirements.md}
arm: both
---
