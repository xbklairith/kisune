---
name: documentation
description: Generate and maintain documentation - function docs, API specs, architecture diagrams, and code explanations. Activates when user requests documentation, explanations, or mentions docs/README.
version: 1.0.0
---

# Documentation Skill

## Purpose

Generate comprehensive, maintainable documentation including code docstrings, API specifications, architecture diagrams, README files, and clear code explanations. Makes code understandable for future developers (including future you).

## Activation Triggers

Activate this skill when:
- User says "document this"
- User asks "how does this work?"
- User asks "explain this code"
- User mentions "README", "docs", or "documentation"
- After completing a feature
- When API endpoints are created
- User says "write comments for this"
- User asks "what does this function do?"

## Documentation Types

### 1. Code Documentation (Docstrings)

**Goal:** Clear, comprehensive function/class documentation

**Python Example:**

```python
def calculate_position_size(
    account_balance: float,
    risk_percentage: float,
    entry_price: float,
    stop_loss: float
) -> float:
    """
    Calculate position size based on risk management rules.

    Determines the number of shares/contracts to buy based on the
    account size, acceptable risk percentage, and the distance between
    entry and stop loss. Uses fixed percentage risk per trade.

    Args:
        account_balance: Total account equity in dollars (e.g., 10000.00)
        risk_percentage: Percentage of account to risk (e.g., 0.02 for 2%)
        entry_price: Price at which to enter position (e.g., 150.50)
        stop_loss: Price at which to exit if trade goes against us (e.g., 148.00)

    Returns:
        Number of shares/contracts to purchase, rounded down to nearest whole number.
        Returns 0 if inputs are invalid or calculation results in negative position.

    Example:
        >>> calculate_position_size(10000, 0.02, 150.50, 148.00)
        80.0

        This means: With $10k account, risking 2%, entry at $150.50, stop at $148.00,
        buy 80 shares. Risk per share is $2.50, total risk is $200 (2% of $10k).

    Raises:
        ValueError: If account_balance is negative or zero
        ValueError: If risk_percentage is not between 0 and 1
        ValueError: If entry_price equals stop_loss (no risk defined)

    Note:
        Always validates that entry_price > stop_loss for long positions.
        For short positions, use inverse logic externally before calling.
    """
    # Input validation
    if account_balance <= 0:
        raise ValueError("Account balance must be positive")
    if not 0 < risk_percentage < 1:
        raise ValueError("Risk percentage must be between 0 and 1")
    if entry_price == stop_loss:
        raise ValueError("Entry price cannot equal stop loss")

    # Calculate dollar amount to risk
    risk_amount = account_balance * risk_percentage

    # Calculate risk per share
    risk_per_share = abs(entry_price - stop_loss)

    # Calculate position size
    position_size = risk_amount / risk_per_share

    return int(position_size)  # Round down to whole shares
```

**JavaScript/TypeScript Example:**

```typescript
/**
 * Validates and sanitizes user input for authentication.
 *
 * Performs comprehensive validation of email and password inputs,
 * checking format requirements and sanitizing to prevent injection
 * attacks. Used before any authentication attempt.
 *
 * @param email - User's email address (must be valid format)
 * @param password - User's password (minimum 8 chars, must include uppercase,
 *                   lowercase, number, and special character)
 *
 * @returns Sanitized credentials object with trimmed, validated values
 *
 * @throws {ValidationError} If email format is invalid
 * @throws {ValidationError} If password doesn't meet requirements
 *
 * @example
 * ```typescript
 * const credentials = validateAuthInput(
 *   "user@example.com",
 *   "SecureP@ss123"
 * );
 * // Returns: { email: "user@example.com", password: "SecureP@ss123" }
 * ```
 *
 * @example
 * ```typescript
 * // Invalid email throws error
 * validateAuthInput("invalid-email", "SecureP@ss123");
 * // Throws: ValidationError: Invalid email format
 * ```
 */
function validateAuthInput(
  email: string,
  password: string
): { email: string; password: string } {
  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    throw new ValidationError("Invalid email format");
  }

  // Password validation
  if (password.length < 8) {
    throw new ValidationError("Password must be at least 8 characters");
  }

  const hasUpper = /[A-Z]/.test(password);
  const hasLower = /[a-z]/.test(password);
  const hasNumber = /[0-9]/.test(password);
  const hasSpecial = /[^A-Za-z0-9]/.test(password);

  if (!hasUpper || !hasLower || !hasNumber || !hasSpecial) {
    throw new ValidationError(
      "Password must include uppercase, lowercase, number, and special character"
    );
  }

  // Return sanitized (trimmed) values
  return {
    email: email.trim().toLowerCase(),
    password: password.trim()
  };
}
```

