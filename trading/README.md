# Trading Plugin for Claude Code

A comprehensive trading analysis and strategy research toolkit for advanced traders. Analyze markets, research strategies, identify patterns, and translate strategies into code across stocks, crypto, forex, and commodities.

## Overview

The **trading** plugin provides four specialized skills to help traders:
1. **Analyze markets** with technical indicators, patterns, and multi-timeframe analysis
2. **Research strategies** systematically with edge validation and documentation
3. **Recognize patterns** across charts and build a personal pattern library
4. **Translate strategies** from documentation into Python or Pine Script code

Perfect for traders who want to systematically develop, document, and implement trading strategies with a focus on edge identification and risk management.

---

## Installation

### Install the Plugin

```bash
# Option 1: Plugin marketplace (recommended)
/plugin marketplace add xbklairith/kisune
/plugin install trading@xbklairith-kisune

# Option 2: Clone repo and cd — plugins auto-load
git clone git@github.com:xbklairith/kisune.git && cd kisune
```

### Verify Installation

```bash
# List plugins to confirm installation
claude plugins list

# You should see "trading" in the list
```

The plugin will be automatically loaded on next Claude Code session start.

---

## Features

### 1. Analyze Skill

Comprehensive multi-market analysis using:
- **Technical Indicators:** RSI, MACD, Bollinger Bands, Moving Averages, Volume Analysis
- **Support/Resistance:** Identify key levels, volume nodes, Fibonacci levels
- **Chart Patterns:** Head & Shoulders, Triangles, Flags, Breakouts
- **Multi-Timeframe:** Analyze higher timeframes for context, lower for entries
- **Risk/Reward:** Calculate specific R:R ratios for trade ideas

**Outputs:** Structured markdown reports with actionable trading ideas

### 2. Research Skill

Systematic strategy development framework:
- **Edge Hypothesis:** Define what market inefficiency you're exploiting
- **Entry/Exit Rules:** Document precise, testable conditions
- **Risk Management:** Position sizing, exposure limits, drawdown rules
- **Backtest Planning:** Metrics to track, success criteria
- **Validation:** Critical thinking questions to validate edge

**Outputs:** Complete strategy documents ready for backtesting

### 3. Pattern Skill

Identify and document chart patterns:
- **Classic Patterns:** H&S, Double Tops/Bottoms, Triangles
- **Continuation Patterns:** Flags, Pennants, Wedges
- **Price Action:** Breakouts, Retests, S/R Flips
- **Multi-Timeframe:** Pattern analysis across timeframes
- **Personal Library:** Build and track your own pattern playbook

**Outputs:** Pattern documentation with entry/exit rules and trade tracking

### 4. Translate Skill

Convert strategies into code:
- **Python:** Pandas-compatible functions for custom backtesting frameworks
- **Pine Script:** TradingView indicators and strategies (v5)
- **Parameterized:** All values configurable, no hardcoding
- **Documented:** Clear docstrings and usage examples
- **Production-Ready:** Error handling, type hints, best practices

**Outputs:** Clean, reusable code ready for implementation

---

## Templates

Three comprehensive templates are included in `trading/templates/`:

### 1. Strategy Document Template
**File:** `templates/strategy-doc.md`

Complete strategy documentation template with:
- Edge hypothesis section
- Entry/exit rules
- Risk management framework
- Backtest planning
- Implementation checklist

**Use for:** Documenting any trading strategy from idea to implementation

---

### 2. Backtest Results Template
**File:** `templates/backtest-results.md`

Comprehensive backtest analysis template with:
- Performance metrics (win rate, profit factor, Sharpe, etc.)
- Equity curve analysis
- Market breakdown (by instrument, time period)
- Qualitative observations
- Next steps and refinements

**Use for:** Recording and analyzing backtest results systematically

---

### 3. Pattern Library Template
**File:** `templates/pattern-library.md`

