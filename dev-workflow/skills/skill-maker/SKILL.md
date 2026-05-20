---
name: skill-maker
description: Create and edit Claude Code skills with TDD methodology. Use when creating or editing skills. Test with subagents before deployment, iterate until bulletproof.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Skill Maker

## Overview

**Creating skills IS Test-Driven Development applied to process documentation.**

Write test cases (pressure scenarios with subagents), watch them fail (baseline behavior), write the skill (documentation), watch tests pass (agents comply), and refactor (close loopholes).

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

## What is a Skill?

Skills are modular packages that extend Claude's capabilities with specialized knowledge, workflows, and tools — like "onboarding guides" for specific domains.

**Skills provide:** Specialized workflows, tool integrations, domain expertise, bundled resources (scripts, references, assets)

**Skills are:** Reusable techniques, patterns, tools, reference guides

**Skills are NOT:** Narratives, one-off solutions, or project-specific conventions (use CLAUDE.md for those)

**Skill Types:** Technique (concrete steps), Pattern (mental models), Reference (API docs/guides), Discipline-Enforcing (rules/requirements)

**Create when:** Technique wasn't obvious, applies broadly, would be referenced again, ensures consistent behavior across instances

**Don't create for:** One-off solutions, standard well-documented practices, project-specific conventions

---

## Skill Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter: name (required), description (required), allowed-tools (optional)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/     - Executable code (deterministic, token-efficient)
    ├── references/  - Documentation loaded as needed (schemas, APIs)
    └── assets/      - Files used in output (templates, boilerplate)
```

**Frontmatter rules:**
- `name`: Letters, numbers, hyphens only (max 64 chars)
- `description`: Third-person, starts with "Use when...", includes triggers AND purpose (Anthropic caps `description` + optional `when_to_use` at 1536 chars combined; aim well under)
- `allowed-tools`: Optional list restricting tool access

**Writing style:** Use imperative/infinitive form ("To accomplish X, do Y"), not second person

**Progressive Disclosure:** Metadata always loaded (~100 words) → SKILL.md on trigger (<5k words) → Resources as needed

**Reference best practices:** Keep SKILL.md lean; if reference files >10k words, include grep patterns in SKILL.md; avoid duplicating content between SKILL.md and references

---

## The Iron Law

```
NO SKILL WITHOUT A FAILING TEST FIRST
```

Applies to NEW skills AND EDITS. Write/edit skill before testing? Delete it. Start over. No exceptions — not for "simple additions", "just a section", or "documentation updates". Delete means delete.

---

## RED-GREEN-REFACTOR for Skills

### RED: Baseline Testing

Run pressure scenarios WITHOUT the skill. Document exact behavior:
- What choices did the agent make?
- What rationalizations did they use (verbatim)?
- Which pressures triggered violations?

**Method:** Create new conversation/subagent → present scenario → apply pressure (time constraints, sunk cost, authority, exhaustion) → document failures

### GREEN: Write Minimal Skill

Write skill addressing those specific rationalizations. Don't add content for hypothetical cases.

Run same scenarios WITH skill present. Agent should now comply. Document any new violations.

### REFACTOR: Close Loopholes

For each new violation: identify rationalization → add explicit counter → re-test until bulletproof.

**For discipline-enforcing skills:** Build rationalization table, create "Red Flags" list, add "No exceptions" counters, address "spirit vs letter" arguments.

---

## Skill Creation Process

### Step 1: Understanding

Clarify concrete examples of usage. Ask: "What should this skill support?", "What triggers it?", "How would it be used?"

**UltraThink before creating structure:**

> "Let me ultrathink what this skill should really accomplish and how it fits the ecosystem."

Question fundamentals: Is this a skill or project docs? What's reusable vs one-off? How will Claude discover it? What rationalizations will agents use? What are we NOT including?

### Step 2: Plan Resources

For each use case: How would you execute from scratch? What scripts, references, or assets would help when executing repeatedly?

### Step 3: Initialize Structure

```bash
mkdir -p dev-workflow/skills/skill-name/{scripts,references,assets}
```

Create `SKILL.md` with frontmatter template:

```markdown
---
name: skill-name
description: Use when [triggers] - [what it does]
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Skill Name

## Overview
[Core principle in 1-2 sentences]

## When to Use
[Activation triggers; when NOT to use]

