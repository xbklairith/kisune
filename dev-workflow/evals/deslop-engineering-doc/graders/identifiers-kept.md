---
type: regex
pattern: '^(?=[\s\S]*`prices`)(?=[\s\S]*`CACHE_TTL_SECONDS`)(?=[\s\S]*900)(?=[\s\S]*`invalidate_on_write\(\)`)(?=[\s\S]*#212)(?=[\s\S]*41[ -]minute)(?=[\s\S]*bulk importer)'
target: {source: file, path: docs/cache-outage.md}
arm: both
---
