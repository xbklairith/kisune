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

16 skills, 8 agents, 7 commands. Language-agnostic, focused on spec-driven development discipline.

### Commands

```
/dev-workflow:spec                 # Launch workflow — auto-picks Quick or Full mode
/dev-workflow:spec:create          # Create new feature specification
/dev-workflow:spec:requirements    # Define requirements using EARS format
/dev-workflow:spec:design          # Generate technical design
/dev-workflow:spec:tasks           # Break down design into TDD tasks
/dev-workflow:spec:execute         # Execute implementation with TDD
/dev-workflow:spec:list            # List all features with status
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
| `systematic-debug` | "debug this", flaky test, unknown failure |
| `post-mortem` | "write a post-mortem", after a fix lands |
| `scrutinize` | "take a hard look", "play devil's advocate", outsider review |
| `skill-maker` | "create a skill", "edit skill" |
| `spec-review` | "review this spec", "check my requirements/design" |

**Comms**
| Skill | Triggers |
|-------|----------|
| `explain-in` | "write this for the VP", "slack update", "executive summary" |

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

- **20 skills** (4 trading + 16 dev-workflow)
- **8 agents** (proactive, auto-activate)
- **7 commands** (`/dev-workflow:spec` and its 6 subcommands)
- **7 templates** (4 dev-workflow + 3 trading)
- **52 files**, ~9,600 lines
- Language-agnostic, spec-compliant

## License

MIT
