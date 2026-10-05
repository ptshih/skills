---
name: handoff
description: Summarize the current session for another agent to continue. Use when the user asks for a handoff, a continuation prompt, or a summary for a fresh session.
---

# Session Handoff

Summarize the conversation so a fresh agent can continue the work.

Save the handoff as Markdown to a unique file in the OS temporary directory. Copy the
same text to the clipboard (`pbcopy` on macOS), then print it in chat with a link to
the file's absolute path. If clipboard access fails, say so and still provide the
chat output and file.

Tailor the handoff to the next session's purpose when the user provides one.

Suggest relevant available skills for the next agent.

Link to existing specs, plans, decisions, issues, commits, and diffs instead of
restating their contents.

Redact secrets and personal information.

For coding work, verify current repository state and clearly distinguish completed,
pending, and unverified work.

## On Herdr

When `HERDR_ENV` is `1`, end by offering in one line to start the next session in a new tab.
Do it when the user says yes, or asked for a new session up front:

1. Open a tab at the repository root without taking focus, and keep the returned root pane:
   `herdr tab create --workspace "$HERDR_WORKSPACE_ID" --cwd <repo root> --label <name> --no-focus`.
2. Start the harness the user named, or this session's own, with this session's flags (read
   them with `herdr pane process-info --pane "$HERDR_PANE_ID"`, leaving out `--resume`,
   `--continue` and `--name`): `herdr agent start <name> --kind <claude|codex|pi> --pane
   <root pane> -- <flags>`, plus `--name <name>` for Claude Code so its inbox answers to it.
   Names match `[a-z][a-z0-9_-]{0,31}`.
3. Read the screen before any input (`herdr agent read <name> --source visible`). Answer a
   folder-trust dialog only for the user's own repository, after reading back the selected
   choice.
4. Send one line that names the file, not the handoff text, since a long paste collapses into
   a placeholder: `herdr agent prompt <name> "Read <absolute path> and continue from it."
   --wait --until working --timeout 20000`.
5. Tell the user the tab label and the agent name. Leave this session running.

Adapted from [Matt Pocock's handoff skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md).
