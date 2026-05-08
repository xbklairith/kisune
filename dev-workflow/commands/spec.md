---
description: Launch spec-driven development workflow — picks Quick (single plan.md) or Full (3-file EARS spec) automatically
---

Route to the appropriate spec-driven skill. Mode (Quick vs Full) is decided by the planning skill from signals or user override.

- **Planning** (create, requirements, design, quick, full): Activate `spec-driven-planning` skill
- **Implementation** (tasks, execute): Activate `spec-driven-implementation` skill (auto-detects mode from filesystem)
- **Utility** (list): Show feature status directly

## Interactive Menu

```
📋 Spec-Driven Development Workflow

Planning:
  1. New feature (auto-pick Quick or Full)
  2. New feature — force Quick mode (single plan.md)
  3. New feature — force Full mode (requirements + design + tasks)
  4. Define requirements (Full mode, EARS)
  5. Generate technical design (Full mode)

Implementation:
  6. Break down into TDD tasks (Full mode)
  7. Execute implementation (auto-detects Quick vs Full)

Utility:
  8. List all features

What would you like to do? (1-8)
```

## Argument Handling

**Planning args:**
```
/dev-workflow:spec                   → Interactive menu
/dev-workflow:spec "feature-name"    → spec-driven-planning, auto-pick mode
/dev-workflow:spec quick "name"      → spec-driven-planning, force Quick
/dev-workflow:spec full "name"       → spec-driven-planning, force Full
/dev-workflow:spec create            → spec-driven-planning (auto-pick)
/dev-workflow:spec requirements      → spec-driven-planning (Full Phase 2)
/dev-workflow:spec design            → spec-driven-planning (Full Phase 3)
```

**Implementation args:**
```
/dev-workflow:spec tasks             → spec-driven-implementation (Full Phase 4)
/dev-workflow:spec execute           → spec-driven-implementation (auto-detect Quick or Full)
```

**Utility:**
```
/dev-workflow:spec list              → Show all features with mode + status
```

## Routing Logic

**IMPORTANT:** Always use the Skill tool to explicitly invoke skills.

| User input | Skill | Notes |
|---|---|---|
| Options 1-5, args `create / "name" / quick / full / requirements / design` | `dev-workflow:spec-driven-planning` | Skill picks mode (or honors `quick`/`full` override) |
| Options 6-7, args `tasks / execute` | `dev-workflow:spec-driven-implementation` | Skill auto-detects `plan.md` vs `tasks.md` |
| Option 8, arg `list` | List `docx/features/` directly | Show NN-name + which file exists (plan.md / tasks.md) + status line |

## Mode Reminder

- **Quick mode** writes one file: `docx/features/[NN-name]/plan.md`. No EARS, no RGR.
- **Full mode** writes three files: `requirements.md` + `design.md` + `tasks.md`. EARS + RGR enforced.
- Implementation auto-detects from which file is present. No flag needed at execute time.

See `dev-workflow:spec-driven-planning` for the mode-selection signals (effort, stakeholders, compliance, ambiguity).
