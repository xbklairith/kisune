---
name: wizard
description: Use when a human must do steps the agent cannot — creating accounts or API keys in a third-party dashboard, filling .env values, setting GitHub Actions secrets/variables, provisioning a service, a one-off migration or cutover. Generates a runnable interactive bash wizard that opens each URL, says what to click, captures values with hidden entry for secrets, and writes them to .env and gh secrets. Not for steps the agent can run itself.
---

# Wizard

## Overview

A **wizard** is a bash script that walks a human through a manual procedure one stage at a time: it opens each URL, says exactly what to click and copy, captures the value, writes it where it belongs (`.env`, a GitHub secret or variable), confirms before anything irreversible, and shows how many stages are left.

**The deliverable is the script.** A markdown checklist of the same steps is not a wizard: the human still copies values by hand, mistypes a secret name, and pastes keys into a terminal history. When a project rule asks for a setup document too, write it, and make its first step "run `scripts/<name>.sh`". The document points at the script; it never replaces it.

The UX is already built in `assets/template.sh` (stage progress, confirm gates, cross-platform URL opening including WSL, hidden secret entry, idempotent `.env` upserts, a refusal to write secrets into an `.env` that git does not ignore, `gh secret`/`gh variable` writes, closing summary). **The job is only to scope the procedure and author its stages.** Never hand-edit the library above the `STAGES` marker; that sameness across wizards is the point.

## When to Use

- "Set up the keys/secrets/env for this project", "walk me through deploying", "I just cloned this, get me running"
- A workflow file references `secrets.*` or `vars.*` that do not exist yet
- A migration or cutover with manual, irreversible steps in a vendor console

**Not for** steps the agent can perform itself (run them), or a single value the user can paste in one line.

## Process

### 1. Scope from the repo, then confirm

Read before asking: `.env.example`, `.env.*`, `README`, `docker-compose*`, framework config, and every `.github/workflows/*`. Each `secrets.X` and `vars.X` is a value the wizard must produce. For a migration: current state, target state, and the irreversible actions between them.

Show the user the ordered stages and the values each produces; they may add, drop or reorder.

**Done when**, for every captured value, you know (a) where the human gets it, (b) where it is written: `.env`, `set_secret`, `set_var`, several, or nowhere, and (c) whether it is secret (`ask_secret`) or public (`ask`).

### 2. Map each stage's journey

Write the exact path a stranger follows: URL, clicks, where the value appears, which variable it fills, e.g. "Dashboard → Developers → API keys → Reveal test key → copy". Where the current UI or command is unknown, say so and check the vendor docs or ask. **Never invent a menu path.**

### 3. Author the stages

Copy `assets/template.sh` to `scripts/setup-<thing>.sh` (or a scratch path when the user wants a one-off). Replace the example stage, one `stage` per focused step, in dependency order. Set `TOTAL_STAGES` to match.

- `open_url` before asking for the value it shows.
- `ask_secret` for anything secret; `ask` only for public values.
- `write_env` every value the app reads locally; `set_secret` only what CI reads; `set_var` for non-secret CI config.
- `confirm` before any irreversible action (deleting data, rotating a live key, DNS cutover).
- **Secrets never appear in the script.** No real key, token, or example that looks real; the script asks for values, it does not contain them. Point at where a credential lives, never at its value.

### 4. Verify and hand off

- `bash -n scripts/setup-<thing>.sh`; run `shellcheck` if installed. `chmod +x`.
- Do not run it end-to-end: it opens browsers and blocks on input. Trace it statically instead: every value from step 1 is captured and lands where step 1 said, and every `set_secret`/`set_var` name exactly matches a `secrets.*`/`vars.*` reference in the workflows.
- Tell the user the one command to run. If it is a repeatable setup path, link it from the README so the next person runs the script instead of asking an agent.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing `SETUP.md` with the steps instead of a script | The script is the deliverable; the doc links to it |
| Copying `.env.example` to `.env` and telling the user to fill it | The wizard asks for each value and writes it |
| A `set_secret` name that differs from the workflow's `secrets.X` | Grep the workflows and match names exactly |
| Guessing a dashboard's menu path | Check docs or say it is unknown |
| Editing the library to tweak a prompt | Change only the stages |

*Adapted from `wizard` in mattpocock/skills (MIT) — see `references/NOTICE.md`.*
