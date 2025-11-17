# Claude Code Plugins - Installation Guide

**Date:** 2025-11-17
**Plugins:** `trading` and `dev-workflow`

## Overview

You now have two custom Claude Code plugins ready to install:

1. **Trading Plugin** - Market analysis and strategy research toolkit
2. **Dev-Workflow Plugin** - Integrated development lifecycle with spec-driven methodology

---

## Installation Steps

### Option 1: Local Development/Testing (Recommended First)

Both plugins are already in your project directory. To use them locally for testing:

```bash
# Current location:
# - /Users/xb/table/kisune/trading/
# - /Users/xb/table/kisune/dev-workflow/

# Test them directly from here first
cd /Users/xb/table/kisune
```

### Option 2: Install to Claude Code Global Plugins

Once you've tested and are ready to use globally:

```bash
# Create plugins directory if it doesn't exist
mkdir -p ~/.claude/plugins

# Copy plugins to Claude Code plugins directory
cp -r /Users/xb/table/kisune/trading ~/.claude/plugins/trading
cp -r /Users/xb/table/kisune/dev-workflow ~/.claude/plugins/dev-workflow

# Verify installation
ls -la ~/.claude/plugins/
```

### Option 3: Create Plugin Marketplace (Advanced)

To share your plugins or install them via `/plugin` command:

1. Create a GitHub repository for your plugins
2. Add a `.claude-plugin/marketplace.json` file
3. Push both plugins to the repository
4. Register your marketplace in Claude Code:
   ```bash
   /plugin marketplace add your-username/your-repo-name
   ```

---

## Before First Use

### Customize Plugin Metadata

Both plugins have placeholder author information. Update before using:

#### Trading Plugin
Edit `trading/.claude-plugin/plugin.json`:
```json
{
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "homepage": "https://github.com/your-username/your-repo",
  "repository": "https://github.com/your-username/your-repo"
}
```

#### Dev-Workflow Plugin
Edit `dev-workflow/.claude-plugin/plugin.json`:
```json
{
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "homepage": "https://github.com/your-username/your-repo",
  "repository": "https://github.com/your-username/your-repo"
}
```

---

## Verification

### Check Plugin Files

**Trading Plugin (14 files):**
```bash
ls -R trading/
# Should see:
# - .claude-plugin/plugin.json
# - 4 skills (market-analysis, strategy-research, pattern-recognition, strategy-translator)
# - 4 commands (analyze.md, research.md, pattern.md, translate.md)
# - 3 templates (strategy-doc.md, backtest-results.md, pattern-library.md)
# - README.md
```

**Dev-Workflow Plugin (12 files):**
```bash
ls -R dev-workflow/
# Should see:
# - .claude-plugin/plugin.json
# - 5 skills (spec-driven, code-quality, git-workflow, documentation, systematic-testing)
# - 2 commands (spec.md, review.md)
# - 3 templates (requirements.md, design.md, tasks.md)
# - README.md
```

### Validate JSON/YAML Syntax

```bash
# Validate trading plugin.json
python3 -m json.tool trading/.claude-plugin/plugin.json > /dev/null && echo "✓ Trading plugin.json valid"

# Validate dev-workflow plugin.json
python3 -m json.tool dev-workflow/.claude-plugin/plugin.json > /dev/null && echo "✓ Dev-workflow plugin.json valid"

# Check for YAML frontmatter in skills (manual inspection)
head -n 10 trading/skills/market-analysis/SKILL.md
head -n 10 dev-workflow/skills/spec-driven/SKILL.md
```

---

## Quick Start

### Trading Plugin

#### 1. Analyze a Market
```
/trading:analyze BTC/USDT 4H technical
```

#### 2. Research a Strategy
```
/trading:research
[Follow interactive prompts to document your strategy]
```

#### 3. Identify Patterns
```
/trading:pattern
[Describe chart or paste screenshot for pattern identification]
```

#### 4. Translate Strategy to Code
```
/trading:translate
[Provide strategy document to generate Python and Pine Script]
```

**Natural Language Usage:**
- "Analyze the SPY daily chart with technical indicators"
- "Help me document my RSI mean reversion strategy"
- "What chart pattern is forming on EUR/USD?"
- "Convert my strategy doc to Python code"

---

### Dev-Workflow Plugin

#### 1. Start New Feature (Spec-Driven)
```
/dev-workflow:spec "user authentication"
```

This will guide you through:
1. Feature creation
2. Requirements (EARS format)
3. Technical design
4. Task breakdown (TDD)
5. Implementation

#### 2. Code Review
```
/dev-workflow:review
[Reviews current staged changes with comprehensive checklist]
```

Or review specific file:
```
/dev-workflow:review src/auth/login.py
```

**Natural Language Usage:**
- "Let's plan a new payment processing feature" → Spec-driven skill activates
- "Review my code changes" → Code quality skill activates
- "Help me write better commit messages" → Git workflow skill activates
- "Document this function" → Documentation skill activates
- "I have a bug in the authentication flow" → Systematic testing skill activates

