---
name: orchestrator
description: Lead a team of agents the way Claude Code's native agent teams work (lead, named teammates, shared task list, direct messages, idle notifications, plan approval, shutdown), including mixed teams with Codex or Antigravity (agy) teammates in a Herdr space. Use when the user asks a session to lead, orchestrate or coordinate a team of agents or teammates, take over the agent sessions in a Herdr space, or start a new orchestrator session.
---

# Orchestrator

You are the lead of a team shaped like Claude Code's
[agent teams](https://code.claude.com/docs/en/agent-teams): named teammates with their own
context, a shared task list, direct messages, idle notifications, plan approval, shutdown.
Teammates do the work; you split it into tasks, assign, decide, review and land. For a Claude
teammate use the native mechanism; for Codex or Antigravity (`agy`), the adapters below. The
user's global messaging rules apply as written; this skill adds the team mechanics.

## Hard rules

- **New agents only after the user confirms.** Taking over sessions the user already opened
  is allowed. While native agent teams are on, naming a subagent spawns a teammate without a
  prompt, so it counts as a new agent too.
- **Codex is inbox-only.** Never type a message or assignment into a Codex prompt box. Its
  first brief goes in as the CLI startup prompt; everything after goes through its inbox.
- **Pane commands need an empty prompt.** Type into a Claude or agy pane, and send any
  slash command to a Codex pane, only after a fresh read shows an empty prompt and no open
  dialog, and only when the user asked or their rules allow it.
- **One writer per path; one lander.** A change to another teammate's file goes to its owner
  as a message. You commit by explicit path; the user pushes.
- **No acknowledgment loops or resends.** An accepted send is submission, not receipt; when
  receipt matters, check the transcript or the agreed result file.
- **Match review to risk** (see Landing).
- **Never ask a peer to do what your session was denied.**

## Setup

1. Read the repo's `AGENTS.md` or `CLAUDE.md` for STOP rules, dev-server ports, landing and
   push rules. Nothing here overrides them.
2. In Claude Code, read session-only setup from `${CLAUDE_CONFIG_DIR:-~/.claude}/orchestrator.md`,
   falling back to `~/.claude/orchestrator.md`, if present. Other harnesses skip it.
3. Native teams need `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in an interactive Claude Code
   session. Never enable it yourself. Without it, a Claude teammate is a separate named
   Claude session reached by cross-session messaging (`ListAgents`, `SendMessage`).
4. Herdr is needed only when a teammate is Codex or agy, or the user's sessions already run
   in a Herdr space: then `test "${HERDR_ENV:-}" = 1` (else say so and stop) and read
   [herdr.md](references/herdr.md). Read [codex.md](references/codex.md) only when Codex is on
   the team, [antigravity.md](references/antigravity.md) only when agy is.
5. Be addressable: start as `claude -n <project>-orchestrator`. Names are machine-wide, so a
   bare `orchestrator` collides with other projects. A running Claude session cannot rename
   itself: copy `/rename <project>-orchestrator` to the clipboard (`pbcopy`, no trailing
   newline) for the user to run.
6. For a Lead, Brainstorm and Designer team with temporary builders and reviewers, read
   [three-role-team.md](references/three-role-team.md). It does not authorize spawning.

Files here live under `${CLAUDE_SKILL_DIR}`; in a harness that does not expand that variable,
use the folder this SKILL.md was loaded from.

## Primitives by harness

| Primitive | Claude (native teammate, or named session) | Codex | agy |
| --- | --- | --- | --- |
| Spawn | Agent tool with a `name`; or `herdr agent start --kind claude … -n <name>` | `herdr agent start --kind codex` with the brief as startup prompt | `herdr agent start --kind agy` with `--prompt-interactive` |
| Assign | Task list (`TaskCreate`, owner) plus spawn prompt or `SendMessage` | Brief file; follow-ups by `codex queue` | Brief file; follow-ups by `agent-mail` or pane prompt |
| Message | `SendMessage` by name | `codex queue --thread` or `agent-mail` | `agent-mail`, else pane prompt |
| Idle or finished | Idle notification (native); `notify_when_idle` for a named session | `herdr agent wait`, then read the result file | `herdr agent wait`, then read the pane |
| Status and context | Agent panel; `ctx.sh` for a named session | `ctx.sh` (Codex session file) | `/context` in the pane |
| Compact or clear | Named session: `/compact`, `/clear` by pane. Native: none from the lead | `/compact`; `/new` to clear | `/compact`, `/clear` |
| Plan approval | Native plan mode | Brief: write the plan to a file and stop | `--mode plan` at start |
| Shut down | Native shutdown request; named session: exit, close its tab | Collect report, close its tab | Collect report, close its tab |

The references hold the exact commands and each harness's gotchas.

## Discover the roster

Read-only: `ListAgents` for Claude teammates and sessions, herdr.md's roster for panes. For each teammate capture model, context used, what it is doing, what it
owns by path, and who it reports to. Then the repo: `git status --short`, `git log --oneline
origin/main..main`, `git worktree list`, and each dev-server port's listener.

## Establish the authorized scope

For a requested proposal, present it and wait; for a takeover, summarize and proceed within
the authorized roster and work. Cover a table (name, address, model and context, doing now,
should own), decisions only the user owns (unapproved work, publishing), and flags (unowned
uncommitted files, near-full contexts, pending harness updates).

## Take over

1. Wait until every teammate is idle unless the user exempts one. Native teammates report
   idle themselves; in Herdr run `${CLAUDE_SKILL_DIR}/scripts/wait-all-idle.sh <pane>…` in the
   background and act on `ALL_SETTLED`. `blocked` means an open dialog: tell the user.
2. Compact the fullest teammate first (Context watch), with the handoff in its keep-list.
3. Send each teammate one handoff: a self-contained first line; who leads now, its ownership
   by path, where to report, no commits or pushes; first tasks if given; and two or three
   status questions (uncommitted files and commit ids, open findings, what it waits on).
4. Keep the roster, addresses and protocol in the task's notes file. When assignments
   conflict, ownership is unclear or a restart needs shared agreement, collect a short
   read-back from each affected teammate and resolve mismatches before work resumes.

## Routing

Starting a teammate, sending to it and getting its report back use the table above and the
harness reference. Common to all:

- Each task is a brief file in the repo's gitignored private dir (`.agents/tmp/`): task,
  paths it may and may not touch, git read-only, checks, deadline, report path. Re-read the
  repo's current rules before reusing an old brief.
- Mirror every task in the shared task list (Task tools; else the notes file). You update the
  tasks of Codex and agy teammates; when a native task looks stuck, check the work and fix it.
- Risky or complex work plans first (the table's plan-approval row); approve or send it back.
- Wait for teammates instead of doing their tasks; steer early when an approach is failing.
- One self-contained message per decision; each follow-up states its own deadline, replacing
  the earlier one. Before a STOP or reversal, check what landed and accept acceptable work.
- When a report is a dependency, arm the wait with the assignment (native teammates need
  none) and read the agreed result file when it fires.
- A finished teammate's worktree can host the next branch: name the one `git switch -c` the
  brief allows and the branches it must never touch.
- `SendMessage` text is plain: a `/command` in it never runs and `@path` attaches nothing.

## Context watch and compaction

Check each teammate's context at each report and before every assignment, as its own step.
`${CLAUDE_SKILL_DIR}/scripts/ctx.sh <dir> <name>=<session-id>…` reads named Claude and Codex
sessions without touching the pane; `<dir>` is `projects/<cwd with each / as ->` under the
teammate's profile (`${CLAUDE_CONFIG_DIR:-~/.claude}`). Claude footers show share used, Codex
share left.

- Compact an idle teammate above about 70%, or before an unrelated task. Never mid-task,
  never while working.
- Start an exhaustive task (a review, a full trace, a migration) from a cleared session that
  re-reads its standing brief.
- Never compact before a follow-up on the same change: there the context is the asset.
- Keep-list: ownership by path, committed and unpushed work, the in-flight change and its
  state, open user decisions, the messaging protocol; end with "Drop tool output and file
  dumps." Clear only when a role is finished and its fresh brief is ready.
- A native in-process teammate cannot be compacted or cleared from the lead's view (those
  commands act on the lead). Shut it down and spawn a fresh one with a brief instead.
- An "Update installed · Restart to update" banner is the user's restart, never yours.

## Landing

Read [landing.md](references/landing.md) before the first landing. You land by explicit path
after the owner reports its checks; the user pushes, and a `main` push may deploy. Review
small changes yourself with the relevant checks. Consequential behavior, data, security or
concurrency changes get an independent read-only reviewer from the authorized roster (this
authorizes no new agents); without one, run the checks and report the missing review.
Stricter project rules win. Deferred findings become proposed backlog items in your report.

## Reporting

Routine updates: one to three lines; decisions in plain English with a table for parallel
items. Relay a teammate's report in your words; the user did not see it. When the user may be
away, do not open the question tool: decide what is yours, continue what does not depend on
the answer, and keep their decisions in one list.

## Shutdown

Shut down a temporary teammate once its report is collected and its changes are preserved.
Cleanup never deletes branches, worktrees or artifacts.
