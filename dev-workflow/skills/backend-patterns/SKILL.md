---
name: backend-patterns
description: Backend architecture patterns — repository/service layers, middleware, query optimization, caching, error handling, auth, and background jobs.
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

```typescript
interface UserRepository {
  findAll(filters?: UserFilters): Promise<User[]>
  findById(id: string): Promise<User | null>
  create(data: CreateUserDto): Promise<User>
  update(id: string, data: UpdateUserDto): Promise<User>
  delete(id: string): Promise<void>
}
```

## Service Layer Pattern

```typescript
class UserService {
  constructor(private userRepo: UserRepository) {}

  async createUser(data: CreateUserDto): Promise<User> {
    // Business logic: validate, transform, orchestrate
    const existing = await this.userRepo.findByEmail(data.email)
    if (existing) throw new ApiError(409, 'Email already registered')

    const hashedPassword = await hash(data.password)
    return this.userRepo.create({ ...data, password: hashedPassword })
  }
}
```

## N+1 Query Prevention

```typescript
// BAD: N+1 queries
const orders = await getOrders()
for (const order of orders) {
  order.user = await getUser(order.userId)  // N queries
}

// GOOD: Batch fetch
const orders = await getOrders()
const userIds = orders.map(o => o.userId)
const users = await getUsersByIds(userIds)  // 1 query
const userMap = new Map(users.map(u => [u.id, u]))
orders.forEach(o => { o.user = userMap.get(o.userId) })
```

## Caching (Cache-Aside)

```typescript
async function getUserWithCache(id: string): Promise<User> {
  const cached = await redis.get(`user:${id}`)
  if (cached) return JSON.parse(cached)

  const user = await db.users.findUnique({ where: { id } })
  if (!user) throw new ApiError(404, 'Not found')

  await redis.setex(`user:${id}`, 300, JSON.stringify(user))
  return user
}
```

## Error Handling

```typescript
class ApiError extends Error {
  constructor(public statusCode: number, public message: string) {
    super(message)
  }
}

function errorHandler(error: unknown): Response {
  if (error instanceof ApiError)
    return json({ error: error.message }, error.statusCode)

  if (error instanceof z.ZodError)
    return json({ error: 'Validation failed', details: error.errors }, 400)

  console.error('Unexpected:', error)
  return json({ error: 'Internal server error' }, 500)
}
```

## Retry with Exponential Backoff

```typescript
async function fetchWithRetry<T>(fn: () => Promise<T>, maxRetries = 3): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try { return await fn() }
    catch (error) {
      if (i === maxRetries - 1) throw error
      await new Promise(r => setTimeout(r, Math.pow(2, i) * 1000))
    }
  }
  throw new Error('Unreachable')
}
```

## Auth Patterns

```typescript
// JWT validation middleware
function requireAuth(handler) {
  return async (req, res) => {
    const token = req.headers.authorization?.replace('Bearer ', '')
    if (!token) return res.status(401).json({ error: 'Unauthorized' })
    try {
      req.user = jwt.verify(token, process.env.JWT_SECRET)
      return handler(req, res)
    } catch { return res.status(401).json({ error: 'Invalid token' }) }
  }
}

// RBAC
const rolePermissions = {
  admin: ['read', 'write', 'delete', 'admin'],
  moderator: ['read', 'write', 'delete'],
  user: ['read', 'write']
}
```

## Structured Logging

```typescript
const logger = {
  info: (msg, ctx) => console.log(JSON.stringify({
    timestamp: new Date().toISOString(), level: 'info', message: msg, ...ctx
  })),
  error: (msg, err, ctx) => console.log(JSON.stringify({
    timestamp: new Date().toISOString(), level: 'error', message: msg,
    error: err.message, stack: err.stack, ...ctx
  }))
}
```

## Key Principles

- Repository abstracts data access, Service contains business logic
- Validate at boundaries, trust internally
- Cache reads, invalidate on writes
- Batch queries to prevent N+1
- Structured JSON logging (never log PII)
- Retry with backoff for external calls
