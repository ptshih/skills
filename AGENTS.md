Skills are organized into bucket folders under `skills/`:

- `engineering/`: daily code work
- `productivity/`: daily non-code workflow tools

Add a bucket deliberately: the folder, its `README.md`, and this list, in the same commit.

Each skill lives at `skills/<bucket>/<name>/SKILL.md`, with an `agents/openai.yaml` beside it
holding the Codex picker metadata (`interface.display_name`, `interface.short_description`).
Supporting files (scripts, formats, templates) sit in the skill's folder, and `SKILL.md`
references them through `${CLAUDE_SKILL_DIR}` with a note for harnesses that do not expand it.
Never write a dollar sign followed by a digit in a `SKILL.md`: Claude Code replaces those with
the words the skill was invoked with. Use `$NF`, `cut`, or a bundled script instead.

Every skill has an entry in its bucket's `README.md` and in the top-level `README.md`, each a
one-line description with the skill name linked to its `SKILL.md`. Both group entries into
**User-invoked** and **Model-invoked**.

Skills are model-invoked by default: the `description` carries rich trigger phrasing so the
agent can reach for them. A user-invoked skill, reachable only by typing its name, sets
`disable-model-invocation: true` in its frontmatter and `policy.allow_implicit_invocation:
false` in its `agents/openai.yaml`.

The install command is `npx skills@latest add ptshih/skills -g --skill <name>`, and
`npx skills@latest update` updates it. Say it that way everywhere.

A skill adapted from someone else's keeps the upstream license notice in its folder
(`THIRD_PARTY_NOTICES.md`) and an attribution line in the top-level `README.md`.

Before publishing a change to a skill with scripts, run `sh -n` on each script and run the
scripts against at least one real repository. `scripts/list-skills.sh` prints every skill.

Commit messages use Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`).
