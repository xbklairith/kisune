---
name: spec-driven-planning
description: Plan new features using spec-driven workflow — auto-picks Quick (single plan.md) or Full (3-file EARS spec) mode. Use when creating features, writing requirements, or designing architecture.
allowed-tools: Read, Write, Bash
---

# Spec-Driven Planning Skill

## Purpose

Guide feature planning in one of two modes:

- **Quick mode** — single `docx/features/[NN-name]/plan.md` with bite-sized tasks. No EARS, no RGR. For solo work, ≤3 days, no compliance/handoff. Derived from the superpowers writing-plans pattern.
- **Full mode** — three files (`requirements.md` EARS + `design.md` + `tasks.md`) with three approval gates and TDD enforcement downstream. For team work, multi-week, compliance/audit, or stakeholder review.

The skill picks a mode (or asks when ambiguous), then runs the matching playbook.

## Activation Triggers

Activate this skill when:
- User says "create a new feature", "plan a feature", "I need to build [X]"
- User mentions "requirements", "specifications", "specs", "architecture", "technical design"
- User uses `/dev-workflow:spec` command (any sub-arg)

---

## Mode Selection (ALWAYS DO THIS FIRST)

Before writing anything, decide Quick vs Full.

### Auto-pick Quick when ALL true:
- Estimated effort ≤ 3 days OR ≤ 8 tasks
- Solo developer; no stakeholder approval needed
- No compliance, audit, or regulatory requirement
- No major architectural decision (no "X vs Y?" trade-off)
- Requirements clear from the user's request
- No cross-team handoff
- User said "quick", "lightweight", "simple plan", or `/dev-workflow:spec quick`

### Auto-pick Full when ANY true:
- Effort > 1 week OR > 15 tasks
- Stakeholders ≠ engineers must approve scope
- Compliance / audit / regulatory traceability required
- Architecture choice with long-term consequences
- Requirements ambiguous; need elicitation
- Multi-developer or handoff likely
- User said "full spec", "EARS", "requirements doc", or `/dev-workflow:spec full`

### Otherwise, treat as ambiguous

The thresholds above are deliberately gapped — 4-7 days of effort, 9-15 tasks, or any partial signal match falls in the middle zone. If you don't get a clean **all-true** Quick or **any-true** Full match, the feature is ambiguous by definition. Ask the user.

### Ambiguous? Ask once with this menu:

```
This feature could go either way. Pick a planning mode:

1. Quick — single plan.md, no EARS, no RGR (recommended for solo, ≤3 days)
2. Full — 3-file spec with EARS + TDD enforcement (recommended for team, >1 week, compliance)

Default if you don't pick: Quick.
```

**Announce the chosen mode:**
> "Using [Quick/Full] mode. [One-sentence reason from signals above.]"

Then run the matching playbook below.

---

## Quick Mode Playbook

**Output:** `docx/features/[NN-feature-name]/plan.md` (single file)

### Step 1: Create feature directory

1. `ls docx/features/` to find next NN number
2. `mkdir -p docx/features/[NN-feature-name]`
3. Read `dev-workflow/templates/plan.md`
4. Write to `docx/features/[NN-feature-name]/plan.md`, replacing `[Feature Name]` with the actual name

### Step 2: Fill in the plan

Audience assumption: an engineer with zero context for this codebase. Be exact.

Required sections:
- **Goal** — one sentence
- **Architecture** — 2-3 sentences, what goes where and why
- **Tech Stack** — key libraries / files
- **Out of Scope** — keeps scope honest
- **Tasks** — bite-sized (2-5 min steps), with:
  - **Files:** exact paths (Create / Modify with line ranges)
  - **Steps:** numbered, each one action. Include complete code, not "add validation here". Include exact verification commands with expected output. End with a commit step.

Granularity rule: if a step takes longer than 5 minutes, split it.

### Step 3: One approval gate

> "Quick plan saved to `docx/features/[NN-feature-name]/plan.md`. Review and approve to proceed to implementation. Run `/dev-workflow:spec execute` when ready."

That's it. No EARS, no design alternatives, no RGR. Implementation is handled by `spec-driven-implementation` (which auto-detects `plan.md` and runs in Quick execution mode).

### Quick mode is wrong if you find yourself...

