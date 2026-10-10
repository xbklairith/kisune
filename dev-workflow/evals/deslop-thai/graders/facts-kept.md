---
type: regex
pattern: '^(?=[\s\S]*`DATABASE_URL`)(?=[\s\S]*`\.env`)(?=[\s\S]*`make migrate`)(?=[\s\S]*`docker compose up -d`)(?=[\s\S]*8080)(?=[\s\S]*v2\.3)(?=[\s\S]*backup|[\s\S]*สำรอง)'
flags: i
target: {source: file, path: docs/deploy-guide.md}
arm: both
---
