---
description: Trigger comprehensive code review with quality checks
---

Activate the `code-quality` skill to perform systematic code review using comprehensive checklist covering code structure, error handling, security, performance, and testing.

## Review Process

1. **Ask What to Review**
   Present options:
   - Current staged changes (`git diff --cached`)
   - Current unstaged changes (`git diff`)
   - Specific file or directory
   - Entire feature (all changes in current branch)
   - Recent commits

2. **Run Appropriate Command**
   ```bash
   # For staged changes
   git diff --cached

   # For unstaged changes
   git diff

   # For specific file
   # Read the file directly

   # For entire feature
   git diff main...HEAD
   ```

3. **Perform Comprehensive Review**
   Use checklist from `code-quality` skill:
   - Code Structure (SRP, DRY, function length, naming, magic numbers)
   - Error Handling (all errors caught, no silent failures, logging, edge cases)
   - Security (input validation, SQL injection, XSS, sensitive data, secrets)
   - Performance (N+1 queries, caching, indexes, unnecessary computations, memory leaks)
   - Testing (tests exist, edge cases tested, happy path tested, error conditions, maintainability)

4. **Generate Review Report**
   Format:
   ```markdown
   ## Code Review: [File/Feature Name]

   ### ✅ Strengths
   [What's done well]

   ### ⚠️ Issues Found

   #### Priority: High - Must Fix Before Merge
   [Critical issues with location, problem, risk, and fix]

   #### Priority: Medium - Should Address
   [Important improvements]

   #### Priority: Low - Consider Improving
   [Optional enhancements]

   ### 💡 Refactoring Suggestions
   [Specific improvements with before/after code examples]

   ### 📊 Code Metrics
   - Complexity: [Low/Medium/High]
   - Test Coverage: [X%]
   - Maintainability: [A/B/C/D/F]

   ### 🎯 Action Items
   - [ ] Fix high-priority issues
   - [ ] Address medium-priority items
   - [ ] Consider refactoring suggestions

   **Overall Assessment:** [Summary]
   **Recommendation:** [Approve/Request Changes/Reject]

   [Confidence: X.X]
   ```

5. **Suggest Next Steps**
   - If critical issues: Must fix before commit
   - If medium issues: Should address before merge
   - If low issues: Optional improvements
   - If clean: Ready to commit/merge

## Argument Handling

**If user provides file path as argument:**
```
/dev-workflow:review src/auth/login.js
```
→ Review that specific file directly

**If user provides directory as argument:**
```
/dev-workflow:review src/auth/
```
→ Review all files in that directory

**If user provides "." as argument:**
```
/dev-workflow:review .
```
→ Review all changes in current directory (recursive)

**If no argument provided:**
```
/dev-workflow:review
```
→ Ask user what to review (staged, unstaged, specific file, etc.)

## Examples

**Example 1: Review staged changes**
```
User: /dev-workflow:review