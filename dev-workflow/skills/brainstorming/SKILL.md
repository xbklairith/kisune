---
name: brainstorming
description: Collaborative refinement of rough ideas into clear requirements/designs through systematic questioning. Use when requirements are vague or exploring architectural options.
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash
---

# Brainstorming Ideas Into Designs

## Overview

Turn a rough idea into an approved design through dialogue: understand the context, ask one question at a time, propose approaches, then present the design in short sections the user approves one by one.

<HARD-GATE>
Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it. This applies to EVERY project regardless of perceived simplicity.
</HARD-GATE>

**"Too simple to need a design" is the trap.** Simple projects are where unexamined assumptions waste the most work. The design can be a few sentences, but present it and get approval before acting.

## When to Use

- A rough idea, unclear scope, or "not sure how to approach this".
- Requirements phase of `spec-driven-planning`: explore *what* to build (scope, must-haves vs nice-to-haves).
- Design phase: explore *how* (architectures, trade-offs).

## The Process

1. **Look first.** Read the project state (files, docs, recent commits) before asking anything you could find out yourself. When the answer depends on how others solve it, research prior art, library docs, or the external API, and share what you found with sources.
2. **Ask one question per message**, multiple choice where possible, until you know the purpose, constraints, and success criteria.
3. **Propose 2-3 approaches** with trade-offs (complexity, maintainability, performance, security, testability). Lead with the one you recommend and say why. When the choice has long-term or security consequences, question the problem first: what are we assuming, what could go wrong, what is the simplest thing that works?
4. **Present the design in sections of 200-300 words** (architecture, components, data flow, error handling, testing) and ask after each whether it looks right. Go back when something doesn't fit.

**YAGNI ruthlessly.** Cut features nobody asked for from every option.

## After Brainstorming

- **Requirements:** write the validated requirements to `docx/features/[NN-feature-name]/requirements.md` in EARS form (see `spec-driven-planning`), then ask "Requirements complete. Ready for design phase?"
- **Design:** write the validated design to `docx/features/[NN-feature-name]/design.md` following the plugin's design template, then ask "Design complete. Ready for task breakdown?" and hand off to `spec-driven-implementation`.

## Example: exploring approaches

```
Based on your answers I see three approaches:

**A. JWT-based auth** (recommended) — stateless, works across services; revocation is harder.
**B. Server sessions** — simple revocation; needs shared session storage to scale.
**C. Hybrid** — both benefits, most complexity.

I recommend A because you mentioned a mobile app and other API clients.
Does that match your thinking?
```
