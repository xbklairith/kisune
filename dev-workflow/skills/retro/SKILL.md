---
name: retro
description: Use when a coding session went badly or slowly and the user asks what to change so the next one goes better — "retro", "retrospective", "that session was painful", "why did that take so long", "improve the agent setup". Reads the session's own log (current project only) and proposes changes to the agent's environment — automated checks, navigation pointers, CLAUDE.md trims, review rules, tooling — ordered by severity.
---

# Retro

## Overview

A retro improves the **environment** the next agent works in, not the code from the last session. The evidence is the session log; the output is a short, severity-ordered list of environment changes, each concrete enough to apply in one step.

**Core principle: a check beats a rule.** A mistake a machine can detect gets a check (lint rule, type check, test, hook, CI job). Prose in `CLAUDE.md` is the last resort, because every line there is loaded into every session and is obeyed only probabilistically.

## 1. Read the primary source

Read the actual log, not a recollection of it. Claude Code keeps logs per project; read **this project's only**:

```bash
python3 <this skill>/scripts/session_log.py list            # sessions for cwd's project
python3 <this skill>/scripts/session_log.py show latest     # or a SESSION_ID from list
python3 <this skill>/scripts/session_log.py show <id> --full  # include the agent's prose
```

- **Never glob across `~/.claude/projects/`.** Other directories there are private chats from unrelated projects. The script derives the one directory from the project path; use it rather than `find`/`grep` over the parent.
- If the user hands you a written log or notes instead, use that.
- **Redact.** Logs contain pasted keys and tokens. Never quote a secret value in the retro; name where it was exposed.

The `show` summary flags the usual waste: files read repeatedly, commands re-run, failed tool calls, and how far into the session the first edit came.

## 2. Find candidates

For each friction point in the log, ask which category removes it next time:

| Category | Signal in the log | Change |
|---|---|---|
| **Automated checks** | The agent made a mistake a tool could catch; or the repo has no guardrail at all (no hook, no CI running lint/type/test) | Wire the check. First read the repo's existing `lint`/`check`/CI config: a check that exists but is unwired or broken is the finding, not a new one |
| **Review rules** | The mistake is a judgement call and review missed it | Add it to what the reviewer reads (the repo's `CODING_STANDARDS.md` or the `review` checklist the team runs) |
| **Navigation** | Long searches for a file or fact; hidden coupling between files | A one-line pointer in the place the agent looked first |
| **Steering trims** | `CLAUDE.md` lines that change no behavior ("write clean code"), or rules a check now enforces | Delete them |
| **Tool economy** | Expensive or repeated tool calls; a noisy CLI or MCP | A script, a flag, a narrower command |
| **Information access** | A fact the agent needed but could not see (server logs, a dashboard, a schema) | Give read access: tee logs to a file, a read-only token, a schema dump |
| **Skills** | The same multi-step procedure re-derived each session | A skill (write it with `skill-maker`) |

### Classify before you prescribe

- **Mechanical** violation (an import shape, a banned API, a file location, a naming pattern, a missing format/type run): **a check, full stop.** Name the exact rule and where it goes, e.g. "`no-restricted-imports` pattern `../*` in `.eslintrc`, run in pre-commit and CI". Do not also add a `CLAUDE.md` line for it.
- **Judgement** call (cross-file consistency, "matches surrounding style"): a review rule. Review runs on a diff with little context pressure; the implementation agent is the one drowning in context, so standards belong in review, not in its prompt.
- Only what is neither, and needed by **every** session, goes in `CLAUDE.md`, usually as a navigation pointer to a doc.

## 3. Budget the steering file

`CLAUDE.md` / `AGENTS.md` (repo and the user's global one) cost context on every turn. A retro should usually leave them **shorter**. Count the lines your proposal adds and removes; if the net is positive, justify each added line as unenforceable and universal. A checklist, file map, or "remember to…" list added to `CLAUDE.md` is the most common wrong fix: the agent that ignored one rule will ignore a longer list.

## 4. Report

Present candidates in severity order (cost to the next session × likelihood it recurs). Each item:

- **Evidence**: the log moment (step number from `show`, or a quote with secrets redacted)
- **Change**: the exact file and edit, rule config, or command
- **Category**: from the table

End with the net line change to steering files. Apply nothing without the user's go-ahead. If the user wants a record, save it to `docx/retros/YYYY-MM-DD-<slug>.md`.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Adding the violated rule to `CLAUDE.md` in bold | The rule was already there or obvious; build the check |
| "Consider adding linting" | Name the rule, the config file, and where it runs |
| Recommending from memory of the session | Read the log; cite steps |
| Searching every project's logs to find the session | `session_log.py` for this project only |
| Proposing a new doc without looking for an existing one | Point to what exists first |

*Adapted from `retro` in mattpocock/skills (MIT) — see `references/NOTICE.md`.*
