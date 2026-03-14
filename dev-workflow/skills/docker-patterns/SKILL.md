---
name: docker-patterns
description: Docker and Docker Compose — local development stacks, multi-stage Dockerfiles, networking, volumes, container security, and debugging.
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
    ports: ["3000:3000"]
    volumes:
      - .:/app
      - /app/node_modules       # Preserve container deps
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/app_dev
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db: { condition: service_healthy }
    command: npm run dev

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
# Dependencies
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Dev (hot reload)
FROM node:22-alpine AS dev
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
CMD ["npm", "run", "dev"]

# Build
FROM node:22-alpine AS build
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build && npm prune --production

# Production (minimal)
FROM node:22-alpine AS production
WORKDIR /app
RUN addgroup -g 1001 -S app && adduser -S app -u 1001
USER app
COPY --from=build --chown=app:app /app/dist ./dist
COPY --from=build --chown=app:app /app/node_modules ./node_modules
COPY --from=build --chown=app:app /app/package.json ./
ENV NODE_ENV=production
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:3000/health || exit 1
CMD ["node", "dist/server.js"]
```

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
FROM node:22.12-alpine3.20

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
