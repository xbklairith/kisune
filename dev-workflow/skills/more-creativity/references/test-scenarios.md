# Test Scenarios

The RED/GREEN scenarios this skill was built against, recorded so the behaviour can be
re-tested after any edit. Run each prompt in a fresh subagent, once without the skill
(RED) and once with it (GREEN).

## Scenario A — idea generation

> I run a B2B SaaS that does inventory management for independent restaurants.
> Monthly churn is 4.5% and I can't get it down. Give me ideas.

## Scenario B — hypothesis generation

> Our API's p99 latency spikes every Monday between 9 and 11am. Nothing deploys on
> weekends. Give me hypotheses for what's going on.

## Baseline (RED) behaviour to expect without the skill

Unaided output is strong on structure and coverage but shows three habits:

1. **Evaluation woven into generation** — "fastest ROI on the list", "half a day of work",
   hypotheses pre-ordered by prior probability.
2. **Early convergence** — ends in an action plan ("What I'd actually do in the next 30
   days", "Start with the first two").
3. **Never leaves the domain playbook** — every churn idea is standard SaaS retention,
   every latency hypothesis standard systems engineering. Zero cross-domain imports.

The baseline does *not* fail on quality. It fails on non-obviousness.

## Pass criteria (GREEN)

| # | Check | Where |
|---|---|---|
| 1 | Techniques named in the header line, and at least one technique **absent from** the problem type's row (rows overlap — shared entries do not count) | §2 |
| 2 | No feasibility / cost / effort / ROI / priority language anywhere before the gate | §3 |
| 3 | `Obvious options skipped:` line present | §4 |
| 4 | Every surviving idea would fail "could the user have thought of this alone?" if removed | §5 |
| 5 | Scenario B only: every hypothesis carries `Mechanism:` and `False if:` | §6 |
| 6 | Scenario B only: `Cheapest discriminators:` triage line present | §6 |
| 7 | Output stops at the list; handoff offered instead of an action plan | §7 |
| 8 | Idea count matches the intensity band | §1 |

## Known trade-off

The skill deliberately suppresses the analytical framing the baseline does well — Scenario
A's baseline split churn into buckets and read the tenure curve, and the skill will not.
That is why §7 hands off. Do not use this skill alone on a question that wanted analysis.
