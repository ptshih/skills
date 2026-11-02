---
name: commit-artisan
description: "Decompose dirty working trees into clean, atomic, bisectable conventional commits. Use when asked to craft commits, split changes, or organize git history."
license: MIT
metadata:
  version: "1.0.0"
---

# Commit-Artisan: Atomic & Bisectable Git Commits

Organize only the authorized changes into logically isolated, bisectable commits. Follow
current user and project git instructions, and preserve other sessions' work.

## Constraints
1. **Explicit paths only:** Never run `git add -A`, `git add .`, `git commit -a`. Stage explicit file paths only.
2. **Follow repository conventions:** Use required message formats and trailers; do not invent attribution.
3. **Keep commits independently valid:** Check affected behavior and project-required gates so commits remain useful for bisecting. Reuse still-current evidence and distinguish pre-existing failures.

## Commit Decomposition

Split by logical change, not by layer. Each commit holds one change a reviewer can understand
alone, together with its tests and docs, so `git show` proves what it claims. When a feature
needs several commits, order them so dependencies land first (a schema and its migration before
the code that reads it), and each commit still builds and passes its tests.

## Conventional Format
Use the repository's convention when it differs; otherwise:

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

# 4. Inspect and report remaining uncommitted work
git status --short
```
