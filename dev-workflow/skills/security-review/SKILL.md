---
name: security-review
description: OWASP Top 10 vulnerability detection. Use PROACTIVELY for code handling user input, auth, APIs, payments, or sensitive data.
allowed-tools: Read, Grep, Bash
---

# Security Review Skill

## When to Activate

- Code handles user input (forms, query params, request body)
- Authentication or authorization logic added/changed
- API endpoints created or modified
- Payment or financial logic implemented
- Sensitive data (PII, credentials, tokens) processed
- External API integrations added
- File upload or download functionality
- Before deploying to production

## Security Checklist

### 1. Secrets Management

**BAD:**
```
API_KEY = "sk-abc123def456"
db_url = "postgres://admin:password@prod-db:5432/app"
```

**GOOD:**
```
API_KEY = env("API_KEY")
db_url = env("DATABASE_URL")
```

**Verify:**
- [ ] No hardcoded API keys, passwords, or tokens in code
- [ ] Secrets loaded from environment variables or secret manager
- [ ] `.env` files listed in `.gitignore`
- [ ] No secrets leaked in logs, error messages, or stack traces
- [ ] Different secrets for dev/staging/prod

### 2. Input Validation

**BAD:**
```
def get_user(request):
    id = request.query("id")          # No validation
    db.query("SELECT * FROM users WHERE id = " + id)  # SQL injection!
```

**GOOD:**
```
def get_user(request):
    id = parse_int(request.query("id"))
    if id is None or id <= 0:
        return error_response(400, "Invalid ID")
    db.query("SELECT * FROM users WHERE id = $1", [id])  # Parameterized
```

**Verify:**
- [ ] All user input validated at system boundaries
- [ ] Type checking on all inputs
- [ ] Length and range limits enforced
- [ ] Allowlist approach over denylist
- [ ] File upload: type, size, and name validated

### 3. SQL Injection Prevention

**Verify:**
- [ ] Parameterized queries only (no string concatenation)
- [ ] ORM queries don't use raw SQL without parameters
- [ ] Database user follows least privilege principle
- [ ] No dynamic table/column names from user input

### 4. Authentication & Authorization

**Verify:**
- [ ] Passwords hashed with bcrypt/argon2 (never MD5/SHA1)
- [ ] Session tokens cryptographically random (min 128 bits)
- [ ] JWT validated: signature, expiry, issuer, audience
- [ ] Role-based access control on every protected endpoint
- [ ] Password reset tokens single-use and time-limited
- [ ] Account lockout after repeated failed attempts

### 5. XSS Prevention

**BAD:**
```
# Rendering raw user HTML without sanitization
render_html(user_comment)
```

**GOOD:**
```
# Sanitize before rendering, or render as plain text
render_html(sanitize(user_comment))
# Or better: render as plain text (no HTML interpretation)
render_text(user_comment)
```

**Verify:**
- [ ] User content HTML-escaped before rendering
- [ ] CSP headers configured and restrictive
- [ ] No dynamic code execution (eval, exec) with user input
- [ ] URL parameters sanitized before use

### 6. CSRF Protection

**Verify:**
- [ ] CSRF tokens on all state-changing requests
- [ ] `SameSite` cookie attribute set to `Strict` or `Lax`
- [ ] `Origin` header validated on API endpoints

### 7. Rate Limiting

**Verify:**
- [ ] Rate limits on authentication endpoints (login, register, reset)
- [ ] Rate limits on public API endpoints
- [ ] Progressive delays or account lockout on failures
- [ ] Rate limit headers returned to clients

### 8. Sensitive Data Exposure

**Verify:**
- [ ] PII encrypted at rest (database-level or field-level)
- [ ] HTTPS enforced (HSTS headers set)
- [ ] API responses don't leak internal fields (IDs, timestamps, stack traces)
- [ ] Minimal data collection — only collect what's needed
- [ ] Proper data retention and deletion policies

### 9. Dependency Security

**Verify:**
- [ ] No known vulnerable dependencies (run your language's audit tool)
- [ ] Dependencies pinned to specific versions
- [ ] Lock files committed to version control
- [ ] Regular dependency updates scheduled

## Pre-Deployment Checklist

- [ ] All security checklist items verified
- [ ] No `TODO: fix security` or `HACK` comments left
- [ ] Error pages don't expose stack traces in production
- [ ] Debug mode disabled in production config
- [ ] Logging doesn't include sensitive data
- [ ] CORS configured restrictively (not `*`)
- [ ] HTTP security headers set (X-Frame-Options, X-Content-Type-Options, etc.)
- [ ] Database migrations reviewed for data safety
- [ ] Backup and recovery tested

## Report Format

```markdown
## Security Review: [Component/Feature]

### Critical — Fix Immediately
[Vulnerabilities that could lead to data breach or system compromise]
- **Location:** `file:line`
- **Issue:** [Description]
- **Risk:** [Impact if exploited]
- **Fix:** [Specific remediation]

### High — Fix Before Deploy
[Issues that weaken security posture]

### Medium — Fix Soon
[Best practice violations]

### Recommendations
[Hardening suggestions]

**Overall Risk Level:** [Critical / High / Medium / Low]
```
