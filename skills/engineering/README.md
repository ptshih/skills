# Engineering

Daily code work.

## User-invoked

- **[lean-build](./lean-build/SKILL.md)**: Build feature work with a high risk of overbuilding: derive acceptance and non-goals, deliver one narrow end-to-end path, and stop when acceptance passes.
- **[tdd](./tdd/SKILL.md)**: Test-first work through behavioral interfaces, one test then one minimal implementation per cycle, using relevant test-design guidance.
- **[walkthrough](./walkthrough/SKILL.md)**: Explain requested code flows step by step, with excerpts extracted from the source; deliver in chat and create a file only when asked.

## Model-invoked

Model- or user-reachable: type `/<name>`, or the agent reaches for it when the request matches.

- **[ast-grep](./ast-grep/SKILL.md)**: Search, outline and rewrite code by syntax with ast-grep instead of regex or whole-file reads.
- **[browser-verify](./browser-verify/SKILL.md)**: Verify affected UI behavior with existing headless browser tools and focused checks, reusing the task's session and dev server.
- **[commit-artisan](./commit-artisan/SKILL.md)**: Split authorized changes into atomic, bisectable commits by explicit path, following repository conventions.
- **[dep-auditor](./dep-auditor/SKILL.md)**: Review dependency additions and material upgrades for alternatives, size, vulnerabilities and the repository's license policy.
- **[design-review](./design-review/SKILL.md)**: Review substantial UI changes or requested design work through visual, interaction and component-polish lenses; work in the main session unless delegation is authorized.
- **[doc-drift-sentinel](./doc-drift-sentinel/SKILL.md)**: Update affected docs when documented behavior, APIs, CLI flags, configuration or usage changes.
- **[migration-guard](./migration-guard/SKILL.md)**: Checklist for a schema migration file: non-destructive, reversible, and rehearsed on a disposable database.
- **[perf-optimizer](./perf-optimizer/SKILL.md)**: Investigate reported performance problems, measured regressions or explicit optimization requests, with before and after measurements.
- **[repo-showcase](./repo-showcase/SKILL.md)**: Improve requested README presentation, badges, demos or GitHub metadata, respecting existing commit and publishing authorization.
- **[security-auditor](./security-auditor/SKILL.md)**: Review security-sensitive changes and requested audits for injection, traversal, SSRF, access-control flaws and related risks.
- **[todo](./todo/SKILL.md)**: Read or update `TODO.md` when the request clearly concerns that backlog; keep operations within scope and commit only when authorized.
- **[type-tightener](./type-tightener/SKILL.md)**: Address unsafe types introduced or exposed by the current change, preserving behavior and leaving unrelated code alone.

