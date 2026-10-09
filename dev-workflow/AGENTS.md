# Dev-Workflow Agents

## Core Principles

1. **Agent-First** — Delegate to specialized agents for quality
2. **Test-Driven** — 80%+ coverage required
3. **Plan Before Execute** — Use spec-driven planning for features

## Agent Registry

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| planner | Implementation planning | Multi-file features or complex refactoring whose architecture is settled |
| code-reviewer | Code quality review | PROACTIVELY after writing/modifying code |
| security-reviewer | Vulnerability detection | PROACTIVELY for auth, user input, APIs, sensitive data |
| tdd-guide | TDD enforcement | PROACTIVELY when writing features or fixing bugs |
| architect | System design and technical decisions | PROACTIVELY when a change needs a system-design or technology decision, scalability assessment, or comparison of architectural options |
| build-error-resolver | Build error resolution | PROACTIVELY when the build fails or type/compilation errors occur |
| database-reviewer | PostgreSQL/Supabase review | PROACTIVELY when writing SQL, creating migrations, designing schemas, or troubleshooting database performance |
| refactor-cleaner | Dead code cleanup | PROACTIVELY for removing unused code, duplicates, and refactoring |

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

- **code-reviewer**: After non-trivial code changes, before commits
- **security-reviewer**: When code touches auth, payments, user input, APIs
- **tdd-guide**: When implementing new features or fixing bugs
- **planner**: When user describes complex multi-file changes
