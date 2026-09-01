---
name: grilling
description: "Relentless round-based interview that stress-tests a plan before building. Maps the plan as a design tree and works it in rounds, asking every unblocked question at once with a recommended answer for each, until nothing is left silently assumed."
allowed-tools: Read, Glob, Grep, Bash, Agent, WebSearch, WebFetch
---

# Grilling

Interview the user relentlessly until reaching shared understanding. Nothing gets silently assumed.

The plan is a **design tree**: every decision branches into the decisions that hang off it. Visit every branch, surfacing the decisions the user has not yet noticed they are making.

## Hand off instead when

| The answers are... | Skill |
|---|---|
| Not formed yet — the plan itself has to be invented | `brainstorming` |
| In the user's head — a plan exists but is undocumented | **`grilling`** |
| On disk — a PR, code, or written design doc you can read | `scrutinize` |

Say so and stop, rather than interviewing someone about a document you could have read. To leave a glossary and ADRs behind, use `grill-with-docs`.

## Rounds

The **frontier** is every decision whose prerequisites are already settled: the questions answerable *now* without guessing at answers not yet heard.

1. Compute the frontier.
2. Ask the **whole frontier** in one round. Number each question. Give a recommended answer for every one.
3. Wait. Do not proceed on assumed answers.
4. Answers reshape the tree — settled decisions push the frontier outward. Recompute and ask the next round.

A question whose answer depends on another still open **in this round** belongs to a *later* round. Placing it now forces a guess, which is the failure this structure exists to prevent.

```
❓ **Q1** — **<question title>**: <question body, may offer multiple choices>

➡️ <recommended answer, and why it is your recommendation>

---

❓ **Q2** — **<question title>**: <question body>

➡️ <recommended answer>
```

Every question carries a recommendation. A user who agrees with all of them should be able to reply "yes to all" and move on. A question without one turns the interview into a quiz.

## Facts are your job, decisions are theirs

**Never ask for anything discoverable.** If a question needs a fact from the environment — the schema, whether a library is already a dependency, how the current handler behaves — go find it. Read the files. Run the command. For a broad sweep, dispatch a subagent (see `spawn-agents`).

**Do not block on fact-finding.** A running exploration is an unsettled prerequisite: only questions downstream of it wait. Ask the rest of the frontier now.

**The decisions are the user's.** Recommending hard is the job; deciding for them is not.

## Termination

The session ends when the frontier is empty. Summarize the settled tree — every decision and the answer it landed on — then ask whether to proceed, and to what.

<HARD-GATE>
Do NOT write code, scaffold, edit files, or invoke any implementation skill until the user confirms shared understanding has been reached. An empty frontier is necessary but not sufficient — the user must say so.
</HARD-GATE>
