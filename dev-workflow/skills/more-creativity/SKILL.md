---
name: more-creativity
description: Use when generating ideas, hypotheses or options — "give me ideas", "what are the possibilities", "I'm stuck", "what else could cause X", "hypotheses for why X". Forces divergence before convergence — suppresses evaluation while generating, requires a cross-domain technique, and gates every survivor on non-obviousness. Not for factual questions, live incidents, or narrowing options into a design — `brainstorming` owns that.
allowed-tools: Read, Glob, Grep, WebSearch
---

# More Creativity

Produce options the user could not have reached alone — then hand off to a convergent skill.

## The problem this solves

Unaided output on an ideation request is already complete, well-structured and prior-ordered. That is the trap: it is also the domain's own playbook, and the user already owns the playbook. Three habits cause it, and each has a counter below.

| Habit | Counter |
|---|---|
| Evaluating while generating — ROI, effort and feasibility woven into each idea | §3 Divergence lock |
| Converging to a recommendation before the space is explored | §3, and stop before the action plan |
| Never leaving the domain's own vocabulary | §2 Forced cross-category technique |

Coverage is not the goal. **Non-obviousness is the goal.** A complete list of predictable options is a failure of this skill.

## Hand off instead when

| The need is... | Skill |
|---|---|
| Narrow options into a requirement or design | `brainstorming` |
| Interrogate a plan that exists in the user's head | `grilling` |
| Review something already written down | `scrutinize` |
| Establish what is actually true | `investigate` |
| Feel out whether a model works, in code | `prototype` |

Diverge here first, then hand off. Running this *after* a convergent skill has already picked a direction wastes it.

**Never proceed from these options to implementation.** `brainstorming` owns the design-approval gate that precedes any code, and this skill does not replace or satisfy it. Producing options is not approval to build them — if the user wants to act on one, route through `brainstorming` first.

## Stay silent when

A factual question with one answer. Mid-debug on a live incident. A simple how-to with no design room. Pure conversation. Unrequested divergence in those moments is noise, not value.

## 1. Intensity

Read an explicit number (`0.3`, `0.8`) as intensity. Default `0.5`.

| Intensity | Name | Surviving ideas | Technique count |
|---|---|---|---|
| 0.1–0.3 | Subtle | 2–3 | 1 |
| 0.4–0.6 | Inspired | 3–5 | 1–2 |
| 0.7–1.0 | Radical | 5–7+ | 2–3, one of which must be `provocation`, `random-stimulus` or `oblique-strategies` |

Intensity raises boldness and technique count. It never lowers the §5 gate.

## 2. Technique selection

Read `references/techniques.md` and select by problem type. **At least one technique must be absent from your problem type's row** — not merely present in some other row as well. Rows overlap, so a technique listed under your own problem type never counts toward this, however many other rows it appears in. Deliberately taking a technique that looks mismatched to the problem is the rule that breaks out of the domain playbook.

| Problem type | Start with |
|---|---|
| Technical / architecture | first-principles, reversal, time-travel |
| Design / UX / naming | forced-analogies, combination, role-swap |
| Strategy / planning / risk | inversion, what-if, negative-space |
| Stuck / looping / blocked | lateral-thinking, provocation, random-stimulus, oblique-strategies |
| New product / feature | combination, constraints, what-if, synthesis |
| Critique / reframe | negative-space, oblique-strategies, time-travel |
| Diagnosis / "why is this happening" | inversion, reversal, role-swap, random-stimulus |

Name the techniques used in the output's header line (§7). An unnamed technique was probably not applied.

## 3. Divergence lock

While generating — everything before §5 — these are forbidden: feasibility, cost, effort, ROI, risk, priority, sequencing, "start with", "quick win", "realistically". Every one is convergence, and convergence during generation silently deletes the options worth having.

The §7 `Risk:` and `How to execute:` fields are *output* fields produced after the gate. They are exempt from this list when the user asks for detail.

Evaluation happens exactly once, at §5. Not before.

If the user explicitly asks for prioritization, finish divergence first, then prioritize as a separate labelled step — never interleaved.

## 4. Quota and discard

Generate **quota + 3**, then cut the three most conventional. Earliest ideas are the most conventional (serial-order effect); the interesting ones arrive once the obvious ones are exhausted. Never count the warmup toward the quota.

**Make the cut visible.** Close the output with one line naming what was dropped:

```
Obvious options skipped: <a>, <b>, <c>
```

Without that line the discard is unverifiable and probably did not happen. It also shows the user the playbook was considered rather than missed — which is what stops the output reading as ignorance of the basics.

## 5. Quality gate

Every surviving idea must pass all three:

1. **Could the user have thought of this alone?** → reject.
2. **Is it surprising but not useful?** → reject.
3. **Is it a lukewarm variation of a known solution?** → reject.

Below quota after the gate? Read another technique and generate more. **Never lower the bar to reach a count.** Three real breakthroughs beat seven padded entries.

## 6. Hypothesis mode

When the ask is diagnostic — "why is this happening", "what could cause this" — each survivor is a falsifiable claim, not a story:

```
HYPOTHESES — <techniques applied>

H<n>. <claim in one sentence>
     Mechanism: <how it would produce the observed effect>
     False if:  <the observation that would kill it>
```

A hypothesis without a `False if:` line is a narrative. Reject it or repair it.

Do not order by prior probability *during* generation — that is convergence leaking in.

**After the gate, always triage.** Close with the two cheapest observations that discriminate between the surviving hypotheses:

```
Cheapest discriminators: <observation 1> splits H2/H3 from the rest; <observation 2> kills H5 or confirms it.
```

A diagnostic answer with no triage is less useful to someone mid-incident than the conventional prior-ordered list it replaced. Divergence earns its place by *adding* candidates, not by withholding direction.

## 7. Output

```
IDEAS — <techniques applied>

1. <one sharp sentence>
   Why it works: <the insight, one line>

2. <one sharp sentence>
   Why it works: <the insight, one line>
```

Add `How to execute:` and `Risk:` lines only when the user asks for detail. Stop at the list — no action plan, no "what I'd do first" unless requested. Offer the handoff instead: "Want `brainstorming` to narrow these?"

## Red flags

| Thought | Reality |
|---|---|
| "These are solid, practical suggestions" | Practical and predictable is the failure mode. Re-run §5. |
| "Let me order these by impact" | That is §3 violation. Diverge first. |
| "I'll add a 30-day plan to be helpful" | Convergence. The user did not ask to narrow yet. |
| "Seven is the quota, close enough" | Padding. Three that pass beat seven that do not. |
| "The domain already has good answers" | Then the user has them. Go outside the domain. |
| "I'll skip the discard, my first ideas were good" | The discard exists because they feel good. Drop them, and name them. |
| "No need for the skipped-options line" | Then the discard is unverifiable. Write it. |
| "Triage would be convergence" | Triage is post-gate and required in §6. Withholding it is not discipline, it is unhelpfulness. |

## Attribution

Technique set and intensity/gate structure adapted from [claude-creativity](https://github.com/KorroAi/claude-creativity) (MIT, © 2026 Korrocorp) — full upstream licence in `references/NOTICE.md`. Quota-and-discard adapted from [creative-director-skill](https://github.com/smixs/creative-director-skill); divergence lock from [claude-brainstorm](https://github.com/MadeByTokens/claude-brainstorm).
