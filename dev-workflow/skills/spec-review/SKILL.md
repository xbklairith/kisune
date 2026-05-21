---
name: spec-review
description: Review feature spec files with 3 focused agents — spec quality (business+correctness+ambiguity), completeness (missing scenarios+safety+testability), and buildability (compatibility+blockers+traceability). Sequential by default.
argument-hint: [feature-name]
allowed-tools: Read, Bash, Glob, Agent
context: fork
---

# Spec Review Skill

## Purpose

Run 3 focused review agents against a feature's spec files, then consolidate into an actionable PASS / NEEDS REVISION report.

Agents run **sequentially by default**. Run in parallel only if the user explicitly requests it.

**Agent count by mode:**
- **Quick mode** (plan.md only): 2 agents (skip Agent 3 — Buildability)
- **Full mode** (all 3 files present): 3 agents
- **Partial Full mode** (some files missing): 2 agents (skip Agent 3)

| Agent | Name | Covers |
|---|---|---|
| 1 | Spec Quality | Business validity, EARS correctness, 10-pattern ambiguity smell scan |
| 2 | Completeness | Missing scenarios, safety invariants, liveness properties, testability scoring |
| 3 | Buildability | Compatibility, implementation blockers, REQ→Design→Tasks traceability |

## Activation Triggers

- "review the spec", "review feature spec", "check the spec"
- "is this spec good?", "validate the spec", "audit the spec"
- Before moving from planning to implementation
- `/dev-workflow:spec review`

---

## Step 1 — Locate the Spec

1. List `docx/features/` to find all feature directories
2. If a feature name was given as argument, match it
3. If ambiguous, show the list and ask which feature to review
4. If `docx/features/` does not exist, stop: "No feature specs found. Run `/dev-workflow:spec create` first."
5. Identify which files exist and record their **absolute paths** — do NOT read contents into context. Agents read files themselves.
   - Quick mode: `plan.md`
   - Full mode: `requirements.md`, `design.md`, `tasks.md` (note which are present)
   - Set `traceability_eligible = true` only if all three Full mode files exist

---

## Dispatch Prompt Template

Each agent prompt must be self-contained. Include:

1. **Role**: "You are reviewing a feature spec for [agent name]."
2. **File paths**: Absolute paths — tell the agent to read them with the Read tool. Do NOT paste content inline.
3. **Checklist**: The check items for that agent (from Step 2 below)
4. **Output format**: `PASS` or `NEEDS REVISION`, then labeled findings with severity icons

---

## Step 2 — Run Review Agents

**Default: sequential** (1 → 2 → 3). Summarize each agent's findings in one line before the next.

**Parallel:** Only if user explicitly says "run in parallel" — emit all Agent tool calls in a single message.

---

### Agent 1: Spec Quality

**Covers:** Business validity + EARS correctness + ambiguity smell scan

Prompt includes: absolute paths to all spec files

**Business:**
- Problem being solved clearly stated?
- Value / benefit to user or system explicit?
- Goals realistic and well-scoped?
- Gold-plated or out-of-scope requirements?
- Acceptance criteria meaningful?
- Unstated business assumptions?

**EARS Correctness (Full mode):**
- Every requirement uses proper EARS syntax (WHEN/THEN, WHILE, IF/THEN, WHERE, ubiquitous SHALL)
- Each requirement is one atomic statement (no compound AND)
- Active voice, SHALL for mandatory, SHOULD for desirable
- No contradicting requirements

**Plan Correctness (Quick mode):**
- Tasks unambiguous and actionable
- Clear done criteria per task

**Ambiguity Smell Scan — flag every occurrence:**

| Smell | Pattern |
|---|---|
| Vague intensifier | "quickly", "appropriate", "reasonable", "good", "user-friendly" |
| Implicit actor | "the system" with no named role |
| Combinatorial explosion | `A and/or B` |
| Ambiguous pronoun | "it", "they", "this" with unclear referent |
| Missing subject | Passive voice with no actor |
| Unbounded quantifier | "all", "every", "any" without scope |
| Escape clause | "where possible", "if applicable", "as needed" |
| Unverifiable adjective | "secure", "reliable", "scalable" without metric |
| Temporal vagueness | "soon", "eventually", "periodically" |
| Implicit assumption | Behavior implied but not stated |

For each smell: cite requirement ID, name the smell, suggest a concrete rewrite.

