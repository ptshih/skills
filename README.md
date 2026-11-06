# Skills

Personal agent skills by [Peter Shih](https://github.com/ptshih), for Claude Code, Codex, Pi and
any other agent that reads Agent Skills.

## Install

```bash
npx skills@latest add ptshih/skills -g --skill <name>
```

`-g` installs for your user rather than one project; pick the agents when prompted, or pass
`-a claude-code -a codex`. Leave out `--skill` to choose from the list. Update later with:

```bash
npx skills@latest update
```

## Engineering

### User-invoked

- **[codebase-design](skills/engineering/codebase-design/SKILL.md)**: Design deep modules with
  focused interfaces, deliberate seams and testability; compare alternative designs in the main
  session when asked.
- **[investigate-first](skills/engineering/investigate-first/SKILL.md)**: Diagnose ambiguous
  failures before editing: rank hypotheses by evidence, then report the cause and its proof.
- **[migration](skills/engineering/migration/SKILL.md)**: Plan and implement reversible
  transitions with compatibility, data preservation and rollback proof, without implicit
  destructive steps.
- **[safe-refactor](skills/engineering/safe-refactor/SKILL.md)**: Restructure code while preserving
  behavior, interfaces and compatibility, with the same proof before and after.
- **[surgical-patch](skills/engineering/surgical-patch/SKILL.md)**: Fix a bug at the narrowest
  responsible layer, with no cleanup outside the fix, and verify the affected behavior.
- **[tdd](skills/engineering/tdd/SKILL.md)**: Test-first work through behavioral interfaces,
  one test then one minimal implementation per cycle, using relevant test-design guidance.
- **[walkthrough](skills/engineering/walkthrough/SKILL.md)**: Explain requested code flows step
  by step, with excerpts extracted from the source. Deliver in chat; create a file only when asked.
- **[verify-and-stop](skills/engineering/verify-and-stop/SKILL.md)**: Check acceptance conditions
  with the smallest sufficient proof, report the result and stop.

### Model-invoked

- **[ast-grep](skills/engineering/ast-grep/SKILL.md)**: Search, outline and rewrite code by syntax
  with ast-grep instead of regex or whole-file reads.
- **[browser-verify](skills/engineering/browser-verify/SKILL.md)**: Verify affected UI behavior
  with existing headless browser tools and focused checks, reusing the task's session and dev server.
- **[commit-artisan](skills/engineering/commit-artisan/SKILL.md)**: Split authorized changes into
  atomic, bisectable commits by explicit path, following repository conventions.
- **[dep-auditor](skills/engineering/dep-auditor/SKILL.md)**: Review dependency additions and
  material upgrades for alternatives, size, vulnerabilities and the repository's license policy.
- **[design-review](skills/engineering/design-review/SKILL.md)**: Review substantial UI changes or requested design work
  against the project's design system through visual, interaction and component-polish lenses,
  delegating only when authorized, then consolidate one severity table.
- **[doc-drift-sentinel](skills/engineering/doc-drift-sentinel/SKILL.md)**: Update affected docs
  when documented behavior, APIs, CLI flags, configuration or usage changes.
- **[migration-guard](skills/engineering/migration-guard/SKILL.md)**: Checklist for a schema
  migration file: non-destructive, reversible, and rehearsed on a disposable database.
- **[perf-optimizer](skills/engineering/perf-optimizer/SKILL.md)**: Investigate reported performance
  problems, measured regressions or explicit optimization requests, with before and after measurements.
- **[security-auditor](skills/engineering/security-auditor/SKILL.md)**: Review security-sensitive
  changes and requested audits for injection, traversal, SSRF, access-control flaws and related risks.
- **[todo](skills/engineering/todo/SKILL.md)**: Read or update `TODO.md` when the request clearly
  concerns that backlog; keep operations within scope and commit only when authorized.
- **[type-tightener](skills/engineering/type-tightener/SKILL.md)**: Address unsafe types introduced
  or exposed by the current change, preserving behavior and leaving unrelated code alone.
- **[vercel-react-best-practices](skills/engineering/vercel-react-best-practices/SKILL.md)**:
  Consult Vercel's React and Next.js performance rules for reported problems, measured regressions
  or explicit optimization reviews, reading only the relevant rules.

## Productivity

### User-invoked

- **[grilling](skills/productivity/grilling/SKILL.md)**: Stress-test a plan, decision or idea one
  focused question at a time, with a recommendation for each, within the requested scope.

- **[retro](skills/productivity/retro/SKILL.md)**: Review a coding session, the current one or a
  named one, for what in the agent's setup slowed it down or let mistakes through: missing
  pointers, checks and guardrails, bloated or no-op instructions, costly tool calls, missing
  information, unused skills and tools, and checks that catch little. It proposes numbered
  changes with evidence and applies only the ones the user picks.

### Model-invoked

- **[clippy](skills/productivity/clippy/SKILL.md)**: Preserve the checkpoint directly, then let the user run native compaction; clipboard output only on request.
- **[handoff](skills/productivity/handoff/SKILL.md)**: Summarize the current session so a fresh
  agent can continue. It prints the handoff in chat, copies the same text to the clipboard, and
  saves a temporary Markdown file with a clickable path. Clipboard copying uses `pbcopy` on
  macOS; if it fails, the agent reports the failure and still provides the chat output and file.
  Inside Herdr, it offers to start the next session in a new tab with the handoff as its first
  prompt.
- **[orchestrator](skills/productivity/orchestrator/SKILL.md)**: Lead a team of agents the way
  Claude Code's native agent teams work: named teammates, a shared task list, direct messages,
  idle notifications, plan approval and shutdown. Claude teammates use the native mechanism;
  Codex and Antigravity teammates run in a Herdr space through per-harness adapters. It confirms
  the authorized scope, watches each teammate's context and compacts at task boundaries, and
  reviews and lands work by path, with review matched to the change's risk.

## Attribution

The handoff skill is adapted from [Matt Pocock's handoff skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md),
with repository-state verification and chat, clipboard, and temporary-file output.

The walkthrough skill follows the linear walkthrough pattern in [Simon Willison's Agentic
Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/).
The [upstream MIT notice](skills/productivity/handoff/THIRD_PARTY_NOTICES.md) is included.

The tdd skill is adapted from [Matt Pocock's tdd skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)
([MIT notice](skills/engineering/tdd/THIRD_PARTY_NOTICES.md)).

The retro skill is adapted from [Matt Pocock's retro skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md)
([MIT notice](skills/productivity/retro/THIRD_PARTY_NOTICES.md)).

The grilling skill is adapted from [Matt Pocock's grilling skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)
([MIT notice](skills/productivity/grilling/THIRD_PARTY_NOTICES.md)).

The codebase-design skill is adapted from [Matt Pocock's codebase-design skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md)
([MIT notice](skills/engineering/codebase-design/THIRD_PARTY_NOTICES.md)).

The vercel-react-best-practices skill is adapted from [Vercel's react-best-practices skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md)
([MIT notice](skills/engineering/vercel-react-best-practices/THIRD_PARTY_NOTICES.md)).

The investigate-first, surgical-patch, safe-refactor, verify-and-stop and migration skills are
adapted from Caveman's [investigate-first](https://github.com/JuliusBrussee/caveman/blob/main/skills/investigate-first/SKILL.md),
[surgical-patch](https://github.com/JuliusBrussee/caveman/blob/main/skills/surgical-patch/SKILL.md),
[safe-refactor](https://github.com/JuliusBrussee/caveman/blob/main/skills/safe-refactor/SKILL.md),
[verify-and-stop](https://github.com/JuliusBrussee/caveman/blob/main/skills/verify-and-stop/SKILL.md)
and [migration](https://github.com/JuliusBrussee/caveman/blob/main/skills/migration/SKILL.md) skills
(Apache-2.0 and MIT notices in each skill's `THIRD_PARTY_NOTICES.md`, for example
[migration's](skills/engineering/migration/THIRD_PARTY_NOTICES.md)).

The repository layout follows [mattpocock/skills](https://github.com/mattpocock/skills).

## License

[MIT](LICENSE)
