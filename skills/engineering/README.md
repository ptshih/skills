# Engineering

Daily code work.

## Model-invoked

Model- or user-reachable: type `/<name>`, or the agent reaches for it when the request matches.

- **[ast-grep](./ast-grep/SKILL.md)**: Search, outline and rewrite code by syntax with ast-grep instead of regex or whole-file reads.
- **[browser-verify](./browser-verify/SKILL.md)**: Check web pages headlessly with Playwright: screenshots, accessibility trees and quick endpoint checks, without touching a running dev server.
- **[commit-artisan](./commit-artisan/SKILL.md)**: Split a dirty working tree into atomic, bisectable Conventional Commits, staged by explicit path.
- **[dep-auditor](./dep-auditor/SKILL.md)**: Vet a new dependency for a standard-library replacement, bundle weight, known vulnerabilities and license.
- **[design-review](./design-review/SKILL.md)**: Review a visually complete feature against the project's design system with three parallel read-only reviewers (visual, interaction, component polish), then consolidate one severity table.
- **[doc-drift-sentinel](./doc-drift-sentinel/SKILL.md)**: After a change to flags, routes, config keys or exported types, find and fix the docs that no longer match.
- **[lean-build](./lean-build/SKILL.md)**: Build feature work with a high risk of overbuilding: derive acceptance and non-goals, deliver one narrow end-to-end path, and stop when acceptance passes.
- **[migration-guard](./migration-guard/SKILL.md)**: Checklist for a schema migration file: non-destructive, reversible, and rehearsed on a disposable database.
- **[perf-optimizer](./perf-optimizer/SKILL.md)**: Measure first, then fix the bottleneck the measurement points to: N+1 queries, missing indexes, quadratic loops, re-renders, memory.
- **[repo-showcase](./repo-showcase/SKILL.md)**: Make a GitHub repository presentable the honest way: badges that state true facts, a recorded or clearly illustrated demo GIF, and an accurate description and topics.
- **[security-auditor](./security-auditor/SKILL.md)**: Audit a diff before commit for injection, path traversal, SSRF, IDOR, timing attacks and ReDoS.
- **[tdd](./tdd/SKILL.md)**: Test-driven development as a red-green loop, with tests through agreed seams and one test then one minimal implementation per cycle.
- **[test-synthesizer](./test-synthesizer/SKILL.md)**: Add the boundary and adversarial test cases a happy-path suite misses, chosen from the inputs the code really accepts.
- **[todo](./todo/SKILL.md)**: Work a repo's engineering backlog in `TODO.md`: show what is open as ready, needs-your-call and blocked tables, add, work, update and close items, and groom the file for stale content and a backlog you can hold in your head.
- **[type-tightener](./type-tightener/SKILL.md)**: Replace `any`, unchecked casts and ignore directives with strict types, schemas and discriminated unions, then typecheck.
- **[ui-craft](./ui-craft/SKILL.md)**: Build polished, accessible web UI from the project's own design system, with spacing, color, interaction-state and accessibility defaults when it has none.
- **[walkthrough](./walkthrough/SKILL.md)**: Write a linear walkthrough of a change, feature or module in execution order, with every code excerpt pulled from the files by a command, and save it to a private temporary Markdown file.

