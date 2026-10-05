# Badges

Badges are compressed claims. A reader trusts them precisely because they look
automatic, so each one must either read live data or state something structurally true.

## Choosing

| Claim | Badge URL pattern | Notes |
|---|---|---|
| Version | `https://img.shields.io/github/v/tag/OWNER/REPO?label=version&sort=semver&color=1f6feb` | Reads tags, so it never goes stale. Use `github/v/release` only if releases exist. |
| License | `https://img.shields.io/github/license/OWNER/REPO?color=1f6feb` | Reads the LICENSE file. |
| Install surface | `https://img.shields.io/badge/Claude%20Code-plugin-D97757?logo=claude&logoColor=white` | Static badge; one per way to install (plugin, npm, pip, brew). |
| Platform / dependency | `https://img.shields.io/badge/runs%20on-Herdr-2ea043` | Link it to the dependency's site. |
| Positioning | `https://img.shields.io/badge/runtime-none%20%C2%B7%20pure%20skill-8b949e` | At most one; it says what the project deliberately is not. |
| CI status | `https://img.shields.io/github/actions/workflow/status/OWNER/REPO/FILE.yml` | Only if `.github/workflows/FILE.yml` exists. |

Static badge syntax is `badge/LABEL-MESSAGE-COLOR`; escape spaces as `%20`, dashes as
`--`, and separators like `·` as `%C2%B7`. `logo=` takes a Simple Icons slug
(`claude`, `npm`, `python`, `github`). Colour hexes used above: GitHub blue `1f6feb`,
Anthropic clay `D97757`, green `2ea043`, neutral grey `8b949e`, purple `6E56CF`.

Skip: star counters (this work is about earning them, not displaying them), download
counts under a few thousand, "maintained" badges, and anything the reader cannot act on.

## Placing

Badges go on consecutive lines directly under the one-line tagline so they render as a
single row. Each is a link: version → CHANGELOG, license → LICENSE, install badges → the
`#quick-start` heading, dependency → its site. Anchor links must match GitHub's slug of
the heading (lowercase, spaces to hyphens, punctuation dropped); a repo's link checker may
enforce this.

```md
[![Version](https://img.shields.io/github/v/tag/OWNER/REPO?label=version&sort=semver&color=1f6feb)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/github/license/OWNER/REPO?color=1f6feb)](LICENSE)
```

## Verifying

Fetch every badge before committing. Shields returns 200 with an SVG whose `<title>`
holds the rendered text, which catches a wrong repo slug or a tag pattern that resolved to
nothing.

```sh
for u in "URL1" "URL2"; do
  printf '%s ' "$(curl -s -o /dev/null -w '%{http_code}' "$u")"
  curl -s "$u" | grep -o '<title>[^<]*</title>' | head -1
done
```

Expect `200 <title>version: v1.2.0</title>` style lines. A title of `version: no tags` or
`license: not identifiable` means the badge would ship a wrong claim.
