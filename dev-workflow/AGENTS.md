# Dev-Workflow Agents

## Core Principles

1. **Agent-First** — Delegate to specialized agents for quality
2. **Test-Driven** — 80%+ coverage required
3. **Security-First** — Never compromise on security
4. **Plan Before Execute** — Use spec-driven planning for features

## Agent Registry

| Agent | Purpose | When to Use | Model |
|-------|---------|-------------|-------|
| planner | Implementation planning | Complex features, refactoring | sonnet |
| code-reviewer | Code quality review | PROACTIVELY after writing/modifying code | sonnet |
| security-reviewer | Vulnerability detection | PROACTIVELY for auth, user input, APIs, sensitive data | sonnet |
| tdd-guide | TDD enforcement | PROACTIVELY when writing features or fixing bugs | sonnet |

## Development Workflow

```
1. Plan     → planner agent (or spec-driven-planning skill for new features)
2. Test     → tdd-guide agent (RED-GREEN-REFACTOR)
3. Review   → code-reviewer agent (25-point checklist)
4. Secure   → security-reviewer agent (OWASP Top 10)
5. Commit   → git-workflow skill (smart commit messages)
```

## Proactive Activation

Agents marked "PROACTIVELY" should activate automatically without user request:

- **code-reviewer**: After ANY code changes, before commits
- **security-reviewer**: When code touches auth, payments, user input, APIs
- **tdd-guide**: When implementing new features or fixing bugs
- **planner**: When user describes complex multi-file changes