---

## Integration with Existing Workflows

### Dev-Workflow + Your Current Setup

The dev-workflow plugin integrates with your existing:
- `/x:spec/*` commands → Now unified in `/dev-workflow:spec`
- Superpowers skills → Optional enhancement (auto-detected)
- `docx/features/` structure → Continues to use this

**Migration Path:**
1. Keep using `/x:spec/*` commands (they still work)
2. Try `/dev-workflow:spec` for new features
3. Gradually transition as you become comfortable
4. Eventually deprecate old commands

---

## Testing Checklist

Before committing to using the plugins, test each feature:

### Trading Plugin Testing
- [ ] Install plugin (local or global)
- [ ] Run `/trading:analyze` on a market you trade
- [ ] Run `/trading:research` and document a test strategy
- [ ] Run `/trading:pattern` with a chart description
- [ ] Run `/trading:translate` with your test strategy
- [ ] Verify natural language activation works
- [ ] Check template accessibility
- [ ] Review generated code quality

### Dev-Workflow Plugin Testing
- [ ] Install plugin (local or global)
- [ ] Run `/dev-workflow:spec` and create test feature
- [ ] Go through all five phases (requirements → design → tasks → execute)
- [ ] Test EARS requirements format
- [ ] Run `/dev-workflow:review` on sample code
- [ ] Make a commit and verify git-workflow skill activates
- [ ] Ask for documentation and verify doc skill activates
- [ ] Test TDD workflow guidance
- [ ] Verify integration with existing `/x:spec/*` commands
- [ ] Check templates are comprehensive

---

## Troubleshooting

### Plugin Not Found
```bash
# Verify plugin location
ls -la ~/.claude/plugins/trading
ls -la ~/.claude/plugins/dev-workflow

# Or check current directory
ls -la /Users/xb/table/kisune/trading
ls -la /Users/xb/table/kisune/dev-workflow
```

### Commands Not Appearing
1. Restart Claude Code
2. Check plugin.json is valid JSON
3. Verify directory structure is correct
4. Ensure `.claude-plugin` directory exists

### Skills Not Activating
1. Check YAML frontmatter in SKILL.md files
2. Verify description field clearly states activation triggers
3. Try using more explicit language (e.g., "analyze this market" vs "what do you think")

### YAML/JSON Errors
```bash
# Validate JSON
python3 -m json.tool plugin.json

# Check YAML frontmatter (look for --- markers)
head -n 15 skills/*/SKILL.md
```

---

## Next Steps

1. **Customize Metadata**
   - Update author info in both plugin.json files
   - Add repository URLs

2. **Test Locally**
   - Run through testing checklist above
   - Document any issues or improvements

3. **Refine Based on Usage**
   - Adjust skill descriptions if activation isn't working well
   - Add examples to skills that need clarification
   - Customize templates to your workflow

4. **Optional: Create Marketplace**
   - Create GitHub repository
   - Add marketplace.json
   - Share with community

5. **Version Control**
   - Commit plugins to your repo
   - Tag versions as you improve them
   - Track changes in README

---

## File Locations

```
/Users/xb/table/kisune/
├── trading/                    # Trading plugin
│   ├── .claude-plugin/
│   ├── skills/ (4)
│   ├── commands/ (4)
│   ├── templates/ (3)
│   └── README.md
├── dev-workflow/               # Dev-workflow plugin
│   ├── .claude-plugin/
│   ├── skills/ (5)
│   ├── commands/ (2)
│   ├── templates/ (3)
│   └── README.md
└── docx/
    └── plans/
        ├── 2025-11-17-trading-plugin-design.md
        ├── 2025-11-17-trading-plugin-implementation.md
        ├── 2025-11-17-dev-workflow-plugin-design.md
        └── 2025-11-17-dev-workflow-plugin-implementation.md
```

---

## Support & Documentation

### Full Documentation
- **Trading Plugin**: `trading/README.md` (606 lines)
- **Dev-Workflow Plugin**: `dev-workflow/README.md` (739 lines)

### Design Documents
- **Trading Design**: `docx/plans/2025-11-17-trading-plugin-design.md`
- **Dev-Workflow Design**: `docx/plans/2025-11-17-dev-workflow-plugin-design.md`

### Implementation Plans
- **Trading Implementation**: `docx/plans/2025-11-17-trading-plugin-implementation.md`
- **Dev-Workflow Implementation**: `docx/plans/2025-11-17-dev-workflow-plugin-implementation.md`

---

## Summary

**Two complete, production-ready plugins:**

1. **Trading Plugin** (14 files, 3,499 lines)
   - Multi-market analysis
   - Strategy research framework
   - Pattern recognition and library
   - Code generation (Python + Pine Script)

2. **Dev-Workflow Plugin** (12 files, 5,116 lines)
   - Spec-driven development (5 phases)
   - Code quality reviews (25-point checklist)
   - Smart git workflows
   - Documentation generation
   - Systematic testing and debugging

**Ready to install and use!** 🚀
