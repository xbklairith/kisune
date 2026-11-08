---
name: explain-in-html
description: Render structure as an HTML page instead of terminal text — Mermaid diagrams, UML, ER and state charts, comparison tables — or put a multi-question round in the browser for the user to answer. Use when the shape of the thing is the point (schemas, state machines, dependency graphs), or when asking three or more structured questions at once. This is the output medium only; skills that decide what to ask, plan or review keep that job and hand the rendering here.
allowed-tools: Artifact, ArtifactData, mcp__claude-artifacts__guide, mcp__claude-artifacts__describe_capabilities, mcp__claude-artifacts__read_declaration, mcp__claude-artifacts__db_query, mcp__claude-artifacts__db_get, mcp__claude-artifacts__db_list, Write, Read
---

# Explain in HTML

A terminal is a poor renderer for anything with a shape. This skill moves that output to a page.

**It owns the medium, not the decision.** `grilling` decides what to interrogate, `brainstorming` decides what to elicit, `scrutinize` decides what to review — each keeps that job and hands the rendering here. When one of them owns the decision, **it runs first and calls this**. Never publish a page to sidestep deciding who should be asking.

## Two modes, inferred from content

| Content | Mode | Output |
|---|---|---|
| Something to understand — architecture, schema, state machine, a comparison | **explain** | A page with diagrams and tables |
| Something to answer — a question round, a set of choices | **interact** | A page with the questions answerable in-browser |

Do not ask which mode. Read the content. **Mixed content is one page** — a short explainer above the questions, never two deliverables.

## Default to the page

Use the page whenever the content has structure worth seeing. Fall back to terminal text only for a trivial confirm — a yes/no, a single pick from two obvious options. One question is a sentence; three are a page; at two, use the page if the choices interact.

## Which artifact tool

Use whichever this session has. The two differ at every step:

| Step | Built-in `Artifact` tool | `claude-artifacts` server |
|---|---|---|
| Page rules | `Artifact` `quickstart`, `intent: "other"`; do not also load `artifact-design` | `claude-artifacts:guide` topics `pages`, then `design` |
| Diagram rules | the `artifact-diagramming` skill | `claude-artifacts:guide` topic `diagrams` |
| Publish | `Artifact`, with `capabilities` on the same call | `claude-artifacts:publish_files`; then, for capabilities, `read_declaration` and `declare_capabilities` |
| Read answers | `ArtifactData` | `claude-artifacts:db_query`, `db_get`, `db_list` |
| Mermaid | renders natively: bare `<pre class="mermaid">`, load nothing | nothing renders it: load the pinned build |

Neither tool: see Fallbacks. In a local file, too, nothing renders Mermaid.

## How to build it

1. **Load the page rules** for your tool (table above).
2. **Figures — delegate, never improvise.** Load the rule-owners; do not restate them here.
   - Mechanism — how it works, what talks to what, before/after → the diagram rules for your tool
   - Quantities — magnitude, distribution, change over time → **`dataviz`**, which has hard requirements of its own (run its palette validator; never a dual-axis chart)

   Pick the form by the kind of diagram:

   | Diagram | Form |
   |---|---|
   | Mechanism, before/after, side-by-side (the default) | hand-authored inline SVG |
   | Sequence, state, ER | Mermaid |
   | A dependency graph too big to place by hand | Graphviz, rendered here by `scripts/dot_svg.py` |

   **Mermaid source with no renderer shows as plain text.** Only the built-in `Artifact` tool renders it; on the server and in a local file, load the exact pinned version, never `@11`. Loader and Graphviz recipes: `references/diagrams.md`.
3. **Publish.** Interact pages follow `grilling`'s rule — **every question carries a recommended answer**, so a user who agrees can say "yes to all" and move on. For interact mode declare `{db: {}, user: {}}` — that is what makes answers savable and readable back (on the server, read `claude-artifacts:describe_capabilities` for `db` before writing the page code). Add `downloads: true` only if the user wants a file too. Explain mode needs none.

## Getting the answers back

**"Saved" means persisted to the artifact server** — not a file on the user's disk. The `db` round-trip *is* the save: what the page writes is readable straight from this session.

Publishing does not wake the session — a published version **starts no turn and sends no notification**. Say plainly that you are waiting, and stop.

| Exit | Declare | Role |
|---|---|---|
| **Save** — server-side, read back here | `db` + `user` | the primary path; `use("db")` returns `null` for a signed-out viewer |
| **Copy** — clipboard as Markdown | nothing | the floor; works when `db` does not |
| Take a file away | `downloads: true`, then `downloads.save({filename, data})` | optional convenience; `.md` and `.html` are allowlisted |

`<a download>`, blob saves and `window.print()` are inert in the viewer sandbox. The `downloads` capability is a separate mechanism and does work — but it is not what "save" means here.

Read answers back with `ArtifactData` or the server's `db_*` tools. These are deferred tools: load the schema via `ToolSearch` before the first call.

## Fallbacks

| No artifact tool | Do this |
|---|---|
| explain mode | Write a standalone `.html` to `docx/explainers/<slug>.html` and give the path; Mermaid needs the pinned loader |
| interact mode | Fall back to `AskUserQuestion` — never silently drop the questions |

Save to `docx/explainers/<slug>.html` only when asked.

## Before publishing

**Redact secrets.** No API keys, passwords, tokens, or personal data. Point at where a credential lives, never at its value.

A published page leaves the machine and lives on claude.ai. When the content is private code, say so once before the first publish of a session.
