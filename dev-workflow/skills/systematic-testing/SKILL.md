---
name: systematic-testing
description: Systematic debugging framework and test generation patterns. Use when writing tests, debugging failures, or investigating bugs.
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

### 1. Test-Driven Development (TDD)

**For complete TDD workflow, use Skill tool to invoke: `dev-workflow:test-driven-development`**

```
Use Skill tool: Skill(skill: "dev-workflow:test-driven-development")
```

The `test-driven-development` skill provides full RED-GREEN-REFACTOR cycle, strict enforcement, anti-patterns, and verification checklists.

**Quick TDD Summary:**
1. **RED:** Write failing test first
2. **GREEN:** Write minimal code to pass
3. **REFACTOR:** Clean up while tests stay green

This skill focuses on test generation strategies and systematic debugging. For TDD methodology details, use the dedicated skill.

---

### 2. Test Generation

**Goal:** Generate comprehensive test suites covering all scenarios

### Test Categories

#### Normal Cases (Happy Path)
Test expected, typical usage with valid inputs and standard flows.

#### Edge Cases (Boundary Conditions)
Test limits and boundaries:
- Very small/large values
- Equal values where difference is expected
- Fractional results requiring rounding
- Empty collections, zero-length strings

#### Error Cases (Invalid Inputs)
Test error handling:
- Negative values, zero values
- Out-of-range parameters
- Null/nil/None inputs
- Invalid types

#### Integration Cases
Test component interactions: full request-response flows, token validation chains, cross-component data passing.

### Test Generation Template

```
suite "[Component/Function Name]":

    setup:    # Reset state, create test data
    teardown: # Clean up, reset mocks

    group "normal operation":
        test "should [expected behavior for typical input]"

    group "edge cases":
        test "should handle [boundary condition]"

    group "error handling":
        test "should reject [invalid input]":
            assert_raises(ExpectedError, invalid_call())

    group "integration":
        test "should work with [other component]"
```

---

## 3. Systematic Debugging Framework

**Goal:** Resolve bugs methodically, not through random trial-and-error

### Phase 1: Root Cause Investigation

1. **Reproduce Bug Consistently** - Document exact steps and reproducibility rate
2. **Identify Symptoms** - Visible errors, expected vs actual behavior
3. **Gather Evidence** - Error messages, stack traces, log entries, network requests, triggering inputs
4. **Form Initial Hypothesis** - State hypothesis, supporting evidence, and next step

### Phase 2: Pattern Analysis

Answer these questions:

1. **When does it fail?** - Specific inputs, users, timing, action sequences?
2. **When does it work?** - Any succeeding inputs, unaffected users, regression timing?
3. **What changed recently?**
   ```bash
   git log --since="2 days ago" --oneline
   git log -p path/to/file
   git bisect  # Find exact commit that introduced bug
   ```
4. **Environmental factors?** - Local vs production, platform-specific, load-related?

Document the pattern: list conditions under FAILS and WORKS to identify the discriminator.

### Phase 3: Hypothesis Testing

1. **Create minimal test case** isolating the bug
2. **Add instrumentation** (logging) to trace execution
3. **Test hypothesis** - Confirm or reject with evidence
4. **Iterate** until root cause is found

### Phase 4: Fix and Protect

1. **Write test reproducing the bug** - Verify it fails before fix
2. **Fix the root cause** - Not just symptoms
3. **Verify test passes** after fix
4. **Add regression tests** for similar edge cases
5. **Document root cause** - What, why, and how it was fixed
6. **Commit with context** - Reference issue numbers, explain the why

---

## Test Coverage Analysis

**Check Coverage:** Run your project's test coverage command (e.g., `--coverage` flag, coverage plugin, or dedicated tool).

**Prioritize coverage gaps by:**
1. Critical business logic (highest priority)
2. Security-sensitive code
3. Complex algorithms
4. Error handling paths
5. Edge cases

## Best Practices

### TDD
1. Always write test first - no exceptions
2. One test at a time - don't batch before implementing
3. Smallest possible step - each cycle should be 5-10 minutes
4. Test behavior, not implementation - don't test private methods
5. Keep tests simple - tests should be easier to understand than code

### Test Quality
1. Clear test names that read like documentation
2. Arrange-Act-Assert structure consistently
3. One assertion per test for clear failures
4. No logic in tests - simple data only
5. Independent tests - no test depends on another

### Debugging
1. Reproduce first - can't fix what you can't reproduce
2. Understand before fixing - don't guess and check
3. Fix root cause - don't just treat symptoms
4. Add regression test - prevent bug from returning
5. Document why - help future debuggers

## Integration with Dev-Workflow

- **`dev-workflow:test-driven-development`** - Guided TDD workflow, enhanced RED-GREEN-REFACTOR
- **`dev-workflow:systematic-testing`** - Complex debugging, root cause tracing, advanced instrumentation

## Common Anti-Patterns to Avoid

- Writing tests after implementation
- Changing tests to match implementation
- Testing implementation details instead of behavior
- Skipping refactor phase
- Making multiple changes before testing
- Debugging by randomly changing code
- Committing debug logging code

## Discipline Mechanisms

### 3-Failures Architectural Gate

If three hypotheses about a bug have failed in a row, **the problem is not your next hypothesis — it's the architecture or your mental model**. Stop debugging. Question:

- Is the system actually structured the way I think?
- Are there hidden interactions I haven't traced?
- Am I solving the symptom or the cause?

> 🗣 Say: "Three hypotheses have failed. Stopping to question architecture before proposing a fourth."

Surface this to the user. Don't burn another round of guessing.

### Multi-Component Instrumentation Pattern

When a bug crosses component boundaries (e.g., Frontend → API → Worker → Database), don't add logs randomly. Use a layered template:

For each boundary:
1. Log the **input** entering the component (with a correlation ID)
2. Log the **output** leaving the component (same correlation ID)
3. Verify the output of one == input of the next

Example:
```
[req-abc123] Frontend → API: payload={...}
[req-abc123] API received: payload={...}
[req-abc123] API → Worker: job={...}
[req-abc123] Worker received: job={...}
```

When values diverge between layers, you've localized the bug.

### Partner Signals You're Off-Track

Watch for these phrases from the user — they indicate you're guessing or skipping evidence:

- **"Is that not happening?"** → you assumed a mechanism that may not exist
- **"Stop guessing"** → you've offered ≥2 hypotheses without evidence
- **"Will it show us X?"** → user is asking for the verification you should have proposed
- **"Why do you think that?"** → you stated a conclusion without grounding

When you hear these, immediately pause hypothesis generation and gather evidence (logs, code reads, test runs).

## Notes

- TDD is slower initially but faster overall (fewer bugs, less debugging)
- Good tests are documentation that never gets outdated
- Debugging is detective work, not guessing
- Always add regression tests after fixing bugs
- Test coverage is a minimum bar, not a goal
