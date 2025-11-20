---
name: brainstorming
description: Use when creating or developing features before writing code or implementation plans - refines rough ideas into fully-formed designs through collaborative questioning, alternative exploration, and incremental validation. Activates during design and planning phases.
allowed-tools: Read, Write, Glob, Grep
---

# Brainstorming Ideas Into Designs

## Overview

Help turn ideas into fully formed designs and specs through natural collaborative dialogue.

Start by understanding the current project context, then ask questions one at a time to refine the idea. Once you understand what you're building, present the design in small sections (200-300 words), checking after each section whether it looks right so far.

## When to Activate

Activate this skill when:
- User has a rough idea that needs refinement
- User is uncertain about scope or approach
- User says "I'm not sure what we need" or "I'm not sure how to approach this"
- During Phase 2 (Requirements) to explore WHAT to build
- During Phase 3 (Technical Design) to explore HOW to build it

**Phase 2 Focus (Requirements):**
- Clarifying what the feature should do
- Exploring different requirement scopes
- Understanding user needs and constraints
- Determining must-haves vs. nice-to-haves

**Phase 3 Focus (Design):**
- Exploring architectural approaches
- Comparing technical solutions
- Analyzing implementation trade-offs

## The Process

**Understanding the idea:**
- Check out the current project state first (files, docs, recent commits)
- Ask questions one at a time to refine the idea
- Prefer multiple choice questions when possible, but open-ended is fine too
- Only one question per message - if a topic needs more exploration, break it into multiple questions
- Focus on understanding: purpose, constraints, success criteria

**When to UltraThink:**
Before proposing architectural approaches, activate deep thinking if:
- Multiple valid solutions exist with significant trade-offs
- Decision has long-term architectural implications
- Requirements involve complex system interactions
- Security or performance are critical concerns

> 🗣 Say: "Let me ultrathink this before proposing approaches. I'll question fundamentals and consider implications from first principles."

**During UltraThink:**
- Question assumptions about requirements
- Consider second-order effects of each approach
- Think about what could go wrong (pre-mortem)
- Evaluate against similar systems you've seen
- Consider future maintainability and evolution

**After UltraThink:** Provide approaches with clear reasoning about trade-offs and long-term implications.

**Exploring approaches:**
- Propose 2-3 different approaches with trade-offs
- Present options conversationally with your recommendation and reasoning
- Lead with your recommended option and explain why
- Consider:
  - Complexity (Low/Medium/High)
  - Maintainability
  - Performance implications
  - Security considerations
  - Testability

**Presenting the design:**
- Once you believe you understand what you're building, present the design
- Break it into sections of 200-300 words
- Ask after each section whether it looks right so far
- Cover: architecture, components, data flow, error handling, testing
- Be ready to go back and clarify if something doesn't make sense

## After Brainstorming

**For Requirements (Phase 2):**
- Write validated requirements to `docx/features/[NN-feature-name]/requirements.md`
- Use EARS format (Event-Driven, State-Driven, Ubiquitous, Conditional, Optional)
- Include:
  - Overview
  - Functional requirements
  - Non-functional requirements (performance, security, usability)
  - Constraints
  - Acceptance criteria
  - Out of scope items
- Ask: "Requirements complete. Ready for design phase?"

**For Design (Phase 3):**
- Write the validated design to `docx/features/[NN-feature-name]/design.md`
- Include:
  - Architecture Overview
  - Component Structure
  - Data Flow
  - API Contracts
  - Error Handling Strategy
  - Security Considerations
  - Performance Considerations
  - Testing Strategy
- Ask: "Design complete. Ready for task breakdown?"

**Transition:**
- After requirements → Proceed to Phase 3 (Technical Design)
- After design → Transition to `spec-driven-implementation` skill for task breakdown

## Key Principles

- **One question at a time** - Don't overwhelm with multiple questions
- **Multiple choice preferred** - Easier to answer than open-ended when possible
- **YAGNI ruthlessly** - Remove unnecessary features from all designs
- **Explore alternatives** - Always propose 2-3 approaches before settling
- **Incremental validation** - Present design in sections, validate each
- **Be flexible** - Go back and clarify when something doesn't make sense
- **Think about testing** - Good designs are testable designs
- **Consider security** - Build security in, don't bolt it on later

## Example Questioning Flow

**Understanding Purpose:**
```
Q: "What's the primary goal of this authentication feature?"
→ User answers

Q: "Should it support multiple auth methods (email/password, OAuth, etc.)
   or just one method initially?"
→ User answers

Q: "What happens when a session expires - force re-login or offer refresh?"
→ User answers
```

**Exploring Approaches:**
```
Based on your requirements, I see 3 main approaches:

**Option A: JWT-Based Authentication** [RECOMMENDED]
Pros: Stateless, scalable, works across services, standard
Cons: Token invalidation complexity, larger payload
Complexity: Medium
Best for: Microservices, APIs, future scalability

**Option B: Session-Based Authentication**
Pros: Simple invalidation, smaller cookies, familiar
Cons: Requires session storage, scaling challenges
Complexity: Low
Best for: Monolithic apps, simple use cases

**Option C: Hybrid Approach**
Pros: Combines benefits of both
Cons: More complex, harder to maintain
Complexity: High
Best for: Complex enterprise requirements

I recommend Option A (JWT) because your requirements mention
potential API integrations and future mobile app support.
JWT is industry-standard for this use case.

Does this align with your thinking?
```

**Presenting Design Incrementally:**
```
Let me present the architecture in sections:

**Section 1: High-Level Flow**
[200-300 words describing auth flow]

Does this look right so far?
→ User validates or requests changes

**Section 2: Component Structure**
[200-300 words describing components]

How does this look?
→ Continue...
```

## Integration with Spec-Driven Workflow

This skill can be used in two phases:

**Phase 2 (Requirements):**
- Use when user has rough idea but unclear requirements
- Helps clarify what to build vs. what's out of scope
- Explores different feature scopes and priorities
- Outputs to `requirements.md` in EARS format

**Phase 3 (Technical Design):**
- Use after requirements are defined
- Helps explore how to build the feature
- Compares architectural approaches with trade-offs
- Outputs to `design.md` with complete technical specs

After brainstorming completes:
- Phase 2 → Proceed to Phase 3 (Technical Design)
- Phase 3 → Transition to `spec-driven-implementation` for task breakdown

## Notes

- **Phase 2:** Focus on "what" (what should system do? what's in/out of scope?)
- **Phase 3:** Focus on "how" (how should we build it? what are trade-offs?)
- Always present multiple options before recommending
- Validate incrementally - don't dump everything at once
- Be ready to backtrack if something doesn't make sense
- One question at a time - let user think and respond
- Good requirements lead to good designs
- Good designs enable good tests - think about testability
- Security and error handling are not afterthoughts
