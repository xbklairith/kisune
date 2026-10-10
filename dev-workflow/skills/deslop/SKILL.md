---
name: deslop
description: Rewrites prose in English or Thai so it reads like a person wrote it - lessons, explanations, research notes, reports, docs, READMEs, commit messages, PR descriptions, changelogs. Reorders it so the point and prerequisites come first, swaps LLM vocabulary for words people actually use, and removes ambiguity, while keeping every fact, citation, number and identifier. Use when the user asks to tighten, clean up, de-slop, humanize or เกลา wording, says existing text reads like AI or ChatGPT, or another skill hands over a draft to polish. Not for writing new text from scratch.
allowed-tools: Read, Edit, Write, Grep
---

# Deslop

Rewrite prose so it reads like a person who knows the subject wrote it. Change how it says things, never what it says.

## When to Use

- The user asks to tighten, clean up, de-slop or humanize text, or says it sounds like AI.
- Another skill hands over a draft to polish (a PR description, a post-mortem).

It works on any existing prose: a lesson, an explanation, research notes, a report, a README, release notes. Not for writing new text from scratch, code, or fiction and creative writing where the voice is the point.

## Keep exactly

These survive a rewrite character for character:

- Identifiers, paths, flags, env vars, commands, error text, version numbers.
- Numbers, dates, names, formulas and equations, issue and PR references.
- Citations and the claim they support; the source's own hedges ("may", "in one study") are facts too.
- Requirement lines (EARS `WHEN … THEN the system SHALL …`), acceptance criteria, quoted text.
- Tables and lists of reference data. A list is fine when the content is a list.

Every claim in the original stays. Do not add a fact, number, cause, owner, benefit, follow-up, or a "that is why" link that the source does not state, even one you know is true. If a sentence needs a missing detail, ask or write the simpler sentence.

## Rearrange

When a template or another skill fixes the structure (section order, labels, headings), keep it and change sentences only.

Order is part of meaning. Before polishing sentences, fix the order:

- Lead with the point: what changed, what to do, or the conclusion. Background after.
- Put prerequisites, warnings and version requirements **before** the step they govern, not in a trailing "Don't forget" note.
- Steps in the order they are run. Related facts together; one idea per paragraph.
- Split a sentence that carries two instructions.

## Plain words

Use the word people in the field say and search for, not the word an LLM reaches for. "use" not "leverage", "help" not "facilitate", "faster" not "more performant", "fix" not "remediate". In Thai, use the words Thai readers in that field use, including English loanwords where they are the norm (deploy, cache, DNA, GDP), instead of coined formal Thai, and drop the formal padding listed in `references/thai.md`.

## No ambiguity

- Replace a pronoun whose referent is unclear ("it", "this", "they"; Thai "มัน", "นี้", "ดังกล่าว") with the noun, when the source makes the referent clear.
- Keep the source's strength: if it says required, write "must"; never soften a requirement to "should" or harden advice to "must".
- When the source contradicts itself ("you should set X; this is required"), the stronger statement wins: write "must" once and drop the hedge.
- If the source does not say what "it" is, or which value, do not guess: keep the gap visible and tell the user what is missing.

## Remove

Full catalogue with examples: `references/patterns.md`. The most common:

| Tell | Instead |
|---|---|
| Importance inflation: "pivotal", "a testament to", "crucial role" | State what changed |
| Benefit padding: "seamless", "robust", "fostering", "ensuring", "enhanced" | Say the concrete effect, or cut it |
| Bold-label bullets: `- **Reliability:** …` | A plain bullet that starts with the change |
| Title Case Headings | Sentence case headings |
| Em and en dashes | Comma, colon, parentheses or a new sentence |
| "It's not just X, it's Y", forced groups of three | One plain statement |
| Chatbot residue: "I hope this helps", "Let me know if…", "Great question" | Delete |
| Stock outlook endings: "the future looks bright", "Moving forward…" | End on the last fact |
| Filler: "In order to", "What happened was that", "It is important to note" | Cut to the verb |
| Describing the previous version: "now", "no longer", "updated to" in docs that are not a changelog | Describe current behaviour |

## Shapes by artifact

- **Lesson:** define a term before the first sentence that uses it; one idea per paragraph; keep every example; match the reader's level. An explanation the source lacks ("That is why plants look green") does not go in the text, however true; offer it to the user as a suggestion.
- **Explanation:** the answer first, then why, then the details.
- **Research notes:** each claim sits in the same sentence as its citation; keep the source's uncertainty.
- **Commit message:** imperative subject, no "This commit"; body only if the why is not obvious.
- **PR description:** what changed and why, then how it was tested. No adjectives about the testing.
- **Changelog / release notes:** one user-visible change per line, in the source's words. No benefits the commits do not state.
- **Post-mortem:** inside each section, facts in time order; no "lessons learned" filler unless the source has a lesson.

## Process

1. Read the whole text. For a file, edit it in place; for pasted text, return the rewrite. Either way, end your reply with any open questions (gaps you would not guess) and suggestions (explanations the source lacks), or nothing if there are none.
2. Fix the order (Rearrange), then mark every tell against the table and `references/patterns.md`.
3. Rewrite. Keep the writer's register: terse stays terse.
4. Thai text: also check `references/thai.md`.
5. Check both directions: every fact, identifier and requirement line in the original is in the rewrite, and every sentence in the rewrite traces to the original (delete or move to your reply any that does not); grep the result for `—`, `–` and the words in the table.

Do not flag a word used in its technical sense: a primary *key*, a *robust* estimator, landscape orientation, financial *leverage*.

---

*Adapted from [humanizer](https://github.com/blader/humanizer) by Siqi Chen (MIT), which is based on Wikipedia's "Signs of AI writing". See `references/NOTICE.md`.*
