# Dev-Workflow Plugin

Integrated development lifecycle plugin for Claude Code combining spec-driven development with code quality, git workflow, documentation, and systematic testing.

## Overview

The Dev-Workflow plugin provides a comprehensive, systematic approach to software development from initial concept through production deployment. It integrates twenty-four specialized skills that work together seamlessly to ensure high-quality, well-tested, properly documented code with no external dependencies.

### What This Plugin Does

- **Guides feature development** through structured phases (requirements → design → tasks → execution)
- **Enforces code quality** through systematic reviews and refactoring suggestions
- **Manages git operations** with smart commits, branch management, and PR creation
- **Drives test-first development** with TDD workflow and systematic debugging
- **Gates completion claims** with evidence-before-assertion validation

### Philosophy

- **Systematic over ad-hoc**: Structured workflows prevent shortcuts and ensure quality
- **Natural activation**: Skills auto-trigger based on context, reducing manual overhead
- **Quality gates**: Built-in checkpoints catch issues early
- **Education through use**: Teaches best practices while working

## Installation

```bash
# In Claude Code: add the kisune marketplace, then install
/plugin marketplace add xbklairith/kisune
/plugin install dev-workflow@kisune

# Claude Code 2.1.275 or later can do both in one step
/plugin install dev-workflow --marketplace xbklairith/kisune

# Later, from a terminal: pull the latest version, then restart Claude Code
claude plugin marketplace update kisune
claude plugin update dev-workflow@kisune
```

To work on the plugin itself, load it from a clone with `claude --plugin-dir ./dev-workflow`. Either way, `/help` in Claude Code should then list `/dev-workflow:spec`.

In a fork, put your own author details in `.claude-plugin/plugin.json`:

```json
{
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  }
}
```

## Core Skills

The plugin includes 28 integrated skills organized into planning, implementation, and quality categories.

### Planning & Design Skills

#### 1. Spec-Driven Planning

**Activation:** User mentions features, requirements, specs, design, or uses `/dev-workflow:spec`

**Purpose:** Guide feature planning through three structured phases (Feature Creation → Requirements → Design)

**Three Planning Phases:**

1. **Feature Creation**
   - Creates directory structure: `docx/features/[NN-feature-name]/`
   - Initializes template files (requirements.md, design.md, tasks.md)
   - Establishes feature tracking

2. **Requirements Definition (EARS Format)**
   - Uses EARS (Easy Approach to Requirements Syntax)
   - Five requirement types: Event-Driven, State-Driven, Ubiquitous, Conditional, Optional
   - Systematic questioning to elicit complete requirements
   - Optional: Activates `brainstorming` skill for scope exploration
   - Captures functional and non-functional requirements

3. **Technical Design**
   - Optional: Activates `brainstorming` skill for architectural exploration
   - Proposes 2-3 architectural approaches with trade-offs
   - Presents recommendation with reasoning
   - Creates comprehensive design document
   - Includes data flow, API contracts, security, performance

#### 2. Brainstorming

**Activation:** User has rough idea needing refinement, during requirements or design phases

**Purpose:** Refine rough ideas into clear requirements or designs through collaborative questioning

**Key Features:**
- One question at a time (no overwhelming)
- Explores 2-3 alternatives before recommending
- Presents the design in short sections
- Validates each section before proceeding
- Dual-phase usage:
  - **Phase 2 (Requirements):** Explores WHAT to build, clarifies scope
  - **Phase 3 (Design):** Explores HOW to build, compares architectures

### Implementation Skills

#### 3. Spec-Driven Implementation

**Activation:** Design is complete, user ready to implement, or uses `/dev-workflow:spec tasks/execute`

**Purpose:** Guide implementation through task breakdown and execution with TDD

**Two Implementation Phases:**

4. **Task Breakdown (TDD)**
   - Breaks design into Red-Green-Refactor tasks
   - Each task: 30-60 minutes
   - Checkbox tracking for progress
   - Clear acceptance criteria

5. **Execution**
   - Activates `test-driven-development` skill for TDD enforcement
   - Follows strict RED-GREEN-REFACTOR cycle
   - Auto-triggers code quality reviews before commits
   - Uses smart git commits
   - Status checkpoints every 2-3 tasks

#### 4. Test-Driven Development (TDD)

**Activation:** During implementation phase, writing any production code

**Purpose:** Enforce strict TDD discipline (test first, watch fail, minimal code to pass)

**Core Principle:** NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST

**Red-Green-Refactor Cycle:**
- **RED:** Write failing test describing desired behavior
- **Verify RED:** Run test - MUST fail for expected reason
- **GREEN:** Write minimal code to make test pass
- **Verify GREEN:** Run test - MUST pass, all tests stay green
- **REFACTOR:** Clean up code while keeping tests green
- **Repeat:** Next test for next behavior

**Strict Enforcement:**
- Write code before test? Delete it. Start over.
- No "keep as reference" - delete means delete
- Addresses all common rationalizations
- Verification checklist before marking work complete

**EARS Format Examples:**

