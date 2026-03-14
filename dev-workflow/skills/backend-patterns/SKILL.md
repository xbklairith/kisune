---
name: backend-patterns
description: Backend architecture patterns — repository/service layers, middleware, query optimization, caching, error handling, and auth. Use when implementing backend services, fixing N+1 queries, or adding caching.
---

# Backend Development Patterns

Architecture patterns and best practices for scalable server-side applications.

## When to Activate

- Implementing repository, service, or controller layers
- Optimizing database queries (N+1, indexing)
- Adding caching (Redis, in-memory, HTTP cache)
- Setting up background jobs or async processing
- Building middleware (auth, logging, rate limiting)
- Structuring error handling for APIs

## Repository Pattern

Abstract data access behind a clean interface. The repository handles queries; callers never see SQL or ORM details.

```
interface UserRepository:
    find_all(filters) -> List[User]
    find_by_id(id) -> User | None
    create(data) -> User
    update(id, data) -> User
    delete(id) -> void
```

**Key rules:**
- One repository per aggregate root
- No business logic in repositories — only data access
- Return domain objects, not raw database rows
- Accept filter/sort/pagination parameters

## Service Layer Pattern

Business logic lives in services. Services orchestrate repositories and enforce domain rules.

```
class UserService:
    def __init__(user_repo, email_service):
        self.user_repo = user_repo
        self.email_service = email_service

    def create_user(data):
        # Business rule: check uniqueness
        existing = user_repo.find_by_email(data.email)
        if existing: raise ConflictError("Email already registered")

        # Business rule: hash password before storage
        data.password = hash(data.password)
        user = user_repo.create(data)

        # Side effect: send welcome email
        email_service.send_welcome(user.email)
        return user
```

**Key rules:**
- Services contain business logic, not controllers or repositories
- Services call repositories, never raw database queries
- One public method = one use case
- Inject dependencies (repositories, external services)

## N+1 Query Prevention

```
# BAD: N+1 queries (1 query + N queries in loop)
orders = get_orders()
for order in orders:
    order.user = get_user(order.user_id)  # N queries!

# GOOD: Batch fetch (2 queries total)
orders = get_orders()
user_ids = [o.user_id for o in orders]
users = get_users_by_ids(user_ids)        # 1 query
user_map = {u.id: u for u in users}
for order in orders:
    order.user = user_map[order.user_id]
```

**Detection:** Any database query inside a loop is likely N+1. Use eager loading, batch fetching, or data loaders.

## Caching (Cache-Aside)

```
def get_user_with_cache(id):
    # 1. Check cache first
    cached = cache.get("user:{id}")
    if cached: return deserialize(cached)

    # 2. Cache miss — fetch from database
    user = db.find_user(id)
    if not user: raise NotFoundError

    # 3. Populate cache with TTL
    cache.set("user:{id}", serialize(user), ttl=300)
    return user
```

**Invalidation strategies:**
- TTL-based (simplest, good for read-heavy data)
- Write-through (update cache on every write)
- Event-driven (invalidate on domain events)

## Error Handling

```
# Define domain-specific error hierarchy
class AppError(message, status_code)
class ValidationError(AppError)     # 400
class AuthError(AppError)           # 401
class ForbiddenError(AppError)      # 403
class NotFoundError(AppError)       # 404
class ConflictError(AppError)       # 409

# Centralized error handler (middleware)
def handle_error(error):
    if error is AppError:
        return response(error.message, error.status_code)
    if error is ValidationFrameworkError:
        return response("Validation failed", 400, details=error.details)
    # Unexpected error — log full details, return generic message
    log.error("Unexpected error", error)
    return response("Internal server error", 500)
```

**Rules:**
- Throw specific error types, catch in centralized handler
- Never expose internal details (stack traces, SQL) to clients
- Log unexpected errors with full context
- Validate at system boundaries, trust internally

## Retry with Exponential Backoff

```
def retry(operation, max_retries=3):
    for attempt in range(max_retries):
        try:
            return operation()
        except TransientError:
            if attempt == max_retries - 1: raise
            sleep(2^attempt * base_delay)  # 1s, 2s, 4s...
```

**Use for:** External API calls, message queue publishing, distributed locks. Never for database writes (may cause duplicates).

## Auth Middleware Pattern

```
# Authentication: verify identity
def require_auth(request):
    token = request.header("Authorization").remove_prefix("Bearer ")
    if not token: raise AuthError("Missing token")
    claims = verify_jwt(token)  # Verify signature, expiry, issuer
    request.user = claims
    return next(request)

# Authorization: verify permissions
def require_role(*allowed_roles):
    def middleware(request):
        if request.user.role not in allowed_roles:
            raise ForbiddenError("Insufficient permissions")
        return next(request)
    return middleware

# Role hierarchy
ROLE_PERMISSIONS = {
    "admin":     ["read", "write", "delete", "admin"],
    "moderator": ["read", "write", "delete"],
    "user":      ["read", "write"],
}
```

## Structured Logging

```
def log(level, message, context={}):
    entry = {
        "timestamp": now_iso8601(),
        "level": level,
        "message": message,
        "request_id": current_request_id(),
        **context,
    }
    write_json(entry)

# Usage
log("info", "User created", {"user_id": user.id, "email": user.email})
log("error", "Payment failed", {"order_id": order.id, "error": str(e)})
```

**Rules:**
- Always use structured (JSON) logging
- Include request/correlation IDs for tracing
- Never log PII, passwords, or tokens
- Use consistent log levels: debug, info, warn, error

## Key Principles

- Repository abstracts data access, Service contains business logic
- Validate at boundaries, trust internally
- Cache reads, invalidate on writes
- Batch queries to prevent N+1
- Structured JSON logging (never log PII)
- Retry with backoff for external calls
- Centralized error handling with specific error types
