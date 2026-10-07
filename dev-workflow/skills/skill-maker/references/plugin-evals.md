# Plugin eval cases for a skill

`claude plugin eval` runs each case with the plugin loaded and (by default) again without it, then grades the trace.

## Layout

```
<plugin>/evals/<case>/
├── case.yaml          # settings
├── prompt.md          # what the user says — organic, no test vocabulary
├── scaffold.sh        # optional: seeds the working directory with fixtures
├── <fixture-dir>/     # optional: files the prompt is about
└── graders/*.md       # one grader per file, YAML frontmatter
```

## case.yaml

```yaml
schema_version: "1.1"
name: bug report invokes the skill
context:
  scaffold_script: scaffold.sh      # runs only with --scaffold
execution:
  max_turns: 25
  allowed_tools: [Skill, Read, Glob, Grep, Edit, Write]
runs: 1
```

- `context.add_dirs` grants **read** access to a path inside the case directory; it does not copy anything into the working directory. To give the agent files to edit, copy them in with `scaffold.sh`.
- Runs use don't-ask mode: the Skill tool and file tools must be in `execution.allowed_tools` AND passed with `--allow-tools`, or every call is denied.
- Per-case model goes under `execution.model`; `--model` on the command line overrides every case.
- A name containing `: ` breaks the YAML; quote it or rephrase.

## scaffold.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cp -R "$here/fixture-project" ./fixture-project
```

## Graders

```yaml
---
type: tool_used            # the skill fired
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?my-skill"'
arm: both                  # score it; without this it is an unscored indicator
---
```

| type | keys |
|---|---|
| `tool_used` | `tool`, `input_match`, `min`, `max` (`min: 0, max: 0` = must NOT fire) |
| `tool_order` | `before`, `after` (fails if either tool never runs) |
| `file_exists` | `path` (glob), `exists` |
| `regex` | `pattern`, `flags` (JS: `i`, `m`…; no inline `(?i)`), `match: contains\|not_contains\|count:N`, `target: last_message\|trace\|files` |
| `llm` | body = rubric; `focus: last_message\|trace\|files`; judge defaults to haiku |

## The three cases every skill gets

1. **Triggers**: an organic prompt the skill exists for → `tool_used` Skill, `arm: both`.
2. **Stays quiet**: a nearby prompt it must not take → `tool_used` Skill with `max: 0`.
3. **Does the work**: a task whose output shows the skill's effect → `file_exists` / `regex` / `llm` on what it produced.

## Running

```bash
claude plugin eval <plugin-dir> --trust-plugin --scaffold \
  --allow-tools Skill Read Glob Grep Edit Write \
  --runs 3 --model sonnet --no-publish
```

Run on every model the plugin targets. Add `--ablation none` to skip the no-plugin arm when comparing two versions of the same skill.
