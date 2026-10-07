---
name: orchestrator
description: Take over and run a Herdr space of named agent sessions as its orchestrator — discover the roster, map ownership, hand coordination over, route work through inboxes, watch context and compact, land by path. Use when the user asks a session to orchestrate or coordinate the agents in a Herdr space, or starts a new orchestrator session.
---

# Orchestrator

You coordinate; the specialist sessions do the work. Your turns are the scarce resource:
relay, decide, land, and keep your own context for decisions. Written from a takeover
of five agents on 2026-09-30 (deck, site, qa, workhorse, harness).

## 1. Preconditions

- `test "${HERDR_ENV:-}" = 1`, or say you are outside Herdr and stop.
- Name this session so peers can address it: `/rename <project>-orchestrator` (the user
  types it, or asks for it). `ListAgents` then shows the name on its first line. Session
  names are machine-wide: a bare `orchestrator` collides with another project's (seen
  2026-10-01, on two projects).
- Read the repo's `AGENTS.md` for STOP rules, dev-server ports, landing and push rules.
  Nothing here overrides them.

## 2. Discover the roster (read-only)

```bash
herdr agent list | jq -r '.result.agents[] | select(.workspace_id=="'"$HERDR_WORKSPACE_ID"'") | "\(.pane_id)\t\(.terminal_title_stripped)\t\(.agent)\t\(.agent_status)"'
herdr tab list        # tab labels are the roles (deck, site, qa, workhorse, harness…)
```

Then `ListAgents` for the message addresses. A Claude session's address is its `/rename`
or `--name` name; an unnamed one shows as `<dir>-<xx>`. Match unnamed rows to panes from
context (another agent's "sent to <project>-0d" line, start times, cwd), or ask the user
to `/rename` each tab to its label. Codex panes never appear in `ListAgents`.

Per agent, read the visible screen (`--lines` fails while an agent is working):

```bash
herdr agent read <pane> --source visible
```

Capture: model, the footer's `Ctx Used` percent, what it is doing, what it owns (its
assignment text usually names paths), and who it reports to. Then the repo:
`git status --short`, `git log --oneline origin/main..main`, `git worktree list`, and
`lsof -nP -iTCP:<port> -sTCP:LISTEN` for each dev-server port.

## 3. Propose before touching anything

Answer "do you accept?" with a plain-English proposal and wait for the go:

1. A table: tab, address, model and context used, doing now, should own.
2. The rules: handoff first (one coordinator; the interim coordinator returns to its
   specialty); one writer per path, changes to another's file go to its owner as a
   message; inboxes, not pane typing; one lander, the user pushes; no polling, agents
   report when done; idle agents stay idle until a well-specified job exists.
3. The decisions only the user owns (go on the handoff, push timing, open calls).
4. Flags: unowned uncommitted files, near-full contexts, pending harness updates.

## 4. Take over

1. **Wait for idle** unless the user exempts an agent.
   `${CLAUDE_SKILL_DIR}/scripts/wait-all-idle.sh <pane>…` polls `herdr agent get` and blocks
   on `herdr agent wait`; run it in the background and act when it prints `ALL_SETTLED`.
   `blocked` means a dialog is open: stop and tell the user.
2. **Compact the fullest agent first** (section 6), with the handoff in its keep-list.
3. **Send the handoff** to each Claude agent with `SendMessage`. First line
   self-contained. Body: who coordinates now, its ownership by path, report to this
   session's name, do not commit, no pushes, SendMessage only, and two or three status
   questions (uncommitted files with commit ids, open findings, what it waits on).
4. **First tasks** go out in the same message when the user has given them.
5. Record the roster, addresses and protocol in memory: sessions restart.
6. **Huddle** with the huddle skill once the handoffs are acknowledged, and again whenever a
   goal starts, the phase changes (build, review, land), a setback lands or agents drift or
   collide: one play to everyone, a read-back from each, then the break.

## 5. Routing

- **Claude → Claude:** `SendMessage`. A message is plain text; a `/command` inside it never
  runs, and `@path` attaches nothing. Send the text itself or name an absolute path.
