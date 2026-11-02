---
name: type-tightener
description: "Address unsafe types introduced or exposed by the current TypeScript or Python change, and explicit type-cleanup requests. Use precise types and necessary guards while preserving behavior and leaving unrelated code alone."
license: MIT
metadata:
  version: "1.0.0"
---

# Type-Tightener: Strict Typing & Schema Hardening

Tighten types in the code affected by the requested change. Preserve behavior and public
contracts. Reuse the project's type and validation tools; this skill does not require new
schema libraries or cleanup elsewhere in a touched file.

## Type Risks to Check in Scope

1. **`any` and `as any` casts:**
   - Replace with generic parameters, typed interfaces, or `unknown` + runtime type guard (`typeof`, `instanceof`, or Zod parser).
2. **`@ts-ignore` / `@ts-nocheck`:**
   - Remove ignore directives. Fix underlying type mismatch or declare missing module augmentation.
3. **Loose object dictionaries (`Record<string, any>` / `dict`):**
   - Replace with explicit TypeScript `interface` or Python `TypedDict` / Pydantic model.
4. **Bare strings and shapeless variants:**
   - A `string` that only ever holds a few values becomes a string literal union (`"draft" | "sent"`).
   - An object whose fields depend on its kind becomes a discriminated union tagged by `type` or `kind`.
   - A string literal union is already strict; leave it as it is.

## Verification
Run the project's configured typecheck with its existing toolchain. Examples:
```bash
# TypeScript
bun run check-types # or the project's equivalent script

# Python
pyright # or mypy .
```
Run tests relevant to any affected behavior and preserve project-required checks. Report exit
codes and distinguish failures caused by the change from pre-existing failures.
