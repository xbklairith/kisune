---
name: docker-patterns
description: Docker and Docker Compose — multi-stage Dockerfiles, networking, volumes, container security, and debugging. Use when containerizing applications or configuring Docker Compose.
---

# Docker Patterns

Docker and Docker Compose best practices for containerized development.

## When to Activate

- Setting up Docker Compose for local development
- Designing multi-container architectures
- Reviewing Dockerfiles for security and size
- Troubleshooting container networking or volumes

## Docker Compose (Standard Web App)

```yaml
services:
  app:
    build: { context: ., target: dev }
    ports: ["8080:8080"]
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/app_dev
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db: { condition: service_healthy }

  db:
    image: postgres:16-alpine
    ports: ["5432:5432"]
    environment: { POSTGRES_USER: postgres, POSTGRES_PASSWORD: postgres, POSTGRES_DB: app_dev }
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]

volumes:
  pgdata:
```

## Multi-Stage Dockerfile

```dockerfile
# Stage 1: Dependencies
FROM <base-image> AS deps
WORKDIR /app
COPY <dependency-manifest> <lock-file> ./
RUN <install-dependencies>

# Stage 2: Dev (hot reload)
FROM <base-image> AS dev
WORKDIR /app
COPY --from=deps /app/<deps-dir> ./<deps-dir>
COPY . .
CMD ["<dev-command>"]

# Stage 3: Build
FROM <base-image> AS build
WORKDIR /app
COPY --from=deps /app/<deps-dir> ./<deps-dir>
COPY . .
RUN <build-command>

# Stage 4: Production (minimal)
FROM <minimal-base> AS production
WORKDIR /app
RUN addgroup -g 1001 -S app && adduser -S app -u 1001
USER app
COPY --from=build --chown=app:app /app/<build-output> ./<build-output>
HEALTHCHECK --interval=30s --timeout=3s CMD <health-check-command>
CMD ["<production-command>"]
```

**Key principles:**
- Each stage has a single purpose
- Production image contains only runtime artifacts
- Non-root user in production
- Health check included

## Container Security

```yaml
services:
  app:
    security_opt: [no-new-privileges:true]
    read_only: true
    tmpfs: [/tmp, /app/.cache]
    cap_drop: [ALL]
```

```dockerfile
# Use specific tags (never :latest)
FROM python:3.12-slim-bookworm

# Run as non-root
RUN addgroup -g 1001 -S app && adduser -S app -u 1001
USER app

# No secrets in image layers
```

## Networking

```yaml
# Services resolve by name
# app connects to db:5432, redis:6379

# Network isolation
services:
  frontend: { networks: [frontend-net] }
  api: { networks: [frontend-net, backend-net] }
  db: { networks: [backend-net] }  # Only reachable from api

# Host-only ports
  db: { ports: ["127.0.0.1:5432:5432"] }
```

## Debugging

```bash
docker compose logs -f app              # Follow logs
docker compose exec app sh              # Shell into container
docker compose exec db psql -U postgres # Connect to postgres
docker compose up --build               # Rebuild
docker compose down -v                  # Stop + remove volumes
docker stats                            # Resource usage
```

## Anti-Patterns

- Running as root
- Using `:latest` tags
- Storing data without volumes
- Secrets in docker-compose.yml or Dockerfile
- One giant container with all services
- Using compose in production without orchestration
