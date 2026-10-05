---
name: type-tightener
description: "Eliminate loose typing (any, as any, unknown passed on without a type guard, @ts-ignore) in modified TypeScript or Python files. Replace with strict schemas, generics, and discriminated unions. Run typecheck to verify."
license: MIT
metadata:
  version: "1.0.0"
---

# Type-Tightener: Strict Typing & Schema Hardening

Hunts down loose types, lazy escape hatches, and missing type guards introduced by LLMs. Replaces with strict, self-documenting types.

## Target Anti-Patterns to Eliminate

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
Run project typecheck; must exit 0:
```bash
# TypeScript
bun x tsc --noEmit # or npx tsc --noEmit

# Python
pyright # or mypy .
```
Ensure all existing unit tests pass via `bun test` / `npm test` after tightening.
