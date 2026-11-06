# Codex teammates

Codex runs in a Herdr pane (see herdr.md). Messages and assignments are inbox-only: the first
brief is the CLI startup prompt, everything after goes through `codex queue` or `agent-mail`.
Never `herdr agent prompt`, `send-keys` or pasted text for a message, not even when delivery
fails: leave it pending and report it.

## Spawn

- `herdr agent start <name> --kind codex --pane <root pane> -- <flags> 'Read /abs/brief.md and
  follow it.'` with the flags from the user's own Codex panes, minus `--no-daemon`: the pane
  shell's `codex` alias adds it, and a second copy fails with "cannot be used multiple times".
- Pass `-m <model>` when the user named one: a repo's `.codex/config.toml` can pin another.
  Read the footer for the model before relying on it.
- A new pane can open on an update dialog (`agent_not_ready`): read it, then
  `herdr pane send-keys <pane> esc`.
- Confirm the start with `herdr agent wait <pane> --until working --timeout 20000`.
- Once the first turn has created the thread, name it per [codex-title.md](codex-title.md).
- A read-only reviewer (`-s read-only -a never`) cannot reach Herdr or `agent-mail`: brief it to
  put the report in its final message and read it with `herdr agent read <pane> --source recent`.

## Message

- `codex queue --thread <session UUID or exact name> --message <text>`. The UUID is
  `.agent_session.value`, or the `id` on the first line of its session file under
  `~/.codex/sessions/<year>/<month>/<day>/`, matched by `cwd`.
- Before its first turn a session may have no thread (`No active session found matching`).
  That is not permission to type into its pane.
- `Cannot verify a unique session label …; matching session UUID: <uuid>`: use that UUID after
  its session file shows your brief.
- Codex reads queued mail only between turns, and a turn can last an hour. Your correction
  arrives after it acted on what you corrected; reconcile before sending more.
- Codex to a Codex lead: `codex queue --thread <lead UUID>` works while the lead is busy. Keep
  that UUID in the team plan and refresh it on takeover.

## Results back to a Claude lead

- File: "write the report to `.agents/tmp/<name>-report.md`, then stop"; wait on the pane.
  Only a session that can write there: a YOLO one (`--dangerously-bypass-approvals-and-sandbox`,
  visible in `herdr pane process-info`), or a sandboxed one started with
  `--add-dir <repo>/.agents/tmp`. Otherwise ask for the report as its final reply and read it
  with `--source recent-unwrapped`.
- Live plan-changing notice, when no inbox route exists and a relay is authorized: a one-shot
  `claude -p --model haiku --tools ListAgents,SendMessage --allowedTools "ListAgents SendMessage"
  --strict-mcp-config --no-session-persistence "<prompt>"` that calls `SendMessage` once with the
  lead's name and the text between unique markers. Test it from your shell first. After a
  `/rename`, tell Codex the new name; when two sessions share a name, give it the `[ref]`.

## agent-mail (optional)

When the user has `agent-mail`, follow the rules in `~/.agents/instructions/messaging.md`. To
Codex it delivers through `codex queue`; each message carries its reply command, so a Codex
teammate, sandboxed or not, answers with no setup. Address by pane id: Herdr names clear when
an agent is replaced. Claude to Claude stays on `SendMessage`.

## Status, compaction, clearing

- `ctx.sh` reads `~/.codex/sessions/*/*/*/rollout-*-<id>.jsonl`: share of the window used. The
  footer shows the share left.
- Slash commands only, at an empty prompt: a "New activity · Earlier messages available" line is
  only the transcript view; with the prompt line empty, `/compact` works.
- Model or effort: submit `/model` with `herdr agent prompt` (a queued message cannot carry the
  setting; `send-keys` takes picker keys, not a pasted command). In the picker press `s` for this
  session only, since Enter can make it everyone's default in `~/.codex/config.toml`; check that
  file afterwards.
- Clear with `/new` (Enter in its picker keeps the worktree). The new conversation starts on the
  config's default model: re-pick with `/model` and `s`, then queue the brief.
- A lone `/` sent with `send-keys` lands invisibly, and the next prompt submits `//new` as a
  message. Read with `--ansi` first: only a dim placeholder means empty.

## Plan approval and shutdown

- Plan first: the brief says "write the plan to `<path>` and stop". Approve or revise through
  the inbox.
- Shut down per herdr.md once the report is collected.