**Docstring Template:**

```
Brief one-line description.

Detailed explanation of purpose and behavior.
Multiple paragraphs if needed.

Args/Parameters:
    param1: Description with type info and examples
    param2: Description with constraints

Returns:
    Description of return value, including type and meaning

Example:
    >>> function_call(example_inputs)
    expected_output

    Explanation of example if needed.

Raises/Throws:
    ErrorType: When this error occurs

Note:
    Important implementation details
    Gotchas or edge cases
    Performance considerations
```

### 2. API Documentation

**Goal:** Complete API reference for endpoints

**REST API Example:**

```markdown
## Authentication API

### POST /api/auth/login

Authenticate user and return JWT access token.

**Request:**

```json
{
  "email": "user@example.com",
  "password": "SecureP@ss123"
}
```

**Request Schema:**
- `email` (string, required): Valid email address
- `password` (string, required): User password, min 8 characters

**Response (200 OK):**

```json
{
  "success": true,
  "data": {
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600,
    "user": {
      "id": "uuid-here",
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

**Response Schema:**
- `success` (boolean): Operation status
- `data.accessToken` (string): JWT access token (1 hour expiry)
- `data.refreshToken` (string): Refresh token (30 days expiry)
- `data.expiresIn` (number): Access token expiry in seconds
- `data.user` (object): User profile information

**Error Responses:**

**401 Unauthorized - Invalid Credentials:**
```json
{
  "success": false,
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Email or password is incorrect"
  }
}
```

**400 Bad Request - Validation Error:**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": {
      "field": "email",
      "value": "invalid-email"
    }
  }
}
```

**429 Too Many Requests - Rate Limited:**
```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many login attempts. Try again in 15 minutes.",
    "retryAfter": 900
  }
}
```

**Example Usage:**

```bash
# cURL
curl -X POST https://api.example.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"SecureP@ss123"}'

# JavaScript (fetch)
const response = await fetch('https://api.example.com/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'SecureP@ss123'
  })
});

const data = await response.json();
console.log(data.data.accessToken);
```

**Security Notes:**
- Always use HTTPS in production
- Passwords must never be logged
- Rate limiting: 5 attempts per 15 minutes per IP
- Access tokens expire in 1 hour
- Refresh tokens expire in 30 days
```

### 3. Architecture Documentation

**Goal:** Clear system overview and component relationships

**Example:**

```markdown
# System Architecture: Trading Platform

## Overview

High-performance trading platform built with microservices architecture,
supporting real-time market data, automated strategy execution, and
portfolio management.

## System Diagram

```
                           ┌──────────────┐
                           │   Frontend   │
                           │  (React SPA) │
                           └──────┬───────┘
                                  │
                                  │ HTTPS/WSS
                                  │
                    ┌─────────────▼──────────────┐
                    │     API Gateway            │
                    │   (Auth, Rate Limiting)    │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────┴──────────────┐
                    │                            │
         ┌──────────▼─────────┐      ┌──────────▼─────────┐
         │  Auth Service      │      │  Trading Service   │
         │  (JWT, Sessions)   │      │  (Orders, Trades)  │
         └──────────┬─────────┘      └──────────┬─────────┘
                    │                            │
                    │                            │
         ┌──────────▼─────────┐      ┌──────────▼─────────┐
         │  User Database     │      │  Trading Database  │
         │  (PostgreSQL)      │      │  (PostgreSQL)      │
         └────────────────────┘      └────────────────────┘
                                              │
                                     ┌────────▼─────────┐
                                     │  Market Data     │
                                     │  (WebSocket)     │
                                     └──────────────────┘
