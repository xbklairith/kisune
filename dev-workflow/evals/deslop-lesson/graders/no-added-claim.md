---
type: regex
pattern: 'why (plants|leaves|they) (look|are|appear)|that.s why|this is why'
flags: i
match: not_contains
target: {source: file, path: notes/photosynthesis.md}
arm: both
---
