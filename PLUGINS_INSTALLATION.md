# Installation Guide

## Quick Start

### Option 1: Plugin Marketplace (recommended for sharing)

If this repo is on GitHub:

```bash
# In Claude Code, add this repo as a marketplace
/plugin marketplace add xbklairith/kisune

# Install the plugins
/plugin install trading@xbklairith-kisune
/plugin install dev-workflow@xbklairith-kisune
```

### Option 2: Local Development (for testing)

```bash
# Clone and cd — plugins auto-load from this directory
git clone git@github.com:xbklairith/kisune.git
cd kisune

# Or load a specific plugin for testing
claude --plugin-dir ./dev-workflow
```

---

## Verify Installation

In Claude Code, check that skills appear:

```
/dev-workflow:spec          # Should show spec-driven workflow menu
/dev-workflow:review        # Should activate code review
```

Skills also auto-activate via natural language:
- "Review my code" → `review` skill activates
- "Plan a new feature" → `spec-driven-planning` activates
- "Analyze BTC daily chart" → `analyze` skill activates

---

## Troubleshooting

**Skills not appearing:**
- Restart Claude Code after installation
- Verify SKILL.md files exist in the correct paths
- Run `/context` to check if skills are loaded

**Plugin not found:**
- Ensure `.claude-plugin/plugin.json` exists in the plugin directory
- Check JSON syntax: `python3 -m json.tool .claude-plugin/plugin.json`

**Agents not triggering:**
- Agents activate proactively — they don't have `/` commands
- They trigger based on context (e.g., `code-reviewer` after code changes)

---

## Directory Structure

```
kisune/
├── trading/                    # Trading plugin
│   ├── .claude-plugin/         # Plugin manifest
│   ├── skills/ (4)             # analyze, research, pattern, translate
│   └── templates/ (3)
├── dev-workflow/               # Dev-workflow plugin
│   ├── .claude-plugin/         # Plugin manifest
│   ├── skills/ (20)            # All dev-workflow skills
│   ├── agents/ (8)             # Proactive agents
│   ├── commands/ (1)           # /dev-workflow:spec
│   └── templates/ (3)
└── docx/                       # Feature specs and plans
```
