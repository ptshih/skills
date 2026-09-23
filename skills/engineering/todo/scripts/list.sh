#!/bin/sh
# One row per open TODO.md item, tab-separated: group, #id, metadata, headline,
# section. Wrapped headlines are joined. The group is blocked (a blocked: tag),
# you (any other tag except doing, a gate declared in TODO.md's legend) or
# ready. Rows run ready -> you -> blocked, then high -> med -> low, then file
# order. Read-only.
awk '
function emit() {
  if (!item) return
  n++
  match(item, /^- \[ \] #[0-9]+/); id = substr(item, 7, RLENGTH - 6)
  meta = ""; if (match(item, / \([^)]*\) /)) meta = substr(item, RSTART + 2, RLENGTH - 4)
  h = ""; if (match(item, /\*\*[^*]+\*\*/)) h = substr(item, RSTART + 2, RLENGTH - 4)
  nf = split(meta, f, ", ")
  p = f[2] == "high" ? 1 : f[2] == "med" ? 2 : 3
  if (meta ~ /blocked:/) { g = 3; group = "blocked" }
  else {
    g = 1; group = "ready"
    for (i = 3; i <= nf; i++) if (f[i] != "doing") { g = 2; group = "you" }
  }
  printf "%d\t%d\t%04d\t%s\t%s\t%s\t%s\t%s\n", g, p, n, group, id, meta, h, sec
  item = ""
}
/^## / { emit(); sec = substr($0, 4); next }
/^- \[ \] #[0-9]+ / { emit(); item = $0; next }
item && /^      / { sub(/^ +/, ""); item = item " " $0; next }
{ emit() }
END { emit() }
' "${1:-TODO.md}" | sort -t "$(printf '\t')" -k1,1n -k2,2n -k3,3n | cut -f4-
