# Antigravity (agy) teammates

agy runs in a Herdr pane (see herdr.md) with a 1M-token window. Its conversation lives in a
protobuf SQLite file that `ctx.sh` cannot read.

## Spawn and assign

- `herdr agent start <name> --kind agy --pane <root pane> -- --model <model> --effort <level>
  --prompt-interactive 'Read /abs/brief.md and follow it.'`. Add `--mode plan` for plan-first
  work; `--conversation <id>` resumes an earlier one.
- A fresh pane opens on a folder-trust dialog: read it, and send `enter` only when the read-back
  shows the trusted choice.
- A new assignment for an existing role goes in as a new session's startup brief. Record the
  previous conversation id first. Do not restart active work only to deliver a message.
- A file inbox must exist, with task-boundary read instructions in the brief, before launch;
  adding a file or editing the brief later does not notify a running agent.

## Message and wait

- `agent-mail` when the user has it (rules in `~/.agents/instructions/messaging.md`); it types
  only while Herdr reports agy settled and never later. Otherwise `herdr agent prompt` at an
  empty prompt with no dialog.
- agy's `idle` is a fallback (no matching rule in `herdr agent explain`): read the pane before
  typing.

## Context, compaction, clearing

Slash commands open a menu: `herdr agent prompt <pane> '/context'` only opens it, so follow with
`herdr agent send-keys <pane> enter`. Never send part of a command: the prompt always presses
Enter, which can complete a fragment (clear the box with `send-keys <pane> ctrl+u`).

- `/context` is local, no model call: read the overlay ("76.5k/1.0M tokens (7.3%)"), then
  `send-keys <pane> esc`.
- `/compact` runs the same way. Whether it takes a keep-list is unverified: send the keep-list as
  a message first.
- `/clear`: the first Enter only completes it into the box; a second Enter runs it. `/context`
  reading 0 tokens is the receipt.

## Shutdown

Per herdr.md once the report is collected.
