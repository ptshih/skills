---
name: migration-guard
description: "Checklist for a database schema migration file (Drizzle, Prisma, SQL, Alembic): non-destructive, reversible, rehearsed on a disposable database. Use when modifying database schemas or creating migration files. For planning a transition across releases, use the migration skill."
license: MIT
metadata:
  version: "1.1.0"
---

# Migration-Guard: Safe & Reversible Schema Evolution

Prevent catastrophic schema migrations, unrecoverable data loss, and locking deadlocks in relational databases.

The repository's own migration procedure (its `AGENTS.md` or README) wins over this checklist.
For sequencing a change across releases (expand, migrate, verify, contract), use the `migration` skill.

## 4 Golden Migration Rules

1. **Reversibility:**
   - Every forward migration (`up.sql`) must have a corresponding tested rollback migration (`down.sql`).
   - Drizzle and Prisma generate forward migrations only: write the rollback by hand. Prisma can
     draft one with `prisma migrate diff` from the new schema to the previous one with `--script`
     (see Prisma's "Generating down migrations" guide).

2. **Non-destructive column changes:**
   - Never `DROP COLUMN` or `RENAME COLUMN` directly in one migration.
   - Follow expand-and-contract pattern:
     - Phase 1: Add new column as nullable.
     - Phase 2: Backfill data and double-write in application code.
     - Phase 3: Drop old column in later release.

3. **Safe defaults on existing tables:**
   - Adding a `NOT NULL` column must provide a default value to prevent failing on non-empty production tables.

4. **Rehearse on a disposable database:**
   - Start a throwaway database (for example `docker run --rm postgres`) and pass its URL
     explicitly. Never point these commands at a shared, staging or production database, and
     check which env file the command loads (Bun and dotenvx can load `.env.local`).
   - Apply the earlier migrations, add rows shaped like production's, then apply the new
     migration, run its rollback, and confirm the earlier schema and the rows are intact.
     Generating a migration applies nothing; these commands do:
     ```bash
     # Drizzle: `generate` only writes SQL; `migrate` applies pending migrations
     DATABASE_URL=<disposable> bunx drizzle-kit migrate

     # Prisma: `migrate deploy` applies without prompts
     DATABASE_URL=<disposable> npx prisma migrate deploy
     ```
   - Never run `prisma migrate dev`, `prisma migrate reset` or `prisma db push` against a
     database you did not create for the rehearsal: `migrate dev` can prompt to reset the
     database when it detects drift.
   - Regenerate ORM client types and verify full test suite passes (`bun test`).
