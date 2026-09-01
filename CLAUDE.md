# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains two production-ready Claude Code plugins:

1. **Trading Plugin** (`trading/`) - Multi-market trading analysis and strategy research toolkit
2. **Dev-Workflow Plugin** (`dev-workflow/`) - Integrated development lifecycle with spec-driven methodology

Both plugins are 100% compliant with official Claude Code plugin specifications.

## Repository Structure

```
kisune/
├── trading/                    # Trading plugin
│   ├── .claude-plugin/        # Plugin metadata
│   ├── skills/                # 4 skills (analyze, research, pattern, translate)
│   ├── templates/             # 3 strategy/analysis templates
│   └── README.md              # Complete documentation
├── dev-workflow/              # Dev-workflow plugin
│   ├── .claude-plugin/        # Plugin metadata
│   ├── skills/                # 23 skills (planning, implementation, quality, review, comms)
│   ├── agents/                # 8 agents (code-reviewer, tdd-guide, security-reviewer, planner)
│   ├── commands/              # 7 slash commands (spec + 6 spec:* subcommands)
│   ├── templates/             # 4 spec-driven templates
│   └── README.md              # Complete documentation
├── .claude-plugin/            # Marketplace metadata
├── docx/                      # Documentation and planning
│   └── plans/                 # Design and implementation documents
└── examples/                  # Example skills and superpowers
```

## Plugin Architecture

### Trading Plugin (4 skills, no commands)

**Skills:**
- `analyze` - Technical analysis with indicators, S/R, multi-timeframe
- `research` - Systematic strategy documentation with edge hypothesis
- `pattern` - Chart pattern identification and personal library
- `translate` - Convert strategies to Python + Pine Script

### Dev-Workflow Plugin (23 skills, 8 agents, 7 commands)

**Bootstrap:**
- `using-kisune` - Loads at session start; enforces skill-check before any action and indexes the skill registry

**Planning Skills:**
- `spec-driven-planning` - 3-phase workflow (Feature → Requirements/EARS → Design)
- `brainstorming` - Collaborative refinement for requirements and design
- `grilling` - Round-based interrogation of an existing plan (user-invoked via `/grilling`); batches the unblocked frontier, one recommended answer per question
- `grill-with-docs` - Composes `grilling` + `domain-modeling` (user-invoked via `/grill-with-docs`)
- `domain-modeling` - Glossary and ADR discipline — writes `docx/glossary.md` and `docx/decisions/NNNN-*.md`
- `codebase-design` - Deep-module vocabulary: module, interface, depth, seam, adapter
- `prototype` - Throwaway code that answers one design question, then gets deleted
- `investigate` - Research against primary sources via background agent; cited findings to `docx/research/`

**Implementation Skills:**
- `spec-driven-implementation` - Task breakdown and execution
- `test-driven-development` - Strict RED-GREEN-REFACTOR enforcement
- `spawn-agents` - Dispatch parallel subagents for independent problems; over-dispatch prevention

**Quality Skills:**
- `review` - 25-point review checklist
- `spec-review` - 3 sequential agents reviewing feature specs for spec quality, completeness, and buildability
- `security-review` - OWASP Top 10 vulnerability detection and remediation
- `git-workflow` - Smart commits, branch management, PR creation
- `completion-validation` - Evidence-before-claims gate before marking work done
- `systematic-debug` - Systematic debugging — 4-mantra discipline (reproduce, trace, falsify, breadcrumbs) + multi-layer investigation
- `post-mortem` - Engineering record of a fixed bug — root cause, mechanism, fix, validation, how it slipped through
- `scrutinize` - Deep outsider-perspective review — questions intent, traces code path end-to-end, verdict: ship/fix/rework/reject
- `skill-maker` - Create/edit skills with TDD methodology

**Communication Skills:**
- `handoff` - Compact the conversation into a handoff doc for a fresh agent (user-invoked via `/handoff`)
- `explain-in` - Rewrite technical content for leadership — shaped for Slack, JIRA, standup, email, or meeting

