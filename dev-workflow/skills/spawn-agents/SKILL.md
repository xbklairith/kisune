---
name: spawn-agents
description: Use when facing 2+ independent problems (different test files, unrelated bugs, separate subsystems) that can be investigated in parallel without shared state — covers the dispatch decision, the actual Claude Code parallelism mechanism, prompt construction, and integration after agents return
---

# Spawn Agents

## Overview

Delegate independent work to subagents with isolated context. By precisely crafting the agent's prompt, you ensure it stays focused and succeeds. Subagents inherit nothing from your session — you construct exactly what they need. This preserves your own context for coordination.

**Core principle:** One agent per independent problem. Parallel only when truly independent. Over-dispatching is more common than under-dispatching.

## The Decision: Dispatch or Not?

**Dispatch when ALL of these hold:**
- 2+ problems exist that are genuinely independent
- Each can be understood without context from the others
- Agents won't edit the same files or rely on the same in-flight changes
- You'd otherwise lose tokens to context bloat investigating sequentially yourself

**DO NOT dispatch when:**
- The problems share a domain model, schema, or core utility (the bugs may have one root cause)
- The work is one cohesive feature decomposed into pieces (e.g. "implement auth: signup + login + reset + verify" — all four touch User, middleware, and schema)
- You don't yet know what's broken (exploratory debugging needs full context)
- The task fits in one agent (don't shard for the sake of sharding)

**Over-dispatch is the failure mode to fear most.** Capable models reach for parallelism reflexively. Resist: if streams share state, agents will conflict and you'll spend more time integrating than you saved dispatching.

**Soft cap: ~3-4 agents per message.** If you're tempted to spawn 5+ in parallel, the more likely diagnosis is that they aren't truly independent — re-examine the decomposition before dispatching.

## The Mechanism (Claude Code)

Parallelism in Claude Code is NOT a special `Task()` function. It is:

> **Multiple `Agent` tool invocations in a single assistant message.**

The harness runs them concurrently. Sequential `Agent` calls across messages run sequentially.

```
✅ One message containing 3 Agent tool calls → all 3 run in parallel
❌ Three messages, one Agent call each → all 3 run sequentially
```

When dispatching N parallel agents, emit all N tool calls in one block.

## Subagent Dynamics

Spawned subagents auto-load `using-kisune`, which has `<SUBAGENT-STOP>` — the subagent skips the bootstrap dance and runs your assignment directly. Implications for your prompt:

- The subagent will NOT auto-invoke other kisune skills unless you tell it to.
- The subagent has NO conversation memory — your prompt must be self-contained.
- If you want the subagent to follow TDD or use `completion-validation`, say so explicitly.

## Prompt Construction

Brief the agent like a smart colleague who walked into the room — they have not seen your conversation, do not know what you've tried, do not know why this matters.

A good dispatch prompt has four parts:

1. **Goal** — one sentence on what to accomplish
2. **Context** — relevant file paths, error messages, prior attempts, why this matters
3. **Constraints** — what NOT to change; scope boundaries
4. **Expected output** — what the agent should report back, in what shape

```markdown
Investigate why src/auth/middleware.ts:42 throws "token not found"
on valid sessions.

Context: Started after PR #312 merged the session-cookie refactor.
Failing path: GET /api/me with valid cookie → 401. Repro: tests/integration/auth.test.ts case "valid session returns user".

Constraints: Do NOT modify production code. Identify root cause only.
You may add console.log in tests.

Return: Root cause in 1-2 sentences, the exact line(s) responsible,
and a proposed fix (do not apply it).
```

## When "Independent" Turns Out Wrong

Mid-flight, you may notice agent A and agent B are converging on the same root cause (shared utility, same schema column, same race). When this happens:

1. **Stop further work** — if either agent has already returned, do not commit those changes blind.
2. **Consolidate** — open a single new investigation that covers both problems together.
3. **Re-dispatch only after** the shared root cause is understood; the new agents must not overlap on the now-shared edit surface.

Sunk-cost fallacy: "the agents are already running, let them finish." Resist. Conflicting edits cost more to untangle than to abort.

## After Agents Return

For each returned agent:

1. Read the summary critically — agent reports describe intent, not necessarily reality.
2. **Verify via diff/state, not the report.** Run `git status`, `git diff`, read the changed files. (See `completion-validation` for the discipline gate before claiming "the agent succeeded".)
3. Check for cross-agent conflicts (same file edited twice, same dependency added differently).
4. Run the full test suite once integrated — independent fixes can still combine into a regression.

**Partial failure (1 of N fails):** Do not silently drop the failed agent's task. Either (a) re-dispatch it with the lessons learned from siblings, (b) take it on yourself if it now needs full-system context, or (c) report the partial state honestly: "2 of 3 fixed, the third needs further investigation". Never claim the whole batch succeeded when one stream failed.

## Common Mistakes

| ❌ | ✅ |
|---|---|
| "Fix all the failing tests" (too broad) | "Fix the 3 failures in src/agents/abort.test.ts" (focused scope) |
| No context, just a goal | Paste error messages, file:line, repro steps |
| No constraints | "Do not change production code" / "Tests only" |
| "Fix it" (vague output) | "Return root cause + line numbers + proposed fix" |
| Dispatch 4 agents on one feature | Sequential single agent for cohesive work |
| Trust agent's "all tests pass" | Verify via git diff + re-run suite yourself |
| One Agent call per message | All N Agent calls in one message → real parallelism |

## When NOT to Spawn

- **Scoped lookups already known**: use `Read` / `Grep` directly, not an agent.
- **One-shot tool execution**: don't wrap a single `Bash` call in an agent.
- **Short reactive tasks**: if the next action is dictated by what you just read, do it yourself.
- **Anything where you'd give the agent the same context you already have**: dispatching adds latency without isolation benefits.

## Integration With Other Kisune Skills

- **`using-kisune`** — defines the `<SUBAGENT-STOP>` semantics that let dispatched agents skip the bootstrap.
- **`completion-validation`** — the verification gate after an agent returns. "Agent said success" is not evidence; check the diff.
- **`brainstorming`** — if the dispatch decision itself is non-obvious (independent vs not?), brainstorm before dispatching.
- **`spec-driven-implementation`** — for Full-mode features, do NOT shard task execution across agents unless tasks are explicitly independent in the plan.