- Writing requirements that need approval from non-engineers → switch to Full
- Comparing 2+ architectural approaches → switch to Full
- Listing > 15 tasks → switch to Full
- Needing traceability from requirement → task → test → switch to Full

To upgrade, see "Upgrade path" at the bottom of this skill.

---

## Full Mode Playbook

Three phases, three approval gates. Use this when signals say Full.

### Phase 1: Feature Creation

**Goal:** Establish feature structure and placeholder files

**Process:**
1. Parse feature name from user input
2. Check existing features using Bash tool: `ls docx/features/`
3. Determine next number (NN) for feature directory
4. Create directory using Bash tool: `mkdir -p docx/features/[NN-feature-name]`
5. Copy templates from plugin to feature directory:
   - Use Read tool: `dev-workflow/templates/requirements.md`
   - Use Write tool: `docx/features/[NN-feature-name]/requirements.md` (replace [Feature Name] with actual name)
   - Use Read tool: `dev-workflow/templates/design.md`
   - Use Write tool: `docx/features/[NN-feature-name]/design.md` (replace [Feature Name] with actual name)
   - Use Read tool: `dev-workflow/templates/tasks.md`
   - Use Write tool: `docx/features/[NN-feature-name]/tasks.md` (replace [Feature Name] with actual name)

**Output:**
```
Created feature: docx/features/[NN-feature-name]/
- requirements.md (from template)
- design.md (from template)
- tasks.md (from template)

Next step: Define requirements using EARS format
```

**User Confirmation:**
> "Feature structure created. Ready to define requirements?"

---

### Phase 2: Requirements Definition (EARS Format)

**Goal:** Capture clear, testable requirements using EARS methodology

**Scope Decomposition Check (do FIRST):**

Before eliciting requirements, scan the request. If it describes multiple independent subsystems (e.g., "auth + billing + admin dashboard"), STOP and decompose into separate features before refining any one. Don't burn elicitation questions on a feature that should be three.

> 🗣 Say: "This request covers [N] independent subsystems. I'll create separate features for each before eliciting requirements."

**No Placeholders Rule:**

