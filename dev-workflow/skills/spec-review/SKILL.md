---
name: spec-review
description: Review feature spec files across 6 dimensions — business, correctness+ambiguity smells, completeness+safety invariants, compatibility+implementation blockers, traceability, and testability scoring — launches 5–6 parallel agents and consolidates findings
argument-hint: [feature-name]
allowed-tools: Read, Bash, Glob
context: fork
---

# Spec Review Skill

## Purpose

Run review agents against a feature's spec files (`requirements.md`, `design.md`, `tasks.md` or `plan.md`) across up to six independent review dimensions, then consolidate results into an actionable review report with a PASS / NEEDS REVISION verdict.

Agents run **sequentially by default** — one at a time, in order. Run in parallel only if the user explicitly requests it.

**Agent count by mode:**
- **Quick mode** (plan.md only): 5 agents (skip Agent 5 — Traceability)
- **Full mode** (all 3 files present): 6 agents
- **Partial Full mode** (some files missing): 5 agents (skip Agent 5)

**Dimensions covered:**

| Agent | Dimension | Includes |
|---|---|---|
| 1 | Business | Goals, value, scope, assumptions |
| 2 | Correctness + Ambiguity Smells | EARS syntax, 10-pattern smell scan |
| 3 | Completeness + Safety/Liveness Invariants | Missing scenarios, invariants, liveness |
| 4 | Compatibility + Implementation Blockers | Internal feasibility, external contracts, obvious blockers |
| 5 | Traceability | REQ→Design→Tasks chain (Full mode only) |
| 6 | Testability Scoring | Per-requirement 0–3 testability score |

## Activation Triggers

Activate this skill when:
- User says "review the spec", "review feature spec", "check the spec"
- User says "is this spec good?", "validate the spec", "audit the spec"
- User mentions reviewing requirements, design, or tasks files
- Before moving from planning to implementation
- `/dev-workflow:spec review` command arg

---

## Step 1 — Locate the Spec

1. List `docx/features/` to find all feature directories
2. If a feature name was given as argument, match it
3. If ambiguous, show the list and ask which feature to review
4. If `docx/features/` does not exist, stop and tell the user: "No feature specs found. Run `/dev-workflow:spec create` to create your first feature."
5. Identify which files exist:
   - Quick mode: `plan.md`
   - Full mode: `requirements.md`, `design.md`, `tasks.md` (note which are present)
   - Record a `traceability_eligible` flag: `true` only if all three Full mode files exist
6. Record the **absolute file paths** — do NOT read file contents into context. Agents will read files themselves.

---

## Dispatch Prompt Template

Each agent prompt must be self-contained — agents have no access to the conversation. Include:

1. **Role**: "You are reviewing a feature spec for [dimension]."
2. **File paths**: Pass the absolute paths to each spec file — tell the agent to read them with the Read tool. Do NOT paste file contents inline. Each agent reads only the files relevant to its dimension.
3. **Checklist**: The specific check items for that dimension (from Step 2 below)
4. **Output format**: Exactly `PASS` or `NEEDS REVISION`, then labeled bullet findings with severity icons

---

## Step 2 — Run Review Agents

**Default: sequential.** Run agents one at a time in order (1 → 2 → 3 → 4 → 5 → 6). After each agent returns, summarize its findings in a brief status line before proceeding to the next.

**Parallel mode:** Only if the user explicitly says "run in parallel", "parallel review", or similar — emit all applicable Agent tool calls in a **single message** so they run concurrently.

Sequential order:
1. Business
2. Correctness + Ambiguity Smells
3. Completeness + Safety/Liveness Invariants
4. Compatibility + Implementation Blockers
5. Traceability (skip if `traceability_eligible = false`)
6. Testability Scoring

---

### Agent 1: Business Review

**Focus:** Does this spec make business sense?

Prompt must include:
- Absolute paths to all spec files (agent reads them with Read tool)
- Feature directory path

Check:
- Is the problem being solved clearly stated?
- Is the value / benefit to the user or system explicit?
- Are the goals realistic and well-scoped?
- Are there requirements that seem gold-plated or out of scope?
- Are acceptance criteria meaningful from a business perspective?
- Are there unstated business assumptions that need surfacing?

Return:
- `PASS` or `NEEDS REVISION`
- Bullet list of findings (each with severity: 🔴 Critical / 🟡 Warning / 🟢 Suggestion)

---

### Agent 2: Correctness + Ambiguity Smells

**Focus:** Are requirements syntactically correct AND free of systematic ambiguity patterns?

Prompt must include:
- Absolute paths to all spec files (agent reads them with Read tool)
- Feature directory path

**EARS Correctness (Full mode):**
- Every requirement uses proper EARS syntax (WHEN/THEN, WHILE, IF/THEN, WHERE, or ubiquitous SHALL)
- Each requirement is one atomic statement — no compound AND requirements that should be split
- Active voice with SHALL for mandatory, SHOULD for desirable
- No contradicting requirements

