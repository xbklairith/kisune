---
type: regex
pattern: '^(?=[\s\S]*WHEN a write to `prices` commits THEN the system SHALL invalidate the matching cache key within 1 second\.)(?=[\s\S]*The system SHALL log every invalidation with the cache key and the writer''s name\.)'
target: {source: file, path: docs/cache-outage.md}
arm: both
---
