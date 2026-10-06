---
name: retro
description: Run a retrospective on a coding session and propose changes to the agent's setup (checks, instruction files, skills, tools, access to information) so future sessions go better, then apply the changes the user picks.
disable-model-invocation: true
argument-hint: "A past session to review, or nothing for this one"
---

# Retro

The user asked for a retrospective. Find what in the agent's **setup** made the session slower,
costlier or more error-prone than it needed to be, propose specific changes, and apply the ones
the user picks. Change the setup, not the code the session was about.

## 1. Read the session

Default to the current session. When the user names another, find its transcript with
`session-search` when it is installed, or in the harness's own logs (Claude Code under
`~/.claude/projects`, Codex under `~/.codex/sessions`, Pi under `~/.pi/agent/sessions`). Read the
tool calls and their results, not a summary of them.

Then read the setup the session ran under: the repository's and the user's instruction files
(`AGENTS.md`, `CLAUDE.md`), the skills it loaded, its hooks, and the repository's own check
commands (package scripts, pre-commit hooks, CI workflows).

## 2. Look for candidates

- **Navigation**: the agent took long to find a file or fact, or missed a hidden dependency
  between files. Propose a pointer where the agent would look first.
- **Automated checks**: the agent made a mistake a check could have caught. Read the repository's
  checks first: one that exists but is unwired or broken is the finding, not a new check. A
  repository with no guardrail (no pre-commit hook and no CI job running its lint, typecheck and
  tests) is a finding in itself.
- **Checks over rules**: a review missed a mistake. A mechanical violation (a banned API, an
  import shape, a file location) gets a deterministic check: a lint rule, a hook or a CI job,
  whichever is cheapest in that repository. Only judgement calls become written rules, and they
  go where review reads them: the reviewer has only a diff to hold, while the implementing agent
  is already full.
- **Instruction bloat**: an instruction file every session loads is large. Propose moving each
  rule to a check, to review-time standards, or to the skill where an agent would meet it.
- **No-ops**: an instruction that changes nothing, because agents do it anyway or it is too vague
  to act on. Propose deleting it.
- **Tool economy**: a tool call was expensive: a huge output, a repeated search, a tool that
  prints more than anyone reads. Propose a narrower command, a flag or a cheaper tool.
- **Information access**: the agent lacked something it needed, such as server logs, a read-only
  view of a third-party service or a document. Propose a way to reach it.
- **Dead weight**: a skill, tool, hook or rule that duplicates another or that recent sessions
  never used. Count its uses in the logs before proposing a cut.
- **Weak checks**: a check that runs often but catches little. Before calling a check effective,
  feed it at least one known-bad input in a scratch directory and report whether it caught it;
  call a check you did not test "untested".

## 3. Report

Give a numbered list, most severe first. Each finding names its category, its evidence (a count,
a `file:line`, the costly tool call) and the exact change: which file, what text or command, added
or removed. Never quote secrets from logs.

Facts and preferences worth remembering are not setup changes: leave them to the user's memory
skill, if there is one.

## 4. Apply the picks

The user answers with numbers. A pick authorizes exactly the change it named. Apply it, verify it
(run a new check against the input that motivated it; re-read an edited instruction file), and
follow each repository's own rules for committing. Leave unpicked findings alone.

Adapted from [Matt Pocock's retro skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md).
