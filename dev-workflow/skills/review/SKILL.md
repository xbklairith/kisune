---
name: review
description: 25-point code quality checklist covering structure, errors, security, performance, and testing. Use before commits or when reviewing code.
allowed-tools: Bash, Read, Grep
---

# Code Quality Skill

## Purpose

Perform systematic code reviews, identify issues, suggest refactorings, and enforce best practices. Acts as an automated code reviewer catching problems before they reach production.

## Activation Triggers

Activate this skill when:
- User says "review this code"
- User asks "can this be improved?"
- User mentions "refactoring", "optimization", or "code smell"
- Before git commits (pre-commit review)
- After completing a feature
- User says "is this code good?"

## Comprehensive Review Checklist

### 1. Code Structure

**Single Responsibility Principle (SRP)**
- Check: Each function/class has one clear purpose
- Red Flag: Functions doing multiple unrelated things
- Fix: Split into focused, single-purpose functions

**DRY (Don't Repeat Yourself)**
- Check: No duplicated logic
- Red Flag: Copy-pasted code blocks
- Fix: Extract to shared function/utility

**Function Length**
- Check: Functions under 50 lines (prefer under 30)
- Red Flag: Functions over 100 lines
- Fix: Break into smaller, composable functions

**Naming Clarity**
- Check: Names clearly describe purpose
- Red Flag: Vague names (data, info, temp, x, y)
- Fix: Use descriptive, intention-revealing names

**Magic Numbers**
- Check: Constants are named
- Red Flag: Unexplained numbers in code
- Fix: Extract to named constants

### 2. Error Handling

**All Errors Caught**
- Check: Error handling around risky operations
- Red Flag: Unhandled exceptions, missing error handling
- Fix: Add comprehensive error handling

**No Silent Failures**
- Check: Errors are logged or surfaced
- Red Flag: Empty catch blocks, ignored errors
- Fix: Log errors with context, alert user appropriately

**User-Friendly Error Messages**
- Check: Errors explain what went wrong and what to do
- Red Flag: Technical jargon exposed to users
- Fix: Translate technical errors to user language

**Logging for Debugging**
- Check: Appropriate logging at key points
- Red Flag: No logging or excessive logging
- Fix: Add structured logging with context

**Edge Cases Covered**
- Check: Boundary conditions handled (null, empty, zero)
- Red Flag: Assumptions about inputs
- Fix: Add defensive checks and validation

### 3. Security

**Input Validation**
- Check: All user inputs validated and sanitized
- Red Flag: Raw user input used directly
- Fix: Add validation with schema validation library

**SQL Injection Prevention**
- Check: Parameterized queries or ORM used
- Red Flag: String concatenation in SQL
- Fix: Use prepared statements or ORM methods

**XSS Prevention**
- Check: HTML output escaped, CSP headers set
- Red Flag: Raw HTML rendering of user content
- Fix: Use safe rendering or sanitize before output

**Sensitive Data Handling**
- Check: Passwords hashed, PII encrypted, secure transmission
- Red Flag: Plain text secrets, sensitive data in logs
- Fix: Use bcrypt/argon2, encrypt at rest, sanitize logs

**Environment Variables for Secrets**
- Check: API keys, credentials in environment or secret manager
- Red Flag: Hardcoded credentials in code
- Fix: Move to environment variables, use secret managers

### 4. Performance

**No N+1 Queries**
- Check: Batch queries, eager loading used
- Red Flag: Query inside loop
- Fix: Use includes/joins, batch operations

**Appropriate Caching**
- Check: Expensive operations cached
- Red Flag: Repeated identical API calls or computations
- Fix: Add caching layer (Redis, in-memory, etc.)

**Database Indexes**
- Check: Indexed columns used in WHERE/JOIN clauses
- Red Flag: Full table scans on large tables
- Fix: Add indexes on frequently queried columns

**Unnecessary Computations**
- Check: Early returns, lazy evaluation
- Red Flag: Work done before checking preconditions
- Fix: Move expensive operations after validation

**Memory Leak Prevention**
- Check: Resources cleaned up, connections closed
- Red Flag: Growing collections, unclosed connections
- Fix: Add cleanup in finally blocks, use resource management patterns

### 5. Testing

**Tests Exist**
- Check: Tests cover new functionality
- Red Flag: No tests for new code
- Fix: Write tests for all new functions/components

**Edge Cases Tested**
- Check: Boundary conditions handled
- Red Flag: Only happy path tested
- Fix: Add tests for edge cases and error conditions

**Happy Path Tested**
- Check: Normal operation verified
- Red Flag: No positive test cases
- Fix: Add tests for expected behavior

**Error Conditions Tested**
- Check: Invalid inputs, failures handled
- Red Flag: Error paths not verified
- Fix: Add tests for error scenarios

**Tests Are Maintainable**
- Check: Clear test names, minimal duplication
- Red Flag: Complex test setup, brittle assertions
- Fix: Extract test helpers, use clear assertions

## Review Process

### Step 1: Determine Scope

Ask user what to review:
1. Current staged changes (`git diff --cached`)
2. Current unstaged changes (`git diff`)
3. Specific file or directory
4. Entire feature
5. Recent commits

### Step 2: Analyze Code

Run appropriate git diff or read files:
```bash
# For staged changes
git diff --cached

# For unstaged changes
git diff

# For specific file
Read file_path

# For feature
git diff main...HEAD
```

### Step 3: Apply Checklist

Systematically go through:
1. Code Structure (5 checks)
2. Error Handling (5 checks)
3. Security (5 checks)
4. Performance (5 checks)
5. Testing (5 checks)

**UltraThink Architectural Issues:**
If review reveals fundamental architectural problems, activate deep thinking:

> Say: "This code has architectural issues. Let me ultrathink whether refactoring or redesign is needed."

**When to UltraThink:**
- Code violates multiple principles (SRP, DRY, YAGNI)
- Tight coupling makes testing difficult
- Similar logic duplicated across multiple files
- Error handling is scattered and inconsistent
- Performance issues suggest wrong data structure/algorithm

**Question deeply:**
- Is this a symptom of wrong architecture?
- Would refactoring fix root cause or just move complexity?
- What would this look like if designed from scratch?
- What's preventing clean separation of concerns?
- Is the domain model wrong?

**After UltraThink:** Recommend tactical fixes (refactor) vs. strategic redesign with clear reasoning.

### Step 4: Generate Review Report

## Review Output Format

```markdown
## Code Review: [File/Feature Name]

### Strengths

[List what's done well - be specific and encouraging]
- Clear function naming in authentication module
- Comprehensive error handling for API calls
- Good test coverage (87%)

### Issues Found

#### Priority: High - Must Fix Before Merge
1. **[Issue Title]**
   - **Location:** `file:line`
   - **Problem:** [Specific description]
   - **Risk:** [What could go wrong]
   - **Fix:** [How to resolve]

#### Priority: Medium - Should Address
1. **[Issue Title]**
   - **Location:** `file:line`
   - **Problem:** [Description]
   - **Impact:** [Effect on code quality]
   - **Suggestion:** [Improvement approach]

#### Priority: Low - Consider Improving
1. **[Issue Title]**
   - **Location:** `file:line`
   - **Note:** [Observation]
   - **Enhancement:** [Optional improvement]

### Refactoring Suggestions

#### Suggestion 1: [Title]
**Current Code:**
[Show problematic pattern]

**Refactored Code:**
[Show improved version]

**Benefits:**
- [Benefit 1]
- [Benefit 2]

### Code Metrics

- **Complexity:** [Low/Medium/High]
- **Test Coverage:** [X%]
- **Maintainability:** [A/B/C/D/F]
- **Lines of Code:** [N]
- **Duplicated Code:** [X%]

### Action Items

- [ ] Fix high-priority issues
- [ ] Address medium-priority items
- [ ] Consider refactoring suggestions
- [ ] Add tests for uncovered paths
- [ ] Update documentation

---

**Overall Assessment:** [Summary statement]
**Recommendation:** [Approve/Request Changes/Reject]

[Confidence: X.X]
```

## Examples

### Example 1: Pre-Commit Review

**User:** "I'm about to commit, can you review my changes?"

**Process:**
1. Run `git diff --cached` to see staged changes
2. Identify changed files
3. Apply 25-point checklist
4. Generate report with priorities

Focus on: Input validation, error handling, security, and test coverage for new code.

### Example 2: Refactoring Request

**User:** "Can you suggest improvements for this module?"

**Process:**
1. Read the file(s)
2. Identify code smells: magic numbers, duplicated logic, long functions
3. Propose specific refactorings with before/after pseudocode
4. Explain benefits of each change

Focus on: Named constants, extracted functions, input validation, and cleaner error handling.

## Integration Points

- Works with `spec-driven-implementation` skill during execution phase
- Works with `git-workflow` skill for pre-commit reviews
- Works with `systematic-testing` skill to verify test quality
- Triggered automatically before commits if integrated

## Notes

- Be thorough but constructive
- Prioritize issues appropriately
- Always provide specific code examples
- Explain WHY something is an issue, not just WHAT
- Offer concrete solutions, not just criticism
- Balance between perfectionism and pragmatism
- Focus on high-impact improvements