- **Commands to a Claude session** (`/compact`, `/clear`): only by pane, only when the
  user asked or the user's rules allow it, only after reading the pane shows an
  empty prompt and no dialog:
  `herdr agent prompt <pane> '/compact <keep-list>' --wait --timeout 300000`. Keep the
  text on one line and under about 500 characters: a longer paste collapses into a
  "[Pasted text]" placeholder and the command is not recognized, so the agent answers it
  as a message instead (seen 2026-09-30). A harness notice above the prompt with numbered
  choices (a "Heads up" line, a survey, an update question) is an open dialog even when the
  status is `done`: do not type, send the work through the inbox uncompacted, and tell the
  user what the notice says (seen 2026-10-06). Verify afterwards: the screen shows `Compacted`;
  if not, resend shorter. The footer and `ctx.sh` keep the old figure until the
  agent's next turn, so neither is the receipt.
- **Claude → Codex:** `codex queue --thread <uuid-or-name> --message <text>` when the
  thread is known; otherwise `herdr agent prompt <pane> "$(cat <assignment-file>)"` at an
  empty prompt. Confirm it started: `herdr agent wait <pane> --until working --timeout 20000`.
  A Codex session with no turn yet has no thread: the queue answers
  `No active session found matching '<name>'`, so its first message goes through the pane.
  After that a name can still be refused with `Cannot verify a unique session label across
  server pages; matching session UUID: <uuid>`; that id works once the session file for it
  under `~/.codex/sessions` shows text only you sent (seen 2026-10-01).
- **Codex → Codex orchestrator:** `codex queue --thread <coordinator UUID> --message <text>`.
  It works between existing Codex sessions, including while the coordinator is working.
  Give peers the new UUID on takeover; their old Claude relay cannot reach the replacement.
  A successful queue result confirms submission, not receipt: confirm an acknowledgment or
  the destination transcript. Keep the report file too, since replies may await a turn boundary.
  If a queue is accepted but an interrupted Codex thread does not receive it, check the
  thread with `mcp__codex_tui__read_thread`, then use the available
  `mcp__codex_tui__send_message_to_thread` inbox (prompt under 1,000 UTF-8 bytes).
  Verify the new turn or acknowledgment; do not type into its pane while an inbox works.
