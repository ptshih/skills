---
name: doc-drift-sentinel
description: "Keep affected documentation aligned when public behavior, CLI flags, APIs, configuration or usage changes. Also use for explicit documentation synchronization or drift-review requests."
license: MIT
metadata:
  version: "1.0.0"
---

# Doc-Drift-Sentinel: Code-to-Docs Synchronization

Check documentation affected by the requested change. Internal refactors with unchanged
documented behavior do not require a separate documentation audit.

## Audit Workflow

### 1. Identify Changed Surfaces
Inspect this session's changes for ones affecting public contracts. Other sessions may share the
checkout, so limit the diff to the paths you changed and leave their work and its docs alone:
```bash
git diff HEAD --name-only -- <paths this session changed>
```
Focus on:
- CLI flags and argument parsers.
- Exported API route paths, request payloads, response formats.
- Configuration keys (`settings.json`, `.env.example`, yaml configs).
- Exported TypeScript interfaces or library entry points.

### 2. Verify Documentation Files
Inspect corresponding docs:
- `README.md` usage examples and command tables.
- `docs/` architecture documents.
- OpenAPI / Swagger / JSON Schema specifications.
- `help` output and `--help` CLI strings.

### 3. Update & Sync Docs
- Update outdated parameter names, flags, and return types.
- Verify changed examples match the implementation, using relevant available checks.
- Keep documentation edits scoped to the changed behavior.
