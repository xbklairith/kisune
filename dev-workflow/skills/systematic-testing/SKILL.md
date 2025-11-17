---
name: systematic-testing
description: Guide test-driven development, generate tests, and provide systematic debugging framework. Activates when writing tests, debugging issues, or investigating failures. Integrates with superpowers TDD and debugging skills if available.
version: 1.0.0
dependencies:
  - superpowers:test-driven-development (if available)
  - superpowers:systematic-debugging (if available)
---

# Systematic Testing Skill

## Purpose

Guide test-driven development (TDD), generate comprehensive test suites, and provide systematic debugging frameworks. Ensures code is well-tested and bugs are resolved methodically rather than through trial-and-error.

## Activation Triggers

Activate this skill when:
- User implements new functionality (auto-suggest tests)
- Tests fail (activate debugging framework)
- User says "write tests for this"
- User mentions "TDD" or "test-driven"
- User asks about debugging or troubleshooting
- User says "this bug..." or "error..."
- Before marking feature complete (verify test coverage)

## Core Capabilities

### 1. Test-Driven Development (RED-GREEN-REFACTOR)

**TDD Philosophy:**

Write the test BEFORE writing implementation code. This ensures:
- Tests actually verify behavior (not written to pass existing code)
- Code is testable by design
- Requirements are clear before coding
- Regression protection from day one

**The RED-GREEN-REFACTOR Cycle:**

```
┌─────────────────────────────────────┐
│  RED: Write Failing Test            │
│  - Define expected behavior         │
│  - Run test, verify it fails        │
│  - Commit test                      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  GREEN: Make Test Pass              │
│  - Write minimal implementation     │
│  - Run test, verify it passes       │
│  - Don't optimize yet               │
│  - Commit implementation            │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  REFACTOR: Improve Code             │
│  - Clean up implementation          │
│  - Remove duplication               │
│  - Improve naming                   │
│  - Run tests, verify still passing  │
│  - Commit refactor                  │
└──────────────┬──────────────────────┘
               │
               └──────> Repeat for next feature
```

### Phase 1: RED - Write Failing Test

**Goal:** Define expected behavior before implementation

**Process:**

1. **Understand Requirement**
   - What should this function/feature do?
   - What are the inputs and outputs?
   - What are the edge cases?

2. **Write Test Describing Behavior**
   ```javascript
   // Example: Testing a login function
   describe('login', () => {
     it('should return access token for valid credentials', async () => {
       // Arrange: Set up test data
       const email = 'user@example.com';
       const password = 'SecureP@ss123';

       // Act: Call the function
       const result = await login(email, password);

       // Assert: Verify expected behavior
       expect(result).toHaveProperty('accessToken');
       expect(result.accessToken).toBeTruthy();
       expect(result.user.email).toBe(email);
     });
   });
   ```

3. **Run Test - Verify Failure**
   ```bash
   npm test

   # Expected output:
   # ✗ should return access token for valid credentials
   #   ReferenceError: login is not defined
   ```

   **Important:** Test MUST fail for the right reason!
   - If function doesn't exist: "not defined" ✓
   - If function returns wrong value: assertion failure ✓
   - If test passes: Something is wrong! ✗

4. **Commit Test**
   ```bash
   git add tests/auth/login.test.js
   git commit -m "test: Add test for login with valid credentials"
   ```

### Phase 2: GREEN - Make Test Pass

**Goal:** Write minimal code to pass test

**Process:**

1. **Write Minimal Implementation**
   ```javascript
   // Simplest possible implementation
   async function login(email, password) {
     // TODO: Add actual logic
     return {
       accessToken: 'fake-token',
       user: { email }
     };
   }
   ```

   Don't worry about:
   - Edge cases yet
   - Performance optimization
   - Perfect design
   - Additional features

   Focus only on: Make this ONE test pass

2. **Run Test - Verify Pass**
   ```bash
   npm test

   # Expected output:
   # ✓ should return access token for valid credentials
   ```

3. **Commit Implementation**
   ```bash
   git add src/auth/login.js
   git commit -m "feat: Implement basic login function"
   ```

