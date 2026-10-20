#!/bin/zsh
# Usage: ctx.sh <project-transcript-dir> <name>=<session-id>...
# Prints each session's current context size without touching its pane, so it works while the
# agent is busy. Session ids come from `herdr agent list` (.agent_session.value).
# - Claude: the last assistant usage record in <project-transcript-dir>/<id>.jsonl (input + cache
#   creation + cache read). The dir is ~/.claude/projects/<cwd with / replaced by ->. Percentages
#   assume a 1M window; the footer's "Ctx Used" on Opus 5.5 sessions matched that on 2026-09-30.
# - Codex: when no Claude transcript has that id, the last token_count record in
#   ~/.codex/sessions/*/*/*/rollout-*-<id>.jsonl: the last request's input tokens against the
#   model's context window, as a share used. Codex's footer shows the share left.
set -u
dir=$1; shift
for pair in "$@"; do
  name=${pair%%=*}; id=${pair#*=}; f="$dir/$id.jsonl"
  if [[ -f "$f" ]]; then
    tail -c 800000 "$f" \
      | jq -R 'fromjson? | select(.type=="assistant") | .message.usage | (.input_tokens + .cache_creation_input_tokens + .cache_read_input_tokens)' 2>/dev/null \
      | tail -1 | awk -v n="$name" '{printf "%-10s ctx~%d tokens  %.0f%% of 1M\n", n, $1, $1/10000}'
    continue
  fi
  codex=(~/.codex/sessions/*/*/*/rollout-*-$id.jsonl(N))
  if (( ${#codex} )); then
    tail -c 800000 "${codex[-1]}" \
      | jq -R -r 'fromjson? | select(.payload.type=="token_count" and .payload.info != null) | .payload.info | "\(.last_token_usage.input_tokens) \(.model_context_window)"' 2>/dev/null \
      | tail -1 | awk -v n="$name" '{printf "%-10s ctx~%d tokens  %.0f%% of %dk (Codex)\n", n, $1, 100*$1/$2, $2/1000}'
    continue
  fi
  echo "$name: no Claude transcript in $dir and no Codex session for $id"
done