Personal pattern library template with:
- Pattern documentation format
- Win rate and R:R tracking
- Entry/exit rules
- Trade examples (wins and losses)
- Lessons learned
- Quick reference table

**Use for:** Building your personal playbook of high-probability patterns

---

## Example Workflows

### Workflow 1: New Strategy Development

```
1. Generate Idea
   User thinks: "Mean reversion after RSI oversold might work"

2. Research Phase
   Ask Claude to research your strategy
   → Documents strategy with edge hypothesis, rules, risk management
   → Output: strategies/rsi-mean-reversion.md

3. Translation Phase
   Ask Claude to translate your strategy to code
   → Converts strategy doc to Python code
   → Output: strategy_rsi_mean_reversion.py

4. Backtest Phase (User runs in their framework)
   → Execute backtest using generated Python code
   → Record results using backtest-results template

5. Analysis Phase
   Ask Claude to analyze BTC/USDT 4H
   → Validate current market conditions match strategy criteria
   → Identify potential entry opportunities

6. Implementation
   → If backtest successful, move to paper trading
   → Track results, refine strategy
```

---

### Workflow 2: Pattern Recognition & Library Building

```
1. Identify Pattern
   Ask Claude to identify a pattern
   → User describes chart setup
   → Claude identifies pattern (e.g., Bull Flag)
   → Provides trading plan

2. Trade Execution (User executes)
   → Enter trade based on pattern rules
   → Track entry, stop, targets

3. Document Result
   → Update pattern-library.md with trade result
   → Track win rate, R:R, lessons learned

4. Iterate
   → Build library of 5-10 high-probability patterns
   → Focus on patterns with >55% win rate and >2:1 R:R
```

---

### Workflow 3: Market Analysis & Trade Planning

```
1. Daily Market Analysis
   Ask Claude to analyze BTC/USDT Daily
   → Understand higher timeframe trend and structure
   → Identify key levels

2. Entry Timing
   Ask Claude to analyze BTC/USDT 4H
   → Find entry opportunities within daily context
   → Get specific entry/stop/target levels

3. Pattern Confirmation
   Ask Claude to identify the pattern
   → Confirm pattern setup aligns with analysis
   → Validate edge and risk/reward

4. Execution
   → Enter trade with defined risk
   → Manage according to plan
```

---

## Skills

### When Skills Auto-Activate

The plugin skills will automatically activate when you:

**analyze:**
- Ask about market conditions
- Request technical analysis
- Mention support/resistance
- Ask "what's happening with [asset]?"

**research:**
- Say "I want to document a strategy"
- Ask about strategy development
- Mention "trading edge" or "hypothesis"

**pattern:**
- Describe chart patterns
- Ask "what pattern is this?"
- Want to document patterns

**translate:**
- Say "convert this strategy to code"
- Ask for Python or Pine Script
- Want to implement a strategy

---

## Best Practices

### Strategy Development

1. **Start with Edge:** Always define WHY the strategy should work
2. **Be Specific:** Vague rules = untestable strategies
3. **Risk First:** Define stop loss before profit targets
4. **Backtest:** Minimum 100 trades for statistical significance
5. **Paper Trade:** Validate in real-time before live trading

### Pattern Recognition

1. **Quality over Quantity:** Master 3-5 patterns vs. mediocre at 20
2. **Track Everything:** Win rate, R:R, market conditions
3. **Multi-Timeframe:** Higher timeframe context is critical
4. **Invalidation:** Always know when pattern has failed
5. **Update Library:** After every trade, update statistics

### Market Analysis

1. **Multiple Timeframes:** Start high (Daily), refine low (4H, 1H)
2. **Confluence:** Look for multiple factors aligning
3. **Context Matters:** Isolated patterns mean nothing
4. **Both Sides:** Identify both bull and bear scenarios
5. **Quantify:** Use specific price levels, not vague statements

### Code Translation