**Plan Correctness (Quick mode):**
- Tasks are unambiguous and actionable
- No vague tasks like "handle errors" without specifics
- Each task has clear done criteria

**Ambiguity Smell Detection — scan every requirement for these 10 patterns:**

| Smell | Pattern | Example |
|---|---|---|
| Vague intensifier | "quickly", "fast", "appropriate", "reasonable", "good", "user-friendly" | "responds quickly" → needs metric |
| Implicit actor | "the system" with no named role | "the system shall notify" → who triggers it? |
| Combinatorial explosion | `A and/or B` | "admin and/or moderator" → split or clarify |
| Ambiguous pronoun | "it", "they", "this" with unclear referent | "it shall return" → what is "it"? |
| Missing subject | Passive voice with no actor | "shall be validated" → by whom/what? |
| Unbounded quantifier | "all", "every", "any", "never" without scope | "all users" → which users? |
| Escape clause | "where possible", "if applicable", "as needed" | Removes enforceability |
| Unverifiable adjective | "secure", "reliable", "scalable" without metric | "shall be secure" → by what measure? |
| Temporal vagueness | "soon", "eventually", "periodically" | Needs concrete time bounds |
| Implicit assumption | Behavior implied but not stated | Missing initial/boundary state |

For each smell found: cite the requirement ID (or text), name the smell type, and suggest a concrete rewrite.

Return:
- `PASS` or `NEEDS REVISION`
- Findings per requirement (EARS issues + smell hits), severity labeled

---

### Agent 3: Completeness + Safety/Liveness Invariants

**Focus:** What scenarios are missing, AND what must always/eventually be true?

Prompt must include:
- Absolute paths to all spec files (agent reads them with Read tool)
- Feature directory path

**Completeness checks:**
- Happy path fully covered?
- Error / failure scenarios specified?
- Edge cases: empty inputs, zero values, max bounds, concurrent access?
- Auth / permission requirements stated?
- Non-functional requirements present: performance, security, scalability?
- Data validation rules specified?
- Rollback / undo behavior defined (if relevant)?
- Are all actors / user roles accounted for?
- Are there implied behaviors not written down?

**Safety Invariants — what must NEVER be true?**
Look for unstated system constraints that should be made explicit:
- State invariants: "the system shall never allow X while Y is true"
- Security invariants: "unauthorized users shall never access Z"
- Data integrity invariants: "account balance shall never go negative"
- Concurrency safety: "two requests shall never simultaneously modify the same record"

For async, stateful, or multi-actor specs: explicitly check whether safety boundaries are stated.

**Liveness Properties — what must EVENTUALLY happen?**
Look for missing progress guarantees:
- "the system shall eventually complete the job" (no infinite-wait)
- "a pending request shall eventually receive a response or timeout"
- "the queue shall eventually drain under normal load"

Flag specs that describe triggering behavior but never guarantee completion or termination.

Return:
- `PASS` or `NEEDS REVISION`
- Missing scenario list (severity labeled) with suggested EARS additions
- Safety invariants that are implied but not written (flag as 🟡 or 🔴 based on risk)
- Missing liveness guarantees (flag as 🟡 if async/stateful behavior is present)

---

### Agent 4: Compatibility + Implementation Blockers

**Focus:** Can we build this, does it play well with the outside world, and are there obvious blockers before a line of code is written?

Prompt must include:
- Absolute paths to all spec files (agent reads them with Read tool)
- Feature directory path

**Our side (internal):**
- Does the design align with the existing tech stack and architecture patterns?
- Does it introduce breaking changes to existing interfaces?
- Are dependencies available and versioned?
- (Only if `tasks.md` is present) Is the task breakdown consistent with the design (no orphaned requirements)?

**Other side (external):**
- Are all external API contracts defined?
- Are integration points with third-party services specified?
- Are data format / schema contracts clear?
- Is backward compatibility addressed?
- Are rate limits, quotas, or SLA constraints mentioned?
- Are there regulatory / compliance implications (GDPR, PCI, HIPAA)?

**Implementation blockers — obvious spec-level issues that will block implementation:**
- Are there requirements that cannot be implemented without a decision that hasn't been made? (e.g., "store user data" — where? which database?)
- Are there requirements that reference systems, APIs, or services that are not yet defined?
- Are there requirements that contradict each other in a way that makes a single implementation impossible?
- Are there missing technical definitions that developers will immediately ask about?

Return:
- `PASS` or `NEEDS REVISION`
- Bullet list of compatibility concerns (severity labeled)
- Bullet list of implementation blockers (each is 🔴 Critical — blocks implementation start)

---

### Agent 5: Traceability

**Focus:** Does every requirement flow end-to-end through design into tasks?

