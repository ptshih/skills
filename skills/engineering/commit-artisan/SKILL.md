---
name: commit-artisan
description: "Decompose dirty working trees into clean, atomic, bisectable conventional commits. Use when asked to craft commits, split changes, or organize git history."
license: MIT
metadata:
  version: "1.0.0"
---

# Commit-Artisan: Atomic & Bisectable Git Commits

Transform dirty working trees into clean, logically isolated, bisectable commits. Strictly complies with `AGENTS.md > Implementation and verification`.

## Hard Constraints (from AGENTS.md)
1. **Explicit paths only:** Never run `git add -A`, `git add .`, `git commit -a`. Stage explicit file paths only.
2. **No Co-Authored-By:** Never add `Co-Authored-By` or AI attribution trailers.
3. **Tests must pass at each commit:** Every commit should leave the build and test suite green so `git bisect` functions properly.

## Commit Decomposition

Split by logical change, not by layer. Each commit holds one change a reviewer can understand
alone, together with its tests and docs, so `git show` proves what it claims. When a feature
needs several commits, order them so dependencies land first (a schema and its migration before
the code that reads it), and each commit still builds and passes its tests.

## Conventional Format
```
<type>(<scope>): <imperative summary under 72 chars>

[optional body explaining intent, constraints, and non-obvious behavior]
```

Types: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `chore`.

## Example Execution
```bash
# 1. Inspect dirty status
git status --porcelain

# 2. The table, with its migration and test
git add src/db/schema.ts src/db/migrations/0007_user_preferences.sql src/db/schema.test.ts
git commit -m "feat(db): add user_preferences table"

# 3. The resolver, with its test
git add src/services/preferences.ts src/services/preferences.test.ts
git commit -m "feat(preferences): fall back to system defaults"

# 4. Verify git status clean
git status --short
```