**Anti-pattern to Avoid:**
Don't write implementation and tests simultaneously. Always test first!

### Phase 3: REFACTOR - Improve Code

**Goal:** Clean up code while maintaining passing tests

**Process:**

1. **Identify Improvements**
   - Duplicated code to extract
   - Unclear variable names
   - Complex logic to simplify
   - Magic numbers to name

2. **Refactor While Tests Pass**
   ```javascript
   // Before refactor
   async function login(email, password) {
     const user = await db.query('SELECT * FROM users WHERE email = $1', [email]);
     if (user && bcrypt.compareSync(password, user.password)) {
       const token = jwt.sign({ id: user.id }, 'secret', { expiresIn: '1h' });
       return { accessToken: token, user: { email: user.email } };
     }
     throw new Error('Invalid credentials');
   }

   // After refactor
   async function login(email, password) {
     const user = await findUserByEmail(email);
     await validatePassword(password, user.password);

     const accessToken = generateAccessToken(user.id);
     const userProfile = sanitizeUserProfile(user);

     return { accessToken, user: userProfile };
   }

   // Extracted helpers
   async function findUserByEmail(email) {
     const user = await db.query('SELECT * FROM users WHERE email = $1', [email]);
     if (!user) throw new Error('Invalid credentials');
     return user;
   }

   async function validatePassword(provided, hashed) {
     const isValid = await bcrypt.compare(provided, hashed);
     if (!isValid) throw new Error('Invalid credentials');
   }

   function generateAccessToken(userId) {
     return jwt.sign(
       { id: userId },
       process.env.JWT_SECRET,
       { expiresIn: JWT_EXPIRY }
     );
   }

   function sanitizeUserProfile(user) {
     return {
       id: user.id,
       email: user.email,
       name: user.name
       // Never include password hash!
     };
   }
   ```

3. **Run Tests After Each Change**
   ```bash
   # After each refactor step
   npm test

   # All tests must still pass
   # ✓ should return access token for valid credentials
   ```

4. **Commit Refactor**
   ```bash
   git add src/auth/login.js src/auth/helpers.js
   git commit -m "refactor: Extract login helper functions"
   ```

**Refactoring Rules:**
- Tests must pass before AND after refactor
- Only refactor when tests are green
- Make small changes and test frequently
- Don't add features during refactor

---

## 2. Test Generation

**Goal:** Generate comprehensive test suites covering all scenarios

### Test Categories

#### Normal Cases (Happy Path)

Test expected, typical usage:

```javascript
describe('calculatePositionSize', () => {
  it('should calculate correct position size for valid inputs', () => {
    const result = calculatePositionSize(
      10000,  // account balance
      0.02,   // 2% risk
      150.50, // entry price
      148.00  // stop loss
    );

    expect(result).toBe(80); // $200 risk / $2.50 per share
  });

  it('should handle large account balances', () => {
    const result = calculatePositionSize(
      1000000, // $1M account
      0.01,    // 1% risk
      100,
      99
    );

    expect(result).toBe(10000);
  });
});
```

#### Edge Cases (Boundary Conditions)

Test limits and boundaries:

```javascript
describe('calculatePositionSize - edge cases', () => {
  it('should handle very small risk percentage', () => {
    const result = calculatePositionSize(
      10000,
      0.001, // 0.1% risk
      100,
      99
    );

    expect(result).toBe(10); // $10 risk / $1 per share
  });

  it('should handle entry price equal to stop loss', () => {
    expect(() => {
      calculatePositionSize(10000, 0.02, 100, 100);
    }).toThrow('Entry price cannot equal stop loss');
  });

  it('should handle very small price differences', () => {
    const result = calculatePositionSize(
      10000,
      0.02,
      100.10,
      100.00
    );

    expect(result).toBe(2000); // $200 / $0.10
  });

  it('should round down fractional shares', () => {
    const result = calculatePositionSize(
      10000,
      0.02,
      150.75, // Creates fractional result
      148.00
    );

    // Should be whole number, not fractional
    expect(Number.isInteger(result)).toBe(true);
  });
});
```

