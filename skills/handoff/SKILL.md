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

Adapted from [Matt Pocock's handoff skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md).
