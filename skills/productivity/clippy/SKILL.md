---
name: clippy
description: Prepare tailored compaction instructions for the current conversation and copy them to the user's clipboard. Use when asked for a compact command or help preparing to compact. Does not execute compaction or start a replacement session.
---

# Clippy

Put a useful, tailored compaction payload on the user's clipboard. A bare `/compact`
is not a tailored result. Keep this a small task; do not turn it into repository
cleanup or another agent's handoff.

1. Build a concise keep-list from the current conversation: objective, current state,
   settled decisions, ownership, unfinished work, authorization boundaries, and
   relevant verification. Preserve explicit pauses. Drop tool dumps and superseded
   plans. Use existing private state notes where useful; do not make the user repeat
   decisions or put private task details into this public skill.
2. Select the current harness's actual input format. Reuse verified knowledge;
   do not repeat a broad documentation search on every invocation. If uncertain,
   check local help/source or authoritative documentation, not merely an example's
   omission of arguments. Do not change global compaction settings.
   - When inline instructions are supported, copy one line such as
     `/compact Preserve <specific keep-list>. Drop tool dumps and stale plans.`
   - **Codex CLI:** `/compact` does not accept inline arguments. Copy a normal
     message beginning `Before I run /compact, preserve ...` with the tailored
     keep-list, ending `Do not resume work or compact yet; confirm briefly.` Tell
     the user to paste that message, wait for confirmation, then submit `/compact`
     separately. Do not label this message an executable compaction command.
   - For another harness with unsupported or unresolved inline syntax, use the
     same two-step preservation-message workflow, naming its verified native
     compaction action separately. If that action is unknown, disclose the gap.
3. Keep the payload preferably under 500 characters, without Markdown fences or a
   trailing newline. Private handoff paths supplement essential constraints; they
   do not replace all meaningful clipboard content. Never silently fall back to a
   bare command or pretend an unsupported suffix will guide native compaction.
4. Copy through an available native clipboard tool. On macOS use `pbcopy` with text
   supplied over stdin, not interpolated shell code. Read back with `pbpaste` and
   compare exactly, without printing previous clipboard contents. On other systems
   use an available native equivalent; do not install utilities. If copying fails,
   report it and provide the payload in chat. If the user cannot paste the copied
   content, show the exact payload rather than repeatedly asserting clipboard success.
5. Confirm what was copied and any separate execution step. A successful readback
   proves clipboard contents, not that compaction ran or preserved everything. Do
   not submit the payload, type into a prompt, queue it to an agent, restart a
   session, or launch a replacement agent.

Verified 2026-10-31: Codex's `SlashCommand::supports_inline_args` excludes `Compact`,
and the installed 0.166.0 `ThreadCompactStartParams` schema accepts only `threadId`.
The [CLI parser](https://github.com/openai/codex/blob/main/codex-rs/tui/src/slash_command.rs)
is the relevant source; the Responses API's compaction instructions are a different
interface. Recheck if a later CLI documents support for custom inline instructions.

For a fresh replacement conversation, use the available handoff workflow instead.
