---
type: regex
pattern: '^(?=[\s\S]*6CO2 \+ 6H2O \+ light → C6H12O6 \+ 6O2)(?=[\s\S]*chloroplast)(?=[\s\S]*chlorophyll)(?=[\s\S]*\bred\b)(?=[\s\S]*\bblue\b)(?=[\s\S]*green)(?=[\s\S]*glucose)(?=[\s\S]*oxygen)'
flags: i
target: {source: file, path: notes/photosynthesis.md}
arm: both
---
