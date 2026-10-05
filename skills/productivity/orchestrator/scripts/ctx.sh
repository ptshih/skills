#!/bin/zsh
# Usage: ctx.sh <project-transcript-dir> <name>=<claude-session-id>...
# Prints each Claude session's current context size from the last assistant usage record in its
# transcript (input + cache creation + cache read). Works while the agent is busy and does not touch
# its pane. Session ids come from `herdr agent list` (.agent_session.value); the transcript dir is
# ~/.claude/projects/<cwd with / replaced by ->. Percentages assume a 1M window; the footer's
# "Ctx Used" on Opus 5.5 sessions matched that on 2026-09-30.
set -u
dir=$1; shift
for pair in "$@"; do
  name=${pair%%=*}; id=${pair#*=}; f="$dir/$id.jsonl"
  if [[ ! -f "$f" ]]; then echo "$name: no transcript at $f"; continue; fi
  tail -c 800000 "$f" \
    | jq -R 'fromjson? | select(.type=="assistant") | .message.usage | (.input_tokens + .cache_creation_input_tokens + .cache_read_input_tokens)' 2>/dev/null \
    | tail -1 | awk -v n="$name" '{printf "%-10s ctx~%d tokens  %.0f%% of 1M\n", n, $1, $1/10000}'
done
