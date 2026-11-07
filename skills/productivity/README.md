# Productivity

General workflow tools, not code-specific.

## User-invoked

Reachable only by typing its name, such as `/retro`; the agent never starts it on its own.

- **[grilling](./grilling/SKILL.md)**: Stress-test a plan, decision or idea one focused question at a time, with a recommendation for each, within the requested scope.

- **[retro](./retro/SKILL.md)**: Review a coding session for what in the agent's setup slowed it down or let mistakes through, propose numbered changes with evidence, and apply only the ones the user picks.

## Model-invoked

Model- or user-reachable: type `/<name>`, or the agent reaches for it when the request matches.

- **[clippy](./clippy/SKILL.md)**: Preserve the checkpoint directly, then let the user run native compaction; clipboard output only on request.
- **[handoff](./handoff/SKILL.md)**: Summarize the current session so a fresh agent can continue, in chat, on the clipboard and in a temporary Markdown file; inside Herdr, it offers to start the next session in a new tab.
- **[orchestrator](./orchestrator/SKILL.md)**: Lead an agent team modeled on Claude Code's native agent teams, with Codex or Antigravity teammates through Herdr: shared task list, inbox messages, context watch and compaction, then review and land by path.
- **[overlord](./overlord/SKILL.md)**: Watch the other agents in a workspace as the user's eyes and ears: flag unsafe actions, churn, overlapping work and git leftovers, keep the decision queue, and break ties between agents.

