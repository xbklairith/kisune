---
name: spec-driven-planning
description: Create feature structure, define requirements using EARS format, and generate technical design. Activates when user mentions feature planning, requirements gathering, specifications, design, architecture, or uses planning commands.
allowed-tools: Read, Write, Glob, Grep
---

# Spec-Driven Planning Skill

## Purpose

Guide feature planning through three structured phases: Feature Creation → Requirements (EARS) → Technical Design. This systematic approach ensures clear requirements and thoughtful design before implementation begins.

## Activation Triggers

Activate this skill when:
- User says "create a new feature"
- User mentions "requirements", "specifications", or "specs"
- User uses `/dev-workflow:spec` command with planning options
- User asks to plan or design a feature
- User says "I need to build [feature]"
- User mentions "architecture" or "technical design"

## Three-Phase Planning Workflow

### Phase 1: Feature Creation

**Goal:** Establish feature structure and placeholder files

**Process:**
1. Parse feature name from user input
2. Check existing features: `ls docx/features/`
3. Determine next number (NN) for feature directory
4. Create directory: `docx/features/[NN-feature-name]/`
5. Copy templates from plugin to feature directory:
   - requirements.md
   - design.md
   - tasks.md
6. Initialize placeholder content with feature name

**Output:**
```
Created feature: docx/features/[NN-feature-name]/
- requirements.md (from template)
- design.md (from template)
- tasks.md (from template)

Next step: Define requirements using EARS format
```

**User Confirmation:**
> "Feature structure created. Ready to define requirements?"

---

### Phase 2: Requirements Definition (EARS Format)

**Goal:** Capture clear, testable requirements using EARS methodology

**Brainstorming Integration (Optional):**
- If user has rough idea but unclear requirements, activate `brainstorming` skill
- Helps clarify what to build vs. what's out of scope
- Explores different feature scopes through collaborative questioning
- Determines must-haves vs. nice-to-haves

**EARS Format Explained:**

EARS (Easy Approach to Requirements Syntax) provides five templates for unambiguous requirements:

1. **Ubiquitous Requirements** - Always true
   - Template: "The system SHALL [requirement]"
   - Example: "The system SHALL validate all user inputs before processing"

2. **Event-Driven Requirements** - Triggered by events
   - Template: "WHEN [trigger] THEN the system SHALL [response]"
   - Example: "WHEN user clicks submit THEN the system SHALL validate form data"

3. **State-Driven Requirements** - Active during specific states
   - Template: "WHILE [state] the system SHALL [requirement]"
   - Example: "WHILE processing payment the system SHALL display loading indicator"

4. **Conditional Requirements** - Based on conditions
   - Template: "IF [condition] THEN the system SHALL [requirement]"
   - Example: "IF user role is admin THEN the system SHALL show management panel"

5. **Optional Requirements** - Feature toggles
   - Template: "WHERE [feature included] the system SHALL [requirement]"
   - Example: "WHERE premium subscription is active the system SHALL enable advanced analytics"

**Systematic Questioning Approach:**

Ask the user these questions to elicit requirements:

1. **Core Functionality**
   - "What is the primary purpose of this feature?"
   - "What problem does it solve?"

2. **Event-Driven Requirements**
   - "What user actions trigger this feature?"
   - "What system events are involved?"

3. **State-Driven Requirements**
   - "Are there different states or modes?"
   - "What should happen during each state?"

4. **Conditional Requirements**
   - "Are there different behaviors for different users/roles?"
   - "What conditions affect functionality?"

5. **Performance Requirements**
   - "Are there response time requirements?"
   - "What's the expected load/scale?"

6. **Security Requirements**
   - "What data needs protection?"
   - "Who should have access?"

7. **Error Handling**
   - "What can go wrong?"
   - "How should errors be handled?"

8. **Edge Cases**
   - "What are the boundary conditions?"
   - "What happens at extremes?"

**Best Practices:**
- Use "SHALL" for mandatory requirements
- Be specific and measurable (avoid "quickly", use "within 2 seconds")
- One requirement per statement
- Avoid ambiguous terms ("appropriate", "reasonable", "user-friendly")
- Use active voice

**Output Format:**
Update `docx/features/[NN-feature-name]/requirements.md` with:
- Overview section
- Functional requirements (organized by EARS type)
- Non-functional requirements (performance, security, usability)
- Constraints
- Acceptance criteria (checkboxes)
- Out of scope items

**User Confirmation:**
> "Requirements complete. Ready for design phase?"

---

