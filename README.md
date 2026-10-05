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

- **[lean-build](skills/engineering/lean-build/SKILL.md)**: Build feature work with a high risk of
  overbuilding: derive acceptance and non-goals, deliver one narrow end-to-end path, leave out
  speculative options, and stop when acceptance passes.
- **[tdd](skills/engineering/tdd/SKILL.md)**: Test-driven development as a red-green loop: tests
  through agreed seams, one test then one minimal implementation per cycle, and the
  anti-patterns that make tests worthless.
- **[todo](skills/engineering/todo/SKILL.md)**: Work a repo's engineering backlog in `TODO.md`:
  show what is open as ready, needs-your-call and blocked tables, add, work, update and close
  items, and groom the file for stale content and a backlog you can hold in your head. Each
  repo's `TODO.md` header declares its own areas and gate tags.
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
