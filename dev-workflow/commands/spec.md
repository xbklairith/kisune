---
description: Launch spec-driven development workflow for features
---

Route to the appropriate spec-driven skill based on phase:
- **Planning phases** (create, requirements, design): Activate `spec-driven-planning` skill
- **Implementation phases** (tasks, execute): Activate `spec-driven-implementation` skill
- **Utility** (list): Show feature status directly

## Interactive Menu

Present this menu to the user:

```
📋 Spec-Driven Development Workflow

Planning Phase:
1. Create new feature
2. Define requirements (EARS format)
3. Generate technical design

Implementation Phase:
4. Break down into tasks (TDD)
5. Execute implementation

Utility:
6. List all features

What would you like to do? (1-6)
```

## Argument Handling & Routing

**Planning Phase Arguments:**
```
/dev-workflow:spec "feature-name"    → Activate spec-driven-planning (Phase 1)
/dev-workflow:spec requirements      → Activate spec-driven-planning (Phase 2)
/dev-workflow:spec design            → Activate spec-driven-planning (Phase 3)
```

**Implementation Phase Arguments:**
```
/dev-workflow:spec tasks             → Activate spec-driven-implementation (Phase 4)
/dev-workflow:spec execute           → Activate spec-driven-implementation (Phase 5)
```

**Utility Arguments:**
```
/dev-workflow:spec list              → Show all features with status
```

## Routing Logic

Based on user's menu choice or argument:

**Options 1-3** or args **[feature-name, requirements, design]:**
→ Activate `spec-driven-planning` skill

**Options 4-5** or args **[tasks, execute]:**
→ Activate `spec-driven-implementation` skill

**Option 6** or arg **[list]:**
→ List features directly with status

## Phase Details

**Planning Phases (1-3)** are handled by `spec-driven-planning` skill:
- Phase 1: Feature Creation - Create directory structure and templates
- Phase 2: Requirements Definition - Use EARS format for clear requirements
- Phase 3: Technical Design - Propose architectural approaches with trade-offs

**Implementation Phases (4-5)** are handled by `spec-driven-implementation` skill:
- Phase 4: Task Breakdown - Break design into TDD tasks (Red-Green-Refactor)
- Phase 5: Execution - Execute tasks systematically with quality gates

See respective skill documentation for detailed phase execution instructions.

## Examples

**Example 1: Interactive Menu**
```
User: /dev-workflow:spec

Assistant presents interactive menu showing planning and implementation phases.
User selects option 1-3 → Routes to spec-driven-planning skill
User selects option 4-5 → Routes to spec-driven-implementation skill
```

**Example 2: Start Planning New Feature**
```
User: /dev-workflow:spec "user authentication"

Assistant activates spec-driven-planning skill at Phase 1 (Feature Creation)
Creates feature structure and begins requirements gathering.
```

**Example 3: Jump to Design Phase**
```
User: /dev-workflow:spec design

Assistant activates spec-driven-planning skill at Phase 3 (Design)
Finds most recent feature and proposes architectural approaches.
```

**Example 4: Start Implementation**
```
User: /dev-workflow:spec tasks

Assistant activates spec-driven-implementation skill at Phase 4 (Task Breakdown)
Reads completed design and breaks into TDD tasks.
```

**Example 5: List Features**
```
User: /dev-workflow:spec list

Assistant lists all features in docx/features/ with current status.
```
