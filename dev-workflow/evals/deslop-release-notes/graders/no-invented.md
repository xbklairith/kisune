---
type: llm
focus: {source: file, path: proj/CHANGELOG.md}
arm: both
---

Judge only the v0.5.0 section. Its source is five commits: rows streamed in export_csv() instead of loading the whole file; --delimiter accepts \t; 6 tests for export edge cases (empty file, BOM, CRLF); Python 3.8 support dropped; crash on an empty column header fixed (#88).

Pass unless the section claims something those commits do not say, such as a performance number, a memory limit, a migration step, a date, or a benefit stated as fact ("much faster", "for large files").
