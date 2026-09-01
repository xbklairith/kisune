---
name: grill-with-docs
description: "Grilling that leaves a paper trail — runs the grilling interview while capturing resolved terminology and hard-to-reverse decisions into docx/ as they settle."
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

# Grill With Docs

Invoke both `grilling` and `domain-modeling` via the Skill tool, and run them together.

`grilling` drives the rounds. `domain-modeling` runs alongside it: challenge terms against the glossary as they come up, sharpen fuzzy language into canonical entries, and write each one to `docx/glossary.md` the moment it settles. Offer an ADR only for decisions that pass all three of its tests.

Capture as it happens, never batched to the end — the reasoning is only fresh while the round is live.

Before handing off, report what was written: every glossary term added or changed and every ADR created, by path. Decisions considered for an ADR and rejected against the three tests get one line each, so the user can overrule.
