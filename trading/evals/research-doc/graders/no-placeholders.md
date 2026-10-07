---
type: regex
pattern: '\[(?:Number|Date|Strategy Name|% or \$|Condition \d|Level/Ratio|Formula or approach|Sessions/Hours[^\]]*)\]'
match: not_contains
target: {source: file, path: docx/strategies/btc-rsi-dip.md}
arm: both
---
