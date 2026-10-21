# Strategy: BTC RSI Dip in Uptrend

**Status:** Research
**Markets:** Crypto (BTC/USDT)
**Timeframe:** 4H

## Edge Hypothesis
In an established uptrend, short-term sellers overshoot on 4H pullbacks; trend-following buyers step back in, so oversold readings revert toward the mean.

## Entry Rules
- Trend filter: close is above the 200-period SMA of closes (the 4H series stands in for the daily 200 MA in this backtest).
- Trigger: RSI(14), Wilder smoothing, closes below 30.
- Execution: signal is evaluated on the candle close; enter long at the NEXT candle's open.

## Exit Rules
- Take profit: RSI(14) closes above 50; exit at the next candle's open.
- Stop loss: entry price minus 2 x ATR(14) measured at the signal candle; exits intrabar if the low touches it.
- One position at a time.

## Risk Management
- Risk 1% of equity per trade.
- Size = (equity x 0.01) / (entry - stop).
- Fees: 0.1% per side.