- **Codex → Claude orchestrator, file:** assignments say "write the report to
  `.agents/tmp/<name>-report.md`, then stop"; you wait with
  `herdr agent prompt … --wait` or `herdr agent wait <pane>` in the background.
  Give that path only to a Codex session that can write it: a YOLO one
  (`--dangerously-bypass-approvals-and-sandbox`, shown by `herdr pane process-info --pane
  <pane>`) can, but a sandboxed one refuses every write under `.agents/` unless it was started
  with `--add-dir <repo>/.agents/tmp` (keep that recipe in the repo's own harness notes).
  Otherwise ask for the report as its final reply and read it with
  `herdr agent read <pane> --source recent-unwrapped`.
- **Codex → Claude orchestrator, live:** when a reply in your inbox is worth about two cents, give the
  Codex session a one-shot relay to run: `claude -p --model haiku --tools
  ListAgents,SendMessage --allowedTools "ListAgents SendMessage" --strict-mcp-config
  --no-session-persistence "<prompt>"`, where the prompt says to call SendMessage once with
  your session's name and the message copied between unique markers. Test it from your
  own shell first. It addresses you by name: after a `/rename` tell the Codex session the
  new name, and give it the `[ref]` when another session shares that name (seen
  2026-10-01, where two sessions were both `orchestrator`).
- **A new Codex worker** (only after the user confirms it): `herdr tab create --workspace
  <ws> --cwd <worktree> --label <name> --no-focus`, then `herdr agent start <name> --kind
  codex --pane <root pane> -- <the flags the user's own Codex sessions run with>`. Read
  the screen for the model, an empty prompt and no dialog, prompt once with one line that
  names an absolute assignment file, and arm `herdr agent wait <name>` in the background.
  The fsd skill's `references/herdr.md` has the full procedure (used 2026-10-01).
  Keep the name under about 32 characters: a longer one starts, then every later
  `herdr agent` call answers `agent_not_found`. To change a running Codex session's model or
  effort, submit `herdr agent prompt <pane> '/model'` at an empty prompt with no dialog
  (a queued message cannot carry the setting). `send-keys` accepts picker keys, not a
  pasted `/model` command. In the picker, Enter may write the choice into `~/.codex/config.toml` as everyone's
  default; press `s` for "this session only", and check the config file afterwards. Its thread id for `codex queue` is the `id`
  on the first line of its session file under `~/.codex/sessions/<year>/<month>/<day>/`,
  matched by `cwd`.
- Before the first prompt to a Codex worker, read its footer for the model: a repo's
  `.codex/config.toml` can pin a different model than `~/.codex/config.toml`, so pass
  `-m <model>` when the user named one (seen 2026-10-02: the repo pinned one model and the user asked for another).
- A worker stops at the deadline in its first brief. Every follow-up brief states a new
  deadline and says the earlier one no longer applies, or the worker reads it and stops.
- Arm one background wait per worker (`herdr agent wait` in a loop that re-checks status);
  zsh has no `wait -n`. Under a cap on concurrent workers, write each pending send into the
  notes file and send it when a wait fires.
- A finished worker's worktree can host the next branch: name the one `git switch -c` the
  brief allows, and say which finished branches there must never be committed to or deleted.
- Assignment files live in the repo's gitignored private dir (`.agents/tmp/`, for example):
  task, files it may touch, files it must not, git read-only, checks, report path.
  A brief copied from an earlier one goes stale: re-read the repo's current skills for
  every rule it quotes (databases, servers, sign-in) before sending it.
- Verify receipt from the tool result, output or an acknowledgment before reporting
  delivery; a sent message is not a read one.
- Never ask a peer to do what your session was denied.

A Claude prompt box can show a dim suggestion of the next input (often your own last
`/compact`) that a plain read cannot tell from typed text. Read the pane with
`herdr agent read <pane> --source visible --ansi`: text wrapped in the faint code (`ESC[2m`)
is a suggestion and the box is empty; anything else is someone's unsent input, so do not type.

## 6. Context watch and compaction

Part of the job: check every agent's context at each report and before each new
assignment. The pane footer's `Ctx Used` truncates when the pane is narrow, so read the
transcripts instead: `${CLAUDE_SKILL_DIR}/scripts/ctx.sh ~/.claude/projects/<dir>
deck=<session-id> …` (in a harness that does not expand `${CLAUDE_SKILL_DIR}`, use the folder
this file was loaded from), with
session ids from `herdr agent list` (`.agent_session.value`). It works while agents are
busy and costs them nothing.

- Compact when an agent is idle, above about 70%, and at a task boundary. Never
  mid-task, never while `working`.
- Before a new assignment, ask whether what the agent holds helps with it, not only how full
  it is. A Claude footer shows the share used; a Codex footer shows the share left.
  - An unrelated task, with more than about 40% used: compact first. The old context is
    dead weight for the new job.
  - An exhaustive task (a review, a full trace of a code path, a migration): start it from a
    cleared session that re-reads its standing brief, whatever the fill level.
  - A follow-up on the same change (a fix round, a re-check): never compact first. There the
    context is the asset.
  Seen 2026-10-05: a researcher at 42% used was given a full removal map, ran out
  mid-task and compacted itself, which is the one moment nobody chooses the keep-list.
- Before compacting, message the agent to run the `refine` skill and reply with its
  `Memory:` and `Skill:` lines; compact once it is idle again. The user's rule is refine
  before compaction, and an agent compacted from outside gets no other chance.
- The keep-list names: its ownership by path, what is committed and unpushed, the
  in-flight change and its state, open user decisions, the messaging protocol.
  End with "Drop tool output and file dumps."
- `/clear` only when a role is finished and a fresh brief is ready to send; it starts a
  new conversation and the agent forgets everything but project memory.
- An "Update installed · Restart to update" banner is the user's restart, never yours.
- Check a worker's context in its own step before the send. Reading the footer in the same
  command that queues the assignment is not a check. Seen 2026-10-06: a reviewer was twice
  handed a large review with about a third of its context left.
- A Codex pane showing "New activity · Earlier messages available" is only its transcript
  view; with the prompt line empty, `/compact` typed there worked every time (2026-10-06). A
  Claude pane with a numbered harness notice is different: see section 5.

## 7. Landing and pushing

One lander, you. Commit by explicit path with the repo's ship procedure after the owner
reports its checks; never stage another agent's file into someone else's commit. A
shared checkout has one index, so two agents committing at once collide. The user
pushes; a `main` push may deploy. Deferred findings become proposed backlog items in your report, not silence;
they go into the backlog when the user says go.

Before landing, a fresh read-only reviewer reads the change. While it reads, the builder
holds its edits; afterwards send one fix list as a file: the findings with their line
numbers, plus your decisions on what the builder left open. Send a second fresh reviewer at
fixes for data loss or secrets, and for any round after that resume that reviewer, so it
re-runs its own probes: a fix round can add a defect. Run the root check and any browser check yourself before
you call a change ready: a worker's exit code is a claim.

Before a merge, `git merge-tree --write-tree main <branch>` shows whether it conflicts without
touching anything; `git merge -F -` does not read stdin, so write the message to a file. Two
branches that each delete neighbouring closed sections of a shared note conflict: remove all of
them. A branch cut before a repo-wide change (a fence, a rename) can bring a file that misses
it: grep for stragglers after the merge. For a small fix after a second review, read the diff
yourself; resuming a reviewer costs its whole context again.

Design documents for the user (a spec, a decisions list, a proof) get a fresh skeptic
reader before they see them, who re-runs the proof and attacks it, then the author revises and
keeps the first version beside it. A finding a buyer or a model could turn on (lexical checks,
for example) gets a reachability check before it is ranked.

When the change talks to an outside service, exercise that path once with the real
credentials right after the deploy; a health check is not that. Seen 2026-10-01:
every test and both reviews passed while production showed nothing, because the provider
refused one field of the query to the app's token, and the tests had only made-up answers.

The hosting is an outside service too. When a fix leans on a property of the database or
the platform (a session setting, a timeout, a pooler, how long a function lives after its
response), ask the real one, read-only, before the fix is built. Seen 2026-10-02:
three reviewers passed a lock-timeout fix on a local Postgres; the hosted pooler dropped
the setting without an error, and `show lock_timeout` there answered `0`.

A reviewer reads a detached snapshot of the builder's head (`git worktree add --detach`),
so the builder never waits; move it with `git checkout --detach <new head>` for a re-check,
which leaves the reviewer's untracked probe scripts in place so it re-runs them unchanged.
Logic that reconciles reads over time (event identities, boundaries, "what was already
seen") takes several rounds: on milton the reader went 8, 3, 1 and 0 findings, then its list
4, 3, 2, 1 and 0. When a fix round adds a defect, have the builder write the rule as a table
before touching code again; the next round shrank every time that was done.

When the user says "land and push" before a verdict is in, hold the words, say so, and carry
them out on a clean verdict without asking again; on any finding, come back instead.

`secret-scrubber` reads only the uncommitted or staged diff: on a clean checkout it prints OK
without scanning anything. For a branch that is already committed, copy the script beside a
short Bun script that pipes `git diff main <branch>` into its exported `scanDiff`, and run it
with `bun --no-env-file` outside the repository.

After a push, `vercel inspect <domain> --scope <team>` names the deployment that domain
serves and its state. `vercel ls` writes its table to stderr, so a poll that drops stderr
sees nothing and ends at once. A project deployed by hand with `vercel deploy` is not built
by a push: list its deployments before reporting it shipped.

To land a branch of many commits as one, run `git merge --squash <branch>` in the main
checkout and commit with `-F <message file>`; `git diff --quiet HEAD <branch>` afterwards
proves the landed tree is the one the reviewer tested.

When a fix you asked for adds machinery and the next review finds a race in it, ask first
whether the product can live without the machinery. Seen 2026-10-05: a deadline
added in one fix round raced the commit it guarded; removing it, and saying plainly what a
stopped run leaves behind, ended the loop that repairing it would have continued.

Order a multi-commit assignment so the part that stands alone comes first, and ask the
builder for a message at that commit. The reviewer reads it from a snapshot while the builder
continues, and it can land by itself if the rest stalls.

A check that fails in the main checkout right after a fast-forward may be the checkout, not
the change: its installed packages go stale while agents install only in their worktrees.
Compare the error with the lockfile before blaming the change, and do not reinstall under the
user's running dev server. Seen 2026-10-05: a missing test dependency failed the type check
and five test files on a tree that had passed in two fresh worktrees.

When your own shell refuses a check (a safety rule that cannot parse the script), do not
rephrase it to get through. The reviewer's run is the independent evidence, and your report
says you did not run it.

When main has moved since a branch was cut (another landing, a backlog commit), it no
longer fast-forwards. Apply its commits with `git cherry-pick <base>..<head>`, which keeps
each one, and prove the result on the paths the branch owns:
`git diff --quiet HEAD <head> -- <those paths>`. A branch stacked on an unlanded one lands the
same way after its base.

A preview serves whatever was last built in its worktree. While a designer, a reviewer or
you are checking one, tell the builder to hold: no branch switch and no build there until
the checks are done.

Arm the wait in the same turn as the send, every time, and for a reviewer too. Seen
2026-10-05: a review finished and sat unread for three hours because its send went out
without one, while a later assignment to the builder was built on the unreviewed branch.

A hosting variable marked sensitive cannot be read back: `vercel env pull` writes
`[SENSITIVE]` for it, so "change one word" means re-entering the whole value with
`vercel env update <name> production` from stdin, and only from a source you can trust for
the full value. `vercel redeploy <deployment> --target production --non-interactive` then
applies it without a push, and the earlier deployment keeps the old value for a rollback.

On a landing that later landings build on (a schema, a wire shape), ask the builder for a
written proposal before any code, and have the reviewer read it against the specification.
Seen 2026-10-06: three schema defects were found before a migration existed. Give a
specification the same treatment: each of three outside reads of one found real defects.

Deleting a directory deletes its `.gitignore` too. After landing a removal, run `git status`
in the main checkout: untracked leftovers the ignore file was hiding (once, a token file from
a live run) reappear and can be staged by accident.

A migration file does not change after it is applied. A wording fix a reviewer asks for goes
in before the landing, and the hash to expect in the journal changes with it: recompute it.

To apply a migration around a scheduled job, take a read-only baseline, wait until the job's
lease has cleared, apply, and compare with the baseline. Explain every count that moved before
calling it clean (once, a row the job itself wrote seconds earlier).

When you replace a section of a shared backlog file by slicing between two headings, list the
items filed there first. Seen 2026-10-06: an open item that lived under the heading was
deleted with the section and had to be restored in the next commit.

## 8. Reporting to the user

Routine updates: one to three lines. Anything the user decides on: plain English,
a table for parallel items, decisions called out. Report outcomes with exit codes and
what was not verified, then the calibrated confidence line the user expects.
Relay a peer's report in your words; the user did not see the message.

To show the user a builder's screens, copy the screenshots to a stable folder and open
them. A path inside another session's scratchpad is not something they can use, and a
signed-in local preview needs a session cookie that would replace their own, because browsers
share localhost cookies across ports.

For a live look, have the builder run a small local proxy on its own port that adds a
synthetic account's session to each request: the user opens that address and their own
browser needs no cookie. Give them screenshots as well, in case the preview is stopped.

A breakpoint on width alone also catches a phone turned on its side. When a handoff
names one, ask what a short screen gets (a sideways phone, a tablet with its keyboard up)
before the build, and put those sizes in the builder's preview checks.

Before designing what a product should notice, ask how that thing reaches the user today,
and on their word take a counts-only read of their real account. Seen 2026-10-06: one answer
("team requests and posts in a channel, never by name") and one probe (13 waiting, 10 of them
over a month old) each overturned a rule already written into a specification.

A user answering from a phone cannot open a local path. Publish rendered options as a private
page and give the link, with one line per choice and the recommendation marked.

Take every time you write into a state file from `date`. An estimated clock drifted two hours
in one working day.

When the user may be away, do not open the question tool: it blocks the session until
someone answers. Decide what is yours, carry on with what does not depend on the answer,
and keep the user's decisions in one list for their return.
