---
name: dep-auditor
description: "Review dependency additions and material upgrades for suitable existing alternatives, size, vulnerabilities and compatibility with the repository's license policy. Also use for explicit dependency audit requests."
license: MIT
metadata:
  version: "1.0.0"
---

# Dep-Auditor: Lean & Secure Dependency Auditing

Review dependencies affected by the requested change. Reuse existing utilities or standard
library functions when they meet the same requirements; preserve unrelated dependencies.

## Audit Checklist for Changed Dependencies

1. **Standard library replacement:**
   - Can existing project utilities or the language's standard library meet the same requirements?
     - `lodash/cloneDeep` -> native `structuredClone()`.
     - `lodash/assign` / shallow merges -> `Object.assign()` or spread. A deep merge (`lodash/merge`) has no native equivalent; keep a small helper or the dependency.
     - `axios` / `request` -> native `fetch()`.
     - `moment` / `dayjs` -> native `Intl.DateTimeFormat` or `Date`.
     - `rimraf` / `mkdirp` -> `fs.rmSync(path, { recursive: true })` / `fs.mkdirSync(path, { recursive: true })`.

2. **Bundle size & unpack overhead:**
   - Prefer zero-dependency or tree-shakeable packages.
   - Inspect added bundle or install cost when material to the project and the dependency's purpose.

3. **Security audit:**
   Use the project's configured vulnerability check when relevant to the changed dependency.
   Use available tools; do not install a scanner just for this review. Examples:
   ```bash
   # npm projects
   npm audit

   # Bun projects (never `bunx audit`: that downloads and runs an unrelated npm package)
   bun audit

   # Rust
   cargo audit

   # Python
   pip-audit
   ```
   Inspect the findings and exit code. Distinguish new or worsened findings from pre-existing
   ones, and report any gaps in the check. Preserve project-required gates; keep fixes scoped
   to the requested dependency change.

4. **License check:**
   Check the changed dependency against the repository's license policy. Flag unclear
   compatibility for a decision instead of imposing a separate blanket license rule.
