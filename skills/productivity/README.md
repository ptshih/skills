# Productivity

General workflow tools, not code-specific.

## User-invoked

Reachable only by typing its name, such as `/retro`; the agent never starts it on its own.

- **[retro](./retro/SKILL.md)**: Review a coding session for what in the agent's setup slowed it down or let mistakes through, propose numbered changes with evidence, and apply only the ones the user picks.

- **[summarize](./summarize/SKILL.md)**: Summarize documents, plans, diffs or threads in plain English, concise by default and detailed when requested.

## Model-invoked

Model- or user-reachable: type `/<name>`, or the agent reaches for it when the request matches.

- **[clippy](./clippy/SKILL.md)**: Preserve the checkpoint directly, then let the user run native compaction; clipboard output only on request.
- **[find-skills](./find-skills/SKILL.md)**: Find and install requested skills after inspecting their instructions, respecting the selected skill and scope.
- **[handoff](./handoff/SKILL.md)**: Summarize the current session so a fresh agent can continue, in chat, on the clipboard and in a temporary Markdown file; inside Herdr, it offers to start the next session in a new tab.
- **[huddle](./huddle/SKILL.md)**: Align an existing authorized team when assignments conflict, ownership is unclear, a restart needs agreement, or the user requests a huddle.
- **[orchestrator](./orchestrator/SKILL.md)**: Lead an agent team modeled on Claude Code's native agent teams, with Codex or Antigravity teammates through Herdr: shared task list, inbox messages, context watch and compaction, then review and land by path.

