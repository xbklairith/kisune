# Requirements: [Feature Name]

**Created:** [Date]
**Status:** Draft

## Overview

[Brief description of what this feature does and why it's needed. 2-3 sentences explaining the problem being solved and the value provided.]

## Functional Requirements

### Event-Driven Requirements

Events that trigger system behavior. Use format: "WHEN [trigger] THEN the system SHALL [response]"

- WHEN [trigger event] THEN the system SHALL [response/action]
- WHEN [trigger event] THEN the system SHALL [response/action]

### State-Driven Requirements

Behavior during specific system states. Use format: "WHILE [state] the system SHALL [requirement]"

- WHILE [system state] the system SHALL [continuous behavior]
- WHILE [system state] the system SHALL [continuous behavior]

### Ubiquitous Requirements

Always-true requirements. Use format: "The system SHALL [requirement]"

- The system SHALL [always-true requirement]
- The system SHALL [always-true requirement]

### Conditional Requirements

Behavior based on conditions. Use format: "IF [condition] THEN the system SHALL [requirement]"

- IF [condition] THEN the system SHALL [conditional behavior]
- IF [condition] THEN the system SHALL [conditional behavior]

### Optional Requirements

Feature-dependent requirements. Use format: "WHERE [feature] the system SHALL [requirement]"

- WHERE [optional feature enabled] the system SHALL [additional behavior]
- WHERE [optional feature enabled] the system SHALL [additional behavior]

## Non-Functional Requirements

### Performance

Specific, measurable performance requirements.

- The system SHALL [performance requirement with specific metrics, e.g., "respond within 200ms"]
- The system SHALL [scalability requirement with numbers, e.g., "support 1000 concurrent users"]

### Security

Security and privacy requirements.

- The system SHALL [security requirement, e.g., "encrypt all PII at rest using AES-256"]
- The system SHALL [authentication/authorization requirement]

### Usability

User experience requirements.

- The system SHALL [usability requirement, e.g., "provide clear error messages"]
- The system SHALL [accessibility requirement, e.g., "meet WCAG 2.1 Level AA standards"]

### Reliability

Availability and reliability requirements.

- The system SHALL [availability requirement, e.g., "maintain 99.9% uptime"]
- The system SHALL [error handling requirement, e.g., "gracefully degrade when API unavailable"]

### Maintainability

Code quality and maintenance requirements.

- The system SHALL [maintainability requirement, e.g., "maintain test coverage above 80%"]
- The system SHALL [documentation requirement]

## Constraints

Technical, business, or regulatory constraints that limit the solution.

- [Constraint 1, e.g., "Must use existing authentication system"]
- [Constraint 2, e.g., "Must comply with GDPR regulations"]
- [Constraint 3, e.g., "Budget limited to $X for external services"]

## Acceptance Criteria

Testable criteria that must be met for feature to be considered complete.

- [ ] [Testable criterion 1, e.g., "User can log in with email and password"]
- [ ] [Testable criterion 2, e.g., "Invalid credentials show appropriate error"]
- [ ] [Testable criterion 3, e.g., "Session persists for 24 hours"]
- [ ] [Testable criterion 4]
- [ ] [Testable criterion 5]

## Out of Scope

Explicitly state what is NOT included in this feature to prevent scope creep.

- [Out of scope item 1, e.g., "Social media login integration"]
- [Out of scope item 2, e.g., "Two-factor authentication"]
- [Out of scope item 3, e.g., "Password reset via SMS"]

## Dependencies

Other features, systems, or external services required.

- [Dependency 1, e.g., "User database schema"]
- [Dependency 2, e.g., "Email service for verification"]

## Risks & Assumptions

Known risks and assumptions being made.

**Assumptions:**
- [Assumption 1, e.g., "Users have valid email addresses"]
- [Assumption 2, e.g., "Email delivery is reliable"]

**Risks:**
- [Risk 1, e.g., "Email provider rate limiting might affect registration"]
- [Risk 2, e.g., "Password complexity rules might frustrate users"]

## References

Links to related documents, research, or external resources.

- [Related document or link]
- [External standard or specification]
