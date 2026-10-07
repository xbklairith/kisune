---
name: research
description: "Turns a trading idea into a documented strategy — edge hypothesis, statistical validation, and entry, exit, and risk rules. Use when the user has a new trading idea, wants to document or formalize a strategy, or asks whether a trading edge is real."
---

# Strategy Research

Turn a trading idea into a documented strategy whose rules are exact enough to code and whose edge has a stated reason to exist.

## 1. Edge hypothesis

Before any rules, answer from first principles:

- **What is the mechanism?** Who is on the other side of the trade, and why do they overpay or undersell (forced liquidations, behavioural overreaction, liquidity provision, structural flows)?
- **Why hasn't it been arbitraged away?** Capacity, cost, risk, or crowding that keeps professionals out.
- **When does it stop working?** The regime change that kills it, and how you would notice.

**Red flags — push back when you see them:** one indicator and no mechanism; works only in one historical window; many conditions (overfitting); vague rules ("enter when momentum is strong"); claimed win rates of 90%+; no risk rules; anything that cannot be backtested objectively.

## 2. Rules

Pin down each element exactly enough that two people would code it the same way:

| Element | Must state |
|---|---|
| Entry | indicator settings and timeframes, the trigger, confirmations, and when the order goes in (candle close, next open, limit) |
| Exit | stop placement and type (fixed, technical, ATR, time); profit exit (target, signal, trailing); partials |
| Sizing | a formula: `size = (equity × risk%) / (entry − stop)` or the volatility-adjusted equivalent |
| Exposure | max simultaneous and correlated positions; daily/weekly loss limits; pause rule |
| Filters | regime, session, volatility, and news conditions under which it does NOT trade |
| Markets | instruments, timeframes, liquidity needed |

Ask the user only what you cannot reasonably choose. When they are unavailable, choose, mark each choice as an **assumption** in the document, and list them together.

## 3. Validation

- **Expectancy:** win rate × avg win − loss rate × avg loss > costs. A 40% win rate needs avg win > 1.5 × avg loss to break even. Check whether the stop and target distances make the required win rate plausible.
- **Costs:** fees, spread, slippage, and funding at the intended size.
- **Sample:** 100+ trades, across more than one regime; out-of-sample or walk-forward before trusting parameters.
- **Execution and psychology:** can it be monitored and executed in the required hours, and can the user sit through the expected drawdown and losing streaks?

Give an honest verdict: the strongest argument against the strategy and what result would make you abandon it.

## 4. Document

Copy the template at `<base>/../../templates/strategy-doc.md` (where `<base>` is this skill's base directory) and fill **every** section. Delete a section that does not apply rather than leave a bracketed placeholder such as `[Number]`. Add a "Why it might not work" subsection under the edge hypothesis.

Save to `docx/strategies/<strategy-name>.md` (lowercase, hyphenated; create the directory if needed). For a backtest results write-up, use `<base>/../../templates/backtest-results.md`.

To turn the document into code, use the `translate` skill.
