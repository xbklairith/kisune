---
name: using-kisune
description: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
disable-model-invocation: true
---

<SUBAGENT-STOP>
Dispatched as a subagent with a scoped task? Skip this and run the assignment.
</SUBAGENT-STOP>

## The rule

Before responding or acting, check whether a kisune skill applies. If there is even a small chance it does, invoke it with the `Skill` tool first, then follow it. If it turns out not to fit, drop it. Load skills through `Skill`, never by reading SKILL.md.

**Before the first edit in any code change, a skill has run.** A bug fix starts with `systematic-debug` or `test-driven-development`; new behaviour starts with `test-driven-development` (or `brainstorming` when the approach is open). This holds for one-line fixes too.

## Who wins

1. The user's explicit instructions (CLAUDE.md, direct messages).
2. Kisune skills.
3. Default behaviour.

Speed or size words ("quick", "just patch it", "simple") describe the goal; they do not switch a skill off. Only an explicit opt-out does ("skip TDD for this, I accept the risk"): then comply and say which skill you skipped. Never skip a rigid skill silently. Push back once, not repeatedly.

Rigid skills (`test-driven-development`, `completion-validation`, `security-review`) are followed exactly. The rest adapt to context; each skill says which it is.

When several apply: process first (`brainstorming`, `systematic-debug`), then gates (`test-driven-development`, `completion-validation`), then execution (`spec-driven-*`, `git-workflow`).

## Kisune Skill Index (27 skills)

| Skill | Use for |
|---|---|
| `spec-driven-planning` | plan a feature, write specs, `/dev-workflow:spec` |
| `more-creativity` | generate ideas or hypotheses before choosing |
| `brainstorming` | open approach, architectural choices |
| `grilling` | stress-test a plan in the user's head |
| `grill-with-docs` | `/grill-with-docs` only |
| `domain-modeling` | contested terms, glossary entry, ADR |
| `codebase-design` | module interfaces, seams |
| `prototype` | throwaway code to answer one design question |
| `investigate` | research against primary sources |
| `wayfinder` | multi-session effort with open decisions |
| `spec-driven-implementation` | execute a plan, `plan.md` or `tasks.md` exists |
| `test-driven-development` | any bug fix or new behaviour |
| `spawn-agents` | 2+ independent problems in parallel |
| `wizard` | keys, secrets, `.env`, new-machine setup |
| `review` | review code, before a commit or PR |
| `security-review` | auth, user input, APIs, secrets, payments |
| `git-workflow` | commit, branch, push, PR |
| `completion-validation` | before claiming done, passing, or ready |
| `systematic-debug` | bugs, errors, flaky or failing tests |
| `post-mortem` | record a fixed bug |
| `scrutinize` | outsider review of a PR, plan, or design |
| `skill-maker` | create or edit a skill |
| `spec-review` | review a feature spec |
| `retro` | session retrospective |
| `handoff` | `/handoff` only |
| `explain-in-html` | diagrams, visual explanations, 3+ structured questions |
| `deslop` | tighten any prose (English or Thai): lessons, explanations, research notes, docs, PR text |
