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
│   ├── skills/                # 4 skills (market-analysis, strategy-research, pattern-recognition, strategy-translator)
│   ├── commands/              # 4 slash commands
│   ├── templates/             # 3 strategy/analysis templates
│   └── README.md              # Complete documentation
├── dev-workflow/              # Dev-workflow plugin
│   ├── .claude-plugin/        # Plugin metadata
│   ├── skills/                # 9 skills (includes brainstorming, TDD, spec-driven planning/implementation, etc.)
│   ├── commands/              # 2 slash commands
│   ├── templates/             # 3 spec-driven templates
│   └── README.md              # Complete documentation
├── .claude-plugin/            # Marketplace metadata
├── docx/                      # Documentation and planning
│   └── plans/                 # Design and implementation documents
└── examples/                  # Example skills and superpowers
```

## Plugin Architecture

### Trading Plugin (4 skills, 4 commands)

**Skills:**
- `market-analysis` - Technical analysis with indicators, S/R, multi-timeframe
- `strategy-research` - Systematic strategy documentation with edge hypothesis
- `pattern-recognition` - Chart pattern identification and personal library
- `strategy-translator` - Convert strategies to Python + Pine Script

**Commands:**
- `/trading:analyze` - Market analysis
- `/trading:research` - Strategy research
- `/trading:pattern` - Pattern identification
- `/trading:translate` - Code generation

### Dev-Workflow Plugin (9 skills, 2 commands)

**Planning Skills:**
- `spec-driven-planning` - 3-phase workflow (Feature → Requirements/EARS → Design)
- `brainstorming` - Collaborative refinement for requirements and design

**Implementation Skills:**
- `spec-driven-implementation` - Task breakdown and execution
- `test-driven-development` - Strict RED-GREEN-REFACTOR enforcement

**Quality Skills:**
- `code-quality` - 25-point review checklist
- `git-workflow` - Smart commits, branch management, PR creation
- `documentation` - Code, API, architecture docs
- `systematic-testing` - TDD guidance and debugging framework
- `skill-maker` - Create/edit skills with TDD methodology

**Commands:**
- `/dev-workflow:spec` - Launch spec-driven workflow (interactive menu)
- `/dev-workflow:review` - Comprehensive code review

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
# Install locally for testing (from this directory)
# Plugins auto-load when Claude Code starts in this directory

# Install globally
cp -r trading ~/.claude/plugins/trading
cp -r dev-workflow ~/.claude/plugins/dev-workflow

# Verify installation in Claude Code
/help | grep trading
/help | grep dev-workflow
```

## Key Technical Details

### Plugin Specification Compliance

Both plugins follow the official Claude Code plugin spec:

**Directory Structure:**
- `.claude-plugin/plugin.json` - Plugin metadata (at plugin root)
- `commands/` - Slash commands (at plugin root, NOT in .claude-plugin)
- `skills/` - Skills (at plugin root)
- `templates/` - Supporting templates (at plugin root)

**Skill Frontmatter (YAML):**
```yaml
---
name: skill-name
description: What it does and when it activates
---
```

**IMPORTANT:** Only `name` and `description` are spec-compliant. Do NOT add:
- `version` field (not in spec)
- `dependencies` field (not in spec)
- Other custom fields in frontmatter

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
- **strategy-research** - Before edge hypothesis formation and validation
- **market-analysis** - When market conditions show conflicting signals
- **skill-maker** - Before creating new skill structures
- **pattern-recognition** - When pattern validity is ambiguous
- **code-quality** - When architectural issues are detected

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
cd /Users/xb/table/kisune

# Start Claude Code in this directory
# Plugins auto-load from ./trading and ./dev-workflow

# Test trading commands
/trading:analyze
/trading:research

# Test dev-workflow commands
/dev-workflow:spec
/dev-workflow:review
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

**IMPORTANT:** Only use spec-compliant frontmatter fields (`name`, `description`).

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

## Important Patterns

### Skill Auto-Activation

Skills should activate naturally based on user intent:

**Trading Skills:**
- "Analyze BTC/USDT" → market-analysis
- "Document my strategy" → strategy-research
- "What pattern is this?" → pattern-recognition
- "Convert to Python" → strategy-translator

**Dev-Workflow Skills:**
- "Plan new feature" → spec-driven-planning (with optional brainstorming)
- "Review my code" → code-quality
- "Commit changes" → git-workflow
- "Document this" → documentation
- "Write tests" → test-driven-development (strict TDD enforcement)
- "Debug this bug" → systematic-testing

### Skill Integration

Dev-workflow skills work together seamlessly:

- **Requirements phase** → Can activate `brainstorming` for scope exploration
- **Design phase** → Can activate `brainstorming` for architectural exploration
- **Implementation phase** → Activates `test-driven-development` automatically
- **Before commits** → `code-quality` auto-triggers for review
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
- 14 files total
- 4 skills, 4 commands, 3 templates
- 3,499 lines of code

**Dev-Workflow Plugin:**
- 26 files total
- 9 skills, 2 commands, 3 templates
- 5,116 lines of code

**Combined:**
- 26 files, 8,615 lines
- 13 skills, 6 commands, 6 templates
- Production-ready, fully documented
