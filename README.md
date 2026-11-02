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

- **[lean-build](skills/engineering/lean-build/SKILL.md)**: Build feature work with a high risk of
  overbuilding: derive acceptance and non-goals, deliver one narrow end-to-end path, leave out
  speculative options, and stop when acceptance passes.
- **[tdd](skills/engineering/tdd/SKILL.md)**: Test-first work through behavioral interfaces,
  one test then one minimal implementation per cycle, using relevant test-design guidance.
- **[walkthrough](skills/engineering/walkthrough/SKILL.md)**: Explain requested code flows step
  by step, with excerpts extracted from the source. Deliver in chat; create a file only when asked.

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
- **[repo-showcase](skills/engineering/repo-showcase/SKILL.md)**: Improve requested README presentation,
  badges, demos or GitHub metadata, respecting existing commit and publishing authorization.
- **[security-auditor](skills/engineering/security-auditor/SKILL.md)**: Review security-sensitive
  changes and requested audits for injection, traversal, SSRF, access-control flaws and related risks.
- **[todo](skills/engineering/todo/SKILL.md)**: Read or update `TODO.md` when the request clearly
  concerns that backlog; keep operations within scope and commit only when authorized.
- **[type-tightener](skills/engineering/type-tightener/SKILL.md)**: Address unsafe types introduced
  or exposed by the current change, preserving behavior and leaving unrelated code alone.

## Productivity

### User-invoked

- **[retro](skills/productivity/retro/SKILL.md)**: Review a coding session, the current one or a
  named one, for what in the agent's setup slowed it down or let mistakes through: missing
  pointers, checks and guardrails, bloated or no-op instructions, costly tool calls, missing
  information, unused skills and tools, and checks that catch little. It proposes numbered
  changes with evidence and applies only the ones the user picks.

- **[summarize](skills/productivity/summarize/SKILL.md)**: Summarize documents, plans, diffs or
  threads in plain English, concise by default and detailed when requested.

### Model-invoked

- **[clippy](skills/productivity/clippy/SKILL.md)**: Preserve the checkpoint directly, then let the user run native compaction; clipboard output only on request.
- **[find-skills](skills/productivity/find-skills/SKILL.md)**: Find and install agent skills when
  asked for one, evaluating instructions before installation and respecting the selected scope.
- **[handoff](skills/productivity/handoff/SKILL.md)**: Summarize the current session so a fresh
  agent can continue. It prints the handoff in chat, copies the same text to the clipboard, and
  saves a temporary Markdown file with a clickable path. Clipboard copying uses `pbcopy` on
  macOS; if it fails, the agent reports the failure and still provides the chat output and file.
  Inside Herdr, it offers to start the next session in a new tab with the handoff as its first
  prompt.
- **[huddle](skills/productivity/huddle/SKILL.md)**: Align an existing authorized team when
  assignments conflict, ownership is unclear, a restart needs agreement, or the user requests
  a huddle. Collect short read-backs, resolve mismatches and agree on a shared start.
- **[orchestrator](skills/productivity/orchestrator/SKILL.md)**: Take over and run a Herdr space
  of named agent sessions as its orchestrator. It discovers the roster, maps ownership by path
  and confirms the authorized scope, then routes work through inboxes, watches each agent's
  context and compacts at task boundaries, and reviews and lands work by path. Review matches
  the change's risk; routine phase changes do not require huddles.
  Herdr only.

## Attribution

The handoff skill is adapted from [Matt Pocock's handoff skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md),
with repository-state verification and chat, clipboard, and temporary-file output.

The walkthrough skill follows the linear walkthrough pattern in [Simon Willison's Agentic
Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/).
The [upstream MIT notice](skills/productivity/handoff/THIRD_PARTY_NOTICES.md) is included.

The tdd skill is adapted from [Matt Pocock's tdd skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)
([MIT notice](skills/engineering/tdd/THIRD_PARTY_NOTICES.md)).

The lean-build skill is adapted from [Caveman's lean-build skill](https://github.com/JuliusBrussee/caveman/blob/main/skills/lean-build/SKILL.md)
([Apache-2.0 and MIT notices](skills/engineering/lean-build/THIRD_PARTY_NOTICES.md)).

The find-skills skill is adapted from [Vercel's find-skills skill](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md)
([MIT notice](skills/productivity/find-skills/THIRD_PARTY_NOTICES.md)).

The retro skill is adapted from [Matt Pocock's retro skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md)
([MIT notice](skills/productivity/retro/THIRD_PARTY_NOTICES.md)).

The repository layout follows [mattpocock/skills](https://github.com/mattpocock/skills).

## License

[MIT](LICENSE)
