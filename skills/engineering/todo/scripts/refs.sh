#!/bin/sh
# Paths TODO.md cites under the repo's top-level folders that no longer
# resolve: "line N: path". A line that says the file lives in git history is a
# deliberate pointer and is skipped. Read-only.
roots=$(git ls-tree -d --name-only HEAD 2>/dev/null | grep -v '^\.' | sed 's/[][\.*^$()+?{}|]/\\&/g' | paste -sd '|' -)
[ -n "$roots" ] || exit 0
pattern="\`($roots)/[^\`]+\`|\\]\\(($roots)/[^)#]+"
grep -nE "$pattern" "${1:-TODO.md}" | grep -v 'git history' | while IFS= read -r line; do
  n=${line%%:*}
  printf '%s\n' "$line" | grep -oE "$pattern" | sed -E 's/^`//; s/`$//; s/^\]\(//; s/:[0-9][0-9,-]*$//' |
    while IFS= read -r p; do [ -e "$p" ] || echo "line $n: $p"; done
done
