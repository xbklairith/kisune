---
name: deployment-patterns
description: CI/CD pipelines, deployment strategies (rolling, blue-green, canary), health checks, rollback strategies, and production readiness checklists.
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
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm test -- --coverage

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
PR: lint → typecheck → unit tests → integration tests → preview deploy
Main: lint → typecheck → tests → build image → staging → smoke tests → production
```

## Health Checks

```typescript
// Simple
app.get("/health", (req, res) => res.json({ status: "ok" }))

// Detailed (internal monitoring)
app.get("/health/detailed", async (req, res) => {
  const checks = {
    database: await checkDatabase(),
    redis: await checkRedis(),
  }
  const healthy = Object.values(checks).every(c => c.status === "ok")
  res.status(healthy ? 200 : 503).json({
    status: healthy ? "ok" : "degraded",
    version: process.env.APP_VERSION,
    uptime: process.uptime(),
    checks,
  })
})
```

## Environment Configuration

```typescript
// Validate at startup — fail fast
import { z } from "zod"
const envSchema = z.object({
  NODE_ENV: z.enum(["development", "staging", "production"]),
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
})
export const env = envSchema.parse(process.env)
```

## Rollback Strategy

```bash
kubectl rollout undo deployment/app      # Kubernetes
vercel rollback                          # Vercel
railway up --commit <previous-sha>       # Railway
```

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
