---
name: doc-drift-sentinel
description: "Detect and eliminate documentation drift. Compare modified functions, CLI flags, configuration keys, and API endpoints against README.md and documentation files to keep docs synchronized with code."
license: MIT
metadata:
  version: "1.0.0"
---

# Doc-Drift-Sentinel: Code-to-Docs Synchronization

Ensure documentation, README guides, and inline documentation stay 100% accurate after code refactors or feature additions.

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
- Ensure all code blocks in `README.md` are syntax-valid and match new implementation.
- Stage updated doc files alongside code changes before committing.