**Agents (proactive):**
- `code-reviewer` - Auto-reviews code after changes
- `tdd-guide` - Enforces write-tests-first methodology
- `security-reviewer` - Flags vulnerabilities in auth, input, APIs
- `planner` - Plans complex features and refactoring
- `architect` - Software architecture specialist, system design and scalability decisions
- `build-error-resolver` - Fixes build/compilation errors with minimal diffs
- `database-reviewer` - PostgreSQL/Supabase query optimization and schema design
- `refactor-cleaner` - Dead code cleanup, removes unused code and duplicates

**Commands:**
- `/dev-workflow:spec` - Launch workflow — auto-picks Quick (plan.md) or Full (3-file EARS spec) mode
- `/dev-workflow:spec:create` - Create new feature specification
- `/dev-workflow:spec:requirements` - Define requirements using EARS format
- `/dev-workflow:spec:design` - Generate technical design
- `/dev-workflow:spec:tasks` - Break down design into TDD tasks
- `/dev-workflow:spec:execute` - Execute implementation with TDD
- `/dev-workflow:spec:list` - List all features with status

**Integration Note:** The dev-workflow plugin integrates with existing `/x:spec:*` commands and uses the same `docx/features/` structure.

## Development Commands

This repository does not have traditional build/test commands as it contains plugin definitions (markdown and JSON files). However, validation can be performed:

### Validate Plugin Structure

```bash
# Validate JSON syntax
python3 -m json.tool trading/.claude-plugin/plugin.json
python3 -m json.tool dev-workflow/.claude-plugin/plugin.json
python3 -m json.tool .claude-plugin/marketplace.json

# Check file structure
ls -R trading/
ls -R dev-workflow/
```

### Test Plugins

```bash
# Option 1: Plugin marketplace (recommended)
/plugin marketplace add xbklairith/kisune
/plugin install trading@xbklairith-kisune
/plugin install dev-workflow@xbklairith-kisune

# Option 2: Local development (cd into this directory)
# Plugins auto-load when Claude Code starts in this directory
```

## Key Technical Details

### Plugin Specification Compliance

Both plugins follow the official Claude Code plugin spec:

**Directory Structure:**
- `.claude-plugin/plugin.json` - Plugin metadata (at plugin root)
- `commands/` - Slash commands (at plugin root, NOT in .claude-plugin)
- `skills/` - Skills (at plugin root)
- `agents/` - Specialized agents (at plugin root)
- `templates/` - Supporting templates (at plugin root)

**Skill Frontmatter (YAML) — 10 valid fields:**
```yaml
---
name: skill-name                    # kebab-case, max 64 chars
description: What it does           # Used for auto-activation
argument-hint: [issue-number]       # Autocomplete hint
disable-model-invocation: true      # Prevent Claude auto-loading
user-invocable: false               # Hide from / menu
allowed-tools: Read, Grep, Bash     # Tools without permission prompts
model: sonnet                       # Model override (haiku/sonnet/opus)
context: fork                       # Run in subagent
agent: Explore                      # Subagent type when context: fork
hooks: {}                           # Skill-scoped hooks
---
```

**IMPORTANT:** Only the 10 fields above are spec-compliant. Do NOT add custom fields like `version`, `dependencies`, `origin`, or `tools`.

**Agent Frontmatter — only 2 fields:**
```yaml
---
name: agent-name
description: What it specializes in
---
```

**Command Frontmatter:**
```yaml
---
description: Command description
---
```

### EARS Requirements Format

The dev-workflow plugin uses EARS (Easy Approach to Requirements Syntax) with five templates:

```
Event-Driven:   WHEN [trigger] THEN the system SHALL [response]
State-Driven:   WHILE [state] the system SHALL [requirement]
Ubiquitous:     The system SHALL [requirement]
Conditional:    IF [condition] THEN the system SHALL [requirement]
Optional:       WHERE [feature included] the system SHALL [requirement]
```

Requirements must use:
- Active voice with "SHALL" for mandatory requirements
- Specific, measurable criteria (avoid "quickly", use "within 2 seconds")
- One requirement per statement
- No ambiguous terms ("appropriate", "reasonable")

### Spec-Driven Development Workflow

The dev-workflow plugin implements a 5-phase workflow:

