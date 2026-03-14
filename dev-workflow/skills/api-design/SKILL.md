---
name: api-design
description: REST API design patterns — resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs.
---

# API Design Patterns

Conventions and best practices for designing consistent, developer-friendly REST APIs.

## When to Activate

- Designing new API endpoints
- Reviewing existing API contracts
- Adding pagination, filtering, or sorting
- Implementing error handling for APIs
- Planning API versioning strategy

## Resource Design

### URL Structure

```
# Resources are nouns, plural, lowercase, kebab-case
GET    /api/v1/users
GET    /api/v1/users/:id
POST   /api/v1/users
PUT    /api/v1/users/:id
PATCH  /api/v1/users/:id
DELETE /api/v1/users/:id

# Sub-resources for relationships
GET    /api/v1/users/:id/orders
POST   /api/v1/users/:id/orders

# Actions that don't map to CRUD (use verbs sparingly)
POST   /api/v1/orders/:id/cancel
POST   /api/v1/auth/login
```

### Naming Rules

```
# GOOD
/api/v1/team-members          # kebab-case
/api/v1/orders?status=active  # query params for filtering
/api/v1/users/123/orders      # nested resources for ownership

# BAD
/api/v1/getUsers              # verb in URL
/api/v1/user                  # singular (use plural)
/api/v1/team_members          # snake_case in URLs
```

## HTTP Methods and Status Codes

| Method | Idempotent | Safe | Use For |
|--------|-----------|------|---------|
| GET | Yes | Yes | Retrieve resources |
| POST | No | No | Create resources, trigger actions |
| PUT | Yes | No | Full replacement |
| PATCH | No* | No | Partial update |
| DELETE | Yes | No | Remove a resource |

### Status Code Reference

```
# Success
200 OK                    — GET, PUT, PATCH (with body)
201 Created               — POST (include Location header)
204 No Content            — DELETE, PUT (no body)

# Client Errors
400 Bad Request           — Validation failure, malformed JSON
401 Unauthorized          — Missing or invalid authentication
403 Forbidden             — Authenticated but not authorized
404 Not Found             — Resource doesn't exist
409 Conflict              — Duplicate entry, state conflict
422 Unprocessable Entity  — Valid JSON, bad data
429 Too Many Requests     — Rate limit exceeded

# Server Errors
500 Internal Server Error — Never expose details
503 Service Unavailable   — Include Retry-After
```

## Response Format

### Success Response

```json
{
  "data": {
    "id": "abc-123",
    "email": "alice@example.com",
    "name": "Alice",
    "created_at": "2025-01-15T10:30:00Z"
  }
}
```

### Collection Response (with Pagination)

```json
{
  "data": [
    { "id": "abc-123", "name": "Alice" },
    { "id": "def-456", "name": "Bob" }
  ],
  "meta": {
    "total": 142,
    "page": 1,
    "per_page": 20,
    "total_pages": 8
  },
  "links": {
    "self": "/api/v1/users?page=1&per_page=20",
    "next": "/api/v1/users?page=2&per_page=20",
    "last": "/api/v1/users?page=8&per_page=20"
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "validation_error",
    "message": "Request validation failed",
    "details": [
      { "field": "email", "message": "Must be a valid email", "code": "invalid_format" },
      { "field": "age", "message": "Must be between 0 and 150", "code": "out_of_range" }
    ]
  }
}
```

## Pagination

### Offset-Based (Simple)

```
GET /api/v1/users?page=2&per_page=20
```

**Pros:** Easy, supports "jump to page N"
**Cons:** Slow on large offsets, inconsistent with concurrent inserts

### Cursor-Based (Scalable)

```
GET /api/v1/users?cursor=eyJpZCI6MTIzfQ&limit=20
```

**Pros:** Consistent performance, stable with concurrent inserts
**Cons:** Cannot jump to arbitrary page

| Use Case | Type |
|----------|------|
| Admin dashboards, small datasets (<10K) | Offset |
| Infinite scroll, feeds, large datasets | Cursor |
| Public APIs | Cursor (default) |
| Search results | Offset |

## Filtering, Sorting, and Search

```
# Simple equality
GET /api/v1/orders?status=active&customer_id=abc-123

# Comparison operators
GET /api/v1/products?price[gte]=10&price[lte]=100

# Multiple values
GET /api/v1/products?category=electronics,clothing

# Sorting (prefix - for descending)
GET /api/v1/products?sort=-created_at,price

# Full-text search
GET /api/v1/products?q=wireless+headphones

# Sparse fieldsets
GET /api/v1/users?fields=id,name,email
```

## Authentication and Rate Limiting

### Token-Based Auth

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
X-API-Key: sk_live_abc123  # server-to-server
```

### Rate Limit Headers

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
```

| Tier | Limit | Use Case |
|------|-------|----------|
| Anonymous | 30/min | Public endpoints |
| Authenticated | 100/min | Standard API |
| Premium | 1000/min | Paid plans |

## Versioning

```
# URL Path (recommended)
/api/v1/users
/api/v2/users

# Rules
- Start with /api/v1/ — don't version until needed
- Maintain at most 2 active versions
- Non-breaking: adding fields/endpoints (no new version)
- Breaking: removing/renaming fields (new version required)
```

## API Design Checklist

- [ ] Resource URL follows naming conventions (plural, kebab-case, no verbs)
- [ ] Correct HTTP method used
- [ ] Appropriate status codes (not 200 for everything)
- [ ] Input validated with schema (Zod, Pydantic, etc.)
- [ ] Error responses follow standard format
- [ ] Pagination on list endpoints
- [ ] Authentication required (or explicitly public)
- [ ] Authorization checked (user owns resource)
- [ ] Rate limiting configured
- [ ] No internal details leaked (stack traces, SQL errors)
- [ ] Consistent naming with existing endpoints
- [ ] Documented (OpenAPI/Swagger)
