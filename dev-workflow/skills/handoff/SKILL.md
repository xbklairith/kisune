---
name: handoff
description: "Compact the current conversation into a handoff document so a fresh agent can pick up the work."
argument-hint: [what the next session will focus on]
disable-model-invocation: true
allowed-tools: Read, Write, Glob, Grep, Bash
---

# Handoff

Write a handoff document summarising the current conversation so a fresh agent can continue without re-deriving anything.

Write it to `docx/handoffs/<slug>.md`. Name the file for the work, not the date, so the next agent can find it by what it is about.

## Include

- **Goal** — what the work is for, in one or two lines.
- **State** — what is done, what is in flight, what is untouched.
- **Decisions made** — and the reason each was chosen, so the next agent does not relitigate them.
- **Open questions** — anything blocked on a person or an unknown.
- **Suggested skills** — name the skills the next agent should invoke, so it starts with the right discipline loaded.

## Rules

**Do not duplicate what other artifacts already hold.** Specs, plans, ADRs, issues, commits, and diffs are the record; reference them by path, SHA, or URL. A handoff that restates a spec goes stale the moment the spec changes.

**Redact secrets.** No API keys, passwords, tokens, or personal data. Point at where a credential lives, never at its value.

**Verify before claiming.** "Tests pass" in a handoff becomes the next agent's assumption. If it has not been run in this session, write what was last observed and when — see `completion-validation`.

If arguments were passed, treat them as the next session's focus and shape the document toward it.
