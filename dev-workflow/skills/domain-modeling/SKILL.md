---
name: domain-modeling
description: "Build and sharpen a project's domain model — challenge terms, resolve them into a glossary, and record hard-to-reverse decisions as ADRs. Use when codebase terminology is fuzzy or contested, when writing or editing a glossary, or when recording an architectural decision."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Domain Modeling

Actively build and sharpen the project's domain model while designing. This is the *active* discipline — challenging terms, inventing edge-case scenarios, and writing decisions down the moment they crystallise. Merely *reading* the glossary for vocabulary is a habit any skill can have; this skill is for when the model is changing.

## Where things go

```
docx/
├── glossary.md              ← canonical terms, one project-wide file
└── decisions/
    ├── 0001-event-sourced-orders.md
    └── 0002-postgres-for-write-model.md
```

Create **lazily** — no `docx/glossary.md` until the first term is resolved, no `docx/decisions/` until the first ADR earns its place. An empty scaffold is noise. If the repo already keeps decisions elsewhere (`docs/adr/`, an ADR tool), use that; confirm once at the first write, then stop asking.

## The four moves

**Challenge against the glossary.** When a term conflicts with `docx/glossary.md`, say so immediately. "The glossary defines *cancellation* as X, but this reads as Y. Which is it?"

**Sharpen fuzzy language.** When a term is vague or overloaded, propose a precise canonical one. "You said *account* — is that the Customer or the User? Those are different things, and the design branches on which."

**Cross-reference with the code.** When someone states how something works, check whether the code agrees. Surface contradictions rather than silently correcting them. "The plan says partial cancellation is possible, but `cancelOrder` only handles whole orders. Which is right?"

**Write inline.** The moment a term settles, append it. Do not batch — the reasoning is only fresh while the discussion is live.

```markdown
## Cancellation

A customer-initiated reversal of an unfulfilled Order. Distinct from a Refund,
which reverses payment on an Order that already shipped.
```

`docx/glossary.md` is a **glossary and nothing else** — no implementation detail, no spec, no scratch notes. An entry describing how something is built belongs in `design.md`.

## Bounded contexts

A term has one meaning *inside a bounded context*: the part of the system (a module, service, or team's area) where one model applies. The same word can correctly mean different things in two contexts. Catalog's *Product* (what is listed for sale, with a price and description) and Warehouse's *Product* (a stock item in a bin, with a quantity) are both right; merging them into one definition blends two models, and the code built on it starts mixing them too.

- **Find the contexts from the code** — top-level modules, services, separate schemas — not from the docs, which often blur them.
- **Ask "which context?" before "which meaning?"** When a word looks overloaded, first check whether each use stays inside its own context. If so, it is two terms, not a conflict to resolve.
- **Group the glossary by context once there are two.** One `## <Context>` section each; terms that mean the same thing everywhere go under `## Shared`. A one-context project stays a flat list.
- **Map the seam.** When a term crosses contexts, add one line under the second entry saying how the two relate and where they are translated: "A Catalog Product maps to one or more Warehouse Products by SKU (`catalog/stock.py`)."
- **Don't split to look thorough.** A word used the same way everywhere is one entry.

```markdown
## Catalog

### Product

What a shopper can buy: a name, a price, and a description.

## Warehouse

### Product

A stock item on a shelf: a SKU, a bin, and a quantity. A Catalog Product
maps to one or more Warehouse Products by SKU.
```

## Offer ADRs sparingly

Record a decision **only when all three hold**:

1. **Hard to reverse** — changing your mind later carries real cost.
2. **Surprising without context** — a future reader will ask "why on earth did they do it this way?"
3. **A real trade-off** — genuine alternatives existed and one was chosen for stated reasons.

Any one missing, skip it. A decisions log padded with obvious choices stops being read.

Write to `docx/decisions/NNNN-kebab-slug.md`, numbering from the highest existing file. Numbers are permanent addresses — supersede, never renumber.

```markdown
# NNNN. <Decision title>

- **Status:** accepted
- **Date:** YYYY-MM-DD

## Context

The situation that forced a decision. What constraint made this hard.

## Decision

What was chosen, in the active voice.

## Alternatives considered

Each real option and the specific reason it lost. An ADR with no alternatives
is a note, not a decision record — that was the third test, and it failed.

## Consequences

What this makes easy, what it makes hard, and what would have to be true to
revisit it.
```

Distinct from `post-mortem`, which records why something *broke*. ADRs record why something was *chosen*.
