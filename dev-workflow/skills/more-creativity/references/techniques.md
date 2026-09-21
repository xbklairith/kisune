# Technique Library

Fifteen divergence techniques. Read the ones §2 selects; apply the *move*, do not just name it.

Each entry: **when** it fits, the **move** to execute, and a worked **example**.

---

## lateral-thinking
**When:** Stuck, looping, the direct approach has failed repeatedly.
**Move:** Stop improving the current answer. Change the question so the current answer becomes irrelevant.
**Example:** "How do we make the queue faster?" → "What if nothing waited in a queue at all?" → push results to clients before they ask.

## first-principles
**When:** Technical or architectural decisions inherited from convention.
**Move:** Strip the problem to physical or economic primitives. Rebuild upward, refusing every "because that's how it's done".
**Example:** "We need a cache" → what is actually scarce? bytes moved, not requests served → shrink the payload and the cache becomes unnecessary.

## inversion
**When:** Strategy, risk, planning — any pursuit of a positive outcome.
**Move:** Ask what would *guarantee failure*, list every cause, then invert each into a prevention.
**Example:** "Make onboarding succeed" → what guarantees abandonment? setup requiring data the user doesn't have yet → let them start with zero data.

## reversal
**When:** A stated assumption is doing load-bearing work unexamined.
**Move:** List the assumptions as explicit sentences. Negate one. Design as if the negation were true.
**Example:** "Users want more control" → reversed: users want *no* control → a single button with no settings at all.

## forced-analogies
**When:** Design, UX, naming, or any problem whose domain vocabulary is exhausted.
**Move:** Pick an unrelated domain, map its mechanism onto the problem, keep the mechanism and drop the surface.
**Example:** Notification fatigue ← epidemiology: model attention as susceptible/infected/recovered; throttle by herd immunity, not per-user rules.

## combination
**When:** Two features, products, or concepts sit adjacent and separate.
**Move:** Fuse the two into one thing that does what neither did, then check what the fusion makes newly possible.
**Example:** Changelog + onboarding → a changelog that re-onboards lapsed users into only what changed since they left.

## synthesis
**When:** Two competing options are deadlocked and both have real support.
**Move:** Refuse the choice. Find the third option that makes the tension productive rather than resolved.
**Example:** Monolith vs microservices → one deployable, hard internal seams, split only where measured contention appears.

## constraints
**When:** Too much freedom; output is bland because everything is permitted.
**Move:** Impose a brutal artificial limit and design under it. The limit does the creative work.
**Example:** "Ship this with no database", "one screen only", "explain it in six words", "10x the load with the same budget".

## provocation
**When:** Blocked and every reasonable idea is exhausted.
**Move:** State a deliberately absurd proposition, refuse to dismiss it, and extract the usable fragment. (De Bono's PO.)
**Example:** "Support tickets answer themselves" → absurd → but: publish the answer at the moment of the question, in the UI where it arises.

## what-if
**When:** Exploring new products, features, or strategic direction.
**Move:** Push one variable to an extreme and follow the consequences seriously.
**Example:** "What if every customer had 1000x the data?" → "What if onboarding took zero minutes?" → "What if it were free?"

## negative-space
**When:** Critique, reframing, or a list that feels complete but inert.
**Move:** Catalogue what is *absent* — the unbuilt feature, the unasked question, the silent user, the missing step.
**Example:** All feedback comes from active users; the churned never speak. The absence *is* the finding.

## random-stimulus
**When:** Severely stuck; thinking has collapsed into one groove.
**Move:** Take a genuinely unrelated word or object and force a connection to the problem. Do not pre-filter for relevance.
**Example:** "Lighthouse" + retention → a signal visible from far away, doing nothing but existing, that users steer by without contacting it.

## oblique-strategies
**When:** Stuck, and the block is one of stance rather than information.
**Move:** Apply an indirect instruction that changes approach instead of content. (Eno/Schmidt.)
**Example:** "Honour thy error as a hidden intention" · "Use an old idea" · "What would your closest collaborator do?" · "Remove the most important part."

## time-travel
**When:** Technical direction, critique, or reframing a current decision.
**Move:** Answer from ten years ago and ten years ahead. What was obvious then that we forgot; what will be obvious later that we cannot see.
**Example:** 2016: this needed a server room. 2036: needing a schema at all looks quaint. Both indict today's design.

## role-swap
**When:** Design, diagnosis, or a problem viewed from only one seat.
**Move:** Solve it as someone with a genuinely different objective function — not a persona costume, a different incentive.
**Example:** Solve the latency spike as the CFO, as an attacker, as the on-call at 3am, as a competitor wanting you to keep it.
