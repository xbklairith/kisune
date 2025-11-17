---
name: git-workflow
description: Manage git operations with best practices - smart commits, branch management, PR creation, and deployment helpers. Activates during git operations or when user mentions commits, branches, or pull requests.
version: 1.0.0
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

1. **Analyze Changes**
   ```bash
   # Check what files changed
   git status

   # See actual changes
   git diff
   ```

2. **Understand Intent**
   - What was added, modified, or removed?
   - What problem does this solve?
   - What feature does this enable?

3. **Generate Commit Message**
   Follow this format:
   ```
   [type]: [concise description in present tense]
   ```

   **Commit Types:**
   - `feat` - New feature
   - `fix` - Bug fix
   - `refactor` - Code restructuring without behavior change
   - `test` - Adding or updating tests
   - `docs` - Documentation changes
   - `chore` - Maintenance tasks (deps, config, etc.)
   - `style` - Code formatting (no logic change)
   - `perf` - Performance improvements

   **Message Guidelines:**
   - Present tense, imperative mood ("Add" not "Added" or "Adds")
   - Concise but descriptive
   - Focus on WHAT and WHY, not HOW
   - Under 72 characters for first line
   - No period at the end

4. **Show and Confirm**
   Present the commit message to user:
   ```
   Proposed commit message:
   feat: Add JWT authentication with refresh tokens

   This will commit:
   - src/auth/jwt.js
   - src/auth/refresh.js
   - tests/auth/jwt.test.js

   Proceed with this commit?
   ```

5. **Execute and Verify**
   ```bash
   # Stage files if not already staged
   git add [files]

   # Commit with generated message
   git commit -m "feat: Add JWT authentication with refresh tokens"

   # Verify commit
   git log -1 --oneline
   ```

**Examples of Good Commit Messages:**
```
feat: Add RSI indicator to market analysis
fix: Handle division by zero in position sizing
refactor: Extract strategy validation into separate function
test: Add edge cases for order execution
docs: Update API documentation with new endpoints
chore: Update dependencies to latest versions
perf: Optimize database queries with indexes
```

**Examples of Bad Commit Messages (Avoid):**
```
updated files            ❌ Too vague
fixed bug               ❌ Which bug?
WIP                     ❌ Not descriptive
asdfgh                  ❌ Nonsense
Added new stuff         ❌ Past tense, vague
implemented feature     ❌ Past tense, which feature?
```

### 2. Branch Management

**Branch Naming Conventions:**

Follow this structure: `[type]/[description]`

**Branch Types:**
- `feature/[feature-name]` - New features
- `fix/[issue-description]` - Bug fixes
- `refactor/[component-name]` - Code restructuring
- `experiment/[idea-name]` - Experimental work
- `hotfix/[critical-issue]` - Urgent production fixes

**Examples:**
```
feature/user-authentication
fix/login-timeout-error
refactor/payment-processing
experiment/ml-price-prediction
hotfix/security-vulnerability
```

**Branch Operations:**

**Creating Branch:**
```bash
# Create and switch to new branch
git checkout -b feature/user-authentication

# Or with newer syntax
git switch -c feature/user-authentication
```

**Switching Branches:**
```bash
# Switch to existing branch
git checkout feature/user-authentication

# Or with newer syntax
git switch feature/user-authentication
```

**Listing Branches:**
```bash
# Local branches
git branch

# All branches (including remote)
git branch -a

# With last commit info
git branch -v
```

**Deleting Branches:**
```bash
# Delete local branch (safe - prevents deleting unmerged)
git branch -d feature/old-feature

# Force delete (use with caution)
git branch -D feature/abandoned-work

# Delete remote branch
git push origin --delete feature/old-feature
```

**Safety Warnings:**

Before dangerous operations, warn user:
```
⚠️ WARNING: You're about to push to main/master
This is generally discouraged. Consider:
1. Creating a feature branch
2. Opening a pull request for review

Proceed anyway? (yes/no)
```

### 3. Pull Request Creation

**Goal:** Create comprehensive PRs with clear context and checklists

**Process:**

1. **Analyze All Commits**
   ```bash
   # See all commits in this branch
   git log main..HEAD --oneline

   # See detailed changes
   git diff main...HEAD
   ```

2. **Review Changes**
   - What's the overall purpose?
   - What are the key changes?
   - Are there breaking changes?
   - What needs testing?

