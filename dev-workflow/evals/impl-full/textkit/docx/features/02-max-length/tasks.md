# Tasks: Slug max length

**Status:** Not Started

## Tasks

- [ ] Task 1: Truncate at a word boundary
    - [ ] RED: Write failing tests in `tests/test_slug.py` for REQ-001, REQ-002 and REQ-003
    - [ ] GREEN: Add `max_length` to `slugify` in `textkit/slug.py`
    - [ ] REFACTOR: Tidy the implementation; all tests stay green

    Acceptance Criteria:
    - [ ] `slugify("Hello big world", max_length=9)` returns `"hello-big"`
    - [ ] `slugify("Supercalifragilistic", max_length=5)` returns `"super"`
    - [ ] Existing tests still pass (REQ-004)
    Linked Requirements: REQ-001, REQ-002, REQ-003, REQ-004

## Progress Summary

- Total Tasks: 1
- Completed: 0/1
