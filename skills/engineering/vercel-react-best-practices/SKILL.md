---
name: vercel-react-best-practices
description: Consult Vercel's React and Next.js performance guidance for reported performance problems, measured regressions or explicit optimization reviews. Read only rules relevant to the affected path; routine React edits do not trigger a performance audit.
license: MIT
metadata:
  author: vercel
  version: "1.0.0"
---

# Vercel React Best Practices

Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Contains 70 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

## When to Apply

Use for reported React or Next.js performance problems, measured regressions, or an explicit
performance review or optimization request. Match guidance to the project's framework version
and the affected path. Measure before and after changes; add caching, memoization, dependencies
or other complexity only when the demonstrated problem justifies it.

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Eliminating Waterfalls | CRITICAL | `async-` |
| 2 | Bundle Size Optimization | CRITICAL | `bundle-` |
| 3 | Server-Side Performance | HIGH | `server-` |
| 4 | Client-Side Data Fetching | MEDIUM-HIGH | `client-` |
| 5 | Re-render Optimization | MEDIUM | `rerender-` |
| 6 | Rendering Performance | MEDIUM | `rendering-` |
| 7 | JavaScript Performance | LOW-MEDIUM | `js-` |
| 8 | Advanced Patterns | LOW | `advanced-` |

## How to Use

Use the category prefixes above to locate relevant files under `${CLAUDE_SKILL_DIR}/rules/`;
in a harness that does not expand `${CLAUDE_SKILL_DIR}`, use the folder this file was loaded
from. Read only the rules needed for the current problem, not the entire collection. For example:

```
rules/async-parallel.md
rules/bundle-barrel-imports.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect code example with explanation
- Correct code example with explanation
- Additional context and references

## Full Compiled Document

For a requested comprehensive review, the compiled guide is `${CLAUDE_SKILL_DIR}/AGENTS.md`. It is reference
material, not a checklist for ordinary code changes.
