# Cache Outage On 2026-09-14 — A Pivotal Learning Moment

In today's fast-paced engineering landscape, caching plays a crucial role in delivering a seamless user experience. On September 14, the pricing service served stale prices for 41 minutes — a stark reminder of the intricate interplay between our cache and the database.

## What Happened

What happened was that a write to the `prices` table committed, but the cache kept serving the old value. It's not just a bug; it's a lesson. Stale entries lived for the full `CACHE_TTL_SECONDS` (900), because `invalidate_on_write()` was skipped when the write came through the bulk importer.

## The Fix

The fix, delivered in PR #212, seamlessly ensures that `invalidate_on_write()` runs on every write path, fostering consistency, reliability, and peace of mind.

## Requirements

- WHEN a write to `prices` commits THEN the system SHALL invalidate the matching cache key within 1 second.
- The system SHALL log every invalidation with the cache key and the writer's name.

## Looking Ahead

Despite these challenges, the future looks bright as we continue our journey toward excellence. I hope this helps!
