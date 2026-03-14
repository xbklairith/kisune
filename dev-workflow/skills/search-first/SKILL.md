---
name: search-first
description: Research-before-coding workflow — search for existing tools, libraries, and patterns before writing custom code. Prevents reinventing the wheel.
---

# Search First — Research Before You Code

Systematizes the "search for existing solutions before implementing" workflow.

## When to Activate

- Starting a feature that likely has existing solutions
- Adding a dependency or integration
- Before creating a new utility, helper, or abstraction
- User asks "add X functionality" and you're about to write code

## Workflow

```
1. NEED ANALYSIS
   Define functionality needed + language/framework constraints

2. PARALLEL SEARCH
   - Package registries (npm, PyPI, crates.io)
   - Existing codebase (grep for similar patterns)
   - GitHub / web search
   - MCP servers and Claude Code skills

3. EVALUATE
   Score: functionality, maintenance, community, docs, license, deps

4. DECIDE
   Adopt | Extend/Wrap | Build Custom

5. IMPLEMENT
   Install package / Configure / Write minimal custom code
```

## Decision Matrix

| Signal | Action |
|--------|--------|
| Exact match, well-maintained, MIT/Apache | **Adopt** — install and use |
| Partial match, good foundation | **Extend** — install + thin wrapper |
| Multiple weak matches | **Compose** — combine 2-3 packages |
| Nothing suitable | **Build** — write custom, informed by research |

## Quick Checklist

Before writing a utility:

0. Does this already exist in the repo? (`rg` through modules)
1. Is this a common problem? (search npm/PyPI)
2. Is there a GitHub implementation? (code search)
3. Is there an MCP server for this?
4. Is there a Claude Code skill for this?

## Common Shortcuts

### Development Tooling
- Linting: `eslint`, `ruff`, `golangci-lint`
- Formatting: `prettier`, `black`, `gofmt`
- Testing: `jest`, `pytest`, `go test`
- Pre-commit: `husky`, `lint-staged`

### Data & APIs
- HTTP: `httpx` (Python), `ky`/`got` (Node)
- Validation: `zod` (TS), `pydantic` (Python)
- DB: Check for ORM/query builder first

### AI/LLM Integration
- Claude SDK for latest API patterns
- Document processing: `pdfplumber`, `mammoth`

## Anti-Patterns

- **Jumping to code** without checking if solution exists
- **Over-customizing** — wrapping a library so heavily it loses benefits
- **Dependency bloat** — installing massive package for one small feature
- **Ignoring internal code** — not checking if repo already has the utility

## Examples

### "Add dead link checking"
```
Need: Check markdown for broken links
Found: textlint-rule-no-dead-link
Action: ADOPT
Result: Zero custom code
```

### "Add HTTP client with retries"
```
Need: Resilient HTTP with retries + timeouts
Found: got (Node) with retry plugin
Action: ADOPT with config
Result: Zero custom code
```
