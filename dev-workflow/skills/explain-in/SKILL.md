---
name: explain-in
description: Rewrite engineer-to-engineer content for leadership audiences — VPs, directors, PMs, release managers. Shapes for the channel: JIRA comment, Slack post, standup note, email, or meeting talking-points. Use after post-mortem or any technical update that needs to flow up the org.
allowed-tools: Read
---

# Explain In

Same audience and translation rules as a written status report, but **shaped for the channel** — JIRA comment, Slack post, async standup, email, or meeting talking-points. The channel decides the length, formatting, and how much structure to leave on the page.

Use this any time engineering content needs to flow up the org, sideways into product/release, or into a non-engineering meeting.

## Activation Triggers

- "write something for management / exec / VP / director / PM / release manager"
- "rewrite this for [non-eng audience]" / "make this non-technical" / "less jargony"
- "send a slack update / standup note / email about [engineering work]"
- "executive summary" / "leadership update" / "status update"
- "talking points for [meeting]" based on an engineering update
- `/explain-in`

**Natural follow-on to `post-mortem`** — `post-mortem` offers this handoff automatically after drafting. Do not re-offer unprompted if already offered.

If the channel is unclear, ask one question — *"JIRA, Slack, standup, email, or meeting talking-points?"* — and stop.

## Audience

Engineering-savvy non-engineers: VPs, directors, PMs, release managers, execs in companies that ship technical products. They read product/framework names and cross-reference issue tracker IDs and PRs. They do **not** read code.

They want: *what's the state, what does it mean for customers, who owns it, what's next.* Not: how the bug works at the function level.

This is **not** for marketing, finance, customer-facing, or ELI5 audiences — flag and confirm before producing one of those.

## Keep / Strip / Translate

**Keep:** Product names, framework names, team-owned component names, issue tracker IDs (JIRA key, GitHub issue, Linear ticket), PR numbers, customer/workload identifiers. These are the cross-reference bridge — losing them breaks tracking.

**Strip:** Function names, file paths, struct fields, commit SHAs, env var names, line numbers, internal data-structure jargon. None of this is actionable to the audience.

**Translate:** Mechanism into one or two sentences of plain-English cause-and-effect. Not *"the kernel reads from `scratchBuf == NULL`"* but *"the GPUs end up reading from an uninitialized buffer and wait forever for a signal that never arrives."* Translate without lying — a race stays a race; a regression stays a regression.

**Don't over-strip.** Engineering-org leadership reads concept-level technical vocabulary fluently — *race condition, synchronization, uninitialized buffer, fast-path, workaround, queue, driver.* The line is: *concept exists and matters here* (keep) vs. *here's the function/struct/file/SHA* (strip). Replacing "race" with "timing issue" patronizes the reader.

**Bias toward** active voice, concrete subjects, short paragraphs. *"We found the bug. Alex wrote the fix. PR is up for review."* beats passive constructions.

**Avoid:**
- Hedging that isn't really hedging (*"we believe," "appears to"*) — state it or don't
- Re-stating the obvious for thoroughness
- Telling leadership how to do their job — give facts, they decide
- Engineering-process minutiae (bisect runs, GDB sessions) — they care you found it, not how

## Channel Shapes

### JIRA comment

Full structured block. Bolded section labels. Easy to scan from the ticket page.

Sections (use as many as fit, order by what matters most):

- **Status / TL;DR** — one bolded line. Reader can stop here. *"Fixed pending merge."* / *"Root cause unknown — investigating."*
- **Impact** — who's affected, how badly, what they see. Customer/workload/product terms, not test-suite terms.
- **What broke** — short paragraph, plain-English mechanism, one level of why, no code identifiers.
- **Why now / how it slipped through** — optional; include when leadership will ask anyway.
- **Owner** — person + team + their PR/branch/issue artifact. One link, not five.
- **Next steps** — concrete, near-term, ordered.
- **Workaround / mitigation** — if customers are hitting it now, one sentence on what they can do today.
- **Risk** — optional; real risks only, don't manufacture.

### Slack post

Single message, no walls of text. Heavy bolded section labels read as "I escaped from JIRA" — don't.

- One **bolded TL;DR** as the first line.
- 2–4 short bullets: impact, owner + link, next step. Drop blocks that don't apply.
- One link, embedded inline (`JIRA-12345` / `PR #5751`). Not a link wall.
- No greeting, no signoff.
- Thread reply: lose the TL;DR — just lead with the answer.

Length target: under ~80 words for a top-level post; under ~40 for a thread reply.

### Standup note

The audience scans 10 of these in 30 seconds. Front-load the verb.

- 1–3 lines, max.
- Pattern: *"\<state\> \<thing\>. \<owner if not me\>. \<next\>."*
- Examples:
  - *"Fixed Tada hang affecting dumbModel runs (JIRA-12345). PR #5751 in review. Backport to v7.2 next."*
  - *"Still chasing the LLM-7B eval-step hang. Reproducer is reliable now; bisecting. No ETA yet."*
- No bullets, no bolded labels. The format **is** the sentence.

### Email

Subject line is half the value.

- **Subject:** TL;DR as a noun phrase. *"Tada hang in dumbModel: fix in review (JIRA-12345)."*
- **Greeting:** match recipient register (*Hi Sam,* / *Hi all,*).
- **Body:** JIRA-comment shape, but as flowing paragraphs separated by blank lines — no bolded section labels. Two or three paragraphs is plenty.
- **Sign off** with the next decision point that needs the recipient's attention, if any.

### Meeting talking-points

You're going to *say* this, not show it.

- Bullet list, max one short clause per bullet.
- Order is the order you'll speak in.
- Include numbers/keys you want to reference out loud, in the bullet itself.
- Skip prose. *"dumbModel LLM-7B fine-tuning was hanging."* / *"Root cause: skipped sync in Tada fast-path."* / *"Alex's fix in review, PR #5751."*

## Output Flow

1. **Confirm the channel** if not stated.
2. **Produce the draft** as a single chat block, formatted as the channel would render it.
3. By default, **print-only** — the user copies it.
4. Issue tracker back-post (JIRA, GitHub Issues, Linear): only if the user explicitly says so. Show the payload, wait for explicit *"post it"* / *"go ahead"*, then post.
5. **Never auto-post to Slack, email, or any non-issue-tracker channel.** Hand the draft to the user; they post it.
6. **One iteration is normal, three is a smell.** On the third revision, ask what specific framing or audience assumption is off — don't keep tweaking blindly.

## Rules

- **Never invent facts.** If the source says "root cause unknown," the rewrite says "root cause unknown."
- **Never strip an issue tracker ID, PR number, or customer/workload name** during de-jargoning.
- **Never invent owners.** If the source doesn't name one, ask the user.
- **Get sign-off before posting to any issue tracker.** Print-only output needs no approval.
- **Never post to Slack, email, or any non-issue-tracker channel from this skill.**
- **Stay out of advocacy.** This skill produces a status update, not a recommendation.