```

## Core Components

### 1. API Gateway
**Responsibility:** Entry point for all client requests

**Functions:**
- Request routing to appropriate service
- JWT token validation
- Rate limiting (100 req/min per user)
- Request/response logging
- CORS handling

**Technology:** Node.js + Express
**Scaling:** Horizontal (3+ instances behind load balancer)

### 2. Auth Service
**Responsibility:** User authentication and session management

**Functions:**
- User registration and login
- JWT token generation (access + refresh)
- Session management with Redis
- Password hashing with bcrypt
- OAuth integration (Google, GitHub)

**Technology:** Node.js + PostgreSQL + Redis
**Scaling:** Stateless, horizontal scaling

### 3. Trading Service
**Responsibility:** Order execution and portfolio management

**Functions:**
- Place/cancel orders
- Real-time position tracking
- P&L calculations
- Risk management checks
- Strategy execution

**Technology:** Node.js + PostgreSQL + WebSocket
**Scaling:** Horizontal with sticky sessions

## Data Flow

### Login Flow
1. User submits email/password to Frontend
2. Frontend sends POST /api/auth/login to API Gateway
3. API Gateway routes to Auth Service
4. Auth Service validates credentials against User Database
5. Auth Service generates JWT tokens
6. Tokens cached in Redis for fast validation
7. Tokens returned to Frontend
8. Frontend stores tokens in memory/localStorage

### Order Placement Flow
1. User creates order in Frontend
2. Frontend sends POST /api/orders with JWT
3. API Gateway validates JWT
4. Request routed to Trading Service
5. Trading Service validates order parameters
6. Trading Service checks account balance/positions
7. Trading Service applies risk management rules
8. Order saved to Trading Database
9. Order sent to market via Market Data service
10. Confirmation returned to Frontend
11. WebSocket update sent to Frontend with execution status

## Integration Points

### External Services
- **Alpaca API**: Market data and order execution
- **Redis Cloud**: Session caching (512MB)
- **Supabase**: Database hosting (PostgreSQL)
- **Vercel**: Frontend hosting and API routes

### Internal APIs
- Auth Service → Trading Service: User validation
- Trading Service → Market Data: Real-time prices
- All Services → API Gateway: Centralized routing

## Security Architecture

### Authentication
- JWT tokens with RS256 signing
- Access tokens: 1 hour expiry
- Refresh tokens: 30 days expiry
- Tokens stored in httpOnly cookies (production)

### Authorization
- Role-based access control (user, admin)
- Resource-level permissions
- API key authentication for service-to-service

### Data Protection
- All passwords hashed with bcrypt (cost 12)
- PII encrypted at rest (AES-256)
- TLS 1.3 for all external communication
- Database connection pooling with SSL

## Performance Considerations

### Caching Strategy
- Session tokens cached in Redis (1 hour TTL)
- Market data cached in memory (1 second TTL)
- User profiles cached (5 minute TTL)

### Database Optimization
- Indexes on frequently queried columns
- Connection pooling (max 20 connections)
- Read replicas for reporting queries

### Scaling Strategy
- Horizontal scaling for stateless services
- Vertical scaling for database
- CDN for static assets
- Background jobs for heavy computations

## Monitoring & Observability

### Metrics
- Request latency (p50, p95, p99)
- Error rates by endpoint
- Active user sessions
- Order execution time

### Logging
- Structured JSON logs
- Centralized logging (CloudWatch)
- Correlation IDs for request tracing

### Alerts
- High error rate (>1% for 5 minutes)
- Slow responses (>500ms p95)
- Database connection pool exhaustion
- Failed authentication attempts spike
```

### 4. README Generation

**Goal:** Comprehensive project README

**Template:**

```markdown
# [Project Name]

[Brief one-sentence description]

[Longer description explaining what problem this solves and why it's useful]

## Features

- 🚀 [Key feature 1]
- ⚡ [Key feature 2]
- 🔒 [Key feature 3]
- 📊 [Key feature 4]

## Demo

[Link to live demo or screenshot]

## Installation

### Prerequisites

- Node.js 18+ or Python 3.11+
- PostgreSQL 14+
- Redis 7+ (optional, for caching)

### Setup

```bash
# Clone repository
git clone https://github.com/user/repo.git
cd repo

# Install dependencies
npm install  # or pip install -r requirements.txt

# Copy environment variables
cp .env.example .env

# Edit .env with your values
# DATABASE_URL=postgresql://...
# JWT_SECRET=your-secret-key

# Run database migrations
npm run migrate  # or python manage.py migrate

# Start development server
npm run dev  # or python app.py
```

## Usage

### Basic Example

```javascript
// Example of main functionality
const result = await doSomething({
  param1: 'value',
  param2: 42
});

console.log(result);
```

### Advanced Example

```javascript
// More complex usage scenario
const advanced = await doAdvancedThing({
  config: {
    option1: true,
    option2: 'custom'
  }
});
```

## API Reference

### `functionName(param1, param2)`

Description of what this function does.

**Parameters:**
- `param1` (string): Description
- `param2` (number): Description

**Returns:** Description of return value

**Example:**
```javascript
const result = functionName('hello', 42);
```

[More API docs...]

## Configuration

Available environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DATABASE_URL` | PostgreSQL connection string | - | Yes |
| `JWT_SECRET` | Secret for JWT signing | - | Yes |
| `PORT` | Server port | 3000 | No |
| `NODE_ENV` | Environment (development/production) | development | No |