#### Error Cases (Invalid Inputs)

Test error handling:

```javascript
describe('calculatePositionSize - error cases', () => {
  it('should reject negative account balance', () => {
    expect(() => {
      calculatePositionSize(-10000, 0.02, 100, 99);
    }).toThrow('Account balance must be positive');
  });

  it('should reject zero account balance', () => {
    expect(() => {
      calculatePositionSize(0, 0.02, 100, 99);
    }).toThrow('Account balance must be positive');
  });

  it('should reject risk percentage over 100%', () => {
    expect(() => {
      calculatePositionSize(10000, 1.5, 100, 99);
    }).toThrow('Risk percentage must be between 0 and 1');
  });

  it('should reject negative risk percentage', () => {
    expect(() => {
      calculatePositionSize(10000, -0.02, 100, 99);
    }).toThrow('Risk percentage must be between 0 and 1');
  });

  it('should handle null inputs gracefully', () => {
    expect(() => {
      calculatePositionSize(null, 0.02, 100, 99);
    }).toThrow();
  });

  it('should handle undefined inputs gracefully', () => {
    expect(() => {
      calculatePositionSize(undefined, 0.02, 100, 99);
    }).toThrow();
  });
});
```

#### Integration Cases

Test component interactions:

```javascript
describe('login flow - integration', () => {
  it('should complete full authentication flow', async () => {
    // Test entire flow from request to response
    const response = await request(app)
      .post('/api/auth/login')
      .send({
        email: 'user@example.com',
        password: 'SecureP@ss123'
      });

    // Verify response
    expect(response.status).toBe(200);
    expect(response.body.data.accessToken).toBeTruthy();

    // Verify token is valid
    const decoded = jwt.verify(
      response.body.data.accessToken,
      process.env.JWT_SECRET
    );
    expect(decoded.id).toBeTruthy();

    // Verify user can access protected route
    const protectedResponse = await request(app)
      .get('/api/user/profile')
      .set('Authorization', `Bearer ${response.body.data.accessToken}`);

    expect(protectedResponse.status).toBe(200);
  });

  it('should prevent access with expired token', async () => {
    // Create expired token
    const expiredToken = jwt.sign(
      { id: 'user-id' },
      process.env.JWT_SECRET,
      { expiresIn: '-1h' } // Already expired
    );

    // Attempt to access protected route
    const response = await request(app)
      .get('/api/user/profile')
      .set('Authorization', `Bearer ${expiredToken}`);

    expect(response.status).toBe(401);
    expect(response.body.error.code).toBe('TOKEN_EXPIRED');
  });
});
```

### Test Generation Template

```javascript
describe('[Component/Function Name]', () => {
  // Setup and teardown
  beforeEach(() => {
    // Reset state, create test data
  });

  afterEach(() => {
    // Clean up, reset mocks
  });

  // NORMAL CASES
  describe('normal operation', () => {
    it('should [expected behavior for typical input]', () => {
      // Test implementation
    });
  });

  // EDGE CASES
  describe('edge cases', () => {
    it('should handle [boundary condition]', () => {
      // Test implementation
    });
  });

  // ERROR CASES
  describe('error handling', () => {
    it('should reject [invalid input]', () => {
      expect(() => {
        // Call with invalid input
      }).toThrow('Expected error message');
    });
  });

  // INTEGRATION
  describe('integration', () => {
    it('should work with [other component]', () => {
      // Test interaction
    });
  });
});
```

---

## 3. Systematic Debugging Framework

**Goal:** Resolve bugs methodically, not through random trial-and-error

**Four-Phase Framework:**

### Phase 1: Root Cause Investigation

**Goal:** Understand exactly what's going wrong

**Process:**

1. **Reproduce Bug Consistently**
   ```
   Steps to reproduce:
   1. Navigate to login page
   2. Enter email: user@example.com
   3. Enter password: TestPass123
   4. Click submit
   5. Observe: Error message "Network request failed"

   Reproducibility: 10/10 attempts failed
   ```

