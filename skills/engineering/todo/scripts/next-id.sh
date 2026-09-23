#!/bin/sh
# The next free TODO.md id: the larger of every `next-id:` counter and every
# id + 1, across all local branches and every worktree's working copy. A
# checkout's own counter is only as fresh as its branch point. Read-only.
{
  git for-each-ref --format='%(refname:short)' refs/heads | while IFS= read -r b; do
    git show "$b:TODO.md"
  done
  git worktree list --porcelain | sed -n 's/^worktree //p' | while IFS= read -r wt; do
    cat "$wt/TODO.md"
  done
} 2>/dev/null | awk '
/\*\*next-id: [0-9]+/ { match($0, /next-id: [0-9]+/); s = substr($0, RSTART, RLENGTH); gsub(/[^0-9]/, "", s); if (s + 0 > m) m = s + 0 }
/^- \[[ x]\] #[0-9]+/ { match($0, /#[0-9]+/); n = substr($0, RSTART + 1, RLENGTH - 1) + 1; if (n > m) m = n }
END { print m + 0 }
'
