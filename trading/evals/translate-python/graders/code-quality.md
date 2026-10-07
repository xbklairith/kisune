---
type: llm
focus: {source: file, path: strategy.py}
arm: both
---

Judge only these two points; ignore style and everything else.

Pass only if BOTH hold:
1. No lookahead: an entry or take-profit signal computed from a candle's close is filled at a LATER candle's open (e.g. via shift(1), a pending flag consumed on the next iteration, or index i+1), never at the signal candle's own open or close.
2. The stop price is the fill price (or signal close) minus a multiple of ATR, and a stop-out is detected by comparing a later candle's low to that stop.