```
Event-Driven:
WHEN user clicks submit THEN the system SHALL validate form data

State-Driven:
WHILE processing payment the system SHALL display loading indicator

Ubiquitous:
The system SHALL validate all user inputs before processing

Conditional:
IF user role is admin THEN the system SHALL show management panel

Optional:
WHERE premium subscription is active the system SHALL enable advanced analytics
```

### Quality Skills

#### 5. Review (Code Quality)

**Activation:** User says "review this code", mentions refactoring, or before commits

**Purpose:** Systematic code reviews and refactoring suggestions

**Review Checklist:**

1. **Code Structure**
   - Single Responsibility Principle
   - DRY (Don't Repeat Yourself)
   - Function length (prefer < 50 lines)
   - Clear naming
   - No magic numbers

2. **Error Handling**
   - All errors caught appropriately
   - No silent failures
   - User-friendly error messages
   - Proper logging
   - Edge cases covered

3. **Security**
   - Input validation
   - SQL injection prevention
   - XSS prevention
   - Sensitive data handling
   - Secrets in environment variables

4. **Performance**
   - No N+1 queries
   - Appropriate caching
   - Database indexes
   - Efficient algorithms
   - Memory leak prevention

5. **Testing**
   - Tests exist for new functionality
   - Edge cases tested
   - Happy path tested
   - Error conditions tested
   - Maintainable tests

**Review Output Format:**
- What I checked (files read, paths traced, commands run)
- Issues by priority (High/Medium/Low)
- Refactoring suggestions with code examples
- Code metrics (complexity, coverage, maintainability)
- Action items with checkboxes

#### 6. Git Workflow

**Activation:** User commits code, mentions branches/PRs, or git operations

**Purpose:** Best-practice git operations with safety checks

**Capabilities:**

**Smart Commits:**
- Analyzes changes with `git status` and `git diff`
- Generates meaningful commit messages
- Format: `[type]: [description]`
- Types: feat, fix, refactor, test, docs, chore, style, perf
- Present tense, imperative mood
- Shows preview before committing

**Branch Management:**
- Naming conventions: `feature/`, `fix/`, `refactor/`, `experiment/`, `hotfix/`
- Safety warnings before dangerous operations
- Prevents accidental pushes to main/master

**Pull Request Creation:**
- Analyzes all commits in branch
- Reviews `git diff main...HEAD`
- Generates comprehensive PR description
- Includes testing and code quality checklists
- Uses `gh pr create` CLI
- Returns PR URL

**Safety Checks:**
- Detects potential secrets before commit
- Verifies tests pass before pushing
- Warns about large commits (>10 files)
- Confirms destructive operations
- Prevents force push to main/master

#### 7. Completion Validation

**Activation:** Before any "done", "tests pass", "ready to commit/PR" claim. Auto-triggers before status reports and phase transitions.

**Purpose:** Evidence-before-claims gate — refuse to claim work is complete without running fresh verification this turn.

**Iron Law:** No completion claims without fresh verification evidence.

**Gate Function:** IDENTIFY → RUN → READ → VERIFY → ONLY THEN claim.

**Kisune-specific patterns covered:** Status Reporting blocks, PM2/long-running commands, `[Confidence: X.X]` score, Full-mode phase gates, User Action Tasks.

#### 8. Systematic Testing

**Activation:** User implements functionality, tests fail, mentions debugging/TDD

**Purpose:** Guide test-driven development and systematic debugging

**TDD Workflow (Red-Green-Refactor):**

**RED Phase:**
1. Understand requirement
2. Write failing test
3. Run test, verify failure
4. Commit test

**GREEN Phase:**
1. Write minimal implementation
2. Run test, verify pass
3. Don't optimize yet
4. Commit implementation

**REFACTOR Phase:**
1. Clean up code
2. Remove duplication
3. Improve naming
4. Run tests, verify still passing
5. Commit refactor

**Test Generation:**
- Normal cases (happy path)
- Edge cases (boundary conditions)
- Error cases (invalid inputs)
- Integration cases (component interactions)

**Systematic Debugging Framework:**

**Phase 1: Root Cause Investigation**
- Reproduce bug consistently
- Identify symptoms
- Gather evidence (logs, errors, stack traces)
- Form hypothesis

**Phase 2: Pattern Analysis**
- When does it fail?
- When does it work?
- What changed recently?
- Environmental factors?

**Phase 3: Hypothesis Testing**
- Create minimal test case
- Add instrumentation
- Test hypothesis
- Iterate until root cause found

**Phase 4: Implementation**
- Write test reproducing bug
- Fix the bug
- Verify test passes
- Add regression tests
- Document root cause

## Slash Commands

### `/dev-workflow:spec`

**Description:** Launch spec-driven development workflow for features

**Usage:**

```bash
# Interactive menu
/dev-workflow:spec

# Create specific feature
/dev-workflow:spec "user authentication"

# Jump to specific phase
/dev-workflow:spec requirements
/dev-workflow:spec design
/dev-workflow:spec tasks
/dev-workflow:spec execute

# List all features
/dev-workflow:spec list
```

**Shortcut Commands:** Direct access to specific phases

```bash
# Phase shortcuts (equivalent to /dev-workflow:spec [phase])
/dev-workflow:spec:create           # Create new feature
/dev-workflow:spec:requirements     # Define requirements (EARS)
/dev-workflow:spec:design           # Generate technical design
/dev-workflow:spec:tasks            # Break down into TDD tasks
/dev-workflow:spec:execute          # Execute implementation
/dev-workflow:spec:list             # List all features

# With arguments
/dev-workflow:spec:create "user authentication"
/dev-workflow:spec:requirements 01-user-auth
/dev-workflow:spec:execute 01-user-auth
```

**Interactive Menu:**
```
📋 Spec-Driven Development Workflow

Choose an option:
1. Create new feature
2. Define requirements (EARS format)
3. Generate technical design
4. Break down into tasks (TDD)
5. Execute implementation
6. List all features

What would you like to do? (1-6)
```

**Phase Flow:**
1. **Create Feature** → Feature structure created in `docx/features/[NN-feature-name]/`
2. **Requirements** → Interactive EARS format elicitation, updates `requirements.md`
3. **Design** → Proposes approaches, creates comprehensive `design.md`
4. **Tasks** → Breaks into TDD tasks, creates `tasks.md` with checkboxes
5. **Execute** → Follows TDD cycle, auto-triggers quality checks, smart commits

## Templates

The plugin includes three comprehensive templates that are copied to feature directories:

### requirements.md Template

**Sections:**
- Overview
- Functional Requirements (EARS format)
  - Event-Driven
  - State-Driven
  - Ubiquitous
  - Conditional
  - Optional
- Non-Functional Requirements
  - Performance
  - Security
  - Usability
  - Reliability
  - Maintainability
- Constraints
- Acceptance Criteria (checkboxes)
- Out of Scope
- Dependencies
- Risks & Assumptions
- References

### design.md Template

**Sections:**
- Architecture Overview
- System Context
- Component Structure (responsibilities, dependencies, interfaces)
- Data Flow (diagram + detailed steps)
- API Contracts (request/response schemas)
- Data Models (schemas, relationships, validation)
- Error Handling (categories, strategies)
- Security Considerations (auth, validation, protection)
- Performance Considerations (caching, optimization, scaling)
- Testing Strategy (unit, integration, E2E, performance)
- Deployment Strategy
- Monitoring & Observability
- Open Questions (checkboxes)
- Alternatives Considered
- Timeline Estimate
- References

### tasks.md Template

**Sections:**
- Implementation Approach
- Progress Summary
- Tasks (TDD: Red-Green-Refactor)
  - Component Tasks (with RED-GREEN-REFACTOR checkboxes)
  - Integration Tasks
  - Error Handling Tasks
  - Performance Optimization Tasks
  - Documentation Tasks
  - Testing & Quality Assurance
  - Final Verification Tasks
- Task Tracking Legend
- Commit Strategy
- Notes (implementation notes, blockers, improvements, lessons)

## Integration with Existing Workflows

### Replaces/Enhances `/x:spec/*` Commands

This plugin integrates and extends existing spec-driven commands:

| Existing Command | Dev-Workflow Equivalent |
|-----------------|------------------------|
| `/x:spec:create` | Phase 1: Feature Creation |
| `/x:spec:requirements` | Phase 2: Requirements (EARS) |
| `/x:spec:design` | Phase 3: Technical Design |
| `/x:spec:tasks` | Phase 4: Task Breakdown |
| `/x:spec:execute` | Phase 5: Execution |
| `/x:spec:list` | `/dev-workflow:spec list` |

**Advantages over separate commands:**
- Single unified workflow
- Natural phase progression with approval gates
- Auto-triggers related skills (review, git-workflow)
- Integrated TDD methodology
- Consistent file structure

### Self-Contained Skill Ecosystem

The dev-workflow plugin is fully self-contained with integrated supporting skills:

**Planning & Design Skills:**
- `spec-driven-planning` - Feature creation, requirements gathering (EARS), technical design
- `more-creativity` - Divergent idea and hypothesis generation — cross-domain techniques, evaluation suppressed while generating, non-obviousness gate
- `brainstorming` - Collaborative exploration for requirements and design (WHAT and HOW)
- `grilling` - Round-based interrogation of an existing plan (model-invoked, or run `/grilling`) — batches the unblocked frontier, recommends an answer per question
- `grill-with-docs` - Composes `grilling` + `domain-modeling`
- `domain-modeling` - Glossary and ADR discipline — `docx/glossary.md` (grouped by bounded context when a term means different things in different modules), `docx/decisions/`
- `codebase-design` - Deep-module vocabulary for interface and seam decisions
- `prototype` - Throwaway code that answers one design question
- `investigate` - Research against primary sources; cited findings to `docx/research/`
- `wayfinder` - Map of decision tickets for efforts too big for one session, under `docx/wayfinder/`; one ticket per session

**Implementation Skills:**
- `spec-driven-implementation` - Task breakdown and execution with TDD
- `test-driven-development` - Strict RED-GREEN-REFACTOR TDD enforcement
- `spawn-agents` - Dispatch parallel subagents for 2+ independent problems; over-dispatch prevention
- `wizard` - Generate a runnable bash wizard for steps only a human can do: dashboard keys, `.env` values, GitHub secrets

**Quality Skills:**
- `review` - Systematic code review and refactoring suggestions
- `security-review` - OWASP Top 10 vulnerability detection and remediation
- `git-workflow` - Smart commits, branch management, PR creation
- `completion-validation` - Evidence-before-claims gate before marking work done
- `systematic-debug` - Systematic debugging framework — 4-mantra discipline plus multi-layer investigation
- `post-mortem` - Engineering record of a fixed bug — root cause, mechanism, fix, validation
- `scrutinize` - Outsider-perspective deep review — verdict: ship/fix/rework/reject
- `skill-maker` - Create/edit skills with TDD methodology
- `retro` - Session retrospective from this project's own log; proposes automated checks before steering-file rules
- `spec-review` - 3-agent spec review: spec quality, completeness, buildability

**Communication Skills:**
- `handoff` - Compact the conversation for a fresh agent to pick up
- `explain-in-html` - Render structure as an HTML page — Mermaid/UML/SVG diagrams, or a question round answered in-browser. Owns the medium, not the decision
- `deslop` - Rewrite prose in English or Thai (lessons, explanations, research notes, docs, PR descriptions, changelogs) so it reads like a person wrote it: reorder so the point comes first, plain words instead of LLM vocabulary, no ambiguity, every fact kept. Adapted from humanizer (MIT)

**Skill Integration:**
Skills automatically activate and work together based on context. For example:
- Requirements phase can activate `brainstorming` for scope exploration
- Design phase can activate `brainstorming` for architectural exploration
- Implementation phase activates `test-driven-development` for TDD enforcement
- Before commits, `review` auto-triggers for review
- Git operations use `git-workflow` for smart commit messages

**No External Dependencies Required** - All skills are included in the plugin.

## Agents

The plugin ships with 8 proactive agents that auto-activate based on context. Unlike skills (which respond to explicit requests), agents monitor the conversation and intervene when their specialization is relevant.

| Agent | Specialization | Activates When |
|-------|---------------|----------------|
| `code-reviewer` | Auto-reviews code after changes | After writing or modifying code |
| `tdd-guide` | Enforces write-tests-first methodology | New features, bug fixes, refactoring |
| `security-reviewer` | Flags vulnerabilities in auth, input, APIs | Auth code, user input, API endpoints |
| `planner` | Plans implementation once the architecture is settled | Multi-file features, complex refactors |
| `architect` | Software architecture specialist for system design and scalability | System-design or technology decisions, comparing architectural options |
| `build-error-resolver` | Fixes build/compilation errors with minimal diffs | Build fails, compilation errors |
| `database-reviewer` | PostgreSQL/Supabase query optimization and schema design | Writing SQL, designing schemas |
| `refactor-cleaner` | Dead code cleanup and consolidation specialist | Dead code, duplicates, unused dependencies |

## Example Workflows

### Workflow 1: Developing a New Feature

```bash
# Start new feature
User: /dev-workflow:spec
Assistant: [Shows interactive menu]

User: 1 (Create new feature)
Assistant: What feature would you like to create?

User: user authentication
Assistant: Created docx/features/01-user-authentication/
Ready to define requirements?

User: yes
Assistant: [Activates spec-driven skill, Phase 2]
Let me ask questions to capture requirements using EARS format...

[Interactive Q&A session - requirements captured]
Assistant: Requirements complete! Ready for design phase?

User: yes
Assistant: [Proposes 2-3 architectural approaches]
I recommend JWT-based authentication because...

User: Sounds good, proceed
Assistant: [Creates comprehensive design.md]
Design complete! Ready for task breakdown?

User: yes
Assistant: [Breaks into TDD tasks with checkboxes]
Tasks defined. Ready to begin implementation?

User: yes
Assistant: [Begins Phase 5 execution]
Starting Task 1: RED phase...
```

### Workflow 2: Quick Code Review

```bash
# Before committing changes
User: Review my changes before I commit
Assistant: [Activates review skill]

Running git diff --cached...

## Code Review: Authentication Module

### What I checked
- Traced the login flow through both callers
- Ran the test suite: 48 passed

### Issues Found

#### Priority: High
1. Missing Input Validation
   Location: src/auth/login.js:23
   Problem: Email and password not validated
   Fix: Add Zod schema validation

[...detailed review with code examples...]

Recommendation: Fix high-priority issues before committing.
```

### Workflow 3: Smart Git Commit

```bash
User: Commit my changes
Assistant: [Activates git-workflow skill]

Analyzing changes...
$ git status
$ git diff

Changes:
- src/auth/login.js (modified)
- src/auth/session.js (new file)
- tests/auth/login.test.js (modified)

Proposed commit message:
feat: Add session management to authentication

Proceed? (yes/no)

User: yes
Assistant: [Runs pre-commit checks, commits, verifies]
Commit successful!

Would you like to push to remote?
```

### Workflow 4: Debugging a Bug

```bash
User: I have a bug where login fails for emails with + symbols
Assistant: [Activates systematic-debug skill]

Let me help debug this systematically.

Phase 1: Root Cause Investigation

First, let me reproduce the issue...
[Writes test case reproducing bug]

Phase 2: Pattern Analysis

Bug Pattern:
- FAILS: user+test@example.com
- WORKS: user@example.com
Pattern identified: Email validation regex issue

Phase 3: Hypothesis Testing

Testing hypothesis: Regex rejects + symbol...
[Adds instrumentation, tests]

Root cause found: Database CHECK constraint too restrictive!

Phase 4: Implementation

Writing regression test...
[Writes test, fixes bug, verifies]

Bug fixed! Test now passes.
```

## File Structure

After using the plugin, your project will have this structure:

```
project/
├── docx/
│   └── features/
│       ├── 01-user-authentication/
│       │   ├── requirements.md
│       │   ├── design.md
│       │   ├── tasks.md
│       │   └── task_*_completed.md (optional)
│       ├── 02-payment-processing/
│       │   ├── requirements.md
│       │   ├── design.md
│       │   └── tasks.md
│       └── ...
├── src/
│   └── [your code]
├── tests/
│   └── [your tests]
└── ...
```

## Best Practices

### When to Use Each Skill

- Spec-Driven: Starting new features, planning complex functionality
- Review: Before commits, after completing components, when refactoring
- Git-Workflow: Every commit, creating branches, opening PRs, before pushing
- Systematic-Testing: Implementing functionality (TDD), when bugs occur, improving coverage

### Tips for Success

1. Follow the Flow - Let the plugin guide you through phases, dont skip ahead
2. Use Approval Gates - Review requirements/design before proceeding
3. Embrace TDD - Write tests first, it pays off
4. Commit Often - Small, focused commits are better
5. Review Early - Catch issues before they compound
6. Document As You Go - Easier than documenting later
7. Trust the Process - The structure prevents common mistakes

## Troubleshooting

### Skills Not Activating

Problem: Skills dont trigger automatically

Solution:
- Explicitly invoke with slash commands
- Use trigger phrases like "review this code" or "write tests"
- Check that plugin is properly installed

### Templates Not Copied

Problem: Feature directory created without templates

Solution:
- Manually copy templates from plugin directory
- Verify templates exist in dev-workflow/templates/
- Check file permissions

### EARS Format Unclear

Problem: Difficulty writing requirements in EARS format

Solution:
- Refer to examples in spec-driven skill documentation
- Start with simple Event-Driven requirements
- The spec-driven skill guides you through with questions

### Git Commands Failing

Problem: Git operations dont work as expected

Solution:
- Ensure youre in a git repository
- Check that gh CLI is installed for PR creation
- Verify git credentials are configured

## Contributing

We welcome contributions! If youd like to improve this plugin:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please follow the existing structure and documentation standards.

## License

MIT License

## Acknowledgments

- EARS requirements format inspired by IEEE standards
- TDD methodology based on Kent Becks practices
- Git workflow patterns from industry best practices
- Integration with Claude Code platform by Anthropic
- Skill and documentation prose edited with [humanizer](https://github.com/blader/humanizer) (MIT), which flags the signs of AI writing catalogued by Wikipedia
- Several v2.4.0 rules (tests of behavior rather than functions, validation at the system edge, PR verification from real command output) follow principles in [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan (MIT)

## Version History

**v2.4.0 (Current)**

**Added**
- `domain-modeling` groups the glossary by bounded context once a project has two, so *Account* can mean a login in `auth/` and a billing party in `billing/` without one definition blending both. A term that crosses contexts says where the two are translated, and a one-context project keeps a flat list.
- 3 `domain-modeling` eval cases: a one-context repo stays flat, a two-meaning term is split, and a plain code change does not start a glossary. All pass 3/3 on Sonnet.
- Every eval case has `tags:`: the skills it exercises, plus `routing` when it only checks that a skill fires or stays quiet. `claude plugin eval . --tag deslop` runs one skill's cases.
- `impl-quick` grader `ticks-each-task`: `plan.md` has a ticked box before Task 2 writes its first file.

**Changed**
- `test-driven-development`: before a refactor, write tests that pass on the current code, so they pin the behavior the refactor must keep. A good test fails when the behavior breaks and still passes after a rename. Every new behavior gets a test through the public interface, a rule `tdd-guide` and `review` now share.
- Coverage: `tdd-guide`, `AGENTS.md` and the requirements, design and tasks templates drop the fixed 80% target. Coverage after a change must be equal to or higher than before it, measured against the base branch, and a project's own CI threshold still applies.
- `review` validates data where it enters the system instead of adding defensive checks in every layer, handles each error where the code can act on it, and splits a function only when that lowers what a reader must trace. Its report, like `code-reviewer`'s, opens with "What I checked" instead of "Strengths".
- `git-workflow`: the PR template is Why / What changed / Scope / Blast radius / Verification. Verification lists only commands run in the session, with their output, and has no checkboxes. `deslop` tightens the other four sections, replacing the v2.3.0 Summary and Changes.
- `build-error-resolver` never casts just to silence a type error, and adds a null check only where null is a legal state.
- `refactor-cleaner`, during feature work, removes what the change makes obsolete and leaves unrelated dead code for a separate cleanup.
- `deslop` flags a colon that joins two clauses.
- `spec-driven-implementation` Quick mode: every box of a task, its steps and its Progress line, is ticked before the next task starts, never in one sweep after the last task. On `impl-quick`, Sonnet now ticks per task in 12 of 12 runs, up from 6 of 15 (Fisher two-sided p = 0.001); Opus did already and stays at 6 of 6.

**Fixed**
- `wizard` template: values are written single-quoted, so `source .env` works with spaces, `#`, `$` and quotes. An existing `.env` keeps its mode and stays a symlink, a new one is created at 0600, EOF at a prompt stops the wizard, the missing-browser warning now shows, and `write_env` also sets `$KEY`. Stages run inside `run_wizard`, so bash parses the whole file before the first prompt. Ported from `mattpocock/skills` (`868c4cf`, `49dd158`) with one correction for macOS `/bin/bash` 3.2, where upstream reads a stored `it's` back as `it\'s`. `tools/wizard-selftest.sh` grows from 6 to 16 cases.
- Install commands use the real marketplace id, `dev-workflow@kisune` and `trading@kisune`. The docs said `@xbklairith-kisune`, which no marketplace answers to. `README.md` and `PLUGINS_INSTALLATION.md` share one install block with update steps, and `tools/check.py` fails on a wrong id in any install or update line, including the one-step `--marketplace xbklairith/kisune` form. This README's Installation section now uses them too, replacing a step that copied the plugin into `~/.claude-code/plugins/`.
- `grilling` is documented as model-invoked (also `/grilling`), matching its frontmatter. `tools/check.py` now fails when a doc labels a skill user-only or model-invoked against its `disable-model-invocation` setting.
- Six eval cases ship their input documents: `deslop-ambiguity`, `deslop-engineering-doc`, `deslop-thai` and the three `domain-model` cases. A contributor's global `docs` ignore had kept them out of git, so a fresh clone ran those cases without them. `.gitignore` re-includes eval `docs/` folders, and `tools/check.py` fails when an ignore rule outside the repo hides an eval file.
- `impl-full` order graders read the trace, so a test or code file written with Write or through Bash counts. The old `tool_order` graders only saw files written with Edit and failed those runs. `red-run-before-code` now also needs the test run to fail, not just to happen.
- `deslop-ambiguity` grader `backup-first` checks the order of the steps. It had failed an Opus rewrite whose intro sentence named `bin/migrate` before step 1, "Back up the database".
- `plan-full-spec`: one LLM judge checked EARS form, coverage and placeholders together, and failed 2 of 6 Sonnet files that pass the mechanical checks. EARS form and placeholders are now regex graders, and the judge checks only that the delimiter, skip-header and missing-column cases are covered.

**v2.3.0**

**Added**
- `deslop` skill: rewrites existing prose in English or Thai (lessons, explanations, research notes, docs, PR descriptions, changelogs) so it reads like a person wrote it. It puts the point and prerequisites first, swaps LLM vocabulary for words people in the field use, replaces unclear pronouns, keeps a requirement's strength, and flags gaps instead of guessing. Facts, numbers, identifiers, citations, hedges and EARS lines stay exactly as written, and nothing is added. Thai tells in `references/thai.md`. Adapted from [humanizer](https://github.com/blader/humanizer) (MIT).
- `git-workflow` tightens a PR's Summary and Changes with `deslop`; `post-mortem` tightens its sentences, keeping sections, labels and order.
- 10 `deslop` eval cases: fires and stays quiet, PR text, engineering doc, release notes, Thai guide, ambiguity, lesson, research notes, pasted text. All pass 3/3 on Sonnet; on Opus 9 of 10 pass 3/3 and research notes passes 2/3.

**v2.2.1**

Prompt audit for current Claude models: dated emphasis, duplicated rules and stale facts removed from skills, agents and commands.

**Changed**
- `brainstorming` and `grilling`: the HARD-GATE blocks are now plain sentences; brainstorming presents the design in short sections instead of 200-300 words.
- `review` reviews the current diff by default instead of offering a menu, and reports metrics only from tools.
- `code-reviewer` runs the `review` checklist; `architect` points ADRs to `domain-modeling`; `build-error-resolver` runs auto-fixers only on files named in the errors; `planner` and `architect` descriptions split settled-architecture planning from design decisions.
- `/dev-workflow:spec:create`, `:execute` and `:list` handle Quick mode (`plan.md`) as well as Full mode (`tasks.md`).
- `AGENTS.md` lists all 8 agents.

**Fixed**
- `tools/wizard-selftest.sh` and `tools/test_skill_scripts.py` no longer inherit a pre-commit hook's `GIT_DIR`; run from a worktree, their temp repos' `git init` set `core.bare=true` on the real repo.

**v2.2.0**

Skills rewritten against Anthropic's [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), with each change checked by before/after behaviour evals on Sonnet and Opus.

**Changed**
- Session-start injection cut from about 9.5 KB to 3.2 KB (`using-kisune`). The index now says what each skill is for, and a new rule says when the user wins: speed words are not an opt-out, and an explicit opt-out is followed and the skipped skill is named. On prompts that push for a quick fix, Opus invoked a skill before editing in about 13 of 18 runs, up from 0 of 3.
- Shortened skills, with no regression on their evals:
  - `spec-driven-planning`: 500 → 250 lines. It also fixes the template path, which broke when the plugin was installed.
  - `test-driven-development`: 377 → 245 lines.
  - `spec-driven-implementation`: 351 → 184 lines. Sonnet's Full-mode runs now commit per phase in 3 of 3 runs, up from 1 of 3.
  - `brainstorming`: 255 → 50 lines.
  - `systematic-debug`: 212 → 161 lines.
- Seven descriptions rewritten to say both what the skill does and when to use it: grilling, spec-review, git-workflow, review, systematic-debug, and the trading skills pattern and research.

**Added**
- `tools/check.py` lints every skill against the guide:
  - name format and length;
  - description length, with no XML in it;
  - a "use when" clause on every model-invocable skill;
  - a body under 500 lines;
  - links one level deep, written with forward slashes;
  - a table of contents in long reference files.

  `tools/check-selftest.sh` proves that each check can fail.
- `dev-workflow/evals/` has 15 `claude plugin eval` cases. They check that:
  - skills fire on their triggers and stay quiet otherwise;
  - the agent reaches for a skill under pressure;
  - Quick and Full planning produce the right files;
  - implementation writes tests before code, runs them, and commits per phase.
- `skill-maker` now leaves at least three eval cases behind with every new skill (trigger, no-trigger, work). Reference: `references/plugin-evals.md`.



**Fixed**
- `SessionStart` hook matcher now includes `resume` — was `startup|clear|compact`, so a resumed session loaded no `using-kisune` router and the skill-check discipline was silently absent there

**Added**
- `skill-maker` RED phase gains a blinding protocol: no leakage words in anything the subagent sees, no chain-eliciting cues, grade the artifact rather than the self-report, judge on a different model family, and treat judge disagreement as an ambiguous rubric rather than a tie to break. Adapted from the `eval.md` playbook in michael-denyer/pstack-claude (MIT)
- `tools/check.py` — fails when a fact kisune keeps in more than one place has drifted: version strings across the three manifests, skill counts in four documents, the `using-kisune` index row set (equality, failing by name), and references to removed skills. `tools/check-selftest.sh` proves each of the four checks can fail
- `.githooks/pre-commit` runs the checker, `tools/test_skill_scripts.py` (the wayfinder and retro scripts) and `tools/wizard-selftest.sh`; enable with `git config core.hooksPath .githooks`

**Added (skills)** — three skills adapted from mattpocock/skills (MIT; notice in each skill's `references/NOTICE.md`)
- `wizard` — generates a runnable bash wizard for steps only a human can do (dashboard keys, `.env`, GitHub secrets/variables). The deliverable is the script; a setup doc may point at it, never replace it. `assets/template.sh` adds a guard upstream lacks: it will not write secrets into an `.env` that git does not ignore without asking. `tools/wizard-selftest.sh` runs 6 behavioural checks against it under the system bash
- `retro` — session retrospective from this project's own log. `scripts/session_log.py` reads only the current project's directory under `~/.claude/projects/` (never other projects' private chats) and summarises re-reads, re-runs and failed calls. Orders fixes check-first: a mechanical mistake gets a lint rule, hook or CI job, not a `CLAUDE.md` line, and a retro should usually shrink the steering file
- `wayfinder` — for efforts too big for one session: a map of decision tickets in `docx/wayfinder/<effort>/`, fog left unsliced until the questions are sharp, one ticket per session. `scripts/frontier.py` computes closed/claimed/blocked/frontier from ticket frontmatter so a fresh session can resume without reading every ticket

**Evaluated, not changed** — upstream updates to `systematic-debug`, `review`, `test-driven-development`, `skill-maker` and `codebase-design` were checked against current behaviour first; each existing skill already produced the target behaviour on its scenario, so nothing was ported

**v2.0.0**

**Removed**
- Remove `explain-in` — the leadership-reframing skill. Its name is reused by `explain-in-html`, which does something different. Any workflow invoking `explain-in` must be updated; `post-mortem` no longer offers the leadership handoff (breaking, hence the major bump)

**Added**
- Add `explain-in-html` skill — renders output as an HTML page instead of terminal text. Two modes inferred from content: **explain** (Mermaid, UML, ER and state charts, hand-authored SVG for before/after comparisons) and **interact** (a question round answered in-browser, answers read back via `ArtifactData`). Owns the medium only — `grilling`, `brainstorming` and `scrutinize` keep deciding *what* to ask or say and hand the rendering here. Delegates page design to `Artifact quickstart` and figure judgment to the built-in `artifact-diagramming` skill. Falls back to a local `docx/explainers/<slug>.html` when Artifacts are unavailable, and to `AskUserQuestion` in interact mode
- Add `docx/explainers/` to the storage convention

**Fixed**
- Correct long-stale skill counts in `dev-workflow/README.md` ("thirteen"/"13") and `PLUGINS_INSTALLATION.md` ("20")

**v1.7.0**
- Add more-creativity skill — divergent idea and hypothesis generation, placed ahead of `brainstorming` in the planning flow. 15-technique library selected by problem type, with at least one technique forced from outside the problem's own category; intensity dial (0.1–1.0); divergence lock suppressing feasibility/cost/priority language until after the quality gate; non-obviousness gate rejecting anything the user could have reached alone; hypothesis mode requiring `Mechanism:` and `False if:` per claim plus a cheapest-discriminator triage line
- more-creativity defers to `brainstorming`'s design-approval gate rather than bypassing it, and makes its discard step observable via an `Obvious options skipped:` line
- Record the skill's RED/GREEN test scenarios in `references/test-scenarios.md` so behaviour is re-testable after edits; upstream MIT notice in `references/NOTICE.md`

**v1.6.1**
- Fix `using-kisune` index — `grilling` was still documented as `/grilling` only after v1.6.0 made it model-invocable
- Fix `skill-maker` definition of `allowed-tools` — it pre-approves tools, it does not restrict them (`disallowed-tools` restricts)
- Correct the frontmatter reference in CLAUDE.md — 19 skill fields (not 10) and 18 agent fields (not 2)

**v1.6.0**
- Add 7 skills derived from the mattpocock/skills reference — `grilling`, `grill-with-docs`, `domain-modeling`, `handoff`, `investigate`, `prototype`, `codebase-design`
- Fix `explain-in` YAML parse failure — an unquoted description containing `": "` broke the frontmatter, silently dropping the skill from CLI discovery
- Establish the `docx/` storage convention — every skill that persists a file now writes under `docx/` (see CLAUDE.md)
- Fix dead `systematic-testing` references in `git-workflow` and `review`
- Correct skill/command/template counts across README, CLAUDE.md, and the `using-kisune` index

**v1.5.0**
- Simplify spec-review to 3 agents (Spec Quality, Completeness, Buildability) — down from 6, significantly lower token usage
- Add context:fork + Agent to spec-review allowed-tools for proper subagent isolation
- Add systematic-debug skill — 4-mantra discipline (reproduce, trace, falsify, breadcrumbs) + multi-layer investigation + 3-Failures Gate
- Add post-mortem skill — canonical engineering record with required-inputs gate, 9 sections, tracker-agnostic
- Add scrutinize skill — outsider-perspective review questioning intent first, traces code path end-to-end, ship/fix/rework/reject verdict
- Add explain-in skill — rewrite engineering content for leadership, shaped per channel (JIRA, Slack, standup, email, talking-points)
- Rename management-talk → explain-in
- Fix 7 review findings: dead systematic-testing ref, broken table row, missing git-workflow chain, double-offer overlap, worked example added
- Generalize JIRA/ticket assumptions across post-mortem and explain-in — supports GitHub Issues, Linear, or no tracker

**v1.4.0**
- Add systematic-debug, post-mortem, scrutinize, explain-in skills

**v1.3.0**
- Add spec-review skill — 6-dimension sequential review (business, correctness+ambiguity smells, completeness+safety invariants, compatibility+implementation blockers, traceability, testability scoring)
- Add allowed-tools frontmatter to 6 high-activity skills — reduces permission prompts
- Add user-invocable: false to completion-validation; disable-model-invocation: true to using-kisune
- Fix broken skill references (TodoWrite→TaskCreate, dead spec-driven/documentation refs)
- Fix translate skill description (Backtrader→pandas/framework-agnostic)
- Update all agent documentation — 8 agents now fully documented in README and CLAUDE.md
- Sharpen skill descriptions: spec-driven-planning, spec-driven-implementation, systematic-testing

**v1.2.1**
- Add spec-review skill with 6-dimension parallel agent review

**v1.2.0**
- Added 6 shortcut commands for direct phase access (/dev-workflow:spec:create, :requirements, :design, :tasks, :execute, :list)
- Fixed skill activation to use explicit Skill tool invocation
- Prevents command collision with global /x:spec:* commands
- Enhanced routing logic for reliable skill triggering

**v1.1.0**
- Split spec-driven into planning and implementation phases
- Added self-contained brainstorming and test-driven-development skills
- Eight integrated skills working seamlessly together
- One slash command (/dev-workflow:spec)
- Three comprehensive templates
- Self-contained with no external dependencies
- Complete documentation

**v1.0.0 (Initial Release)**
- Ten core skills (spec-driven planning/implementation, brainstorming, TDD, review, security-review, git-workflow, completion-validation, systematic-testing)
- One slash command (/spec)
- Three comprehensive templates
- Complete documentation

## Support

For issues, questions, or feedback:
- Open an issue in the repository
- Refer to skill documentation in skills/*/SKILL.md files
- Check Claude Code documentation for plugin system details

---

Happy Coding with Dev-Workflow!

Remember: Systematic beats heroic. Quality beats speed. Tests beat debugging. Documentation beats memory.