3. **Generate PR Description**
   Use this template:

   ```markdown
   ## Summary
   [Brief overview of what this PR does and why]

   ## Changes
   - [Key change 1]
   - [Key change 2]
   - [Key change 3]

   ## Type of Change
   - [ ] Bug fix (non-breaking change which fixes an issue)
   - [ ] New feature (non-breaking change which adds functionality)
   - [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests pass
   - [ ] Integration tests pass
   - [ ] Manual testing completed
   - [ ] Edge cases tested

   ## Code Quality
   - [ ] Code follows project style guidelines
   - [ ] Self-review completed
   - [ ] Comments added for complex logic
   - [ ] No console.log or debug code left
   - [ ] Documentation updated

   ## Screenshots (if applicable)
   [Add screenshots for UI changes]

   ## Related Issues
   Closes #[issue number]
   ```

4. **Create PR with gh CLI**
   ```bash
   # Create PR with title and body
   gh pr create --title "[Type]: Brief description" --body "$(cat <<'EOF'
   ## Summary
   [Description]

   ## Changes
   - [Change 1]
   - [Change 2]

   ## Testing
   - [ ] All tests pass
   EOF
   )"
   ```

5. **Return PR URL**
   ```
   ✅ Pull Request Created!

   URL: https://github.com/user/repo/pull/42
   Title: feat: Add user authentication system

   Next steps:
   - Request reviewers
   - Wait for CI/CD checks
   - Address review feedback
   ```

### 4. Safety Checks

**Pre-Commit Safety:**

Before allowing commit, check:

1. **No Secrets**
   ```bash
   # Look for potential secrets
   git diff --cached | grep -i "api_key\|secret\|password\|token"
   ```

   If found:
   ```
   ⚠️ SECURITY WARNING: Potential secrets detected!

   Found suspicious patterns:
   - API_KEY on line 23 of config.js

   DO NOT commit secrets to version control!

   Actions:
   1. Add to .gitignore
   2. Use environment variables
   3. Use secret management tools

   Abort commit? (yes/no)
   ```

2. **Tests Pass**
   ```bash
   # Run test suite
   npm test
   ```

   If tests fail:
   ```
   ⚠️ TEST FAILURE: Cannot commit with failing tests

   Failed tests:
   - auth.test.js: login should return token
   - auth.test.js: invalid password should reject

   Fix tests before committing.
   ```

3. **Large Commits Warning**
   If more than 10 files changed:
   ```
   ⚠️ LARGE COMMIT WARNING

   This commit changes 23 files.
   Consider breaking into smaller, focused commits:

   Example:
   1. Commit core logic changes
   2. Commit test updates
   3. Commit documentation

   Proceed with large commit anyway? (yes/no)
   ```

**Pre-Push Safety:**

Before pushing:

1. **Check Current Branch**
   ```bash
   git branch --show-current
   ```

   If on main/master:
   ```
   ⚠️ DANGER: You're on the main branch!

   Direct pushes to main are discouraged.
   Recommended workflow:
   1. Create feature branch
   2. Make changes
   3. Open pull request
   4. Merge after review

   Proceed with push to main? (yes/no)
   ```

2. **Force Push Warning**
   If user attempts `git push --force`:
   ```
   🚨 CRITICAL WARNING: Force push detected!

   Force push to main/master is DESTRUCTIVE and will:
   - Rewrite history for all collaborators
   - Potentially lose work from others
   - Break ongoing pull requests

   This should ONLY be done if you know exactly what you're doing.

   Branch: [branch-name]
   Target: origin/[branch-name]

   Type "I understand the risks" to proceed:
   ```

**Pre-Merge Safety:**

Before merging:

1. **Check for Conflicts**
   ```bash
   git merge --no-commit --no-ff [branch]
   git merge --abort
   ```

2. **Verify CI Status**
   ```bash
   gh pr checks
   ```

3. **Confirm Approvals**
   ```bash
   gh pr view --json reviews
   ```

## Workflow Examples

### Example 1: Standard Feature Development

**User:** "I've finished the authentication feature, let's commit"