1. **Document First:** Complete strategy doc before coding
2. **Parameterize:** Never hardcode values
3. **Test Thoroughly:** Run on sample data before full backtest
4. **Version Control:** Keep strategy docs and code in sync
5. **Iterate:** Refine code based on backtest results

---

## Tips for Advanced Traders

### Leverage Multiple Markets

The plugin is designed for multi-market trading:
- **Crypto:** 24/7 markets, high volatility, different characteristics
- **Stocks:** Market hours, sector rotation, fundamentals matter
- **Forex:** Currency pairs, interest rate differentials, macro drivers
- **Commodities:** Supply/demand, seasonal patterns, inflation hedge

Test strategies across markets to find where edge is strongest.

### Build Your System

Use the plugin to create a complete trading system:
1. **Strategy Library:** Document all tested strategies
2. **Pattern Library:** Personal playbook of setups
3. **Analysis Framework:** Consistent market analysis approach
4. **Code Repository:** Reusable Python/Pine Script functions

### Track Performance

Create feedback loops:
- Document strategies → Backtest → Analyze results → Refine
- Identify patterns → Trade → Track stats → Update library
- Analyze markets → Enter trades → Review → Improve analysis

### Combine Skills

Most powerful when combining multiple skills:
- Use **research** to document strategy
- Use **translator** to code it
- Use **analysis** to find entries
- Use **pattern** to validate setups

---

## Troubleshooting

### Skill Not Activating

**Problem:** Skill doesn't activate when expected

**Solution:**
- Be specific in your request ("Analyze BTC/USDT" vs. "What about BTC?")
- Check that plugin is installed in correct directory

### Code Generation Issues

**Problem:** Generated code doesn't work with your framework

**Solution:**
- Specify your framework when asking Claude to translate
- Request specific library compatibility (e.g., "pandas only, no ta-lib")
- Ask for modular functions you can adapt vs. complete system

### Strategy Too Vague

**Problem:** Strategy documentation lacks specific rules

**Solution:**
- Ask Claude to research your strategy, which guides you through specific questions
- Ask Claude to challenge vague statements
- Ensure every rule is testable and quantifiable

---

## Contributing

Want to improve the trading plugin? Suggestions:

### Ideas for Enhancement

- Add sentiment analysis integration
- Include backtesting metrics calculator
- Add trade journal template
- Create position sizing calculator
- Add correlation analysis skill

### Feedback

Share your experience:
- Which skills do you use most?
- What features would be valuable?
- What markets do you trade?
- How can the plugin better serve advanced traders?

---

## Support & Resources

### Learning Resources

- [Technical Analysis Basics](https://www.investopedia.com/technical-analysis-4689657)
- [TradingView Pine Script Docs](https://www.tradingview.com/pine-script-docs/)
- [Pandas for Trading](https://pandas.pydata.org/docs/)
- [Backtest Overfitting](https://www.quantstart.com/articles/Successful-Backtesting-of-Algorithmic-Trading-Strategies-Part-I/)

### Recommended Reading

- *Technical Analysis of the Financial Markets* by John Murphy
- *Evidence-Based Technical Analysis* by David Aronson
- *Quantitative Trading* by Ernest Chan
- *Trading Systems* by Emilio Tomasini & Urban Jaekle

---

## License

MIT License - See LICENSE file for details

---

## Version History

- **v1.0.0** (2024-01-15): Initial release
  - Analyze skill (market analysis)
  - Research skill (strategy research)
  - Pattern skill (pattern recognition)
  - Translate skill (strategy translator)
  - 3 templates

---

## About

Built for advanced traders who want to systematically develop, document, and implement trading strategies with a focus on edge identification, risk management, and multi-market analysis.

**Philosophy:** Trading is a systematic, quantifiable discipline. Document everything, test rigorously, manage risk religiously, and continuously refine your edge.

---

**Happy Trading!**

Remember: No strategy works 100% of the time. Focus on positive expectancy, proper risk management, and continuous improvement. The plugin is a tool to help you think systematically - but YOU are the trader making the decisions.
