# trading behaviour evals

Cases for `claude plugin eval`: each trading skill fires on its trigger, stays quiet on a generic coding question, and produces work that holds up (a strategy doc with no template placeholders, a backtest without lookahead, readings computed from the data rather than invented).

```bash
cd trading
DOCKER_CONFIG=$(mktemp -d) claude plugin eval . --trust-plugin --scaffold \
  --allow-tools Skill Read Glob Grep Edit Write Bash \
  --runs 3 -j 8 --no-publish --model sonnet --judge-model sonnet --ablation none
```

- `data/*.csv` fixtures are synthetic (seeded random walk: a 150-candle decline, then a 150-candle rally). The ground truth in `analyze-csv/graders/readings-match-data.md` was computed from that file; regenerate both together.
- The sandbox Python may lack pandas. Prompts don't promise it; the agent falls back to the standard library.
- Prefer `regex` graders for long artifacts; `llm` judges get noisy past ~10k characters, so keep their rubrics to the points that need judgement.
- Full suite ≈ $2.1 (Sonnet) / $4.6 (Opus) at 3 runs.
