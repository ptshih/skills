---
name: repo-showcase
description: Make a GitHub repository presentable and discoverable the honest way — shields.io badges that state true facts, a README demo GIF (a real recording, or a terminal-style animation rendered from a JSON storyboard with the bundled script), a rewritten repository description and topics, then proof that GitHub renders it all. Use whenever the user wants a repo to look good, get legitimate attention or stars, add badges, add a demo/animation/screencast to a README, set GitHub topics, or fix a stale description — even when they ask for only one of those pieces. Also use to redirect requests for manufactured engagement (fake accounts, star gaming) toward what actually works.
---

# Repo showcase

A stranger landing on the repo should understand in ten seconds what it is, see it
working, and be able to find it by search. Everything added must be true today and stay
true without upkeep: badges read live data, the GIF says whether it is recorded or
illustrated, and the description matches the README rather than an older plan.

## Ground rules

- **No manufactured engagement.** Fake accounts, star rings and vote trading break
  GitHub's terms and get repos flagged. Decline in one sentence and offer this skill's
  work instead; the user usually wants attention, not the specific trick.
- **Badges assert facts.** Only add a badge the repo backs right now: no CI badge without
  a workflow, no "tests passing" without CI, no star or download counters, no hardcoded
  version when a tag-reading badge exists.
- **A GIF is a recording or an illustration; the caption says which.** An illustration
  drawn from the repo's own documented behaviour is fine and often the only practical
  option; passing it off as a screen recording is not.
- **The repo's own gates win.** Read its validators, tests and contribution conventions
  before adding files. Some repos allowlist file types (the fsd repo rejected anything
  that was not `.md`/`.json`/`.mjs`), so a binary asset may need a scoped allowance plus a
  test, not a bypass.

## Workflow

The references, script and example storyboard live in this skill's folder, `${CLAUDE_SKILL_DIR}`; in a
harness that does not expand `${CLAUDE_SKILL_DIR}`, use the folder this file was loaded from.

### 1. Inspect before touching anything

```sh
gh repo view OWNER/REPO --json name,description,homepageUrl,repositoryTopics,licenseInfo,defaultBranchRef,isPrivate
gh api repos/OWNER/REPO/contents --jq '.[] | "\(.type)\t\(.name)"'
gh release list -R OWNER/REPO -L 5; git -C CLONE tag -l | tail -5
```

Find the local clone (`git remote -v` in likely places; an installed-skill or plugin
directory may be the clone). Read the README, the package manifest, any check or test
script that validates documentation, `.github/workflows` (decides the CI badge), and the
last few commit messages for trailer conventions. Write down every constraint before
designing; retrofitting to a validator costs more than reading it.

### 2. Badges

Read `${CLAUDE_SKILL_DIR}/references/badges.md`. Pick four to six: version from tags, license, one badge per
install surface, one per hard dependency or platform, and at most one "positioning" badge
(for example runtime: none). Verify every URL returns 200 and the rendered title says what
you expect before it goes in the README.

### 3. Demo GIF

Read `${CLAUDE_SKILL_DIR}/references/demo-gif.md`. Prefer a real recording when the flow is cheap to run and
a recorder exists (`vhs`, `asciinema` + `agg`, or a screen capture). Otherwise storyboard a
terminal-style animation from the repo's own documented behaviour (examples, role files,
CLI output in docs) and render it with:

```sh
python3 ${CLAUDE_SKILL_DIR}/scripts/render_terminal_gif.py storyboard.json demo.gif --frames ./frames
```

The script exits non-zero when a line overflows its pane or the font lacks a glyph; fix
those before looking at frames. Always open the sample frames it writes and read them
like a user would. Start from `${CLAUDE_SKILL_DIR}/assets/example-spec.json`, which is a complete storyboard
(coordinator plus two worker panes) that rendered cleanly.

### 4. Wire the README

Under the title and one-line tagline, in this order: badges on consecutive lines, the GIF
with descriptive alt text, an italic one- or two-line caption that says recorded or
illustrated and links to the source material, then the existing prose. Store the GIF at
`assets/demo.gif` with a relative link so GitHub renders it and any link checker validates
it. Keep whatever the repo uses for release notes current (a CHANGELOG "Unreleased"
line is enough).

### 5. Description and topics

Read `${CLAUDE_SKILL_DIR}/references/github-metadata.md`. Rewrite the description from the README's tagline
and audience; delete stale claims. Choose ten to fifteen topics covering the category, the
ecosystems it plugs into, and the problem words a searcher would type. Apply with
`gh repo edit` and read the result back.

### 6. Verify, land, confirm on GitHub

Run the repo's own checks and record exit codes. Commit by explicit path, following the
repo's trailer convention. Push when the user pointed at the GitHub URL or otherwise asked
for the result to be on GitHub; if they only asked for local changes, stop before the push
and say so. Then confirm from the outside:

```sh
gh api repos/OWNER/REPO/readme -H "Accept: application/vnd.github.html" | grep -c '<img'
curl -sIL https://github.com/OWNER/REPO/raw/BRANCH/assets/demo.gif | grep -iE '^(HTTP|content-type|content-length)'
gh repo view OWNER/REPO --json description,repositoryTopics
```

## Report

Lead with where the result lives (URL and commit). Then, in a few bullets each: what the
GIF shows and whether it is recorded or illustrated, which badges and why, the new
description and topics, and any repo-specific change that was needed to admit the asset.
Finish with a small table of executed checks and their exit codes, and the path to the
storyboard so the GIF can be regenerated.
