# Requirements: Slug max length

**Status:** Approved

## Functional Requirements

- **REQ-001** WHERE `max_length` is given the system SHALL return a slug of at most `max_length` characters.
- **REQ-002** WHEN truncation is needed THEN the system SHALL cut at the last hyphen at or before `max_length`, so the slug never ends mid-word.
- **REQ-003** IF the first word alone is longer than `max_length` THEN the system SHALL return that word cut to `max_length` characters.
- **REQ-004** The system SHALL behave exactly as today when `max_length` is not given.
