---
name: dep-auditor
description: "Audit dependency additions in package.json, Cargo.toml, or requirements.txt for bundle bloat, CVE vulnerabilities, license compliance, and standard library alternatives."
license: MIT
metadata:
  version: "1.0.0"
---

# Dep-Auditor: Lean & Secure Dependency Auditing

Prevent agents from pulling in heavy, unvetted, or vulnerable dependencies when existing utilities or standard library functions suffice.

## Audit Checklist for Added Dependencies

1. **Standard library replacement:**
   - Can this be done in modern JS/TS standard library?
     - `lodash/cloneDeep` -> native `structuredClone()`.
     - `lodash/assign` / shallow merges -> `Object.assign()` or spread. A deep merge (`lodash/merge`) has no native equivalent; keep a small helper or the dependency.
     - `axios` / `request` -> native `fetch()`.
     - `moment` / `dayjs` -> native `Intl.DateTimeFormat` or `Date`.
     - `rimraf` / `mkdirp` -> `fs.rmSync(path, { recursive: true })` / `fs.mkdirSync(path, { recursive: true })`.

2. **Bundle size & unpack overhead:**
   - Prefer zero-dependency or tree-shakeable packages.
   - Flag packages pulling > 50 transitive sub-dependencies for simple utilities.

3. **Security audit:**
   Run project security vulnerability scanner:
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
   Must exit 0 with zero high or critical CVEs.

4. **License check:**
   Ensure license is permissive (MIT, Apache-2.0, BSD-2/3-Clause, ISC). Reject viral GPL/AGPL in proprietary repositories.
