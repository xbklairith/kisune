---
name: investigate
description: "Research a question against high-trust primary sources and capture the findings as a cited Markdown file. Use when a topic needs researching, docs or API facts gathered, or reading legwork delegated to a background agent."
allowed-tools: Read, Write, Glob, Grep, Bash, Agent, WebSearch, WebFetch
---

# Investigate

Dispatch a **background agent** to do the reading, so the main session keeps working while it researches. See `spawn-agents` for the dispatch mechanics.

Its job:

1. **Follow every claim to the source that owns it.** Official docs, source code, specs, first-party APIs — not a blog post summarising them. A secondary write-up is a lead, not a citation.
2. **Write findings to a single Markdown file**, citing the source for each claim.
3. **Match the repo's existing convention** for where such notes live. If there is none, use `docx/research/<topic>.md` and say where it went.

## What makes a finding trustworthy

- **Dated.** Library behaviour changes. Note the version or the date the source was published.
- **Quoted where it matters.** For a claim a decision hangs on, quote the source rather than paraphrasing it.
- **Explicit about gaps.** "The docs do not say" is a finding. Silence read as confirmation is how wrong decisions get made.
- **Separated from opinion.** Findings first, then a clearly-marked recommendation if one was asked for.

Report back with the file path and the two or three findings that actually change what the caller should do.
