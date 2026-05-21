---
name: using-kisune
description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
disable-model-invocation: true
---

<SUBAGENT-STOP>
If you were dispatched as a subagent with a specific scoped task, skip this skill — run the assignment.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a kisune skill might apply to what you are doing, you MUST invoke it via the `Skill` tool.

If a skill applies, you do not have a choice. Invoke it. This is not negotiable. You cannot rationalize your way out of it ("just a simple question", "I'll check first", "the skill is overkill").
</EXTREMELY-IMPORTANT>

## Instruction Priority

1. **The user's explicit instructions** (CLAUDE.md, direct messages) — highest priority
2. **Kisune skills** — override default behavior where they conflict
3. **Default system prompt** — lowest priority

If CLAUDE.md says "skip TDD for spikes" and `test-driven-development` says "always TDD", follow the user. The user is in control.

## How to Access Skills

Use the `Skill` tool. The skill content is loaded and presented to you — follow it directly. **Never `Read` the SKILL.md file** — that bypasses the activation pathway and returns stale content.

## The Rule

**Invoke relevant skills BEFORE any response or action.** Even a 1% chance a skill might apply = invoke it to check. If the skill turns out wrong for the situation, abandon it — but the check comes first.

## Decision Flow

```
User message
   ↓
Might any kisune skill apply? ── definitely not ──→ Respond
   ↓ yes (even 1%)
Invoke Skill tool
   ↓
Announce: "Using <skill> to <purpose>"
   ↓
Has a checklist? ── yes ──→ Create TodoWrite todo per item
   ↓ no
Follow skill exactly
   ↓
Then act / respond
```

## Red Flags — STOP, You're Rationalizing

| Thought | Reality |
|---------|---------|
| "This is just a simple question" | Questions are tasks. Check skills. |
| "I need more context first" | Skill check BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I'll quickly check git/files" | Files lack conversation context. Check skills. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "I remember this skill" | Skills evolve. Read current via `Skill`. |
| "The skill is overkill" | Simple things become complex. Use it. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |
| "This feels productive" | Undisciplined action wastes time. |
| "I know what that means" | Knowing the concept ≠ following the skill. |

## Kisune Skill Index (15 skills)

**Planning**

| Skill | Triggers |
|---|---|
| `spec-driven-planning` | "plan a feature", "create specs", `/dev-workflow:spec`, ambiguous goals |
| `brainstorming` | "not sure how to approach", "what do you think", before any architectural decision |

**Implementation**

| Skill | Triggers |
|---|---|
| `spec-driven-implementation` | "implement this", "execute the plan", any `plan.md` or `tasks.md` exists |
| `test-driven-development` | "write tests", "fix this bug", new feature work |
| `spawn-agents` | 2+ independent problems (different test files, unrelated bugs); parallel dispatch |

**Quality / Debug**

| Skill | Triggers |
|---|---|
| `review` | "review my code", "check this", before opening PR |
| `security-review` | code touches auth, user input, APIs, secrets, payments |
| `git-workflow` | "commit", "push", "create PR", any git operation |
| `completion-validation` | **Before any "done", "tests pass", "ready to commit" claim** — non-negotiable gate |
| `systematic-debug` | "debug this", flaky test, can't reproduce — 4-mantra discipline (reproduce, trace, falsify, breadcrumbs) + multi-layer investigation |
| `post-mortem` | "write a post-mortem", "document the bug", after a fix lands — engineering record of root cause, mechanism, fix, validation, how it slipped through |
| `scrutinize` | "take a hard look at this", "play devil's advocate", "outsider review" — deep outsider-perspective review, questions intent, traces code path end-to-end, verdict: ship/fix/rework/reject |
| `skill-maker` | "create a skill", "edit skill", behavior-shaping changes |
| `spec-review` | "review the spec", "check the spec", "validate spec" — 3 agents: spec quality, completeness, buildability |

**Comms**

| Skill | Triggers |
|---|---|
| `explain-in` | "write for management/exec/VP/director/PM", "make this non-technical", "slack update/standup/email about this fix", "executive summary", "talking points for the meeting"; proactively offered after `post-mortem` |

## Skill Priority When Multiple Apply

1. **Process skills first** (brainstorming, systematic-debug) — these determine HOW to approach
2. **Discipline gates next** (completion-validation, test-driven-development) — these enforce non-negotiables
3. **Implementation skills last** (spec-driven-*, git-workflow) — these guide execution

Examples:
- "Let's build X" → `brainstorming` → `spec-driven-planning` → `spec-driven-implementation`
- "Fix this bug" → `systematic-debug` → `test-driven-development`
- "Done, ready to commit" → `completion-validation` → `git-workflow`

## Skill Types

**Rigid** (TDD, completion-validation, security-review): Follow exactly. Do not adapt away discipline. "Just this once" = lying.

**Flexible** (brainstorming, systematic-debug): Adapt principles to context.

The skill itself tells you which.

## User Instructions Are WHAT, Not HOW

"Add X" / "Fix Y" / "Implement Z" describes the goal. It does NOT, by itself, authorize skipping the workflow.
- "Just add a quick fix" → still triggers `test-driven-development` if there's risk
- "Done, commit it" → still triggers `completion-validation` before the commit
- "Simple feature, no need to plan" → still triggers `brainstorming` if architecture is non-obvious

The user pushing for speed is not, on its own, permission to skip discipline. Push back ONCE if a shortcut would violate a rigid skill.

### Resolving the priority-vs-discipline tension

The Instruction Priority section says the user wins. The discipline gates say push back. Both are true — here is the rule:

1. **Implicit shortcuts** ("just commit it", "skip the tests", time pressure) → invoke the skill anyway. Goal-language is not opt-out.
2. **Explicit, informed opt-out** ("I know completion-validation says re-run; commit without re-running, I accept the risk") → comply, but surface the trade-off in your reply: "Acknowledging your override of completion-validation. Committing without fresh verification."
3. **Never silently skip a rigid skill.** Either the user explicitly opted out (then say so) or they didn't (then run the skill).

This protects user authority and discipline at the same time.

## Even "Trivial" Actions Trigger the Check

There is no "definitely not" escape hatch for tasks that touch the codebase. The 1% rule is a one-way valve:
- "Just `ls src/`" → check skills first. Most likely none apply, then proceed. Cost: one second of thought.
- "Read this file" → same.
- "Run the existing test command" → same.

The check itself is the discipline. Skipping the check because "obviously no skill applies" is exactly the rationalization the Red Flags table forbids.

## On Session Start

When this skill loads at session start, immediately:
1. Note the skill index above (you don't need to invoke each one — just know they exist).
2. On the **next user message**, run the decision flow before any other action.
3. If the user's message clearly maps to a skill (e.g., "plan a feature", "review this", "commit"), invoke it via `Skill` before responding.
