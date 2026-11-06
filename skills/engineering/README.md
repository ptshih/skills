# Engineering

Daily code work.

## User-invoked

- **[codebase-design](./codebase-design/SKILL.md)**: Design deep modules with focused interfaces, deliberate seams and testability; compare alternative designs in the main session when asked.
- **[investigate-first](./investigate-first/SKILL.md)**: Diagnose ambiguous failures before editing: rank hypotheses by evidence, then report the cause and its proof.
- **[migration](./migration/SKILL.md)**: Plan and implement reversible transitions with compatibility, data preservation and rollback proof, without implicit destructive steps.
- **[safe-refactor](./safe-refactor/SKILL.md)**: Restructure code while preserving behavior, interfaces and compatibility, with the same proof before and after.
- **[surgical-patch](./surgical-patch/SKILL.md)**: Fix a bug at the narrowest responsible layer, with no cleanup outside the fix, and verify the affected behavior.
- **[tdd](./tdd/SKILL.md)**: Test-first work through behavioral interfaces, one test then one minimal implementation per cycle, using relevant test-design guidance.
- **[walkthrough](./walkthrough/SKILL.md)**: Explain requested code flows step by step, with excerpts extracted from the source; deliver in chat and create a file only when asked.
- **[verify-and-stop](./verify-and-stop/SKILL.md)**: Check acceptance conditions with the smallest sufficient proof, report the result and stop.

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
- **[security-auditor](./security-auditor/SKILL.md)**: Review security-sensitive changes and requested audits for injection, traversal, SSRF, access-control flaws and related risks.
- **[todo](./todo/SKILL.md)**: Read or update `TODO.md` when the request clearly concerns that backlog; keep operations within scope and commit only when authorized.
- **[type-tightener](./type-tightener/SKILL.md)**: Address unsafe types introduced or exposed by the current change, preserving behavior and leaving unrelated code alone.
- **[vercel-react-best-practices](./vercel-react-best-practices/SKILL.md)**: Consult Vercel's React and Next.js performance rules for reported problems, measured regressions or explicit optimization reviews, reading only the relevant rules.