## [Main content sections]
```

### Step 4: Execute RED-GREEN-REFACTOR

Follow the cycle above: baseline test (RED) → write content addressing failures (GREEN) → close loopholes (REFACTOR).

**Skill content must answer:** What is the purpose? When should it be used? How should Claude use it?

### Step 5: Iterate After Deployment

Use skill on real tasks → notice struggles → baseline test again → update → verify.

---

## Claude Search Optimization (CSO)

> **Note:** "CSO" is kisune's framing, not an official Anthropic term. The underlying mechanics are official: Claude matches user intent against the frontmatter `description` (and optional `when_to_use`) of available skills to decide which to auto-invoke. **The body of SKILL.md is NOT scanned for matching** — padding the body with keywords does not help activation. Only frontmatter participates.

### Description field rules

- Start with "Use when..." in third person (not second person)
- Include concrete triggers, error messages, and symptom keywords a user or agent would search for in the description itself (body keywords are wasted for matching)
- Describe the *problem* the skill solves, not implementation details
- Anthropic caps `description` + `when_to_use` at **1536 chars combined**; aim for 200-400 chars to leave headroom

### Naming rules

- Use verb-first or gerund form: `creating-skills`, `testing-async-code`, `dispatching-agents`
- Letters, numbers, and hyphens only; max 64 chars
- Avoid vague labels (`helper`, `utils`, `common`)

### Token efficiency targets

> **Official guidance:** Anthropic recommends SKILL.md body **under 500 lines** and progressive disclosure (move bulk into `references/`). The word-count tiers below are kisune heuristics layered on top, not Anthropic policy.

| Skill type | Kisune target word count |
|---|---|
| Getting-started / bootstrap | < 150 words |
| Frequently-loaded (auto-trigger common workflows) | < 500 words |
| Domain / reference | < 1000 words |
| Discipline-enforcing | up to 1500 words (rationalization tables justify length) |

Hard ceiling either way: **500 lines** of SKILL.md body. If you're approaching that, move material to `references/`.

If SKILL.md exceeds the target, move reference material to a `references/` subfolder and link to it.

### Cross-referencing rules

- Reference other skills by name only (e.g., "use `dev-workflow:test-driven-development`")
- Avoid `@filename.md` syntax — it force-loads files into context and defeats progressive disclosure
- Use a "REQUIRED SUB-SKILL:" marker when a sub-skill must be invoked

---

## Testing by Skill Type

| Type | Test With | Success Criteria |
|------|-----------|-----------------|
| **Discipline** | Academic questions + pressure scenarios (3+ combined: time, sunk cost, exhaustion) | Agent follows rule under maximum pressure |
| **Technique** | Application scenarios, variations, missing info tests | Agent applies technique to new scenario |
| **Pattern** | Recognition, application, counter-examples | Agent knows when/how to apply (and when NOT to) |
| **Reference** | Retrieval, application, gap testing | Agent finds and correctly applies information |

---

## Skill Creation Checklist

Use TaskCreate to create todos for EACH item.

**RED Phase:**
- [ ] Create pressure scenarios (3+ combined pressures for discipline skills)
- [ ] Run scenarios WITHOUT skill - document baseline verbatim
- [ ] Identify patterns in rationalizations/failures

**GREEN Phase:**
- [ ] Valid frontmatter: name (letters/numbers/hyphens), description ("Use when...", third person, <1536 chars combined with `when_to_use`; aim for 200-400)
- [ ] Keywords throughout for search (errors, symptoms, tools)
- [ ] Clear overview with core principle
- [ ] Address specific baseline failures from RED
- [ ] One excellent example (not multi-language)
- [ ] Run scenarios WITH skill - verify compliance

**REFACTOR Phase:**
- [ ] Add counters for new rationalizations
- [ ] Build rationalization table and red flags list
- [ ] Re-test until bulletproof

**Quality Checks:**
- [ ] Overview answers: What? When? How?
- [ ] Quick reference table or bullets
- [ ] Common mistakes section
- [ ] No narrative storytelling
- [ ] Token count within targets

**Deployment:**
- [ ] Commit skill to git
- [ ] Update documentation if needed

---

## Anti-Patterns

- **Narrative examples** ("In session 2025-10-03...") — too specific, not reusable
- **Multi-language dilution** (example-js, example-py, example-go) — mediocre quality, maintenance burden
- **Generic labels** (helper1, step3) — use semantic names
- **Untested skills** — guarantees issues in production
- **Vague descriptions** ("Helps with coding") — Claude won't know when to activate

---

## Integration with Dev-Workflow

**Leverage existing skills:** `test-driven-development` for testing, `review` for code review, `brainstorming` for design exploration.

**Activation context:** Consider when skill activates in the workflow (planning, implementation, quality) and whether it auto-activates or requires explicit invocation.

**Tool restrictions by phase:**
- Planning: `Read, Write, Glob, Grep`
- Implementation: `Read, Write, Edit, Glob, Grep, Bash`
- Quality: `Read, Grep, Glob`

---

## The Bottom Line

**Creating skills IS TDD for process documentation.** Same Iron Law, same cycle (RED → GREEN → REFACTOR), same benefits. If you follow TDD for code, follow it for skills.