1. **Feature Creation** → Creates `docx/features/[NN-feature-name]/`
2. **Requirements (EARS)** → Interactive elicitation, creates `requirements.md`
3. **Technical Design** → Proposes approaches, creates `design.md`
4. **Task Breakdown** → TDD tasks with checkboxes, creates `tasks.md`
5. **Execution** → RED-GREEN-REFACTOR cycle with auto quality checks

**Approval Gates:** Always request approval before moving between phases.

### TDD Enforcement

The `test-driven-development` skill enforces strict discipline:

**Core Principle:** NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST

**Cycle:**
1. **RED** - Write failing test, verify failure
2. **GREEN** - Write minimal code to pass
3. **REFACTOR** - Clean up while keeping tests green

**Strict Rules:**
- Code written before test? Delete it. Start over.
- No "keep as reference" - delete means delete completely
- Verification checklist before marking work complete

### UltraThink Pattern

The UltraThink pattern is integrated across 8 skills to ensure deep, first-principles thinking for complex decisions:

**What is UltraThink?**
- Deep thinking pattern that questions fundamentals, not just symptoms
- Activates before major architectural, strategic, or high-stakes decisions
- Forces consideration of assumptions, second-order effects, and failure modes

**When Skills Use UltraThink:**
- **brainstorming** - Before proposing architectural approaches
- **spec-driven-planning** - Before technical design with complex architectures
- **spec-driven-implementation** - Before task breakdown for complex implementations
- **research** - Before edge hypothesis formation and validation
- **analyze** - When market conditions show conflicting signals
- **skill-maker** - Before creating new skill structures
- **pattern** - When pattern validity is ambiguous
- **review** - When architectural issues are detected

**UltraThink Process:**
1. **Trigger** - Skill identifies high-complexity decision point
2. **Announcement** - "Let me ultrathink [specific aspect] before [action]"
3. **Deep Questions** - Question assumptions, consider failure modes, think from first principles
4. **Output** - Provide decision with explicit reasoning about trade-offs

**Example Trigger:**
> 🗣 Say: "This design requires deep thinking. Let me ultrathink the architectural fundamentals before proposing approaches."

**Benefit:** Prevents heading down wrong paths that seemed obvious but have hidden complexities or flawed assumptions.

## Common Workflows

### Testing a Plugin Locally

```bash
# Navigate to repository
cd kisune

# Start Claude Code in this directory
# Plugins auto-load from ./trading and ./dev-workflow

# Test dev-workflow commands
/dev-workflow:spec
```

### Modifying Plugin Metadata

```bash
# Edit plugin metadata
nano trading/.claude-plugin/plugin.json
nano dev-workflow/.claude-plugin/plugin.json

# Update author info, version, etc.
# Validate JSON after editing
python3 -m json.tool trading/.claude-plugin/plugin.json
```

### Adding New Skills

When adding skills to either plugin:

