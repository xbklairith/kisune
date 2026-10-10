---
type: regex
pattern: '^(?=[\s\S]*\bmay help consolidate\b|[\s\S]*\bmay consolidate\b|[\s\S]*\bmay help\b)(?=[\s\S]*\bmay not\b|[\s\S]*\bmight not\b|[\s\S]*\bunclear whether\b)(?=[\s\S]*\bone study\b|[\s\S]*\ba study\b)'
flags: i
target: {source: file, path: notes/sleep-memory.md}
arm: both
---
