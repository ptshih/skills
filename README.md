# Skills

Personal agent skills by [Peter Shih](https://github.com/ptshih).

## Install

```bash
npx skills add ptshih/skills --skill handoff
```

## Handoff

[handoff](skills/handoff/SKILL.md) summarizes a session so a fresh agent can continue.
It prints the handoff in chat, copies the same text to the clipboard, and saves a
temporary Markdown file with a clickable path. Clipboard copying uses `pbcopy` on
macOS; if it fails, the agent reports the failure and still provides the chat output
and file.

Ask your agent:

> Use the handoff skill to prepare a fresh session focused on the remaining work.

## Attribution

The handoff skill is adapted from [Matt Pocock's handoff skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md),
with repository-state verification and chat, clipboard, and temporary-file output.
The [upstream MIT notice](skills/handoff/THIRD_PARTY_NOTICES.md) is included.