**Assistant:**
```
Activating git-workflow skill for smart commit.

Analyzing changes...
$ git status
$ git diff

Changes detected:
- src/auth/login.js (new file, 150 lines)
- src/auth/session.js (new file, 80 lines)
- tests/auth/login.test.js (new file, 200 lines)
- package.json (modified, +2 dependencies)

Commit type: feat (new feature)

Proposed commit message:
feat: Add JWT authentication with session management

This includes:
- Login endpoint with JWT generation
- Session management with refresh tokens
- Comprehensive test coverage

Proceed with this commit? (yes/no)
```

**User:** "yes"

**Assistant:**
```
Running pre-commit checks...
✅ No secrets detected
✅ Tests passing (52/52)
✅ Linter clean

Committing...
$ git add src/auth tests/auth package.json
$ git commit -m "feat: Add JWT authentication with session management"

✅ Commit successful!

[feature/user-authentication a1b2c3d] feat: Add JWT authentication with session management
 4 files changed, 432 insertions(+)

Next steps:
- Push to remote: git push -u origin feature/user-authentication
- Create pull request

Would you like me to push and create a PR?

[Confidence: 0.9]
```

### Example 2: Creating Pull Request

**User:** "Create a PR for my authentication feature"

**Assistant:**
```
Activating git-workflow skill for PR creation.

Analyzing branch changes...
$ git log main..HEAD --oneline

Commits to include:
a1b2c3d feat: Add JWT authentication with session management
b2c3d4e test: Add edge cases for token expiration
c3d4e5f docs: Update API documentation for auth endpoints

$ git diff main...HEAD --stat

Files changed:
- src/auth/ (6 files, 430 additions)
- tests/auth/ (4 files, 350 additions)
- docs/api.md (45 additions)

Generating PR description...

## Summary
Implements JWT-based authentication system with session management and refresh token support. Provides secure user login, token validation, and automatic session renewal.

## Changes
- JWT token generation and validation
- Refresh token mechanism for extended sessions
- Session middleware for protected routes
- Comprehensive test suite with edge cases
- API documentation updates

## Type of Change
- [x] New feature (non-breaking change which adds functionality)

## Testing
- [x] Unit tests pass (52/52)
- [x] Integration tests pass (12/12)
- [x] Manual testing completed
- [x] Edge cases tested (token expiration, invalid tokens)

## Code Quality
- [x] Code follows project style guidelines
- [x] Self-review completed
- [x] Comments added for complex logic
- [x] No debug code left
- [x] Documentation updated

Creating PR...
$ gh pr create --title "feat: Add JWT authentication system" --body "[body]"

✅ Pull Request Created!

URL: https://github.com/user/repo/pull/42
Title: feat: Add JWT authentication system
Status: Open

Next steps:
1. Request reviewers: gh pr review --request @reviewer
2. Monitor CI checks: gh pr checks
3. Address feedback when reviews come in

[Confidence: 0.9]
```

### Example 3: Preventing Dangerous Operation

**User:** "Push my changes to main"

**Assistant:**
```
Activating git-workflow skill for safety check.

$ git branch --show-current
main

⚠️ DANGER: You're about to push directly to main!

This is generally discouraged because:
- No code review before merging
- Potential to break production
- No CI/CD verification gate
- Difficult to revert if issues arise

Recommended workflow:
1. Create feature branch: git checkout -b feature/your-feature
2. Push to feature branch: git push -u origin feature/your-feature
3. Create pull request: gh pr create
4. Get code review
5. Merge via PR after approval

Alternative: If this is your personal project and you're certain, you can:
- Ensure all tests pass first
- Review your own changes carefully
- Proceed with direct push

What would you like to do?
1. Create feature branch and PR (recommended)
2. Run tests then push to main (risky)
3. Cancel operation

[Confidence: 1.0]
```

## Integration Points

- Works with `code-quality` skill for pre-commit reviews
- Works with `spec-driven` skill for commit messages during execution
- Works with `systematic-testing` skill to verify tests before commit

## Best Practices

1. **Commit Often**: Small, frequent commits are better than large, infrequent ones
2. **One Concern Per Commit**: Each commit should represent one logical change
3. **Write Good Messages**: Future you will thank present you
4. **Review Before Push**: Always review your own changes first
5. **Use Branches**: Never work directly on main
6. **Create PRs**: Always use pull requests, even for solo projects
7. **Keep History Clean**: Use meaningful commits, not "WIP" or "fix"

## Notes

- Always prioritize safety over convenience
- Default to the safer option when in doubt
- Educate user on git best practices
- Prevent destructive operations with clear warnings
- Make it easy to do the right thing
