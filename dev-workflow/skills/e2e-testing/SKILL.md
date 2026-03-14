---
name: e2e-testing
description: Playwright E2E testing — Page Object Model, configuration, flaky test strategies, artifact management, and CI/CD integration.
---

# E2E Testing Patterns

Playwright patterns for stable, fast, and maintainable E2E test suites.

## When to Activate

- Setting up E2E testing infrastructure
- Writing Playwright tests for user flows
- Debugging flaky tests
- Configuring CI/CD for E2E tests

## File Organization

```
tests/
├── e2e/
│   ├── auth/
│   │   ├── login.spec.ts
│   │   └── register.spec.ts
│   └── features/
│       ├── browse.spec.ts
│       └── search.spec.ts
├── fixtures/
│   └── auth.ts
└── playwright.config.ts
```

## Page Object Model

```typescript
export class ItemsPage {
  readonly searchInput: Locator
  readonly itemCards: Locator

  constructor(private page: Page) {
    this.searchInput = page.locator('[data-testid="search-input"]')
    this.itemCards = page.locator('[data-testid="item-card"]')
  }

  async goto() {
    await this.page.goto('/items')
    await this.page.waitForLoadState('networkidle')
  }

  async search(query: string) {
    await this.searchInput.fill(query)
    await this.page.waitForResponse(r => r.url().includes('/api/search'))
  }

  async getItemCount() { return this.itemCards.count() }
}
```

## Playwright Configuration

```typescript
export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
})
```

## Flaky Test Patterns

### Common Causes and Fixes

```typescript
// BAD: Assumes element is ready
await page.click('[data-testid="button"]')

// GOOD: Auto-wait locator
await page.locator('[data-testid="button"]').click()

// BAD: Arbitrary timeout
await page.waitForTimeout(5000)

// GOOD: Wait for specific condition
await page.waitForResponse(r => r.url().includes('/api/data'))

// BAD: Click during animation
await page.click('[data-testid="menu-item"]')

// GOOD: Wait for stability
await page.locator('[data-testid="menu-item"]').waitFor({ state: 'visible' })
await page.locator('[data-testid="menu-item"]').click()
```

### Quarantine Flaky Tests

```typescript
test('flaky: complex flow', async ({ page }) => {
  test.fixme(true, 'Flaky - Issue #123')
})

// Detect flakiness
// npx playwright test tests/search.spec.ts --repeat-each=10
```

## Artifacts

```typescript
await page.screenshot({ path: 'artifacts/after-login.png' })
await page.screenshot({ path: 'artifacts/full-page.png', fullPage: true })
await page.locator('[data-testid="chart"]').screenshot({ path: 'artifacts/chart.png' })
```

## CI/CD Integration

```yaml
- run: npx playwright install --with-deps
- run: npx playwright test
- uses: actions/upload-artifact@v4
  if: always()
  with:
    name: playwright-report
    path: playwright-report/
    retention-days: 30
```
