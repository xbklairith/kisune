---
name: database-migrations
description: Safe database schema changes — zero-downtime migrations, expand-contract pattern, and rollback strategies. Use when altering database tables, adding columns, or running schema changes.
---

# Database Migration Patterns

Safe, reversible database schema changes for production systems.

## When to Activate

- Creating or altering database tables
- Adding/removing columns or indexes
- Running data migrations (backfill, transform)
- Planning zero-downtime schema changes

## Core Principles

1. **Every change is a migration** — never alter production manually
2. **Migrations are forward-only in production** — rollbacks use new forward migrations
3. **Schema and data migrations are separate** — never mix DDL and DML
4. **Test against production-sized data** — 100 rows != 10M rows
5. **Migrations are immutable once deployed** — create new migration instead

## Safety Checklist

- [ ] Migration has both UP and DOWN (or marked irreversible)
- [ ] No full table locks on large tables
- [ ] New columns have defaults or are nullable
- [ ] Indexes created concurrently
- [ ] Data backfill is separate from schema change
- [ ] Tested against production-sized data
- [ ] Rollback plan documented

## PostgreSQL Patterns

### Adding a Column Safely

```sql
-- GOOD: Nullable, no lock
ALTER TABLE users ADD COLUMN avatar_url TEXT;

-- GOOD: With default (Postgres 11+ instant, no rewrite)
ALTER TABLE users ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT true;

-- BAD: NOT NULL without default (full table rewrite + lock)
ALTER TABLE users ADD COLUMN role TEXT NOT NULL;
```

### Index Without Downtime

```sql
-- BAD: Blocks writes
CREATE INDEX idx_users_email ON users (email);

-- GOOD: Non-blocking
CREATE INDEX CONCURRENTLY idx_users_email ON users (email);
```

### Renaming a Column (Expand-Contract)

```sql
-- Step 1: Add new column
ALTER TABLE users ADD COLUMN display_name TEXT;

-- Step 2: Backfill (separate migration)
UPDATE users SET display_name = username WHERE display_name IS NULL;

-- Step 3: Deploy app reading/writing both columns
-- Step 4: Drop old column (separate migration)
ALTER TABLE users DROP COLUMN username;
```

### Large Data Migrations

```sql
-- BAD: One transaction, locks table
UPDATE users SET normalized_email = LOWER(email);

-- GOOD: Batch with progress
DO $$
DECLARE batch_size INT := 10000; rows_updated INT;
BEGIN
  LOOP
    UPDATE users SET normalized_email = LOWER(email)
    WHERE id IN (
      SELECT id FROM users WHERE normalized_email IS NULL
      LIMIT batch_size FOR UPDATE SKIP LOCKED
    );
    GET DIAGNOSTICS rows_updated = ROW_COUNT;
    EXIT WHEN rows_updated = 0;
    COMMIT;
  END LOOP;
END $$;
```

## Zero-Downtime Strategy (Expand-Contract)

```
Phase 1: EXPAND
  - Add new column/table (nullable or with default)
  - Deploy: app writes to BOTH old and new
  - Backfill existing data

Phase 2: MIGRATE
  - Deploy: app reads from NEW, writes to BOTH
  - Verify data consistency

Phase 3: CONTRACT
  - Deploy: app only uses NEW
  - Drop old column/table in separate migration
```

## Anti-Patterns

| Anti-Pattern | Better Approach |
|-------------|-----------------|
| Manual SQL in production | Always use migration files |
| Editing deployed migrations | Create new migration |
| NOT NULL without default | Add nullable, backfill, then constrain |
| Inline index on large table | CREATE INDEX CONCURRENTLY |
| Schema + data in one migration | Separate migrations |
| Drop column before removing code | Remove code first, drop next deploy |
