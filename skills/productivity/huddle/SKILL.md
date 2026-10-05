---
name: huddle
description: Get every agent on a multi-agent team on the same page in one short exchange. The orchestrator sends one message with the situation, the play (who does what, which paths each owns, in what order) and the start signal; each agent reads back its part; then a break message corrects any mismatch, credits specific work and starts the play. Use when an orchestrator or lead agent kicks off a goal with several agents, changes phase (build, review, land), recovers from a setback, takes on a new or compacted teammate, or sees agents drift or collide, and when the user says "huddle", "huddle up", "call a play", "get everyone on the same page" or "rally the team".
---

# Huddle

A huddle is one short exchange between plays. The orchestrator calls the play, every agent
reads back its part, and the team breaks to work. It replaces a trickle of one-off messages that
each agent reads differently, and it ends with specific credit so each agent knows what to keep
doing.

Keep it short: every agent carries the huddle in its context for the rest of the play.

## When to call one

- A goal starts and more than one agent has a part.
- The phase changes: build to review, review to land.
- After a setback: a failed review, a reverted change, a broken build, a missed deadline.
- The roster changes: an agent joins, is compacted or cleared, or coordination is handed over
  (after the handoff message, not instead of it).
- Agents drift or collide: two writers on one path, duplicated work, conflicting assumptions.
- The user asks for one.

One agent's next task is a brief to that agent, not a huddle.

## 1. Check the play is yours to call

Call it yourself when the play only restates or reorders work the user already approved; fixing
a defect in approved work is not new work. A play that adds work, moves a path to a new owner,
changes a deadline, or touches something the user reserved (pushing, deploying, spending,
writing to anyone outside the team) goes to the user first, in plain English, and waits for the
go.

If the user is away, do not block on a question. Huddle on the approved part, hold the rest, and
keep it on the list of decisions for their return.

## 2. Scout first (read-only)

- **Roster.** Each agent's address, how it can reply to you, what it is doing now, and the paths
  it owns. Huddle only the agents with a row in the play; a row can be "hold" or "keep going on
  X" for an agent whose paths the play touches. Every other agent, idle or working, sits this
  one out.
- **Score.** What is done (commit ids), in flight, broken or blocked, and which user decisions
  are open. Take it from git and the agents' latest reports, not from memory.
- **Context.** An agent near the end of its context window will not hold the play. Compact it
  first, or leave it out of the play.
- **Timing.** Huddle between plays when you can. A message can reach a busy agent between its
  tool calls, which is why the SNAP tells it to finish its step first. If the reason is a
  collision, first send the agents involved a one-line stop.

## 3. Call the play

Send one message, the same text to every agent in the huddle, so each sees its neighbors' parts.
Number huddles so a later one can replace an earlier one, and keep the current number and play
in your compaction keep-list.

```text
HUDDLE <n>: <the goal in one line>

SITUATION
<Three to five lines: where we are, what changed since the last huddle,
what is broken or blocked, the deadline. When an agent had an earlier
huddle or brief, say "Replaces huddle <n-1> and any earlier brief, and
their deadlines.">

PLAY
| Agent | Does | Owns (paths) | Done when |
|-------|------|--------------|-----------|
| ...   | ...  | ...          | ...       |
Order: <who goes first, what waits on what>
Rules: <only the team rules this play could break: one writer per path,
who commits, no pushes>

SNAP
Now: finish the step you are on, read back, then hold.
Start: on BREAK <n>, not before.
Reply by: <each agent's route to you, e.g. "claude: message <your
address>; codex: write <path>, then stop">
Report: by the same route when done, when blocked, or when you find
something that changes the play.

READ BACK
Reply with three lines, then wait for BREAK <n>:
1. My part: <what you will do and the paths you own>
2. First move: <the first concrete step>
3. Concern: <what is wrong or missing in the play, or "none">
```

When a path changes owner, the play says where the old owner's uncommitted edits there go: to the
new owner, as a message or a diff, never reverted.

Keep the message under about 40 lines. A play with more than about six rows is two huddles, or a
spec that the huddle points to by path.

## 4. Collect the read-backs

Wait for every read-back; agents reply when they get the message, so do not chase them with
status messages. Check each against the play:

- **Matches:** nothing to do.
- **Mismatch** (wrong path, wrong order, wrong finish line): correct it in the break, addressed
  to that agent. When the correction changes its paths or finish line, ask it for a fresh
  read-back before the break.
- **Concern:** decide it when step 1 says it is yours, otherwise take it to the user. When the
  answer changes more than one agent's part, call a new huddle instead of patching this one.
- **No reply:** look at the agent before assuming anything; it may be busy, stuck on a dialog or
  out of context, or the message may be held for its owner's approval. Do not break without it
  unless you take it out of the play and say so in the break.

## 5. Break

Send one message to the same agents:

```text
BREAK <n>
Changes: <corrections from the read-backs, or "none, play as called">

<agent>: <one specific thing it did and why it mattered>
<agent>: ...

<one line on what this play gets the team>
Ready... break!
```

The credit is information, not cheering: it tells each agent what to keep doing.

- Name the work and its effect: "deck: you caught the stale price on slide 4 before it shipped.
  Bring that eye to the pricing table."
- Take it from the record: a commit, a report, a finding. At a kickoff, a read-back that
  improved the play counts. Never invent it, and skip an agent with nothing real to credit
  rather than padding.
- No ranking and no generic praise ("great job, everyone").

The rally line ties the play to the goal ("One clean review from shipping."). One line, then the
call.

## 6. Tell the user

Two or three lines: the huddle number, the play in one sentence, whether the read-backs were
clean or what changed, and any decision waiting on the user.

## On Herdr

When the orchestrator skill is installed, take the mechanics from its sections instead of
improvising:

- At a takeover, the handoff from "Take over" goes first; the first huddle follows once the
  agents have acknowledged it.
- Roster and what each agent is doing: "Discover the roster".
- Context check and compaction before the huddle: "Context watch and compaction".
- Sending the huddle and the break: "Routing", through each session's inbox (`SendMessage` for
  Claude, `codex queue` for Codex), typing into a pane only as its fallback.
- Read-backs from Codex sessions: the report-file or relay routes in "Routing"; a Codex session
  cannot reply through `SendMessage`.
- Waiting for every read-back: `wait-all-idle.sh` from "Take over", run in the background.
  Arm it only after each agent shows `herdr agent wait <pane> --until working`, or it can
  settle on the state from before the huddle. A finished Codex turn reports `done`, not
  `idle`, so a hand-written wait needs `--until done` too.
