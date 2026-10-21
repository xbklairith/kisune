# Design: Slug max length

**Status:** Approved

Add an optional keyword argument `max_length=None` to `slugify` in `textkit/slug.py`. After the existing slug is built, if `max_length` is set and the slug is longer, take `slug[:max_length + 1]`, cut at its last `-` (REQ-002), and fall back to `slug[:max_length]` when there is no hyphen (REQ-003). No other module changes (REQ-004). Tests go in `tests/test_slug.py`.
