# Kisune — Claude Code Plugins

Two plugins for Claude Code: **trading analysis** and **dev-workflow** toolkit.

## Install

### Option 1: Plugin Marketplace (recommended)

```bash
# Add this repo as a marketplace, then install
/plugin marketplace add xbklairith/kisune
/plugin install trading@xbklairith-kisune
/plugin install dev-workflow@xbklairith-kisune
```

### Option 2: Local Development

```bash
# Clone and cd — plugins auto-load from this directory
git clone git@github.com:xbklairith/kisune.git && cd kisune

# Or load a specific plugin for testing
claude --plugin-dir ./dev-workflow
```

---

## Trading Plugin

4 skills that auto-activate via natural language.

| Skill | Triggers | What it does |
|-------|----------|-------------|
| `analyze` | "analyze BTC", "check this chart" | Technical indicators, S/R, multi-timeframe |
| `research` | "document my strategy" | Systematic strategy documentation |
| `pattern` | "what pattern is this?" | Chart pattern identification |
| `translate` | "convert to Python" | Strategy to Python + Pine Script |

---

## Dev-Workflow Plugin

12 skills, 8 agents, 1 command. Language-agnostic, focused on spec-driven development discipline.

### Command

```
/dev-workflow:spec    # Launch spec-driven workflow (interactive menu)
```

### Skills by Category

**Bootstrap**
| Skill | Triggers |
|-------|----------|
| `using-kisune` | Session start; enforces skill-check before any action |

**Planning**
| Skill | Triggers |
|-------|----------|
| `spec-driven-planning` | "plan new feature", "create specs" |
| `brainstorming` | "not sure how to approach this" |

**Implementation**
| Skill | Triggers |
|-------|----------|
| `spec-driven-implementation` | "implement this", "let's code" |
| `test-driven-development` | "implement feature", "fix this bug" |
| `spawn-agents` | 2+ independent problems, parallel investigation |

**Quality**
| Skill | Triggers |
|-------|----------|
| `review` | "review my code", "check this" |
| `security-review` | "check security", handles auth/input code |
| `git-workflow` | "commit", "create PR", "push" |
| `completion-validation` | "done", "ready to commit", before any success claim |
| `systematic-testing` | "write tests", "debug this" |
| `skill-maker` | "create a skill", "edit skill" |

### Agents (auto-activate proactively)

| Agent | When it activates |
|-------|------------------|
| `architect` | Planning new features, architectural decisions |
| `build-error-resolver` | Build fails, compilation errors |
| `code-reviewer` | After writing or modifying code |
| `database-reviewer` | Writing SQL, designing schemas |
| `planner` | Complex feature requests, large refactors |
| `refactor-cleaner` | Dead code, duplicates, unused dependencies |
| `security-reviewer` | Auth code, user input, API endpoints |
| `tdd-guide` | New features, bug fixes, refactoring |

---

## Stats

- **24 skills** (4 trading + 20 dev-workflow)
- **8 agents** (proactive, auto-activate)
- **1 command** (`/dev-workflow:spec`)
- **51 files**, ~9,600 lines
- Language-agnostic, spec-compliant

## License

MIT