Return: `PASS` or `NEEDS REVISION` + severity-labeled findings

---

### Agent 2: Completeness

**Covers:** Missing scenarios + safety/liveness invariants + testability scoring

Prompt includes: absolute paths to all spec files

**Completeness:**
- Happy path covered?
- Error / failure scenarios?
- Edge cases: empty inputs, zero values, max bounds, concurrent access?
- Auth / permission requirements?
- NFRs: performance, security, scalability?
- Data validation rules?
- Rollback / undo behavior (if relevant)?
- All actors / user roles accounted for?
- Implied behaviors not written down?

**Safety Invariants — what must NEVER be true?**
- State: "shall never allow X while Y"
- Security: "unauthorized users shall never access Z"
- Data integrity: "balance shall never go negative"
- Concurrency: "two requests shall never simultaneously modify the same record"

Flag specs with async/stateful/multi-actor behavior that have no safety boundaries stated.

**Liveness — what must EVENTUALLY happen?**
- No infinite-wait guarantees
- Every pending request eventually gets a response or timeout
- Every queue eventually drains

**Testability (0–3 per requirement):**

| Score | Meaning |
|---|---|
| 3 | Automatable — clear oracle, deterministic |
| 2 | Manual-testable — defined procedure |
| 1 | Partially testable — some aspects vague |
| 0 | Not testable — vague or no pass/fail criteria |

For each 0 or 1: explain the blocker and suggest a rewrite that raises the score.

Return: `PASS` or `NEEDS REVISION` + missing scenarios + invariants + testability scorecard + avg score

---

### Agent 3: Buildability

**Covers:** Compatibility + implementation blockers + traceability

**Only dispatch when `traceability_eligible = true`** (all 3 Full mode files present). Skip for Quick mode and partial Full mode.

Prompt includes: absolute paths to all spec files

**Compatibility:**
- Design aligns with existing tech stack?
- Breaking changes to existing interfaces?
- Dependencies available and versioned?
- External API contracts defined?
- Integration points with third-party services specified?
- Backward compatibility addressed?
- Rate limits, quotas, SLA constraints mentioned?
- Regulatory / compliance implications (GDPR, PCI, HIPAA)?

**Implementation Blockers** — flag anything that will immediately block a developer:
- Requirements that need an unresolved decision ("store user data" — where?)
- References to undefined systems, APIs, or services
- Contradicting requirements that make a single implementation impossible
- Missing technical definitions developers will ask about immediately

**Traceability chain:**
- REQ→Design: every requirement addressed by at least one design decision?
- Design→Tasks: every design element has at least one implementing task?
- Tasks→REQ: every task traces back to a requirement or design element?
- Acceptance criteria in requirements consistent with done-criteria in tasks?

If requirements have no REQ-XXX IDs, trace by text — don't fail silently.

Return: `PASS` or `NEEDS REVISION` + compatibility concerns + blockers (🔴) + traceability matrix (`REQ | Design | Tasks | Status`)

---

## Step 3 — Consolidate

Wait for all agents to return before consolidating.

```
# Spec Review: [Feature Name]
**Mode:** Quick | Full | Partial Full  **Date:** [today]

## Verdict: PASS ✅ | NEEDS REVISION ❌

## 1. Spec Quality [PASS|NEEDS REVISION]
[business + correctness + smell findings]

## 2. Completeness [PASS|NEEDS REVISION]
[missing scenarios + invariants + testability scorecard + avg score]

## 3. Buildability [PASS|NEEDS REVISION|N/A]
[compatibility + blockers + traceability matrix]

---

## Action Items
| # | Sev | Agent | Issue | Fix |
|---|---|---|---|---|
...

## Summary
Critical: N  Warnings: N  Suggestions: N  Avg testability: X.X/3.0
→ [Proceed to implementation | Revise spec first]
```

---

## Verdict Rules

- **PASS** — zero 🔴 Critical issues across all agents
- **NEEDS REVISION** — any 🔴 Critical issue blocks implementation
- Agent 3 is `N/A` for Quick mode or partial Full mode

If NEEDS REVISION: offer to open the spec file or activate `spec-driven-planning` to revise.

---

## Severity

| Icon | Meaning |
|---|---|
| 🔴 | Blocks implementation |
| 🟡 | Risk of rework — fix before implementing |
| 🟢 | Optional improvement |
