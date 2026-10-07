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
3. Read `plan.md` from the plugin's templates (`<base>/../../templates/plan.md`, where `<base>` is this skill's base directory)
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

**Templates** live in the plugin's `templates/` directory, two levels above this skill's base directory (`<base>/../../templates/`). Read them from there, not from the user's project.

### Phase 1: Feature Creation

1. Find the next `NN` in `docx/features/` and create `docx/features/[NN-feature-name]/`.
2. Copy `requirements.md`, `design.md` and `tasks.md` from the templates, replacing `[Feature Name]`.

> "Feature structure created. Ready to define requirements?"

---

### Phase 2: Requirements Definition (EARS Format)

**Scope check first.** If the request spans independent subsystems ("auth + billing + admin dashboard"), split it into separate features before eliciting anything.

**Research before asking.** Look at how similar features and products handle it (WebSearch / WebFetch on docs and APIs) and record what you learn under `## Research Summary` in requirements.md.

**Elicit** what the request leaves open: purpose, triggering events, states, role- or condition-dependent behaviour, performance targets, security, failure modes, and edge cases. For a rough idea with unclear scope, invoke `dev-workflow:brainstorming` first.

**Write every requirement in one EARS form:**

| Form | Template |
|---|---|
| Ubiquitous | The system SHALL [requirement] |
| Event-driven | WHEN [trigger] THEN the system SHALL [response] |
| State-driven | WHILE [state] the system SHALL [requirement] |
| Conditional | IF [condition] THEN the system SHALL [requirement] |
| Optional | WHERE [feature included] the system SHALL [requirement] |

- One requirement per statement, active voice, measurable ("within 2 seconds", not "quickly").
- Give each a sequential ID (`REQ-001`, …) across functional and non-functional requirements, so design and tasks can trace back to it.

**No placeholders.** Never write "TBD", "etc.", "add appropriate X", "handle errors as needed", "similar to Y", a bare "update/improve/fix", or a reference to a REQ-ID or module that doesn't exist. If you cannot state a requirement concretely, ask.

Fill the sections of the requirements template (overview, functional, non-functional, constraints, acceptance criteria, out of scope).

> "Requirements complete. Ready for design phase?"

---

### Phase 3: Technical Design

1. **Research** candidate architectures and libraries (docs, similar projects, external APIs) and record sources under `## Technical Research` in design.md.
2. **Explore approaches.** Invoke `dev-workflow:brainstorming` to work through 2-3 approaches. When the design has several services, non-obvious trade-offs, or security/scale impact, stop and question the problem itself first: are we solving the right problem, what are we assuming, and what is the simplest thing that works?
3. **Compare** the options (pros, cons, complexity) and **recommend** one with the reason it best fits the requirements.
4. **Write design.md** by filling the design template: architecture, components and interfaces, data flow, API contracts, error handling, security, performance, testing strategy. Reference the REQ-IDs each part satisfies.

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