2. **Identify Symptoms**
   - What's the visible error?
   - What error messages appear?
   - What's the expected vs actual behavior?

3. **Gather Evidence**
   ```bash
   # Check logs
   tail -f logs/app.log

   # Check network requests (browser dev tools)
   # Check console errors
   # Check server logs
   ```

   Collect:
   - Error messages (full text)
   - Stack traces
   - Log entries
   - Network requests/responses
   - Input values that trigger bug

4. **Form Initial Hypothesis**
   ```
   Hypothesis: API endpoint is returning 500 error instead of 400

   Evidence:
   - Console shows "Network request failed"
   - Server logs show 500 error at time of attempt
   - Database logs show constraint violation

   Next step: Check what's causing the 500
   ```

### Phase 2: Pattern Analysis

**Goal:** Identify when bug occurs and when it doesn't

**Questions to Answer:**

1. **When Does It Fail?**
   - Specific inputs?
   - Certain users?
   - Particular time of day?
   - After specific sequence of actions?

2. **When Does It Work?**
   - Any inputs that succeed?
   - Any users unaffected?
   - Worked before, broken now?

3. **What Changed Recently?**
   ```bash
   # Check recent commits
   git log --since="2 days ago" --oneline

   # Check what changed in specific file
   git log -p path/to/file.js

   # See when bug was introduced
   git bisect
   ```

4. **Environmental Factors?**
   - Works locally, fails in production?
   - Browser-specific?
   - Network conditions?
   - Load-related (works with 1 user, fails with 100)?

**Pattern Analysis Example:**
```
Bug Pattern Analysis:

FAILS when:
- Email contains + symbol (e.g., user+test@example.com)
- Password is exactly 8 characters
- User account was created after 2025-01-01

WORKS when:
- Email is standard format (user@example.com)
- Password is 9+ characters
- User account is older

Pattern identified: Email validation regex doesn't handle + symbol
```

### Phase 3: Hypothesis Testing

**Goal:** Test theories systematically until root cause found

**Process:**

1. **Create Minimal Test Case**
   ```javascript
   // Isolate the bug
   it('should accept email with plus symbol', () => {
     const email = 'user+test@example.com';
     const result = validateEmail(email);
     expect(result).toBe(true); // Currently fails
   });
   ```

2. **Add Instrumentation**
   ```javascript
   function validateEmail(email) {
     console.log('Input email:', email);

     const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
     const isValid = regex.test(email);

     console.log('Regex test result:', isValid);
     console.log('Regex used:', regex);

     return isValid;
   }
   ```

3. **Test Hypothesis**
   ```javascript
   // Hypothesis: Regex doesn't handle + symbol

   // Test with minimal input
   validateEmail('user+test@example.com');
   // Output:
   // Input email: user+test@example.com
   // Regex test result: true
   //
   // Hypothesis REJECTED: Regex accepts + symbol

   // Form new hypothesis: Something else is rejecting it

   // Check database constraint
   // Found: Database column has CHECK constraint excluding +
   // Hypothesis CONFIRMED!
   ```

4. **Iterate Until Root Cause Found**
   Keep forming and testing hypotheses until you identify exact cause.

### Phase 4: Implementation

**Goal:** Fix bug permanently with regression protection

**Process:**

1. **Write Test Reproducing Bug**
   ```javascript
   // This test should FAIL before fix
   it('should accept email with plus symbol', async () => {
     const email = 'user+test@example.com';
     const password = 'SecureP@ss123';

     const response = await request(app)
       .post('/api/auth/register')
       .send({ email, password });

     expect(response.status).toBe(201);
     expect(response.body.user.email).toBe(email);
   });
   ```

   Run test - verify it fails:
   ```bash
   npm test
   # ✗ should accept email with plus symbol
   #   Expected: 201, Received: 400
   ```

2. **Fix the Bug**
   ```sql
   -- Remove overly restrictive database constraint
   ALTER TABLE users DROP CONSTRAINT email_format_check;

   -- Or update to correct constraint
   ALTER TABLE users ADD CONSTRAINT email_format_check
     CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$');
   ```