## Development

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- auth.test.js
```

### Code Style

This project uses:
- ESLint for linting
- Prettier for formatting
- Husky for pre-commit hooks

```bash
# Check linting
npm run lint

# Format code
npm run format
```

### Project Structure

```
project/
├── src/
│   ├── api/          # API routes
│   ├── services/     # Business logic
│   ├── models/       # Database models
│   └── utils/        # Utility functions
├── tests/            # Test files
├── docs/             # Documentation
└── scripts/          # Build/deploy scripts
```

## Deployment

### Production Build

```bash
# Build for production
npm run build

# Start production server
npm start
```

### Docker

```bash
# Build image
docker build -t project-name .

# Run container
docker run -p 3000:3000 --env-file .env project-name
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details

## Acknowledgments

- [Library/tool] for [functionality]
- [Person/project] for inspiration
```

### 5. Code Explanations

**Goal:** Clear explanations of complex code

**Process:**

1. **High-Level Purpose**
   - What problem does this solve?
   - Where does it fit in the system?

2. **Step-by-Step Logic**
   - Break down into phases
   - Explain each step clearly
   - Use analogies when helpful

3. **Key Algorithms/Patterns**
   - Identify important algorithms
   - Explain why this approach
   - Note time/space complexity

4. **Edge Cases**
   - What unusual inputs are handled?
   - What assumptions are made?
   - What validation is performed?

**Example Explanation:**

```markdown
## Explanation: Position Size Calculator

### Purpose
This function calculates how many shares to buy based on risk management
principles. It ensures that no single trade risks more than a specified
percentage of the account balance.

### How It Works

**Step 1: Validate Inputs**
First, we check that all inputs make sense:
- Account balance must be positive (can't trade with $0)
- Risk percentage must be between 0-100% (but really should be 1-5%)
- Entry price can't equal stop loss (would mean no risk defined)

**Step 2: Calculate Dollar Risk**
We determine how much money we're willing to lose:
```
risk_amount = account_balance * risk_percentage
```
Example: $10,000 account × 2% = $200 risk

**Step 3: Calculate Risk Per Share**
We figure out how much we'd lose per share if stopped out:
```
risk_per_share = |entry_price - stop_loss|
```
Example: |$150.50 - $148.00| = $2.50 per share

**Step 4: Calculate Position Size**
Divide total risk by per-share risk:
```
position_size = risk_amount / risk_per_share
```
Example: $200 ÷ $2.50 = 80 shares

### Why This Approach?

This is the "fixed percentage risk" method, which is standard in trading
because:
1. **Consistency**: Every trade risks the same percentage
2. **Scalability**: Works as account grows/shrinks
3. **Protection**: Limits damage from losing trades
4. **Simplicity**: Easy to understand and implement

### Edge Cases Handled

- **Entry equals stop**: Raises error (infinite position size)
- **Negative prices**: Absolute value prevents issues
- **Fractional shares**: Rounds down to whole shares
- **Zero risk**: Would cause division by zero, caught by validation

### Alternative Approaches

We could also use:
1. **Fixed dollar risk**: Risk same $ amount every trade (doesn't scale)
2. **Kelly Criterion**: Math-based optimal position (requires win rate data)
3. **Volatility-based**: Use ATR instead of stop distance (more complex)

We chose fixed percentage for simplicity and reliability.
```

## When to Document

**Always Document:**
- Public APIs and endpoints
- Complex algorithms
- Non-obvious logic
- Security-sensitive code
- Performance-critical sections
- Error handling strategies

**Consider Documenting:**
- Helper functions with multiple params
- Class constructors
- Configuration options
- Database schema

**Don't Bother Documenting:**
- Trivial getters/setters
- Self-explanatory code
- Temporary/experimental code

## Best Practices

1. **Write for Future You**: Assume you'll forget everything in 6 months
2. **Explain Why, Not What**: Code shows what, docs explain why
3. **Keep Examples Current**: Update examples when code changes
4. **Use Consistent Format**: Follow language conventions
5. **Be Concise**: Every word should add value
6. **Use Active Voice**: "Returns user" not "User is returned"
7. **Include Edge Cases**: Document unusual inputs and outputs
8. **Update With Code**: Outdated docs are worse than no docs

## Integration Points

- Works with `spec-driven` skill for feature documentation
- Works with `code-quality` skill to verify docs exist
- Auto-triggered after feature completion

## Notes

- Default to clear code over comments (code is always correct, comments lie)
- Good naming reduces need for documentation
- Complex logic deserves explanation
- APIs require comprehensive documentation
- When in doubt, document it
