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

### Model-invoked

- **[ast-grep](skills/engineering/ast-grep/SKILL.md)**: Search, outline and rewrite code by syntax
  with ast-grep instead of regex or whole-file reads.
- **[browser-verify](skills/engineering/browser-verify/SKILL.md)**: Check web pages headlessly with
  Playwright: screenshots, accessibility trees and quick endpoint checks, without touching a running
  dev server.
- **[commit-artisan](skills/engineering/commit-artisan/SKILL.md)**: Split a dirty working tree into
  atomic, bisectable Conventional Commits, staged by explicit path.
- **[dep-auditor](skills/engineering/dep-auditor/SKILL.md)**: Vet a new dependency for a
  standard-library replacement, bundle weight, known vulnerabilities and license.
- **[design-review](skills/engineering/design-review/SKILL.md)**: Review a visually complete feature
  against the project's design system with three parallel read-only reviewers (visual, interaction,
  component polish), then consolidate one severity table.
- **[doc-drift-sentinel](skills/engineering/doc-drift-sentinel/SKILL.md)**: After a change to flags,
  routes, config keys or exported types, find and fix the docs that no longer match.
- **[lean-build](skills/engineering/lean-build/SKILL.md)**: Build feature work with a high risk of
  overbuilding: derive acceptance and non-goals, deliver one narrow end-to-end path, leave out
  speculative options, and stop when acceptance passes.
- **[migration-guard](skills/engineering/migration-guard/SKILL.md)**: Checklist for a schema
  migration file: non-destructive, reversible, and rehearsed on a disposable database.
- **[perf-optimizer](skills/engineering/perf-optimizer/SKILL.md)**: Measure first, then fix the
  bottleneck the measurement points to: N+1 queries, missing indexes, quadratic loops, re-renders,
  memory.
- **[repo-showcase](skills/engineering/repo-showcase/SKILL.md)**: Make a GitHub repository
  presentable the honest way: badges that state true facts, a recorded or clearly illustrated demo
  GIF, and an accurate description and topics.
- **[security-auditor](skills/engineering/security-auditor/SKILL.md)**: Audit a diff before commit
  for injection, path traversal, SSRF, IDOR, timing attacks and ReDoS.
- **[tdd](skills/engineering/tdd/SKILL.md)**: Test-driven development as a red-green loop: tests
  through agreed seams, one test then one minimal implementation per cycle, and the
  anti-patterns that make tests worthless.
- **[test-synthesizer](skills/engineering/test-synthesizer/SKILL.md)**: Add the boundary and
  adversarial test cases a happy-path suite misses, chosen from the inputs the code really accepts.
- **[todo](skills/engineering/todo/SKILL.md)**: Work a repo's engineering backlog in `TODO.md`:
  show what is open as ready, needs-your-call and blocked tables, add, work, update and close
  items, and groom the file for stale content and a backlog you can hold in your head. Each
  repo's `TODO.md` header declares its own areas and gate tags.
- **[type-tightener](skills/engineering/type-tightener/SKILL.md)**: Replace `any`, unchecked casts
  and ignore directives with strict types, schemas and discriminated unions, then typecheck.
- **[ui-craft](skills/engineering/ui-craft/SKILL.md)**: Build polished, accessible web UI from the
  project's own design system, with spacing, color, interaction-state and accessibility defaults
  when it has none.
- **[walkthrough](skills/engineering/walkthrough/SKILL.md)**: Write a linear walkthrough of a
  change, feature or module in execution order. Every code excerpt comes from a command such as
  `sed -n` or `git show`, never retyped, and the result is saved to a private temporary
  Markdown file.

## Productivity

### Model-invoked

- **[find-skills](skills/productivity/find-skills/SKILL.md)**: Find and install agent skills when
  asked for one. It installs only a skill the user approves by name, then reads it and reports
  what it can run.
- **[handoff](skills/productivity/handoff/SKILL.md)**: Summarize the current session so a fresh
  agent can continue. It prints the handoff in chat, copies the same text to the clipboard, and
  saves a temporary Markdown file with a clickable path. Clipboard copying uses `pbcopy` on
  macOS; if it fails, the agent reports the failure and still provides the chat output and file.
  Inside Herdr, it offers to start the next session in a new tab with the handoff as its first
  prompt.
- **[huddle](skills/productivity/huddle/SKILL.md)**: Get a team of agents on the same play in one
  short exchange. The orchestrator sends the situation, the play (who does what, which paths each
  owns, in what order) and the start signal; each agent reads back its part; and a break message
  corrects mismatches, credits specific work and starts the play. Harness-neutral, with a short
  section for Herdr.
- **[summarize](skills/productivity/summarize/SKILL.md)**: Summarize a document, plan, diff or
  thread in plain English with full coverage, for a reader who did not watch the work.

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

The repository layout follows [mattpocock/skills](https://github.com/mattpocock/skills).

## License

[MIT](LICENSE)
