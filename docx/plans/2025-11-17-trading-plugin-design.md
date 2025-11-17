# Trading Plugin Design

**Date:** 2025-11-17
**Plugin Name:** `trading`
**Purpose:** Multi-market trading analysis and strategy research toolkit

## Overview

A Claude Code plugin for advanced traders to systematically research, analyze, and develop trading strategies across multiple markets (stocks, crypto, forex, commodities). Focuses on market analysis and strategy exploration with outputs in Markdown, Python, and Pine Script.

## Target User

- Advanced trader with existing trading bot
- Has custom backtesting framework
- Exploring new trading strategies
- Multi-market trader (stocks, crypto, forex, commodities)

## Plugin Structure

```
trading/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── market-analysis/
│   │   └── SKILL.md
│   ├── strategy-research/
│   │   └── SKILL.md
│   ├── pattern-recognition/
│   │   └── SKILL.md
│   └── strategy-translator/
│       └── SKILL.md
├── commands/
│   ├── analyze.md
│   ├── research.md
│   ├── pattern.md
│   └── translate.md
└── templates/
    ├── strategy-doc.md
    ├── backtest-results.md
    └── pattern-library.md
```

## Core Skills

### 1. Market Analysis Skill

**File:** `skills/market-analysis/SKILL.md`

**Frontmatter:**
```yaml
---
name: market-analysis
description: Analyze stocks, crypto, forex, and commodities using technical indicators, fundamentals, sentiment, and quantitative methods. Activates when user requests market analysis or chart interpretation.
version: 1.0.0
---
```

**Capabilities:**
- Technical analysis (RSI, MACD, Bollinger Bands, Volume Profile)
- Support/resistance identification
- Trend analysis and chart patterns
- Cross-market intelligence and correlations
- Quantitative metrics (volatility, volume, probability)
- Risk/reward ratio calculations

**Output:** Structured markdown report with key levels, indicators, and actionable insights

### 2. Strategy Research Skill

**File:** `skills/strategy-research/SKILL.md`

**Frontmatter:**
```yaml
---
name: strategy-research
description: Research and document trading strategies systematically. Guide hypothesis formation, edge identification, and strategy documentation. Activates when exploring new trading ideas or refining existing strategies.
version: 1.0.0
---
```

**Workflow:**
1. **Hypothesis Formation**
   - What edge is being exploited?
   - Market conditions where it works
   - Why should this work?

2. **Strategy Documentation Template**
   - Edge hypothesis
   - Entry conditions
   - Exit strategy
   - Risk management
   - Backtest considerations

3. **Edge Validation**
   - Positive expectancy check
   - Execution feasibility
   - Risk analysis

### 3. Pattern Recognition Skill

**File:** `skills/pattern-recognition/SKILL.md`

**Frontmatter:**
```yaml
---
name: pattern-recognition
description: Identify chart patterns, trading setups, and market conditions across multiple timeframes and markets. Helps document pattern characteristics and success criteria.
version: 1.0.0
---
```

**Pattern Categories:**
- Classic patterns (H&S, Double Top/Bottom, Triangles)
- Price action setups (Breakouts, Failed breakouts, Support/resistance)
- Multi-timeframe context analysis
- Pattern documentation with success criteria

### 4. Strategy Translator Skill

**File:** `skills/strategy-translator/SKILL.md`

**Frontmatter:**
```yaml
---
name: strategy-translator
description: Translate trading strategies from markdown documentation into Python code snippets and TradingView Pine Script. Generates reusable functions compatible with custom backtesting frameworks.
version: 1.0.0
---
```

**Translation Capabilities:**
- Strategy doc → Python functions (pandas-compatible)
- Strategy doc → Pine Script indicators
- Clean, parameterized, documented code
- Risk management logic included
- Edge case handling

## Slash Commands

### 1. `/trading:analyze`
Activate market-analysis skill for comprehensive market/asset analysis.

**Usage:**
- `/trading:analyze` → Prompt for asset, timeframe, analysis type
- `/trading:analyze BTC/USDT 4H` → Direct analysis

### 2. `/trading:research`
Activate strategy-research skill to document new strategy ideas.

**Guides through:**
- Edge/hypothesis definition
- Entry/exit conditions
- Risk management rules
- Backtest considerations

### 3. `/trading:pattern`
Activate pattern-recognition skill to identify or document chart patterns.

**Helps with:**
- Pattern identification
- Pattern documentation
- Trading plan creation
- Personal pattern library

### 4. `/trading:translate`
Activate strategy-translator skill to convert strategies into code.

**Outputs:**
- Python code (for custom backtesting framework)
- Pine Script (for TradingView)
- Both formats with full documentation

## Templates

### 1. Strategy Document Template
```markdown
# Strategy: [Name]
- Market, timeframe, edge hypothesis
- Entry/exit rules
- Risk management
- Backtest notes
- Implementation checklist
```

### 2. Backtest Results Template
```markdown
# Backtest Results
- Performance metrics
- Win rate, profit factor, Sharpe, drawdown
- Observations
- Next steps
```

### 3. Pattern Library Template
```markdown
# Personal Pattern Library
- Pattern name, win rate, markets
- Setup conditions
- Entry/stop/target rules
- Personal observations
```

## Example Workflow

1. **Research Phase:**
   ```
   /trading:research
   → Documents strategy hypothesis and rules
   ```

2. **Analysis Phase:**
   ```
   /trading:analyze BTC/USDT 4H
   → Analyzes current market conditions
   ```

3. **Translation Phase:**
   ```
   /trading:translate
   → Converts strategy to Python + Pine Script
   ```

4. **Backtest Phase:**
   ```
   User runs backtest in custom framework
   Documents results in backtest-results.md
   ```

## Future Extensions

**Phase 2 (Planned):**
- Real-time market monitoring skill
- Trending analysis and alerts
- Live trade journaling
- Performance analytics

**Additional Commands:**
- `/trading:monitor` - Real-time market monitoring
- `/trading:journal` - Trade journaling and review

## Design Principles

1. **Extensible** - Easy to add new skills and commands
2. **Modular** - Each skill is independent
3. **Market-Agnostic** - Core logic works across all markets
4. **Output Flexibility** - Markdown docs + Python + Pine Script
5. **Advanced Focus** - Designed for experienced traders
6. **Framework Compatible** - Works with custom backtesting systems

## Dependencies

None required. Works standalone with Claude Code.

**Optional integrations:**
- Data providers APIs (user's existing setup)
- Trading platform APIs (user's existing setup)
- Custom backtesting framework (user's existing setup)

## Success Metrics

- Faster strategy research and documentation
- Systematic approach to strategy development
- Reusable pattern library
- Seamless translation to implementation code
- Multi-market analysis capability