### Phase 3: Technical Design

**Goal:** Create comprehensive technical design with architectural decisions

**Process:**

1. **Brainstorming Integration**
   - Activate `brainstorming` skill for collaborative design exploration
   - Explore 2-3 different architectural approaches
   - Discuss trade-offs for each approach

**UltraThink for Complex Designs:**
Before proposing technical approaches, activate deep thinking when:
- Architecture involves multiple services or complex data flows
- Trade-offs between approaches aren't obvious
- Design impacts security, performance, or scalability
- Requirements seem contradictory or incomplete

> 🗣 Say: "This design requires deep thinking. Let me ultrathink the architectural fundamentals before proposing approaches."

**During UltraThink, question:**
- Are we solving the right problem?
- What are we assuming that might be wrong?
- What could break at scale?
- What's the simplest architecture that works?
- What are the hidden costs of each approach?
- What would we do differently if starting from scratch?

**After UltraThink:** Present approaches with explicit reasoning about architectural trade-offs and scalability considerations.

2. **Approach Comparison**
   Present options with trade-offs:

   **Option A: [Approach Name]**
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Complexity: Low/Medium/High
   - Timeline: [Estimate]

   **Option B: [Approach Name]**
   - Pros: [Advantages]
   - Cons: [Disadvantages]
   - Complexity: Low/Medium/High
   - Timeline: [Estimate]

3. **Recommendation**
   - State recommended approach
   - Provide clear reasoning
   - Explain why it best fits requirements

4. **Design Document Structure**
   Create comprehensive `design.md` covering:

   **Architecture Overview**
   - How feature fits into system
   - High-level component diagram (ASCII art)

   **Component Structure**
   - List components with responsibilities
   - Define dependencies between components
   - Specify public interfaces

   **Data Flow**
   - Step-by-step data movement
   - Diagram showing flow

   **API Contracts**
   - Input/output schemas
   - Error responses
   - Example requests/responses

   **Error Handling**
   - Error scenarios and handling strategy
   - Fallback behaviors

   **Security Considerations**
   - Authentication/authorization
   - Input validation
   - Data protection

   **Performance Considerations**
   - Optimization strategies
   - Caching approach
   - Database indexing needs

   **Testing Strategy**
   - Unit test areas
   - Integration test scenarios
   - E2E test workflows

**Approval Gate:**
> "Design complete. Ready for task breakdown?"

Wait for explicit user approval before proceeding.

---

## Next Steps

After design approval, use `/dev-workflow:spec tasks` or `/dev-workflow:spec execute` to activate the `spec-driven-implementation` skill, which will:
- Break down your design into TDD tasks with Red-Green-Refactor cycles
- Guide systematic execution with quality gates
- Track progress with checkbox updates
- Integrate with code-quality and git-workflow skills

---

## Examples

### Example 1: Creating User Authentication Feature

**User:** "I need to add user authentication"

**Assistant:**
```
Activating spec-driven-planning skill for feature planning.

Let me create the feature structure:

Created feature: docx/features/01-user-authentication/
- requirements.md
- design.md
- tasks.md

Phase 1 Complete. Ready to define requirements?
```

**User:** "Yes"

**Assistant:**
```
Phase 2: Requirements Definition (EARS Format)

Let me ask some questions to capture clear requirements:

1. Core Functionality:
   - What authentication methods should be supported? (email/password, OAuth, etc.)
   - Should there be session management?

2. Events:
   - What happens when user tries to log in?
   - What happens when session expires?

[...continues with systematic questioning...]
```

### Example 2: Resuming at Design Phase

**User:** "/dev-workflow:spec design"

**Assistant:**
```
Activating spec-driven-planning skill at Phase 3: Design

Found latest feature: docx/features/01-user-authentication/

Requirements already defined. Let me propose architectural approaches:

**Option A: JWT-Based Authentication**
Pros: Stateless, scalable, works across services
Cons: Token invalidation complexity, larger payload
Complexity: Medium

**Option B: Session-Based Authentication**
Pros: Simple invalidation, smaller cookies, familiar pattern
Cons: Requires session storage, scaling challenges
Complexity: Low

Recommendation: Option A (JWT-Based)
Reasoning: Better for microservices, future-proof, industry standard

Proceed with JWT-based design?
```

---

## Notes

- Always request explicit approval between phases
- Use EARS format strictly for requirements
- Focus on "what" and "how", not "doing"
- Create clear, complete documentation before implementation
- Explore multiple architectural options before recommending one
- Wait for user approval before activating implementation skill
