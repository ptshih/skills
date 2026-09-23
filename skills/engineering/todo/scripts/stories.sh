#!/bin/sh
# TODO.md <-> STORIES.md drift: an item naming a story whose `Delivers:` omits
# it or that does not exist, a `Delivers: #N` no longer open, and a `doing`
# story with no `doing` item. Prints nothing when the files agree. Read-only.
stories=${1:-STORIES.md}
todo=${2:-TODO.md}
[ -s "$stories" ] || exit 0
awk '
function flush_story() {
  if (!sid) return
  st[sid] = stat; t = sblk; sub(/.*Delivers:/, "", t)
  if (sblk ~ /Delivers:/) while (match(t, /#[0-9]+/)) {
    del[sid, substr(t, RSTART, RLENGTH)] = 1; dl[sid] = dl[sid] " " substr(t, RSTART, RLENGTH)
    t = substr(t, RSTART + RLENGTH)
  }
  sid = ""
}
function flush_item() {
  if (!iid) return
  open[iid] = 1; if (imeta ~ /doing/) doing[iid] = 1
  t = iblk
  if (match(t, /Stor(y|ies) S[0-9]+([,-] ?S?[0-9]+| and S[0-9]+)*/)) {
    t = substr(t, RSTART, RLENGTH)
    while (match(t, /S[0-9]+/)) { names[iid] = names[iid] " " substr(t, RSTART, RLENGTH); t = substr(t, RSTART + RLENGTH) }
  }
  iid = ""
}
FNR == 1 { flush_story(); flush_item() }
NR == FNR && /^- \[ \] S[0-9]+ / { flush_story(); match($0, /S[0-9]+/); sid = substr($0, RSTART, RLENGTH); match($0, /\([^)]*\)/); stat = substr($0, RSTART, RLENGTH); sblk = $0; next }
NR == FNR && sid && /^      / { sblk = sblk " " $0; next }
NR == FNR { flush_story(); next }
/^- \[ \] #[0-9]+ / { flush_item(); match($0, /#[0-9]+/); iid = substr($0, RSTART, RLENGTH); match($0, / \([^)]*\) /); imeta = substr($0, RSTART, RLENGTH); iblk = $0; next }
iid && /^      / { iblk = iblk " " $0; next }
{ flush_item() }
END {
  flush_story(); flush_item()
  for (i in names) { n = split(names[i], a, " "); for (k = 1; k <= n; k++) { s = a[k]
    if (!(s in st)) print i " names " s ", which is not in STORIES.md"
    else if (!((s, i) in del)) print i " names " s ", but " s " Delivers: does not list " i } }
  for (k in del) { split(k, p, SUBSEP); if (!(p[2] in open)) print p[1] " Delivers: " p[2] ", which is not open in TODO.md" }
  for (s in st) if (st[s] ~ /doing/) { ok = 0; n = split(dl[s], a, " "); for (k = 1; k <= n; k++) if (a[k] in doing) ok = 1
    if (!ok) print s " is doing, but none of its Delivers:" dl[s] " is tagged doing" }
}
' "$stories" "$todo" | sort
