---
name: eval-harness
description: Eval-driven development (EDD) — define pass/fail criteria before coding, measure with pass@k metrics. Use when defining completion criteria or measuring agent reliability.
---

# Eval Harness

Formal evaluation framework implementing eval-driven development (EDD) — treating evals as unit tests for AI development.

## When to Activate

- Setting up eval-driven development for AI workflows
- Defining pass/fail criteria for task completion
- Measuring agent reliability with pass@k metrics
- Creating regression test suites for prompt/agent changes

## Philosophy

- Define expected behavior BEFORE implementation
- Run evals continuously during development
- Track regressions with each change
- Use pass@k metrics for reliability measurement

## Eval Types

### Capability Evals
Test if Claude can do something new:
```markdown
[CAPABILITY EVAL: feature-name]
Task: What Claude should accomplish
Success Criteria:
  - [ ] Criterion 1
  - [ ] Criterion 2
  - [ ] Criterion 3
```

### Regression Evals
Ensure changes don't break existing functionality:
```markdown
[REGRESSION EVAL: feature-name]
Baseline: SHA or checkpoint
Tests:
  - existing-test-1: PASS/FAIL
  - existing-test-2: PASS/FAIL
Result: X/Y passed
```

## Grader Types

| Type | When | How |
|------|------|-----|
| **Code grader** | Deterministic checks | `<test-command> && echo PASS` |
| **Rule grader** | Regex/schema constraints | Pattern matching |
| **Model grader** | Open-ended quality | LLM-as-judge rubric |
| **Human grader** | Ambiguous outputs | Manual review |

## pass@k Metrics

- **pass@1**: First attempt success rate
- **pass@3**: Success within 3 attempts (practical reliability)
- **pass^3**: All 3 trials succeed (stability test)

### Thresholds
- Capability evals: pass@3 >= 90%
- Regression evals: pass^3 = 100% for release-critical paths

## Workflow

### 1. Define (Before Coding)
```markdown
## EVAL: add-authentication

Capability Evals:
- [ ] User can register with email/password
- [ ] Invalid credentials rejected
- [ ] Sessions persist across reloads

Regression Evals:
- [ ] Public routes still accessible
- [ ] API responses unchanged

Success: pass@3 > 90%, regression pass^3 = 100%
```

### 2. Implement
Write code to pass defined evals.

### 3. Evaluate
Run evals, record PASS/FAIL.

### 4. Report
```markdown
EVAL REPORT: add-authentication
Capability: 3/3 passed (pass@3: 100%)
Regression: 3/3 passed (pass^3: 100%)
Status: SHIP IT
```

## Anti-Patterns

- Overfitting prompts to known eval examples
- Measuring only happy-path outputs
- Ignoring cost/latency while chasing pass rates
- Allowing flaky graders in release gates

## Best Practices

1. Define evals BEFORE coding
2. Run evals frequently
3. Track pass@k over time
4. Use code graders when possible (deterministic > probabilistic)
5. Human review for security (never fully automate)
6. Keep evals fast
7. Version evals with code
