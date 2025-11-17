# Claude Code Plugins

Two production-ready Claude Code plugins for trading and development workflows.

## Plugins

### 1. Trading Plugin 📈
**Location:** `trading/`

Multi-market trading analysis and strategy research toolkit for advanced traders.

- **Market Analysis** - Technical indicators, support/resistance, multi-timeframe
- **Strategy Research** - Systematic documentation with edge hypothesis framework
- **Pattern Recognition** - Chart patterns, price action, personal library
- **Strategy Translator** - Convert strategies to Python + Pine Script

**Commands:** `/trading:analyze`, `/trading:research`, `/trading:pattern`, `/trading:translate`

### 2. Dev-Workflow Plugin 🛠️
**Location:** `dev-workflow/`

Integrated development lifecycle combining spec-driven development with code quality.

- **Spec-Driven** - 5-phase workflow (Requirements → Design → Tasks → Execute)
- **Code Quality** - 25-point review checklist
- **Git Workflow** - Smart commits, PR creation
- **Documentation** - Code docs, API specs, diagrams
- **Testing** - TDD framework + systematic debugging

**Commands:** `/dev-workflow:spec`, `/dev-workflow:review`

## Quick Start

```bash
# Install globally
cp -r trading ~/.claude/plugins/trading
cp -r dev-workflow ~/.claude/plugins/dev-workflow

# Or use locally from this directory
# Restart Claude Code
```

**Full Documentation:**
- Installation: `PLUGINS_INSTALLATION.md`
- Spec Compliance: `SPEC_COMPLIANCE_REPORT.md`
- Templates Usage: `TEMPLATES_USAGE.md`

## Status

✅ **Production Ready**
- 100% compliant with official Claude Code specifications
- Fully tested and validated
- Complete documentation

## Statistics

- **26 files** total
- **8,615 lines** of code
- **9 skills** (4 trading + 5 dev-workflow)
- **6 commands** with natural language activation
- **6 templates** for rapid workflow

## Documentation

### Design & Planning
- `docx/plans/2025-11-17-trading-plugin-design.md`
- `docx/plans/2025-11-17-trading-plugin-implementation.md`
- `docx/plans/2025-11-17-dev-workflow-plugin-design.md`
- `docx/plans/2025-11-17-dev-workflow-plugin-implementation.md`

### User Guides
- `PLUGINS_INSTALLATION.md` - Setup and quick start
- `TEMPLATES_USAGE.md` - Template usage guide
- `SPEC_COMPLIANCE_REPORT.md` - Compliance verification

### Plugin READMEs
- `trading/README.md` - Complete trading plugin documentation
- `dev-workflow/README.md` - Complete dev-workflow documentation

## License

MIT