**Only dispatch when `traceability_eligible = true`** (all three Full mode files — `requirements.md`, `design.md`, `tasks.md` — are present). Skip for Quick mode and partial Full mode.

Prompt must include:
- Absolute paths to `requirements.md`, `design.md`, and `tasks.md` (agent reads only what it needs)
- Feature directory path

**Requirements → Design:**
- Extract every `REQ-XXX` from `requirements.md`. If requirements do not use REQ-XXX IDs, note this and trace by requirement text/bullet instead.
- For each REQ, check that at least one section or decision in `design.md` addresses it
- Flag any REQ with no design coverage

**Design → Tasks:**
- Extract every named component / decision from `design.md`
- For each design element, check that at least one task in `tasks.md` implements it
- Flag design elements with no tasks

**Tasks → Requirements (reverse):**
- Extract every task from `tasks.md`
- Check that each task traces back to at least one REQ or design element
- Flag orphaned tasks

**Consistency:**
- Are acceptance criteria in requirements consistent with done-criteria in tasks?
- Does the scope in `design.md` match the scope in `requirements.md`?

Return:
- `PASS` or `NEEDS REVISION`
- Traceability matrix: `REQ-XXX | Design Coverage | Task Coverage | Status`
- Broken links list (severity labeled)

---

### Agent 6: Testability Scoring

**Focus:** How testable is each requirement, and what's blocking test automation?

Prompt must include:
- Absolute paths to all spec files (agent reads them with Read tool)
- Feature directory path

Score every requirement on this 0–3 scale:

| Score | Label | Meaning |
|---|---|---|
| 3 | Automatable | Clear oracle, deterministic, can be a unit/integration/e2e test today |
| 2 | Manual-testable | Can be verified by a human tester with a defined procedure |
| 1 | Partially testable | Some aspects can be tested, others are vague or environment-dependent |
| 0 | Not testable | Vague, subjective, or no way to verify pass/fail |

For each requirement scoring 0 or 1:
- Explain what blocks testability (vague metric, missing oracle, environmental dependency, etc.)
- Suggest a concrete rewrite that would raise the score to 2 or 3

Also flag:
- Requirements that conflict with TDD (no test can be written before implementation)
- Missing acceptance criteria that would serve as test oracles
- NFRs (performance, security) with no measurable threshold

Return:
- `PASS` (avg score ≥ 2.0, no score-0 requirements) or `NEEDS REVISION`
- Testability scorecard table: `REQ-XXX | Score | Blocker | Suggested Fix`
- Overall average testability score

---

## Step 3 — Consolidate Results

Wait for **all dispatched agent tool calls to return** before starting this step. Do not partially consolidate.

After all agents return, synthesize into a single report:

```
# Spec Review: [Feature Name]
**Files reviewed:** [list]
**Mode:** Quick | Full | Partial Full
**Agents run:** [N]
**Date:** [today]

## Verdict: PASS ✅ | NEEDS REVISION ❌

---

## 1. Business [PASS|NEEDS REVISION]
[findings]

## 2. Correctness + Ambiguity Smells [PASS|NEEDS REVISION]
[EARS findings + smell hits per requirement]

## 3. Completeness + Safety/Liveness [PASS|NEEDS REVISION]
[missing scenarios + invariants + liveness gaps]

## 4. Compatibility + Implementation Blockers [PASS|NEEDS REVISION]
[compatibility concerns + blockers]

## 5. Traceability [PASS|NEEDS REVISION|N/A]
[traceability matrix + broken links]

## 6. Testability Scoring [PASS|NEEDS REVISION]
[scorecard table + avg score]

---

## Action Items
| # | Severity | Dimension | Issue | Suggested Fix |
|---|---|---|---|---|
| 1 | 🔴 | Correctness | REQ-003 uses "quickly" | Replace with "within 200ms" |
...

## Summary
- Critical issues: N
- Warnings: N
- Suggestions: N
- Avg testability score: X.X / 3.0
- Recommended action: [Proceed to implementation | Revise spec first]
```

---

## Verdict Rules

- **PASS** — zero 🔴 Critical issues across all dispatched agents. May have warnings/suggestions.
- **NEEDS REVISION** — any 🔴 Critical issue in any dimension. Block implementation until resolved.
- Traceability (Agent 5) is `N/A` for Quick mode or partial Full mode.

If NEEDS REVISION: offer to open the relevant spec file for editing, or activate `spec-driven-planning` to revise the appropriate phase.

---

## Severity Definitions

| Icon | Level | Meaning |
|---|---|---|
| 🔴 | Critical | Blocks implementation — ambiguous, missing, incompatible, or untestable |
| 🟡 | Warning | Should fix before implementation — risk of rework |
| 🟢 | Suggestion | Optional improvement — clarity, coverage, or testability enhancement |
