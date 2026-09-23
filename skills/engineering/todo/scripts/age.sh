#!/bin/sh
# Days since any line of each open TODO.md item last changed, oldest first:
# "<days><TAB>#id". Read-only.
git blame --line-porcelain "${1:-TODO.md}" | awk -v now="$(date +%s)" '
/^author-time / { t = $2; next }
/^\t/ {
  line = substr($0, 2)
  if (match(line, /^- \[ \] #[0-9]+/)) { id = substr(line, 7, RLENGTH - 6); last[id] = t; order[++n] = id; next }
  if (id != "" && line ~ /^      /) { if (t > last[id]) last[id] = t; next }
  id = ""
}
END { for (i = 1; i <= n; i++) printf "%d\t%s\n", int((now - last[order[i]]) / 86400), order[i] }
' | sort -rn
