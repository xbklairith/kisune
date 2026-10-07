---
name: analyze
description: Technical analysis with indicators (RSI, MACD, MA), support/resistance, multi-timeframe trends, and sentiment. Use when analyzing markets or interpreting charts.
---

# Market Analysis

Produce technical analysis with concrete levels, both bull and bear cases, and invalidation points. Every number must come from data.

## Data first

- **Data provided** (CSV, pasted candles, screenshot): compute indicators with code (`Bash` + Python) rather than eyeballing. State the data's last timestamp. If it is old, or looks synthetic or mislabeled, say so before the analysis.
- **Market-data tool available** (for example a TradingView or exchange connector): fetch candles for every timeframe you discuss.
- **No data and no tool:** say plainly that you cannot see the current chart. Do not state a current price, indicator reading, or support/resistance level as if read from today's chart. Ask for an export or screenshot, or explain what you would check and why. Mark any example numbers as illustrative.

## Framework

1. **Context.** Trend on the higher timeframe, the market phase (accumulation, markup, distribution, markdown), and major levels. Higher timeframes set direction; lower timeframes time entries.
2. **Indicators.** Read them for what they add, not as a checklist:
   - RSI: overbought/oversold relative to the regime, and divergences.
   - MACD: crossovers and histogram momentum.
   - Bollinger Bands: band riding vs squeeze.
   - Moving averages (20/50/200): alignment and distance from price.
   - Volume: confirmation, climax, divergence.
   - ATR: volatility and stop distance.
3. **Levels.** Swing highs and lows, round numbers, high-volume nodes, prior breakout zones, Fibonacci levels where relevant. Rank them by touches, timeframe, and volume.
4. **Patterns.** Name structure (higher highs/lows, breakouts, retests, failed breakouts). For a full pattern read, use the `pattern` skill.
5. **Conflicts.** When timeframes or indicators disagree, say which signal you weight and why. Ask what would make you wrong and whether you are seeing what you want to see.
6. **Trade ideas.** For each scenario, give the entry trigger, stop at the invalidation level, targets, and the risk:reward ratio (1:2 or better preferred). Do not present a stretched market as a fresh entry without naming the risk.

Cross-market context, where it matters:
- Crypto: BTC dominance and funding.
- Stocks: the index, sector, and VIX.
- Forex: rate differentials and the calendar.
- Commodities: seasonality and supply.

## Output

```markdown
# Market Analysis: [ASSET] | [TIMEFRAME] | data to [last candle time]

## Summary
- Trend / Phase / Bias

## Key Levels
- R1, R2 … and S1, S2 … each with its reason

## Indicators
- RSI, MACD, Bands, MAs, Volume, ATR: reading and what it implies

## Multi-Timeframe Context

## Trade Ideas
### Bullish scenario: entry trigger, stop, T1/T2 with R:R, condition
### Bearish scenario: entry trigger, stop, T1/T2 with R:R, condition

## Risk
- Volatility, conditions, confidence, and what invalidates the thesis
```

Leave out sections the data cannot support rather than filling them with guesses.
