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

- **[todo](skills/engineering/todo/SKILL.md)**: Work a repo's engineering backlog in `TODO.md`:
  show what is open as ready, needs-your-call and blocked tables, add, work, update and close
  items, and groom the file for stale content and a backlog you can hold in your head. Each
  repo's `TODO.md` header declares its own areas and gate tags.

## Productivity

### Model-invoked

- **[handoff](skills/productivity/handoff/SKILL.md)**: Summarize the current session so a fresh
  agent can continue. It prints the handoff in chat, copies the same text to the clipboard, and
  saves a temporary Markdown file with a clickable path. Clipboard copying uses `pbcopy` on
  macOS; if it fails, the agent reports the failure and still provides the chat output and file.

## Attribution

The handoff skill is adapted from [Matt Pocock's handoff skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md),
with repository-state verification and chat, clipboard, and temporary-file output.
The [upstream MIT notice](skills/productivity/handoff/THIRD_PARTY_NOTICES.md) is included.

The repository layout follows [mattpocock/skills](https://github.com/mattpocock/skills).

## License

[MIT](LICENSE)
