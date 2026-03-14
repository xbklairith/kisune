---
name: agentic-engineering
description: Operate as an agentic engineer — eval-first execution, task decomposition, cost-aware model routing (Haiku/Sonnet/Opus), and AI-generated code review focus.
---

# Agentic Engineering

Engineering workflows where AI agents perform most implementation and humans enforce quality and risk controls.

## When to Activate

- Setting up AI-assisted development workflows
- Planning agent task decomposition
- Optimizing model selection for cost/quality
- Reviewing AI-generated code

## Operating Principles

1. Define completion criteria before execution
2. Decompose work into agent-sized units
3. Route model tiers by task complexity
4. Measure with evals and regression checks

## Eval-First Loop

1. Define capability eval and regression eval
2. Run baseline and capture failure signatures
3. Execute implementation
4. Re-run evals and compare deltas

## Task Decomposition

Apply the **15-minute unit rule**:
- Each unit independently verifiable
- Each unit has a single dominant risk
- Each unit exposes a clear done condition

## Model Routing

| Tier | Use For | Cost |
|------|---------|------|
| **Haiku** | Classification, boilerplate, narrow edits | Lowest |
| **Sonnet** | Implementation, refactors | Medium |
| **Opus** | Architecture, root-cause analysis, multi-file invariants | Highest |

Escalate model tier only when lower tier fails with a clear reasoning gap.

## Session Strategy

- Continue session for closely-coupled units
- Start fresh session after major phase transitions
- Compact after milestone completion, not during active debugging

## Review Focus for AI-Generated Code

Prioritize:
- Invariants and edge cases
- Error boundaries
- Security and auth assumptions
- Hidden coupling and rollout risk

Skip: Style-only disagreements when automated format/lint already enforces style.

## Cost Discipline

Track per task:
- Model used
- Token estimate
- Retries
- Wall-clock time
- Success/failure
