#!/bin/zsh
# Usage: wait-all-idle.sh [--timeout SECONDS] <pane-or-agent-name>...
# Polls `herdr agent get` for each target and blocks on `herdr agent wait` for the first
# working one until none is working. Prints transitions; exits 0 on ALL_SETTLED (blocked
# targets are listed, not waited on), 2 on timeout. Run it in the background.
set -u
limit=2700
if [[ "${1:-}" == "--timeout" ]]; then limit=$2; shift 2; fi
(( $# )) || { echo "usage: $0 [--timeout SECONDS] <pane-or-agent-name>..." >&2; exit 1; }
deadline=$(( $(date +%s) + limit ))
while true; do
  busy=(); blocked=()
  for t in "$@"; do
    st=$(herdr agent get "$t" 2>/dev/null | jq -r '.result.agent.agent_status // "missing"')
    case "$st" in
      working) busy+=("$t");;
      blocked) blocked+=("$t");;
    esac
  done
  echo "$(date +%H:%M:%S) busy:[${(j: :)busy}] blocked:[${(j: :)blocked}]"
  if (( ${#busy} == 0 )); then echo "ALL_SETTLED blocked:[${(j: :)blocked}]"; exit 0; fi
  if (( $(date +%s) > deadline )); then echo "TIMEOUT busy:[${(j: :)busy}]"; exit 2; fi
  herdr agent wait "${busy[1]}" --timeout 300000 >/dev/null 2>&1 || true
done
