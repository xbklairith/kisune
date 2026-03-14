---
name: review
description: 25-point code quality checklist covering structure, errors, security, performance, and testing. Use before commits or when reviewing code.
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
- ✅ Check: Each function/class has one clear purpose
- ❌ Red Flag: Functions doing multiple unrelated things
- 💡 Suggestion: Split into focused, single-purpose functions

**DRY (Don't Repeat Yourself)**
- ✅ Check: No duplicated logic
- ❌ Red Flag: Copy-pasted code blocks
- 💡 Suggestion: Extract to shared function/utility

**Function Length**
- ✅ Check: Functions under 50 lines (prefer under 30)
- ❌ Red Flag: Functions over 100 lines
- 💡 Suggestion: Break into smaller, composable functions

**Naming Clarity**
- ✅ Check: Names clearly describe purpose
- ❌ Red Flag: Vague names (data, info, temp, x, y)
- 💡 Suggestion: Use descriptive, intention-revealing names

**Magic Numbers**
- ✅ Check: Constants are named
- ❌ Red Flag: Unexplained numbers in code
- 💡 Suggestion: Extract to named constants

### 2. Error Handling

**All Errors Caught**
- ✅ Check: Try-catch blocks around risky operations
- ❌ Red Flag: Unhandled promise rejections, missing error handling
- 💡 Suggestion: Add comprehensive error handling

**No Silent Failures**
- ✅ Check: Errors are logged or surfaced
- ❌ Red Flag: Empty catch blocks, ignored errors
- 💡 Suggestion: Log errors with context, alert user appropriately

**User-Friendly Error Messages**
- ✅ Check: Errors explain what went wrong and what to do
- ❌ Red Flag: Technical jargon exposed to users
- 💡 Suggestion: Translate technical errors to user language

**Logging for Debugging**
- ✅ Check: Appropriate logging at key points
- ❌ Red Flag: No logging or excessive logging
- 💡 Suggestion: Add structured logging with context

**Edge Cases Covered**
- ✅ Check: Boundary conditions handled (null, undefined, empty, zero)
- ❌ Red Flag: Assumptions about inputs
- 💡 Suggestion: Add defensive checks and validation

### 3. Security

**Input Validation**
- ✅ Check: All user inputs validated and sanitized
- ❌ Red Flag: Raw user input used directly
- 💡 Suggestion: Add validation with schema libraries (Zod, Joi, etc.)

**SQL Injection Prevention**
- ✅ Check: Parameterized queries or ORM used
- ❌ Red Flag: String concatenation in SQL
- 💡 Suggestion: Use prepared statements or ORM methods

**XSS Prevention**
- ✅ Check: HTML output escaped, CSP headers set
- ❌ Red Flag: innerHTML with user content
- 💡 Suggestion: Use textContent or framework's safe rendering

**Sensitive Data Handling**
- ✅ Check: Passwords hashed, PII encrypted, secure transmission
- ❌ Red Flag: Plain text secrets, sensitive data in logs
- 💡 Suggestion: Use bcrypt, encrypt at rest, sanitize logs

**Environment Variables for Secrets**
- ✅ Check: API keys, credentials in .env files
- ❌ Red Flag: Hardcoded credentials in code
- 💡 Suggestion: Move to environment variables, use secret managers

### 4. Performance

**No N+1 Queries**
- ✅ Check: Batch queries, eager loading used
- ❌ Red Flag: Query inside loop
- 💡 Suggestion: Use includes/joins, batch operations

**Appropriate Caching**
- ✅ Check: Expensive operations cached
- ❌ Red Flag: Repeated identical API calls or computations
- 💡 Suggestion: Add caching layer (Redis, in-memory, etc.)

**Database Indexes**
- ✅ Check: Indexed columns used in WHERE/JOIN clauses
- ❌ Red Flag: Full table scans on large tables
- 💡 Suggestion: Add indexes on frequently queried columns

**Unnecessary Computations**
- ✅ Check: Early returns, lazy evaluation
- ❌ Red Flag: Work done before checking preconditions
- 💡 Suggestion: Move expensive operations after validation

**Memory Leak Prevention**
- ✅ Check: Event listeners cleaned up, connections closed
- ❌ Red Flag: Growing arrays, unclosed connections
- 💡 Suggestion: Add cleanup in finally blocks, use weak references

### 5. Testing

**Tests Exist**
- ✅ Check: Tests cover new functionality
- ❌ Red Flag: No tests for new code
- 💡 Suggestion: Write tests for all new functions/components

**Edge Cases Tested**
- ✅ Check: Boundary conditions, null/undefined handled
- ❌ Red Flag: Only happy path tested
- 💡 Suggestion: Add tests for edge cases and error conditions

**Happy Path Tested**
- ✅ Check: Normal operation verified
- ❌ Red Flag: No positive test cases
- 💡 Suggestion: Add tests for expected behavior

**Error Conditions Tested**
- ✅ Check: Invalid inputs, failures handled
- ❌ Red Flag: Error paths not verified
- 💡 Suggestion: Add tests for error scenarios

**Tests Are Maintainable**
- ✅ Check: Clear test names, minimal duplication
- ❌ Red Flag: Complex test setup, brittle assertions
- 💡 Suggestion: Extract test helpers, use clear assertions

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

> 🗣 Say: "This code has architectural issues. Let me ultrathink whether refactoring or redesign is needed."

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

### ✅ Strengths

[List what's done well - be specific and encouraging]
- Clear function naming in authentication module
- Comprehensive error handling for API calls
- Good test coverage (87%)

### ⚠️ Issues Found

#### Priority: High - Must Fix Before Merge
1. **[Issue Title]**
   - **Location:** `file.js:42`
   - **Problem:** [Specific description]
   - **Risk:** [What could go wrong]
   - **Fix:** [How to resolve]

#### Priority: Medium - Should Address
1. **[Issue Title]**
   - **Location:** `file.js:78`
   - **Problem:** [Description]
   - **Impact:** [Effect on code quality]
   - **Suggestion:** [Improvement approach]

#### Priority: Low - Consider Improving
1. **[Issue Title]**
   - **Location:** `file.js:120`
   - **Note:** [Observation]
   - **Enhancement:** [Optional improvement]

### 💡 Refactoring Suggestions

#### Suggestion 1: [Title]
**Current Code:**
```javascript
// Show problematic code
```

**Refactored Code:**
```javascript
// Show improved version
```

**Benefits:**
- [Benefit 1]
- [Benefit 2]

#### Suggestion 2: [Title]
[Similar format]

### 📊 Code Metrics

- **Complexity:** [Low/Medium/High]
- **Test Coverage:** [X%]
- **Maintainability:** [A/B/C/D/F]
- **Lines of Code:** [N]
- **Duplicated Code:** [X%]

### 🎯 Action Items

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

**Assistant:**
```
Activating review skill for pre-commit review.

Running: git diff --cached

Found changes in:
- src/auth/login.js
- src/auth/session.js
- tests/auth/login.test.js

Performing comprehensive review...

## Code Review: Authentication Changes

### ✅ Strengths
- Comprehensive test coverage for login flow
- Clear separation of concerns between login and session
- Good use of async/await for API calls

### ⚠️ Issues Found

#### Priority: High - Must Fix Before Merge
1. **Missing Input Validation**
   - **Location:** `src/auth/login.js:23`
   - **Problem:** Email and password not validated before API call
   - **Risk:** Invalid inputs could crash backend or expose security issue
   - **Fix:** Add validation with Zod schema

**Current Code:**
```javascript
const login = async (email, password) => {
  const response = await api.post('/auth/login', { email, password });
  return response.data;
};
```

**Suggested Fix:**
```javascript
import { z } from 'zod';

const loginSchema = z.object({
  email: z.string().email('Invalid email format'),
  password: z.string().min(8, 'Password must be at least 8 characters')
});

const login = async (email, password) => {
  // Validate inputs
  const validated = loginSchema.parse({ email, password });

  const response = await api.post('/auth/login', validated);
  return response.data;
};
```

#### Priority: Medium - Should Address
1. **Missing Error Handling**
   - **Location:** `src/auth/login.js:23`
   - **Problem:** No try-catch for API call
   - **Impact:** Unhandled promise rejections
   - **Suggestion:** Add error handling with user-friendly messages

[...continues with full review...]

**Overall Assessment:** Good implementation with solid test coverage, but needs input validation and error handling before commit.

**Recommendation:** Request Changes - Fix high-priority issues before committing.

[Confidence: 0.9]
```

### Example 2: Refactoring Request

**User:** "Can you suggest improvements for src/utils/calculator.js?"

**Assistant:**
```
Activating review skill for refactoring analysis.

Reading: src/utils/calculator.js

Analyzing code structure and quality...

## Code Review: Calculator Utility

### ✅ Strengths
- Pure functions, no side effects
- Good mathematical accuracy

### 💡 Refactoring Suggestions

#### Suggestion 1: Extract Magic Numbers
**Current Code:**
```javascript
function calculateFee(amount) {
  return amount * 0.029 + 0.30;
}
```

**Refactored Code:**
```javascript
const STRIPE_PERCENTAGE_FEE = 0.029;
const STRIPE_FIXED_FEE = 0.30;

function calculateFee(amount) {
  return amount * STRIPE_PERCENTAGE_FEE + STRIPE_FIXED_FEE;
}
```

**Benefits:**
- Self-documenting code
- Easier to update fees
- Clearer business logic

#### Suggestion 2: Add Input Validation
**Current Code:**
```javascript
function calculateFee(amount) {
  return amount * 0.029 + 0.30;
}
```

**Refactored Code:**
```javascript
function calculateFee(amount) {
  if (typeof amount !== 'number' || amount < 0) {
    throw new Error('Amount must be a non-negative number');
  }
  return amount * STRIPE_PERCENTAGE_FEE + STRIPE_FIXED_FEE;
}
```

**Benefits:**
- Prevents calculation errors
- Fails fast with clear error
- Self-validating function

[...continues with more suggestions...]

Would you like me to apply these refactorings?

[Confidence: 0.9]
```

## Integration Points

- Works with `spec-driven` skill during execution phase
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
