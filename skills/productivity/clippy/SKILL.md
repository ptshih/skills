---
name: clippy
description: Preserve the current conversation's checkpoint directly before compaction, then tell the user which native command to run. Use when asked for Clippy, a compact command, or help preparing to compact. Clipboard output is available on explicit request. Does not execute compaction or start a replacement session.
---

# Clippy

Prepare the checkpoint yourself so the user can run the native compaction command
immediately. Do not require a clipboard, paste-back message or extra confirmation
turn by default. Keep this small; do not resume task work or turn it into repository
cleanup or another agent's handoff.

1. Preserve the objective, current state, settled decisions, ownership, unfinished
   work, approvals, constraints and relevant verification. Keep explicit pauses.
   Reconcile delayed messages against completed work; drop stale plans and tool dumps.
2. Update existing private checkpoint/coordination notes that this session owns,
   preserving collaborators' work. Use established locations rather than inventing
   another handoff. If no notes exist, preserve a concise checkpoint in the current
   conversation; create a private note only when useful and verify it stays out of
   version control. Never put private task details into this public skill.
3. Read back changed notes and confirm briefly that the checkpoint is preserved.
   Name the native compaction command the user can now run. For Codex CLI, say
   `You can run /compact now.` Do not ask the user to paste preservation instructions
   first, and do not claim that you pasted anything into their prompt box.
4. Stop and wait for the user. Clippy does not execute compaction, type into prompts,
   queue a self-message, restart a session, launch a replacement agent or change
   global compaction settings. Preserved notes are not proof that compaction ran.

## Explicit clipboard requests

If the user specifically asks for clipboard output, provide a tailored keep-list
as an additional output. Prefer fewer than 500 characters, without Markdown fences
or a trailing newline. Copy using a native clipboard tool; on macOS pass text to
`pbcopy` over stdin and compare `pbpaste` exactly, without printing prior clipboard
contents. Do not install utilities. If copying fails, report it and show the payload.

Use the harness's verified input format. For inline-capable commands, a tailored
`/compact Preserve ...` is appropriate. Codex CLI does not accept inline compaction
instructions: use a normal preservation message if the user explicitly wants that
workflow, and explain that `/compact` is a separate command. This optional workflow
must not replace direct checkpoint preservation by default.

Reuse verified harness knowledge; check local help/source or official documentation
only when uncertain. Verified 2026-10-31: Codex's
`SlashCommand::supports_inline_args` excludes `Compact`, and installed version
0.166.0 accepts only `threadId` in `ThreadCompactStartParams`. The
[CLI parser](https://github.com/openai/codex/blob/main/codex-rs/tui/src/slash_command.rs)
is the relevant source; Responses API compaction instructions are a different
interface. Recheck if a later CLI documents support for custom inline instructions.

For a fresh replacement conversation, use the available handoff workflow instead.
