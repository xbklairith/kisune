---
name: git-workflow
description: Smart git operations — commit messages, branch management, PR creation with summaries. Use for any git workflow.
allowed-tools: Bash, Read
---

# Git Workflow Skill

## Purpose

Manage git operations with best practices, generating meaningful commit messages, managing branches safely, creating comprehensive pull requests, and preventing common git mistakes.

## Activation Triggers

Activate this skill when:
- User says "commit my changes"
- User mentions "create a branch"
- User asks to "create a PR" or "pull request"
- User says "push to remote"
- Before any destructive git operation
- User mentions git or version control

## Core Capabilities

### 1. Smart Commits

**Goal:** Generate meaningful, consistent commit messages that explain WHY changes were made

**Process:**

1. **Analyze Changes** — Run `git status` and `git diff`
2. **Understand Intent** — What was added/modified/removed? What problem does this solve?
3. **Generate Commit Message** using format: `[type]: [concise description in present tense]`

**Commit Types:**
- `feat` or `feature` - New feature
- `fix` - Bug fix
- `refactor` - Code restructuring without behavior change
- `test` - Adding or updating tests
- `docs` - Documentation changes
- `chore` - Maintenance tasks (deps, config, etc.)
- `style` - Code formatting (no logic change)
- `perf` - Performance improvements

**Message Guidelines:**
- Present tense, imperative mood ("Add" not "Added")
- Focus on WHAT and WHY, not HOW
- Under 72 characters for first line
- No period at the end

**Good examples:**
```
feat: Add RSI indicator to market analysis
fix: Handle division by zero in position sizing
refactor: Extract strategy validation into separate function
```

**Avoid:** Vague messages ("updated files"), past tense ("Added new stuff"), or non-descriptive ("WIP", "asdfgh").

4. **Show and Confirm** — Present proposed message, list of files, and ask for approval
5. **Execute and Verify** — Stage files, commit, verify with `git log -1 --oneline`

### 2. Branch Management

**Naming Convention:** `[type]/[description]`

| Type | Purpose | Example |
|------|---------|---------|
| `feature/` | New features | `feature/user-authentication` |
| `fix/` | Bug fixes | `fix/login-timeout-error` |
| `refactor/` | Code restructuring | `refactor/payment-processing` |
| `experiment/` | Experimental work | `experiment/ml-price-prediction` |
| `hotfix/` | Urgent production fixes | `hotfix/security-vulnerability` |

**Key Operations:**
- Create: `git switch -c feature/name`
- Switch: `git switch feature/name`
- List: `git branch -v` (or `-a` for remote)
- Delete (safe): `git branch -d feature/old`
- Delete remote: `git push origin --delete feature/old`

**Safety:** Before pushing to main/master, warn the user and recommend creating a feature branch with a PR instead.

### 3. Pull Request Creation

**Process:**

1. **Analyze all commits:** `git log main..HEAD --oneline` and `git diff main...HEAD`
2. **Review changes** — overall purpose, key changes, breaking changes, testing needs
3. **Generate PR description** using this template:

```markdown
## Summary
[Brief overview of what this PR does and why]

## Changes
- [Key change 1]
- [Key change 2]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Code Quality
- [ ] Follows project style guidelines
- [ ] Self-review completed
- [ ] No debug code left
- [ ] Documentation updated

## Related Issues
Closes #[issue number]
```

4. **Create PR:** Use `gh pr create --title "[Type]: Brief description" --body "..."`
5. **Return PR URL** with next steps (request reviewers, monitor CI, address feedback)

### 4. Safety Checks

**Pre-Commit:**

1. **No Secrets** — Scan staged changes for `api_key`, `secret`, `password`, `token`. If found, warn and recommend `.gitignore` or environment variables. Abort by default.
2. **Tests Pass** — Run test suite. Block commit if tests fail.
3. **Large Commit Warning** — If 10+ files changed, suggest breaking into smaller commits.

**Pre-Push:**

1. **Branch Check** — If on main/master, warn and recommend feature branch + PR workflow.
2. **Force Push Warning** — If `--force` detected, issue critical warning about history rewriting, lost work, and broken PRs. Require explicit confirmation.

**Pre-Merge:**

1. Check for conflicts: `git merge --no-commit --no-ff [branch]` then `git merge --abort`
2. Verify CI status: `gh pr checks`
3. Confirm approvals: `gh pr view --json reviews`

## Workflow Example: Preventing Dangerous Operations

**User:** "Push my changes to main"

**Response:**
- Detect current branch is `main`
- Warn about risks: no code review, potential production breakage, no CI gate
- Recommend: create feature branch, push there, create PR, get review
- Offer alternatives: (1) Create branch + PR, (2) Run tests then push, (3) Cancel

## Integration Points

- Works with `review` skill for pre-commit reviews
- Works with `spec-driven-implementation` skill for commit messages during execution
- Works with `systematic-testing` skill to verify tests before commit

## Best Practices

1. **Commit Often** — Small, frequent commits over large, infrequent ones
2. **One Concern Per Commit** — Each commit represents one logical change
3. **Write Good Messages** — Future you will thank present you
4. **Review Before Push** — Always review your own changes first
5. **Use Branches** — Never work directly on main
6. **Create PRs** — Always use pull requests, even for solo projects
7. **Keep History Clean** — Meaningful commits, not "WIP" or "fix"

## Notes

- Always prioritize safety over convenience
- Default to the safer option when in doubt
- Prevent destructive operations with clear warnings
- Make it easy to do the right thing
