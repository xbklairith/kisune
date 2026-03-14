---
name: e2e-testing
description: Playwright E2E testing — Page Object Model, configuration, flaky test strategies, and CI/CD integration. Use when writing, debugging, or configuring E2E tests.
---

# E2E Testing Patterns

Playwright patterns for stable, fast, and maintainable E2E test suites. Playwright supports multiple languages (TypeScript, Python, Java, .NET) — adapt examples to your project's language.

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
│   │   ├── login.spec.*
│   │   └── register.spec.*
│   └── features/
│       ├── browse.spec.*
│       └── search.spec.*
├── fixtures/
│   └── auth.*
└── playwright.config.*
```

## Page Object Model

Encapsulate page interactions in page objects for reusability and maintainability:

```
class ItemsPage:
    search_input = locator('[data-testid="search-input"]')
    item_cards   = locator('[data-testid="item-card"]')

    def goto():
        navigate('/items')
        wait_for_load()

    def search(query):
        search_input.fill(query)
        wait_for_response(url_contains('/api/search'))

    def get_item_count():
        return item_cards.count()
```

**Rules:**
- One page object per page or major component
- Page objects expose actions (search, login), not raw selectors
- Tests read like user stories: `items_page.search("widget")`
- Use `data-testid` attributes for stable selectors

## Configuration

Key configuration settings for any Playwright project:

```
config:
  test_dir: './tests/e2e'
  fully_parallel: true
  forbid_only: true (in CI)
  retries: 2 (in CI), 0 (locally)
  workers: 1 (in CI), auto (locally)
  base_url: from env or 'http://localhost:8080'
  trace: 'on-first-retry'
  screenshot: 'only-on-failure'
  video: 'retain-on-failure'
  web_server:
    command: '<dev-server-command>'
    url: 'http://localhost:8080'
    reuse_existing: true (locally)
```

## Flaky Test Patterns

### Common Causes and Fixes

```
# BAD: Assumes element is ready
page.click('[data-testid="button"]')

# GOOD: Auto-wait locator
page.locator('[data-testid="button"]').click()

# BAD: Arbitrary timeout
page.wait(5000)

# GOOD: Wait for specific condition
page.wait_for_response(url_contains('/api/data'))

# BAD: Click during animation
page.click('[data-testid="menu-item"]')

# GOOD: Wait for stability
locator('[data-testid="menu-item"]').wait_for(state='visible')
locator('[data-testid="menu-item"]').click()
```

### Quarantine Flaky Tests

Mark flaky tests as fixme with issue reference. Detect flakiness by running tests with `--repeat-each=10`.

## Artifacts

Capture screenshots for debugging:
- After key actions (login, form submission)
- Full-page screenshots for visual regression
- Component-level screenshots for specific elements

## CI/CD Integration

```yaml
- name: Install Playwright
  run: playwright install --with-deps
- name: Run E2E tests
  run: playwright test
- name: Upload report
  uses: actions/upload-artifact@v4
  if: always()
  with:
    name: playwright-report
    path: playwright-report/
    retention-days: 30
```
