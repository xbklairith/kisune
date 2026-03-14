---
name: deployment-patterns
description: CI/CD pipelines, deployment strategies (rolling, blue-green, canary), health checks, and rollback strategies. Use when setting up CI/CD or preparing production releases.
---

# Deployment Patterns

Production deployment workflows and CI/CD best practices.

## When to Activate

- Setting up CI/CD pipelines
- Planning deployment strategy
- Implementing health checks and readiness probes
- Preparing for a production release
- Configuring environment-specific settings

## Deployment Strategies

### Rolling (Default)
Replace instances gradually. Old and new run simultaneously.
- **Use when:** Standard deployments, backward-compatible changes
- **Requires:** Backward-compatible changes

### Blue-Green
Two identical environments. Switch traffic atomically.
- **Use when:** Critical services, zero-tolerance for issues
- **Benefit:** Instant rollback (switch back)

### Canary
Route small % of traffic to new version first.
- **Use when:** High-traffic services, risky changes
- **Pattern:** 5% → 50% → 100%

## CI/CD Pipeline

```yaml
# .github/workflows/ci.yml
name: CI/CD
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup language runtime
        # Use appropriate setup action for your language
      - name: Install dependencies
        run: <install-command>
      - name: Lint
        run: <lint-command>
      - name: Type check
        run: <typecheck-command>
      - name: Test with coverage
        run: <test-command>

  build:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        run: echo "Deploying ${{ github.sha }}"
```

### Pipeline Stages

```
PR:   lint → type check → unit tests → integration tests → preview deploy
Main: lint → type check → tests → build image → staging → smoke tests → production
```

## Health Checks

```
# Simple health endpoint
GET /health → { "status": "ok" }

# Detailed health (internal monitoring)
GET /health/detailed →
{
  "status": "ok" | "degraded",
  "version": "<app-version>",
  "uptime": <seconds>,
  "checks": {
    "database": { "status": "ok", "latency_ms": 2 },
    "cache":    { "status": "ok", "latency_ms": 1 }
  }
}
# Return 200 if healthy, 503 if degraded
```

## Environment Configuration

```
# Validate all required config at startup — fail fast
# Use your language's validation library (Pydantic, Zod, viper, etc.)

Required variables:
  APP_ENV:      "development" | "staging" | "production"
  PORT:         integer, default 8080
  DATABASE_URL: valid connection string
  JWT_SECRET:   string, minimum 32 characters
```

**Rules:**
- Validate at startup, crash immediately if invalid
- Never hardcode secrets — use environment variables or secret managers
- Different configs per environment (dev/staging/prod)

## Rollback Strategy

```bash
kubectl rollout undo deployment/app      # Kubernetes
# Or redeploy the previous container image tag
```

**Rules:**
- Always tag releases with git SHA or semantic version
- Keep previous 3 versions deployable
- Test rollback procedure before you need it

## Production Readiness Checklist

### Application
- [ ] All tests pass (unit, integration, E2E)
- [ ] No hardcoded secrets
- [ ] Error handling covers edge cases
- [ ] Structured logging (no PII)
- [ ] Health check endpoint works

### Infrastructure
- [ ] Docker image reproducible (pinned versions)
- [ ] Environment variables documented and validated
- [ ] Resource limits set (CPU, memory)
- [ ] SSL/TLS on all endpoints

### Monitoring
- [ ] Application metrics exported
- [ ] Alerts for error rate spikes
- [ ] Log aggregation set up
- [ ] Uptime monitoring on health endpoint

### Security
- [ ] Dependencies scanned for CVEs
- [ ] CORS configured restrictively
- [ ] Rate limiting on public endpoints
- [ ] Auth/authz verified
- [ ] Security headers set

### Operations
- [ ] Rollback plan tested
- [ ] Database migration tested against prod data
- [ ] Runbook for common failures
- [ ] On-call rotation defined
