# dev-workflow behaviour evals

Cases for `claude plugin eval`. Each checks that a skill runs when it should (or stays quiet when it shouldn't), graded from the tool trace.

```bash
cd dev-workflow
claude plugin eval . --trust-plugin --scaffold \
  --allow-tools Skill Read Glob Grep Edit Write Bash \
  --runs 3 -j 6 --no-publish --model sonnet --ablation none
```

- `--scaffold` runs each case's `scaffold.sh`, which copies the case's fixture into the agent's working directory. `add_dirs` only grants reads; it does not seed the workspace.
- The Skill tool and file tools need both the case's `execution.allowed_tools` and `--allow-tools`; runs are in don't-ask mode.
- Bash is refused if `~/.docker` holds a symlink. Point `DOCKER_CONFIG` at an empty directory for the run (`DOCKER_CONFIG=$(mktemp -d) claude plugin eval …`); your real Docker config is not touched.
- Judge with `--judge-model sonnet`; an `llm` grader with `focus: files` sees only the list of changed file names, so judge content with `focus: {source: file, path: …}`.
- Pin the model with `--model`. Per-case model lives under `execution:`, not at the top level.
- Cases named "indicator (unscored)" are measured, not gated; their graders omit `arm: both`.
- Run on Sonnet and Opus before and after changing `using-kisune` or a skill's description. Full suite ≈ $2.5 (Sonnet) / $5.7 (Opus) at 3 runs.