Requirements and downstream plans MUST NOT contain:
- "TBD" / "to be determined" / "to be defined later"
- "add appropriate X" / "handle errors as needed" / "validate as required"
- "similar to [other thing]" / "see above" without specifics
- vague verbs without objects: "update", "improve", "fix", "enhance"
- "etc." or trailing ellipses in requirement text
- references to undefined names (REQ-IDs that don't exist, modules not yet specified)
If you cannot specify a requirement concretely, ask the user. Don't write a placeholder.

**Brainstorming Integration (Optional):**
- If user has rough idea but unclear requirements, use Skill tool to invoke: `dev-workflow:brainstorming`
- Helps clarify what to build vs. what's out of scope
- Explores different feature scopes through collaborative questioning
- Determines must-haves vs. nice-to-haves

**How to activate:**
```
Use Skill tool: Skill(skill: "dev-workflow:brainstorming")
```

**EARS Format Explained:**

EARS (Easy Approach to Requirements Syntax) provides five templates for unambiguous requirements:

1. **Ubiquitous Requirements** - Always true
   - Template: "The system SHALL [requirement]"
   - Example: "The system SHALL validate all user inputs before processing"

2. **Event-Driven Requirements** - Triggered by events
   - Template: "WHEN [trigger] THEN the system SHALL [response]"
   - Example: "WHEN user clicks submit THEN the system SHALL validate form data"

3. **State-Driven Requirements** - Active during specific states
   - Template: "WHILE [state] the system SHALL [requirement]"
   - Example: "WHILE processing payment the system SHALL display loading indicator"

4. **Conditional Requirements** - Based on conditions
   - Template: "IF [condition] THEN the system SHALL [requirement]"
   - Example: "IF user role is admin THEN the system SHALL show management panel"

5. **Optional Requirements** - Feature toggles
   - Template: "WHERE [feature included] the system SHALL [requirement]"
   - Example: "WHERE premium subscription is active the system SHALL enable advanced analytics"

**Research Protocol (Before Eliciting Requirements):**

Before diving into requirement questions, gather context through research:

1. **Prior Art Research**
   - Use WebSearch to find similar features/products
   - Query: "[feature type] best practices 2025"
   - Query: "[feature type] common requirements"

2. **Technical Documentation**
   - Use WebFetch on relevant technical docs, APIs, or standards
   - Fetch competitor/similar product documentation

3. **API Research (if applicable)**
   - Use Bash with `curl` to explore API endpoints
   - Fetch API documentation and schemas

4. **Document Findings**
   - Summarize key insights in requirements.md under "## Research Summary"
   - Note patterns, anti-patterns, and industry standards discovered

> 🗣 Say: "Let me research similar implementations before we define requirements."

---

**Systematic Questioning Approach:**

Ask the user these questions to elicit requirements:

1. **Core Functionality**
   - "What is the primary purpose of this feature?"
   - "What problem does it solve?"

2. **Event-Driven Requirements**
   - "What user actions trigger this feature?"
   - "What system events are involved?"

3. **State-Driven Requirements**
   - "Are there different states or modes?"
   - "What should happen during each state?"

4. **Conditional Requirements**
   - "Are there different behaviors for different users/roles?"
   - "What conditions affect functionality?"

5. **Performance Requirements**
   - "Are there response time requirements?"
   - "What's the expected load/scale?"

6. **Security Requirements**
   - "What data needs protection?"
   - "Who should have access?"

7. **Error Handling**
   - "What can go wrong?"
   - "How should errors be handled?"

8. **Edge Cases**
   - "What are the boundary conditions?"
   - "What happens at extremes?"

**Best Practices:**
- Use "SHALL" for mandatory requirements
- Be specific and measurable (avoid "quickly", use "within 2 seconds")
- One requirement per statement
- Avoid ambiguous terms ("appropriate", "reasonable", "user-friendly")
- Use active voice

**Requirement IDs & Traceability:**
- Assign unique IDs to every requirement using a consistent prefix (e.g., `REQ-001`).
- Keep numbering sequential across all requirement types (functional + non-functional).
- Record the IDs directly in each requirement line so later tasks can reference them.
- Add a short traceability note indicating how tasks/design will map back to these IDs.

**Output Format:**
Update `docx/features/[NN-feature-name]/requirements.md` with:
- Overview section
- Functional requirements (organized by EARS type)
- Non-functional requirements (performance, security, usability)
- Constraints
- Acceptance criteria (checkboxes)
- Out of scope items

**User Confirmation:**
> "Requirements complete. Ready for design phase?"

---

### Phase 3: Technical Design

**Goal:** Create comprehensive technical design with architectural decisions

**Research Protocol (Before Design):**

Before proposing architectural approaches, research solutions:

1. **Architecture Research**
   - Use WebSearch: "[technology] architecture patterns 2025"
   - Use WebSearch: "[problem domain] implementation approaches"

2. **Library/Framework Research**
   - Use WebFetch on documentation for potential libraries
   - Compare approaches used by similar projects

3. **API Research (if applicable)**
   - Use WebFetch on external API documentation
   - Use Bash with `curl` to test API endpoints
   - Understand integration requirements and constraints

4. **Document Findings**
   - Add "## Technical Research" section to design.md
   - Include links to sources and key insights

> 🗣 Say: "Let me research technical approaches before proposing architecture options."

---

**Process:**

1. **Brainstorming Integration**
   - Use Skill tool to invoke: `dev-workflow:brainstorming` for collaborative design exploration
   - Explore 2-3 different architectural approaches
   - Discuss trade-offs for each approach

   **How to activate:**
   ```
   Use Skill tool: Skill(skill: "dev-workflow:brainstorming")
   ```

**UltraThink for Complex Designs:**
Before proposing technical approaches, activate deep thinking when:
- Architecture involves multiple services or complex data flows
- Trade-offs between approaches aren't obvious
- Design impacts security, performance, or scalability
- Requirements seem contradictory or incomplete

> 🗣 Say: "This design requires deep thinking. Let me ultrathink the architectural fundamentals before proposing approaches."

**During UltraThink, question:**
- Are we solving the right problem?
- What are we assuming that might be wrong?
- What could break at scale?
- What's the simplest architecture that works?
- What are the hidden costs of each approach?
- What would we do differently if starting from scratch?

**After UltraThink:** Present approaches with explicit reasoning about architectural trade-offs and scalability considerations.

2. **Approach Comparison**
   Present options with trade-offs:

   **Option A: [Approach Name]**
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Complexity: Low/Medium/High
   - Timeline: [Estimate]

   **Option B: [Approach Name]**
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Complexity: Low/Medium/High
   - Timeline: [Estimate]

3. **Recommendation**
   - State recommended approach
   - Provide clear reasoning
   - Explain why it best fits requirements

4. **Design Document Structure**
   Create comprehensive `design.md` covering:

   **Architecture Overview**
   - How feature fits into system
   - High-level component diagram (ASCII art)

   **Component Structure**
   - List components with responsibilities
   - Define dependencies between components
   - Specify public interfaces

   **Data Flow**
   - Step-by-step data movement
   - Diagram showing flow

   **API Contracts**
   - Input/output schemas
   - Error responses
   - Example requests/responses

   **Error Handling**
   - Error scenarios and handling strategy
   - Fallback behaviors

   **Security Considerations**
   - Authentication/authorization
   - Input validation
   - Data protection

   **Performance Considerations**
   - Optimization strategies
   - Caching approach
   - Database indexing needs

   **Testing Strategy**
   - Unit test areas
   - Integration test scenarios
   - E2E test workflows

**Approval Gate:**
> "Design complete. Ready for task breakdown?"

Wait for explicit user approval before proceeding.

---

## Next Steps

### After Quick mode (plan.md saved):
Run `/dev-workflow:spec execute`. The implementation skill auto-detects `plan.md` and runs Quick execution: follow the steps, run verification commands, commit. No RGR enforcement.

### After Full mode (design.md approved):
Run `/dev-workflow:spec tasks` then `/dev-workflow:spec execute`. The implementation skill detects `tasks.md` and runs Full execution: RED-GREEN-REFACTOR per task, traceability to requirement IDs, quality gates.

Both modes integrate with `dev-workflow:review`, `dev-workflow:git-workflow`, and `dev-workflow:test-driven-development` (the last one is mandatory in Full mode, optional in Quick).

---

## Upgrade Path: Quick → Full

If a Quick feature outgrows its plan (scope expands, stakeholders enter, architecture decisions emerge):

1. Read existing `docx/features/[NN-name]/plan.md`
2. Seed the three Full-mode files from it:
   - **requirements.md** — extract Goal + implicit requirements from tasks; rewrite in EARS; assign REQ-### IDs
   - **design.md** — extract Architecture + Tech Stack; add "Alternatives Considered" by interviewing the user
   - **tasks.md** — re-break tasks into RED/GREEN/REFACTOR with linked requirement IDs
3. Rename `plan.md` → `plan.archived.md` for traceability
4. Resume from Phase 2 (Requirements) or Phase 3 (Design) of the Full playbook

Downgrade (Full → Quick) is **not supported**. Once EARS requirements exist, throwing them away is wasteful — just continue in Full mode.

---

## Examples

### Example A: Quick mode (auto-picked)

**User:** "Add a CSV export button to the reports page"

**Assistant:**
```
Signals: solo, ~1 day, no compliance, no architectural decision → Quick mode.

Created docx/features/03-csv-export/plan.md with 4 tasks.
Review and approve, then run /dev-workflow:spec execute.
```

### Example B: Full mode (auto-picked)

**User:** "Add user authentication across web + mobile, must meet SOC 2"

**Assistant:**
```
Signals: multi-platform, compliance required, JWT vs session decision → Full mode.

Created docx/features/04-user-authentication/{requirements,design,tasks}.md.
Phase 1 complete. Phase 2: I'll elicit requirements in EARS format.

1. What authentication methods should be supported?
2. What's the session lifetime requirement?
[...]
```

### Example C: Ambiguous (asks user)

**User:** "Add a notifications system"

**Assistant:**
```
Scope is ambiguous between Quick and Full. Pick one:

1. Quick — single plan.md, no EARS, no RGR (≤3 days, solo)
2. Full — 3-file spec with EARS + TDD (>1 week, team, compliance)

Default if you don't pick: Quick.
```

---

## Notes

- Always request explicit approval between phases
- Use EARS format strictly for requirements
- Focus on "what" and "how", not "doing"
- Explore multiple architectural options before recommending one
