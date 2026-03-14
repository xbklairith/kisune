---
name: documentation
description: Generate function docs, API specs, architecture diagrams (Mermaid), READMEs, and code explanations. Use when documenting code or APIs.
---

# Documentation Skill

## Purpose

Generate comprehensive, maintainable documentation including code docstrings, API specifications, architecture diagrams, README files, and clear code explanations.

## Activation Triggers

Activate this skill when:
- User says "document this", "explain this code", "how does this work?"
- User mentions "README", "docs", or "documentation"
- After completing a feature or creating API endpoints
- User says "write comments for this"

## Documentation Types

### 1. Code Documentation (Docstrings)

**Goal:** Clear, comprehensive function/class documentation

**Key Components:**
- **Brief description** (one line)
- **Detailed explanation** (purpose and behavior)
- **Args/Parameters** (types, constraints, examples)
- **Returns** (type and meaning)
- **Example** (realistic usage)
- **Raises/Throws** (error conditions)
- **Note** (implementation details)

**Language-Specific Formats:**
- **Python:** `"""triple quotes"""`, Args/Returns/Raises format
- **JavaScript/TypeScript:** JSDoc `/** */`, @param/@returns/@throws tags
- **Java:** Javadoc `/** */`, @param/@return/@throws tags
- **C#:** XML comments `/// <summary>`

### 2. API Documentation

**Goal:** Complete API reference for each endpoint

**Required sections per endpoint:**
- HTTP method and path
- Brief description
- Request schema (params, body with types and constraints)
- Success response (status code, schema, example)
- Error responses (status codes, error codes, messages)
- Example usage (cURL and/or language-specific)
- Security notes (auth, rate limits, etc.)

**Template:**

```markdown
### METHOD /api/path

Description of what this endpoint does.

**Request:**
- `field` (type, required/optional): Description

**Response (200 OK):**
- `field` (type): Description

**Errors:** 400 (validation), 401 (auth), 429 (rate limit)

**Security:** Auth required, rate limit X req/min
```

### 3. Architecture Documentation

**Goal:** Clear system overview and component relationships

**Required sections:**
- **Overview:** System purpose and architecture style
- **System Diagram:** ASCII or Mermaid diagram showing components and connections
- **Core Components:** For each component: responsibility, functions, technology, scaling strategy
- **Data Flow:** Step-by-step flows for key operations
- **Integration Points:** External services and internal APIs
- **Security Architecture:** Authentication, authorization, data protection
- **Performance:** Caching strategy, database optimization, scaling strategy
- **Monitoring:** Metrics, logging, alerts

### 4. README Generation

**Goal:** Comprehensive project README

**Essential Sections:**
1. **Title + one-line description** - What problem it solves
2. **Features** - Key features as bullet list
3. **Installation** - Clone, install, configure, run
4. **Usage** - Basic code example
5. **Configuration** - Environment variables table (Variable, Description, Required)
6. **Development** - Test, lint, build commands
7. **License**

**Optional Sections** (add as needed):
- Demo/screenshots, API Reference, Project Structure, Deployment, Contributing

### 5. Code Explanations

**Goal:** Clear explanations of complex code

**Process:**

1. **High-Level Purpose** - What problem does this solve? Where does it fit?
2. **Step-by-Step Logic** - Break down into phases, explain each clearly
3. **Key Algorithms/Patterns** - Identify algorithms, explain approach, note complexity
4. **Edge Cases** - Unusual inputs handled, assumptions made, validation performed

**Structure each explanation as:**
- Purpose (what and why)
- How It Works (numbered steps with formulas/logic)
- Why This Approach (rationale and alternatives considered)
- Edge Cases Handled (list with explanations)

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
- Works with `review` skill to verify docs exist
- Auto-triggered after feature completion

## Notes

- Default to clear code over comments (code is always correct, comments lie)
- Good naming reduces need for documentation
- Complex logic deserves explanation
- APIs require comprehensive documentation
- When in doubt, document it
