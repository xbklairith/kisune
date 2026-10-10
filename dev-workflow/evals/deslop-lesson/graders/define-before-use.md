---
type: regex
pattern: '^(?:(?!chloroplast)[\s\S])*chloroplasts?\b[^.\n]*(?:is|are|:|—|,)\s*(?:a |the )?(?:small |tiny )?(?:structure|part|organelle)'
flags: i
target: {source: file, path: notes/photosynthesis.md}
arm: both
---
