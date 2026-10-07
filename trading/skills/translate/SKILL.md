---
name: translate
description: "Converts a strategy document into lookahead-free backtest code in Python and TradingView Pine Script v6. Use when the user wants a strategy coded, backtested, or turned into a TradingView indicator or strategy."
---

# Strategy Translator

Turn a strategy document into backtest code (Python) or TradingView code (Pine Script) that does exactly what the document says, with no information from the future.

## Workflow

1. **Read the strategy document.** List every rule: indicators and settings, entry trigger, order timing, stop, exits, sizing, costs, filters.
2. **Resolve gaps.** Where the document is ambiguous, pick the conventional reading, and list each choice in your reply and in the code's module docstring.
3. **Write the code** following the rules below.
4. **Run it.** Execute it on the user's data (or a small synthetic series if none) and report the trade count, win rate, net return, and max drawdown, plus anything suspicious (zero trades, every bar a trade, returns far too good to be true).

## Backtest rules (non-negotiable)

- **No lookahead.** A signal computed from a candle's close fills at the NEXT candle's open (`shift(1)`, a pending order consumed next bar, or index `i + 1`). Never fill at the signal bar's own open or close. Higher-timeframe values (a daily MA on 4H bars) come only from completed bars.
- **Standard indicator math.** RSI and ATR use Wilder smoothing (`ewm(alpha=1/n, adjust=False)`); ATR uses true range. State any non-standard choice.
- **Stops are intrabar.** Compare each later bar's low (high for shorts) with the stop; if the bar opens beyond it, fill at the open, not the stop price.
- **Costs.** Apply fees per side and a slippage parameter on every fill.
- **One place for parameters.** Periods, thresholds, multipliers, risk %, and fees live in a parameters object or the function signature, not as literals in the logic.
- **Fail loudly on bad input.** Check required columns and sort by time; reject empty data.

## Python

Use pandas and numpy when installed; otherwise write the same structure in the standard library and do not install packages without asking. Structure: `calculate_indicators()`, `entry_signal()`, `exit_signal()`, `position_size()`, and a `backtest()` loop that tracks equity and returns the trade list, plus a `__main__` that runs it on a CSV path.

## Pine Script

Write Pine Script v6 (`//@version=6`) unless the user's existing scripts use v5.

- Use `strategy()` with `commission_type`, `commission_value`, and `slippage` set from the document.
- Put every parameter in an `input.*()` call.
- The default `process_orders_on_close=false` fills on the next bar's open, so keep it.
- For higher timeframes, use `request.security(syminfo.tickerid, "D", ta.sma(close, 200)[1], lookahead = barmerge.lookahead_on)`, the documented non-repainting pattern. Otherwise leave the default `lookahead_off`.
- Plot the indicators and mark entries and exits.

## Reply

Give file paths, how to run the code, the assumptions list, the run results, and known limitations (for example, a 4H MA standing in for a daily one, or no funding costs).
