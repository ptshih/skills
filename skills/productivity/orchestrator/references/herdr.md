# Herdr panes

Used only when the team includes a Codex or agy teammate, or the user's sessions already
run in a Herdr space. Every command answers JSON; `herdr agent <cmd> --help` has the rest.

## Roster

```bash
herdr agent list | jq -r '.result.agents[] | select(.workspace_id=="'"$HERDR_WORKSPACE_ID"'") | "\(.pane_id)\t\(.terminal_title_stripped)\t\(.agent)\t\(.agent_status)"'
herdr tab list    # tab labels are the roles
```

- `ListAgents` gives Claude addresses: the `-n`/`/rename` name, or `<dir>-<xx>` when unnamed.
  Match unnamed rows to panes from context (cwd, start time, another agent's "sent to" line)
  or ask the user to `/rename` each tab to its label. Codex panes never appear in `ListAgents`.
- Session ids for `ctx.sh` and Codex threads: `.agent_session.value` from `herdr agent list`.
- Read a screen with `herdr agent read <pane> --source visible`; `--lines` fails while the agent
  works. A finished reply: `--source recent-unwrapped`.

## Naming

- Name agents role first and short; add a model suffix only for standing reviewers
  (`review-<model>`), and name temporary workers by task.
- One name under about 32 characters is the tab label, the Herdr agent name and the harness's
  own name. A longer one starts, then every later `herdr agent` call answers `agent_not_found`.
- Check `herdr agent list` and `ListAgents` for collisions before launch.
- Renaming yourself: get `tab_id` from `herdr agent get <pane>`, run `herdr agent rename <pane>
  <name>` and `herdr tab rename <tab_id> <name>`, then read back the session title, `herdr agent
  get` and `herdr tab get`. Report any name still waiting on the user.

## Spawning

- New tab: `herdr tab create --workspace <ws> --cwd <worktree> --label <name> --no-focus`, then
  `herdr agent start <name> --kind <claude|codex|agy> --pane <root pane> -- <flags> '<brief>'`,
  where the brief is `Read /absolute/path/to/brief.md and follow it.`
- Take flags from `herdr pane process-info --pane <pane>` on one of the user's own sessions.
- A Claude teammate gets `-n <name>`: that is its `SendMessage` address.
- `herdr agent start` can time out, or answer `agent_not_ready`, while the startup brief is
  already running. Read the pane and process arguments before any retry.
- Read the new screen to verify the model and that the brief began, then arm a wait.

## Typing into a pane

Only at an empty prompt with no open dialog (the hard rule), and never into Codex except
slash commands.

- `herdr agent prompt <pane> '<text>' --wait --timeout 300000`. It always presses Enter, so
  never send part of a command.
- Keep a command on one line under about 500 characters: a longer paste collapses into
  "[Pasted text]" and arrives as a message instead of a command.
- A dim suggestion in an empty box looks like typed text in a plain read. Read with
  `--source visible --ansi`: text in the faint code (`ESC[2m`) is a suggestion; anything else
  is someone's unsent input, so do not type.
- A harness notice above the prompt with numbered choices (a "Heads up", a survey, an update
  question) is an open dialog even when the status is `done`. Send the work through the inbox
  and tell the user what it says.
- `/compact` succeeded when the screen shows `Compacted`; the footer and `ctx.sh` keep the old
  figure until the next turn. If it did not, resend shorter.
- A folder-trust dialog on a fresh pane: answer only for the user's own repo, after reading back
  the selected choice.

## Waiting

- `herdr agent wait <pane> --timeout <ms>` matches idle, done or blocked. A finished Codex turn
  reports `done`, not `idle`. Arm a wait only after the pane shows `--until working`, or it
  settles on the earlier state.
- One background wait per teammate; zsh has no `wait -n`. Under a cap on concurrent teammates,
  queue pending sends in the notes file and send each when a wait fires.
- `${CLAUDE_SKILL_DIR}/scripts/wait-all-idle.sh [--timeout S] <pane>…` waits for all; exit 0 on
  `ALL_SETTLED` (blocked panes listed, not waited on), 2 on timeout.
- For a named Claude session, `SendMessage` with `notify_when_idle` works without Herdr.

## Shutting down

After the report is collected, its changes preserved and the pane idle: `herdr tab close
<tab_id>`. That ends the session only; never delete its branch, worktree or artifacts.
