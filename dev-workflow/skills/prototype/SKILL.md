---
name: prototype
description: "Build a throwaway prototype to answer a design question. Use when sanity-checking whether a state model or logic feels right, or exploring what a UI should look like, before committing the decision to real code."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Prototype

A prototype is **throwaway code that answers a question**. The question decides the shape.

## Pick the branch first

Identify which question is being answered — from the prompt, the surrounding code, or by asking:

- **"Does this logic or state model feel right?"** → a single shareable HTML file: free-play controls plus a guided walkthrough that pushes the state machine through the cases that are hard to reason about on paper. A non-developer should be able to drive it.
- **"What should this look like?"** → several radically different variations on one route, switchable via a URL search param or a floating switcher bar.

The two produce very different artifacts, so getting this wrong wastes the whole prototype. If genuinely ambiguous and the user is unreachable, default by context — a backend module implies logic, a page or component implies UI — and state the assumption at the top.

## Rules for both

1. **Throwaway from day one, and marked as such.** Put it next to the code it prototypes for so context is obvious, but name it so nobody mistakes it for production. Follow the project's existing routing or module conventions; do not invent a new top-level structure for it.
2. **Trivial to run.** One command from the project's task runner, or a single HTML file the user double-clicks. No setup thinking.
3. **No persistence by default.** State lives in memory. Persistence is usually the thing being *checked*, not something to depend on. If the question genuinely involves a database, use a scratch one named so it is obviously disposable.
4. **Skip the polish.** No tests, no error handling beyond what makes it runnable, no abstractions. `test-driven-development` does not apply here — this code is designed to be deleted, and TDD's Iron Law covers production code.
5. **Surface the state.** After every action, render or print the full relevant state so the user can see exactly what changed.

## Capture it when done

Fold the validated decision into the real code. Keep the prototype itself as a primary source: commit it to a throwaway branch off main, never merged.

Then record the outcome in `docx/prototypes/<question-slug>.md` — the question asked, the verdict, and the branch holding the code. A prototype whose answer was never written down has to be built twice. If the verdict is a hard-to-reverse architectural choice, promote it to an ADR via `domain-modeling` instead.

Main keeps the decision, never the prototype.
