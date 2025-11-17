# Plugin Templates Usage Guide

**Date:** 2025-11-17

## Overview

Both plugins include template files at the plugin root level for easy access. While the official Claude Code spec recommends placing templates within skill directories, having them at the root makes them easier to find and use directly.

---

## Templates Location

### Trading Plugin Templates
**Location:** `trading/templates/`

1. **strategy-doc.md** - Complete strategy documentation template
2. **backtest-results.md** - Backtest results recording template
3. **pattern-library.md** - Personal pattern library template

### Dev-Workflow Plugin Templates
**Location:** `dev-workflow/templates/`

1. **requirements.md** - EARS requirements template
2. **design.md** - Technical design template
3. **tasks.md** - TDD task breakdown template

---

## How to Use Templates

### Method 1: Copy Template Directly

```bash
# Trading plugin - create a new strategy document
cp trading/templates/strategy-doc.md strategies/my-new-strategy.md

# Dev-workflow plugin - create requirements for a feature
cp dev-workflow/templates/requirements.md docx/features/01-auth/requirements.md
```

### Method 2: Ask Claude to Use Templates

**For Trading:**
```
"Use the strategy documentation template to help me document my mean reversion strategy"
```

**For Dev-Workflow:**
```
"Create requirements for user authentication using the EARS requirements template"
```

Claude will access the template files and help you fill them out.

### Method 3: Reference in Skills

The skills are aware of the templates and will reference them automatically:

- **Trading skills** know about strategy-doc, backtest-results, and pattern-library templates
- **Dev-workflow skills** know about requirements, design, and tasks templates

---

## Template Contents

### Trading Templates

#### strategy-doc.md
Complete strategy documentation with sections for:
- Edge hypothesis
- Market conditions
- Entry/exit rules
- Risk management
- Backtest planning
- Implementation checklist

#### backtest-results.md
Comprehensive backtest results with:
- Performance metrics table
- Equity curve analysis
- Market breakdown
- Trade statistics
- Qualitative observations
- Next steps

#### pattern-library.md
Personal pattern library with:
- Pattern characteristics
- Win rate tracking
- Setup conditions
- Entry/stop/target rules
- Trade examples
- Lessons learned

---

### Dev-Workflow Templates

#### requirements.md
EARS requirements format with:
- Event-driven requirements (WHEN...THEN)
- State-driven requirements (WHILE...)
- Ubiquitous requirements (SHALL)
- Conditional requirements (IF...THEN)
- Non-functional requirements
- Acceptance criteria

#### design.md
Technical design documentation with:
- Architecture overview
- Component structure
- Data flow diagrams
- API contracts
- Error handling
- Security considerations
- Testing strategy

#### tasks.md
TDD task breakdown with:
- Red-Green-Refactor structure
- Task-by-task checklist format
- Acceptance criteria per task
- Component organization
- Integration tasks
- Final verification checklist

---

## Customization

Templates are meant to be customized to your workflow:

### For Trading:
1. **Adapt to your strategy types** - Add sections for specific strategy categories
2. **Add your metrics** - Include metrics you track in backtest results
3. **Build your pattern library** - Document patterns you trade most

### For Dev-Workflow:
1. **Adjust to your tech stack** - Modify design template sections
2. **Customize requirements** - Add project-specific requirement categories
3. **Adapt task structure** - Match your team's task breakdown preferences

---

## Best Practices

### Keep Templates Updated
As you use the templates, improve them:
```bash
# Edit the master template based on what works
vim trading/templates/strategy-doc.md

# Or create your own variations
cp trading/templates/strategy-doc.md trading/templates/strategy-doc-crypto.md
```

### Version Control Templates
Track changes to your customized templates:
```bash
git add trading/templates/
git commit -m "customize strategy doc template for crypto strategies"
```

### Share Improvements
If you make improvements to templates, consider:
1. Updating the templates in your local plugins
2. Contributing improvements back to the community
3. Creating template variations for specific use cases

---

## Template Access from Skills

### How Skills Reference Templates

Skills can reference templates in two ways:

1. **Direct Path Reference**
   ```markdown
   Use the template at `trading/templates/strategy-doc.md`
   ```

2. **Content Inclusion**
   Skills can read and present template content to help guide you through filling it out.

### Automatic Template Usage

When you use slash commands, templates are automatically referenced:

- `/trading:research` → Uses strategy-doc.md template
- `/trading:pattern` → Updates pattern-library.md
- `/dev-workflow:spec` requirements phase → Uses requirements.md template
- `/dev-workflow:spec` design phase → Uses design.md template
- `/dev-workflow:spec` tasks phase → Uses tasks.md template

---

## Alternative: Templates in Skill Directories

If you prefer following the official Claude Code convention exactly, you can reorganize templates:

```bash
# Move trading templates into skill directories
mv trading/templates/strategy-doc.md trading/skills/strategy-research/
mv trading/templates/pattern-library.md trading/skills/pattern-recognition/
mv trading/templates/backtest-results.md trading/skills/strategy-research/

# Move dev-workflow templates into spec-driven skill
mkdir dev-workflow/skills/spec-driven/templates
mv dev-workflow/templates/*.md dev-workflow/skills/spec-driven/templates/

# Update skill SKILL.md files to reference new paths
```

**Trade-offs:**
- **Pro:** Follows official convention exactly
- **Pro:** Templates are co-located with related skills
- **Con:** Harder to browse all templates at once
- **Con:** Less convenient for direct copying

---

## Summary

**Current Structure (Easier to Use):**
```
plugin-root/
├── templates/          # All templates in one place
│   ├── template1.md
│   ├── template2.md
│   └── template3.md
└── skills/
    └── skill-name/
        └── SKILL.md    # References ../templates/
```

**Official Convention (Better Organized):**
```
plugin-root/
└── skills/
    └── skill-name/
        ├── SKILL.md
        └── template.md  # Co-located with skill
```

**Recommendation:** Keep current structure for convenience, or reorganize if you prefer strict adherence to official conventions. Both work fine!

---

## Questions?

If you need help with:
- Customizing templates for your workflow
- Creating new template variations
- Organizing templates differently
- Automating template usage

Just ask! The templates are designed to be flexible and adaptable to your needs.
