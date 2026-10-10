---
type: regex
pattern: '^(?=[\s\S]*\./bin/migrate --to 3)(?=[\s\S]*QUEUE_MODE=durable)(?=[\s\S]*config\.toml)(?=[\s\S]*maintenance window)(?=[\s\S]*back)'
flags: i
target: {source: file, path: docs/upgrade.md}
arm: both
---
