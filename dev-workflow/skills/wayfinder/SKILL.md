---
name: wayfinder
description: Use when an effort is too big for one agent session and the route is foggy — "huge job, don't know where to start", a migration or re-architecture spanning weeks, "pick up where we left off" on a multi-session plan. Charts a shared map of decision tickets under docx/wayfinder/, then resolves one ticket per session until the way to the destination is clear and normal planning can take over.
---

# Wayfinder

## Overview

A loose idea, too big for one session, wrapped in fog: the way from here to the **destination** is not visible yet. Wayfinding finds that way instead of charging at the destination. It keeps a **map** of **decision tickets** (questions whose answer is a decision or a fact a decision waits on) and resolves them one per session until nothing is left to decide.

**Plan, don't do.** A ticket produces a decision, not a deliverable. The pull to start building is the signal that you have reached the edge of the map: hand off to `spec-driven-planning` (or `spec-driven-implementation`) with the decisions as input. An effort can override this in its map's Notes.

**Don't chart what you can't see.** A full phase-by-phase task list for a multi-month effort, written before the first question is answered, is a guess dressed as a plan. Ticket only questions you can state sharply now; leave the rest as fog.

## When to Use

- The work spans more sessions than one context can hold, and key decisions are still open
- The user says they don't know where to start on something large
- A session should resume a map: "continue the migration plan", "what's next on <effort>"

**Not for** work one session can plan: if charting surfaces no fog, say so and use `spec-driven-planning` directly.

## The map on disk

```
docx/wayfinder/<effort>/
├── map.md
└── tickets/
    ├── 01-<slug>.md
    └── 02-<slug>.md
```

`map.md` is an **index, not a store**. It is read once per session; ticket detail lives only in the ticket.

```markdown
# <Effort name>

## Destination
<What reaching the end looks like: a spec to hand off, a locked decision, a change made. One or two lines.>

## Notes
<Domain, constraints, skills every session should load, standing preferences.>

## Decisions so far
- [<ticket title>](tickets/03-<slug>.md): <one-line gist of the answer>

## Not yet specified
<In-scope fog: questions you can see coming but can't phrase sharply yet. Loose prose.>

## Out of scope
- <gist> — <why>, see [<ticket title>](tickets/NN-<slug>.md) if one was closed for it
```

A ticket, sized to one session:

```markdown
---
type: grilling | research | prototype | task
status: open
claimed:
blocked_by: [01, 04]
---
# <Question as a title>

## Question
<The decision or investigation this resolves, and why it matters to the destination.>
```

**Frontier** = open, unclaimed tickets whose blockers are all closed. Do not compute it by eye:

```bash
python3 <this skill>/scripts/frontier.py docx/wayfinder/<effort>
```

Refer to tickets by **title** in everything the human reads, with the link riding inside the title. "#3, #4, #7" is illegible.

## Ticket types

Every ticket is **HITL** (resolved in live exchange with the human, who answers for themselves) or **AFK** (agent alone). Never answer a HITL ticket's questions on the human's behalf.

| Type | Mode | Resolve with |
|---|---|---|
| `grilling` | HITL | `grilling` + `domain-modeling`. The default |
| `research` | AFK | `investigate` (background agent; findings to `docx/research/`) |
| `prototype` | HITL | `prototype` — when "how should it look/behave" is the question |
| `task` | AFK or HITL | Do the manual work a decision is waiting on (get access, run a discovery query, sign up to judge an API). Records facts, not decisions. Use `wizard` for steps only the human can take |

## Chart the map (first session)

1. **Name the destination** with `grilling` + `domain-modeling`. It fixes the scope.
2. **Map the frontier breadth-first**: fan out across the space, surfacing open decisions and the first steps takeable now. No fog surfaced → no map needed; stop and say so.
3. **Write `map.md`**: Destination, Notes, empty Decisions, the fog in Not yet specified.
4. **Write the tickets you can state sharply now**, then wire `blocked_by` in a second pass. Run `frontier.py` to check the wiring.
5. **Start the `research` tickets** in the background with `investigate`.
6. **Stop.** Charting is one session; it resolves nothing by hand.

## Work the map (every later session)

1. Read `map.md` and run `frontier.py`. Do not read every ticket.
2. Take the ticket the user named. Otherwise choose by who is here:
   - **The human is in this session** (they asked you to continue, or said they have time): take the first HITL frontier ticket and work it with them. Start frontier `research` tickets in the background alongside; do not spend their time on AFK work.
   - **The human is away**: take an AFK frontier ticket, and end by naming the HITL ticket that is waiting for them.

   **Claim it first**: set `claimed:` before any work. A claim is only visible to other sessions once it is on disk where they read (committed and pulled, if they work in other clones).
3. Resolve it. Open other tickets only as needed; load the skills the Notes name.
4. Record it: append `## Resolution` to the ticket, set `status: closed`, add one line to Decisions so far.
5. Update the map: new tickets the answer surfaced (create, then wire); graduate any fog that is now sharp, removing it from Not yet specified; a ticket now beyond the destination is closed with a line in Out of scope; tickets the decision invalidates are rewritten or closed.

**One ticket per session**, except `research`, which runs in parallel.

**Fog or ticket?** Whether you can *state* the question precisely now, not whether you can answer it. A sharp question that is blocked is still a ticket. Do not pre-slice fog into ticket-sized pieces.

## Common Mistakes

| Mistake | Fix |
|---|---|
| A five-phase task list on day one | Tickets for sharp questions; the rest is fog |
| Tickets that say "implement X" | That is a build step; it belongs after the map, in a spec |
| Agent answers a grilling ticket itself | HITL tickets wait for the human |
| Restating a decision in `map.md` | One-line gist plus a link; detail lives in the ticket |
| Resolving three tickets in one session | One per session keeps each answer reviewable |

*Adapted from `wayfinder` in mattpocock/skills (MIT) — see `references/NOTICE.md`.*
