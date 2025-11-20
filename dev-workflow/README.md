# Dev-Workflow Plugin

Integrated development lifecycle plugin for Claude Code combining spec-driven development with code quality, git workflow, documentation, and systematic testing.

## Overview

The Dev-Workflow plugin provides a comprehensive, systematic approach to software development from initial concept through production deployment. It integrates eight specialized skills that work together seamlessly to ensure high-quality, well-tested, properly documented code with no external dependencies.

### What This Plugin Does

- **Guides feature development** through structured phases (requirements → design → tasks → execution)
- **Enforces code quality** through systematic reviews and refactoring suggestions
- **Manages git operations** with smart commits, branch management, and PR creation
- **Generates documentation** for code, APIs, architecture, and user guides
- **Drives test-first development** with TDD workflow and systematic debugging

### Philosophy

- **Systematic over ad-hoc**: Structured workflows prevent shortcuts and ensure quality
- **Natural activation**: Skills auto-trigger based on context, reducing manual overhead
- **Quality gates**: Built-in checkpoints catch issues early
- **Education through use**: Teaches best practices while working

## Installation

1. **Copy Plugin to Claude Code Plugins Directory:**
   ```bash
   # macOS/Linux
   cp -r dev-workflow ~/.claude-code/plugins/

   # Windows
   xcopy dev-workflow %USERPROFILE%\.claude-code\plugins\dev-workflow /E /I
   ```

2. **Verify Installation:**
   ```bash
   # In Claude Code
   /help
   # Should show /dev-workflow:spec and /dev-workflow:review commands
   ```

3. **Update Plugin Metadata (Optional):**
   Edit `.claude-plugin/plugin.json` to add your author information:
   ```json
   {
     "author": {
       "name": "Your Name",
       "email": "your.email@example.com"
     }
   }
   ```

## Core Skills

The plugin includes 8 integrated skills organized into planning, implementation, and quality categories.

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
- Presents information incrementally (200-300 word sections)
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

#### 5. Code Quality

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
- Strengths (what's done well)
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

#### 7. Documentation

**Activation:** User says "document this", asks "how does this work?", mentions docs/README

**Purpose:** Generate and maintain comprehensive documentation

**Documentation Types:**

**Code Documentation (Docstrings):**
- Function/class documentation
- Parameters, return values, examples
- Exceptions/errors
- Implementation notes
- Language-specific formats (Python, TypeScript, etc.)

**API Documentation:**
- Endpoint descriptions
- Request/response schemas
- Example payloads
- Error codes and descriptions
- Authentication requirements

**Architecture Documentation:**
- Component overview diagrams (ASCII art)
- Data flow descriptions
- Integration points
- Technology stack
- Security architecture
- Performance considerations

**README Generation:**
- Project overview
- Installation instructions
- Usage examples
- API reference
- Configuration options
- Contributing guidelines

**Code Explanations:**
- High-level purpose
- Step-by-step logic flow
- Key algorithms/patterns
- Edge cases handled
- Performance considerations

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

### `/dev-workflow:review`

**Description:** Trigger comprehensive code review with quality checks

**Usage:**

```bash
# Interactive (asks what to review)
/dev-workflow:review

# Review specific file
/dev-workflow:review src/auth/login.js

# Review directory
/dev-workflow:review src/auth/

# Review all changes
/dev-workflow:review .
```

**Review Process:**
1. Asks what to review (staged, unstaged, specific file, feature)
2. Runs appropriate `git diff` or reads files
3. Applies comprehensive checklist (structure, errors, security, performance, testing)
4. Generates detailed report with priorities
5. Suggests refactorings with code examples
6. Provides action items

**Review Output:**
- ✅ Strengths (what's done well)
- ⚠️ Issues Found (High/Medium/Low priority)
- 💡 Refactoring Suggestions (with before/after code)
- 📊 Code Metrics (complexity, coverage, maintainability)
- 🎯 Action Items (checkboxes)
- Overall assessment and recommendation

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
- Auto-triggers related skills (code-quality, git-workflow)
- Integrated TDD methodology
- Consistent file structure

### Self-Contained Skill Ecosystem

The dev-workflow plugin is fully self-contained with integrated supporting skills:

**Planning & Design Skills:**
- `spec-driven-planning` - Feature creation, requirements gathering (EARS), technical design
- `brainstorming` - Collaborative exploration for requirements and design (WHAT and HOW)

**Implementation Skills:**
- `spec-driven-implementation` - Task breakdown and execution with TDD
- `test-driven-development` - Strict RED-GREEN-REFACTOR TDD enforcement

**Quality Skills:**
- `code-quality` - Systematic code review and refactoring suggestions
- `git-workflow` - Smart commits, branch management, PR creation
- `documentation` - Code, API, and architecture documentation generation
- `systematic-testing` - Testing guidance and systematic debugging framework

**Skill Integration:**
Skills automatically activate and work together based on context. For example:
- Requirements phase can activate `brainstorming` for scope exploration
- Design phase can activate `brainstorming` for architectural exploration
- Implementation phase activates `test-driven-development` for TDD enforcement
- Before commits, `code-quality` auto-triggers for review
- Git operations use `git-workflow` for smart commit messages

**No External Dependencies Required** - All skills are included in the plugin.

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
Assistant: [Activates code-quality skill]

Running git diff --cached...

## Code Review: Authentication Module

### Strengths
- Clean separation of concerns
- Comprehensive test coverage

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
Assistant: [Activates systematic-testing skill]

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
- Code-Quality: Before commits, after completing components, when refactoring
- Git-Workflow: Every commit, creating branches, opening PRs, before pushing
- Documentation: After implementing functions, creating APIs, completing features
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

## Version History

**v1.2.0 (Current)**
- Added 6 shortcut commands for direct phase access (/dev-workflow:spec:create, :requirements, :design, :tasks, :execute, :list)
- Fixed skill activation to use explicit Skill tool invocation
- Prevents command collision with global /x:spec:* commands
- Enhanced routing logic for reliable skill triggering

**v1.1.0**
- Split spec-driven into planning and implementation phases
- Added self-contained brainstorming and test-driven-development skills
- Eight integrated skills working seamlessly together
- Two slash commands (/dev-workflow:spec, /dev-workflow:review)
- Three comprehensive templates
- Self-contained with no external dependencies
- Complete documentation

**v1.0.0 (Initial Release)**
- Five core skills (spec-driven, code-quality, git-workflow, documentation, systematic-testing)
- Two slash commands (/spec, /review)
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
