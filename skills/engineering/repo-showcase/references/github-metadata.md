# Description and topics

The description and topics are what GitHub search, the Explore page, and social previews
show. They are cheap to change and easy to leave stale.

## Description

One sentence, under ~200 characters (GitHub allows 350). Lead with the category noun a
searcher would use, then what it does, then who or what it works with:

> Agent skill that coordinates coding agents from implementation through review and
> integration — Herdr tabs, Git worktrees and filesystem handoffs, for Claude Code, Pi and Codex.

Derive it from the README's current tagline and quick start. Remove claims the README no
longer makes (the fsd repo's old description promised "cross-device sync" while its README
said cross-machine coordination is unsupported). Leave `homepageUrl` empty unless the
project has its own site; pointing it at a dependency's site is misleading.

## Topics

Rules GitHub enforces: lowercase, letters/digits/hyphens, 50 characters max, 20 topics
max. Aim for ten to fifteen drawn from four buckets:

- **Category:** what kind of thing it is (`agent-skill`, `cli`, `library`, `github-action`).
- **Ecosystem:** every platform it installs into or drives (`claude-code`,
  `claude-code-plugin`, `codex`, `herdr`, `pi-package`).
- **Problem words:** what a searcher types (`code-review`, `agent-orchestration`,
  `multi-agent`, `git-worktree`).
- **Broad reach:** one or two high-traffic umbrellas (`ai-agents`, `developer-tools`, `llm`).

Avoid topics that mean something else to most people: `pi` is Raspberry Pi, `go` is the
language, `spring` is the framework. Prefer the compound (`pi-package`).

## Applying and verifying

```sh
gh repo edit OWNER/REPO --description "…" \
  --add-topic agent-skill --add-topic claude-code   # one flag per topic
gh repo view OWNER/REPO --json description,repositoryTopics \
  --jq '.description, ([.repositoryTopics[].name] | sort | join(" "))'
```

`--add-topic` appends; use `--remove-topic` for stale ones. The rendered README check
belongs with this step too:

```sh
gh api repos/OWNER/REPO/readme -H "Accept: application/vnd.github.html" \
  | grep -o '<img[^>]*alt="[^"]*"' | sed 's/.*alt=//'
```

Every badge and the GIF should appear once, with the alt text you wrote.
