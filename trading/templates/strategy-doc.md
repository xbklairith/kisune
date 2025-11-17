# Strategy: [Strategy Name]

**Created:** [Date]
**Last Updated:** [Date]
**Status:** [Research/Backtesting/Paper Trading/Live]
**Markets:** [Stocks/Crypto/Forex/Commodities]
**Timeframe:** [Primary timeframe]

---

## Edge Hypothesis

### What is the edge?
[Describe the market inefficiency being exploited]

### Why should this work?
[Logical basis for the edge - behavioral patterns, liquidity dynamics, market structure, etc.]

### Market conditions where it works best:
- [Condition 1: e.g., Trending markets with clear momentum]
- [Condition 2: e.g., Medium to high volatility environments]
- [Condition 3: e.g., During high liquidity sessions]

---

## Entry Rules

### Prerequisites
- [ ] [Condition 1: e.g., Daily trend is bullish (price above 200 MA)]
- [ ] [Condition 2: e.g., 4H timeframe shows higher highs and higher lows]
- [ ] [Condition 3: e.g., No major news events in next 24 hours]

### Entry Trigger
[Exact conditions that trigger entry - be specific, no ambiguity]

1. [Indicator/Pattern requirement: e.g., RSI crosses above 50 on 4H chart]
2. [Confirmation requirement: e.g., MACD histogram turns positive]
3. [Price action requirement: e.g., Price breaks above prior swing high]
4. [Volume requirement: e.g., Volume exceeds 1.5x 20-period average]

### Entry Execution
- **Order Type:** [Market/Limit/Stop]
- **Timing:** [Immediate/Wait for candle close/Next candle open]
- **Partial Entry:** [Yes/No - if yes, describe scaling approach]

---

## Exit Rules

### Stop Loss
- **Placement:** [Specific rule: e.g., Below entry candle low OR 2x ATR from entry, whichever is closer]
- **Type:** [Fixed/Technical/Trailing]
- **Maximum Risk:** [% or $: e.g., 1% of account or $100 maximum]

### Profit Targets
- **Target 1:** [Level/Ratio: e.g., 1:2 R:R or nearest resistance] - [% of position: e.g., 50%]
- **Target 2:** [Level/Ratio: e.g., 1:3 R:R or measured move] - [% of position: e.g., 30%]
- **Target 3:** [Level/Ratio: e.g., 1:5 R:R or major resistance] - [% of position: e.g., 20%]

### Trailing Stop
[If applicable, describe trailing mechanism]
- [e.g., After Target 1 hit, move stop to breakeven]
- [e.g., After Target 2 hit, trail stop at 1x ATR below price]

### Time-Based Exit
[If applicable, describe time stop]
- [e.g., Exit at market close if position held overnight and strategy is intraday]
- [e.g., Exit after 20 bars if no progress toward Target 1]

---

## Risk Management

### Position Sizing
- **Risk per trade:** [% or $: e.g., 1% of account balance]
- **Calculation method:** [Formula: e.g., (Account × 1%) / (Entry - Stop) = Position Size]

### Exposure Limits
- **Max simultaneous positions:** [Number: e.g., 3]
- **Max correlated positions:** [Number: e.g., No more than 2 positions in same sector/asset class]
- **Max sector/market exposure:** [%: e.g., No more than 30% of account in crypto]

### Drawdown Rules
- **Daily loss limit:** [% or $: e.g., 3% of account or 3 consecutive losses]
- **Weekly loss limit:** [% or $: e.g., 5% of account]
- **Strategy pause threshold:** [Condition to stop trading: e.g., Drawdown exceeds 10% or 5 consecutive losses]

---

## Filters & Conditions

### Market Regime Filter
- **Trade when:** [Market conditions: e.g., VIX below 30, uptrend on daily, medium-high volume]
- **Avoid when:** [Market conditions: e.g., Major news events, low liquidity, choppy/ranging price action]

### Time Filters
- **Trade during:** [Sessions/Hours: e.g., US market hours 9:30 AM - 4:00 PM EST]
- **Avoid during:** [Sessions/Hours/Events: e.g., First/last 15 minutes of session, FOMC announcements]

### Volatility Filters
- **Minimum volatility:** [ATR or other metric: e.g., ATR > 0.5% of price]
- **Maximum volatility:** [ATR or other metric: e.g., ATR < 3% of price]

---

## Backtest Plan

### Data Requirements
- **Time period:** [Date range: e.g., 2020-01-01 to present]
- **Minimum sample size:** [Number of trades: e.g., 100 trades minimum]
- **Markets to test:** [List: e.g., BTC/USDT, ETH/USDT, SPY, QQQ]

### Metrics to Track
- [ ] Win rate (target: >40% for 2:1 R:R strategies)
- [ ] Average win vs average loss (target: avg win > 2x avg loss)
- [ ] Profit factor (target: >1.5)
- [ ] Sharpe ratio (target: >1.0)
- [ ] Maximum drawdown (target: <20%)
- [ ] Average trade duration
- [ ] Expectancy per trade (target: positive)
- [ ] Recovery factor (net profit / max drawdown)

### Success Criteria
[What results would validate this strategy?]
- Minimum win rate: [%: e.g., 40%]
- Minimum profit factor: [Number: e.g., 1.5]
- Maximum drawdown: [%: e.g., 20%]
- Minimum Sharpe ratio: [Number: e.g., 1.0]

---

## Implementation Checklist

### Pre-Launch
- [ ] Strategy fully documented with clear rules
- [ ] Backtested with sufficient sample size (100+ trades)
- [ ] Positive expectancy confirmed across multiple markets/periods
- [ ] Risk management rules defined and tested
- [ ] Execution plan created (order types, entry timing)
- [ ] Code/indicators set up (if automated or semi-automated)
- [ ] Slippage and commission costs accounted for

### Paper Trading
- [ ] Run strategy in paper trading for [X weeks/months: e.g., 4 weeks]
- [ ] Track all trades in journal with screenshots
- [ ] Verify execution matches backtesting assumptions
- [ ] Confirm psychological readiness (can follow rules consistently)
- [ ] Achieve similar results to backtest (within reasonable variance)

### Live Trading
- [ ] Start with minimum position size (e.g., 0.25x normal size)
- [ ] Gradually scale up after [X] successful trades (e.g., 10 winning trades)
- [ ] Review performance weekly (compare to backtest expectations)
- [ ] Adjust if market regime shifts (pause if conditions change)
- [ ] Keep detailed trade journal (entries, exits, emotions, lessons)

---

## Notes & Observations

[Space for ongoing notes, improvements, and observations]

### Strengths
- [What works well with this strategy]

### Weaknesses
- [What doesn't work or needs improvement]

### Improvements to Test
- [Ideas for refinement or optimization]

### Market Observations
- [Patterns noticed, correlations, regime changes]

---

## Version History

- **v1.0** ([Date]): Initial strategy documentation
- **v1.1** ([Date]): [Description of changes]
- **v2.0** ([Date]): [Major revision description]