3. **Verify Test Passes**
   ```bash
   npm test
   # ✓ should accept email with plus symbol
   ```

4. **Add Regression Tests**
   ```javascript
   // Add more tests for similar edge cases
   describe('email validation - special characters', () => {
     const validEmails = [
       'user+test@example.com',
       'user.name@example.com',
       'user_name@example.com',
       'user-name@example.com',
       'user123@example.com'
     ];

     validEmails.forEach(email => {
       it(`should accept ${email}`, async () => {
         const response = await request(app)
           .post('/api/auth/register')
           .send({ email, password: 'SecureP@ss123' });

         expect(response.status).toBe(201);
       });
     });
   });
   ```

5. **Document Root Cause**
   ```javascript
   /*
    * Bug Fix: Email validation now accepts RFC-compliant characters
    *
    * Root Cause:
    * Database CHECK constraint was too restrictive, excluding the + symbol
    * which is valid in email addresses per RFC 5322.
    *
    * Fix:
    * Updated CHECK constraint to use proper regex pattern matching RFC 5322.
    *
    * Date: 2025-01-17
    * Related Issue: #234
    */
   ```

6. **Commit Fix with Context**
   ```bash
   git add migrations/003_fix_email_constraint.sql
   git add tests/auth/register.test.js
   git commit -m "fix: Accept + symbol in email addresses

   Database CHECK constraint was rejecting valid emails containing
   the + symbol. Updated constraint to match RFC 5322 standard.

   Closes #234"
   ```

---

## Test Coverage Analysis

**Goal:** Identify untested code

**Check Coverage:**
```bash
# Generate coverage report
npm run test:coverage

# Typical output:
# File           | % Stmts | % Branch | % Funcs | % Lines |
# ---------------|---------|----------|---------|---------|
# src/auth.js    |   87.5  |    75.0  |  100.0  |   87.5  |
# src/orders.js  |   45.2  |    33.3  |   60.0  |   45.2  |
```

**Identify Gaps:**
- Functions without any tests
- Branches not covered (if statements, error paths)
- Edge cases not tested
- Integration paths missing

**Prioritize:**
1. Critical business logic (highest priority)
2. Security-sensitive code
3. Complex algorithms
4. Error handling paths
5. Edge cases

## Best Practices

### TDD Best Practices
1. **Always write test first**: No exceptions
2. **One test at a time**: Don't write multiple tests before implementing
3. **Smallest possible step**: Each cycle should be quick (5-10 minutes)
4. **Test behavior, not implementation**: Don't test private methods
5. **Keep tests simple**: Tests should be easier to understand than code

### Test Quality
1. **Clear test names**: Should read like documentation
2. **Arrange-Act-Assert**: Structure tests consistently
3. **One assertion per test**: Makes failures clear
4. **No logic in tests**: Tests should be simple data
5. **Independent tests**: No test depends on another

### Debugging Best Practices
1. **Reproduce first**: Can't fix what you can't reproduce
2. **Understand before fixing**: Don't guess and check
3. **Fix root cause**: Don't just treat symptoms
4. **Add regression test**: Prevent bug from returning
5. **Document why**: Help future debuggers

## Integration with Superpowers

**If `superpowers:test-driven-development` available:**
- Use for guided TDD workflow
- Enhanced RED-GREEN-REFACTOR cycle
- Additional TDD best practices

**If `superpowers:systematic-debugging` available:**
- Use for complex debugging scenarios
- Root cause tracing framework
- Advanced instrumentation guidance

## Common Anti-Patterns to Avoid

❌ Writing tests after implementation
❌ Changing tests to match implementation
❌ Testing implementation details instead of behavior
❌ Skipping refactor phase
❌ Testing code that's already tested (overwriting working tests)
❌ Making multiple changes before testing
❌ Debugging by randomly changing code
❌ Committing "console.log" debugging code

## Notes

- TDD is slower initially but faster overall (fewer bugs, less debugging)
- Good tests are documentation that never gets outdated
- Debugging is detective work, not guessing
- Always add regression tests after fixing bugs
- Test coverage is a minimum bar, not a goal