1. Create skill directory: `skills/[skill-name]/`
2. Create `SKILL.md` with proper frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Activation triggers and purpose
   ---
   ```
3. Document skill thoroughly in body
4. Update plugin README.md
5. Test skill activation

**IMPORTANT:** Only use the 10 spec-compliant frontmatter fields documented above. Keep SKILL.md under 500 lines — move reference material to separate files.

### Creating New Commands

When adding slash commands:

1. Create `commands/[command-name].md`
2. Add frontmatter:
   ```yaml
   ---
   description: Brief command description
   ---
   ```
3. Document command usage in body
4. Update plugin README.md
5. Test command invocation

## File Locations

**Plugin Manifests:**
- `trading/.claude-plugin/plugin.json`
- `dev-workflow/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json` (marketplace metadata)

**Documentation:**
- `README.md` - Repository overview
- `trading/README.md` - Trading plugin documentation (607 lines)
- `dev-workflow/README.md` - Dev-workflow documentation (819 lines)
- `PLUGINS_INSTALLATION.md` - Installation guide
- `SPEC_COMPLIANCE_REPORT.md` - Compliance verification
- `TEMPLATES_USAGE.md` - Template usage guide

**Design Documents:**
- `docx/plans/2025-11-17-trading-plugin-design.md`
- `docx/plans/2025-11-17-trading-plugin-implementation.md`
- `docx/plans/2025-11-17-dev-workflow-plugin-design.md`
- `docx/plans/2025-11-17-dev-workflow-plugin-implementation.md`

**Templates:**
- Trading: `trading/templates/` (strategy-doc.md, backtest-results.md, pattern-library.md)
- Dev-workflow: `dev-workflow/templates/` (requirements.md, design.md, tasks.md)

## docx/ Storage Convention

**Every skill that persists a file writes it under `docx/`.** No skill writes to the OS temp directory, the repo root, or an invented top-level folder. Each category is a sibling directory:

```
docx/
├── core/                       # human-authored orientation (product goals, tech stack, codebase guide)
├── features/[NN-name]/         # requirements.md, design.md, tasks.md, plan.md
├── decisions/NNNN-slug.md      # ADRs                       — domain-modeling
├── glossary.md                 # canonical domain terms     — domain-modeling
├── postmortems/<bug>.md        # bug-fix records            — post-mortem
├── research/<topic>.md         # cited primary-source notes — investigate
├── prototypes/<question>.md    # prototype verdicts         — prototype
├── handoffs/<slug>.md          # session handoffs           — handoff
├── strategies/<name>.md        # trading strategy docs      — trading:research
├── patterns/<name>.md          # chart pattern library      — trading:pattern
├── logs/                       # command output worth keeping
└── UserInstructions/<name>.md  # manual setup steps for the user
```

**Rules:**
- Create directories **lazily** — only when there is a first real file to put in them. An empty scaffold is noise.
- If the repo already has an established location for a category (`docs/adr/`, an ADR tool), use that instead. Confirm once at the first write, then stop asking.
- Source code is not storage. Prototype code, tests, and skill files live where the code lives; only the *record* of them goes in `docx/`.
- When adding a skill that persists anything, add its directory to this table.

## Important Patterns

### Skill Auto-Activation

Skills should activate naturally based on user intent:

**Trading Skills:**
- "Analyze BTC/USDT" → analyze
- "Document my strategy" → research
- "What pattern is this?" → pattern
- "Convert to Python" → translate

**Dev-Workflow Skills:**
- "Plan new feature" → spec-driven-planning (with optional brainstorming)
- "Review my code" → review
- "Commit changes" → git-workflow
- "Write tests" → test-driven-development (strict TDD enforcement)
- "Debug this bug" → systematic-debug
- "Done" / "ready to commit" → completion-validation (evidence-before-claims gate)
- "Review the spec" / "check the spec" / "validate spec" → spec-review (3-agent review)

### Skill Integration

Dev-workflow skills work together seamlessly:

- **Requirements phase** → Can activate `brainstorming` for scope exploration
- **Design phase** → Can activate `brainstorming` for architectural exploration
- **Implementation phase** → Activates `test-driven-development` automatically
- **Before commits** → `review` auto-triggers for review
- **Git operations** → `git-workflow` generates smart commit messages

All skills are self-contained within the plugin (no external dependencies).

### Template Usage

Templates are at plugin root for easy access:

```bash
# Trading templates
cat trading/templates/strategy-doc.md
cat trading/templates/backtest-results.md
cat trading/templates/pattern-library.md

# Dev-workflow templates
cat dev-workflow/templates/requirements.md
cat dev-workflow/templates/design.md
cat dev-workflow/templates/tasks.md
```

Skills reference and copy these templates during workflow execution.

## Compliance & Standards

**Status:** ✅ 100% Compliant with Official Claude Code Plugin Spec

**Key Compliance Points:**
- ✅ Correct directory structure
- ✅ Valid plugin manifests (JSON validated)
- ✅ Spec-compliant skill frontmatter (no extra fields)
- ✅ Proper command format
- ✅ Clean, validated syntax

**References:**
- Plugin Guide: https://code.claude.com/docs/en/plugins
- Plugin Reference: https://code.claude.com/docs/en/plugins-reference
- Skills Guide: https://code.claude.com/docs/en/skills

## Statistics

**Trading Plugin:**
- 4 skills, 3 templates

**Dev-Workflow Plugin:**
- 23 skills, 8 agents, 7 commands, 4 templates

**Combined:**
- 27 skills, 8 agents, 7 commands, 7 templates
- 59 files, ~9,918 lines
- Language-agnostic, spec-compliant
