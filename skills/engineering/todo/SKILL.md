---
name: todo
description: Work a repo's engineering backlog in TODO.md — show what is open, add an item, work one, update or close it, or groom the file. Use for "what's on the todo list", "what should I pick up", "what needs my call", "anything blocked", "add a todo", "save as a todo", "let's work on #12", "let's work on the todo to…", "mark that done", "drop that one", "groom the backlog".
allowed-tools: Bash(sh ${CLAUDE_SKILL_DIR}/scripts/*)
---

# Todo

<!-- Editing this file: never write a dollar sign followed by a digit. The skill
loader replaces those with the words the skill was invoked with, which once
turned an awk field reference into "length(only:)". Use $NF or cut instead. -->

The backlog is ONE file: `TODO.md` at the repo root. No database, no CLI — the
**format is the interface and `grep` is the query engine.** An item earns its
place only if a human can read it in a diff.

The scripts in `scripts/` beside this file are query recipes too long to
retype: each reads and prints, none writes. Run them from the repo root as
`sh ${CLAUDE_SKILL_DIR}/scripts/<name>.sh`; in a harness that does not expand
`${CLAUDE_SKILL_DIR}`, use the folder this file was loaded from. They need
`git`, `awk` and `sort`.

## The item format

```
- [ ] #12 (api, low, founder) **Add rate limiting to the signup form.** Then
      as much context as it takes, wrapped and indented six spaces.
```

| Field    | Values                                                  | Rule                                                                                                                                                                                                     |
| -------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `#id`    | `#1`, `#2`, …                                           | Stable, **never reused**. The next id is the larger of `next-id:` and the highest id + 1, across every branch and worktree — `scripts/next-id.sh` (Adding). Deleting the newest item must not hand its id on. |
| area     | the repo's closed set                                   | Declared in TODO.md's legend. Adding one is fine but do it deliberately: the legend, same commit.                                                                                                        |
| priority | `high` `med` `low`                                      | `high` = it blocks something or someone is waiting. Most items are `low`; a file where everything is high sorts nothing.                                                                                 |
| tags     | the repo's gates, then `doing`, then `blocked: <why or #id>` | Optional, in that order.                                                                                                                                                                            |

**TODO.md's header is the repo's configuration.** Its legend names the areas
and the **gate tags**: whatever an agent cannot supply on its own, such as
`paid` (spends real money), `founder` (a person owns it or must say go) or
`device` (needs real hardware). Every tag other than `doing` and `blocked:` is
a gate, and an item carrying one waits on a person. Read the header before the
first edit in a session, and never use a tag the legend does not define.

Two tags are built in. **`doing`** means work toward it has landed and the item
is still open — never a claim (Updating says why). **`blocked:`** names what
would unblock it — prefer `blocked: #4` over prose when another item is the
blocker, so closing one surfaces the other.

**The headline states the task in 60 characters or fewer**, verb first: "Split
the order's freight across suppliers", not "Invoices." Every list shows the
headline and nothing else, so it has to stand alone; the context after it is
for whoever builds it. A legacy headline comes within the rule the next time
its item is updated.

**One item is one landing.** Work that needs several landings is several items
under one section, and the section's preamble is their shared spec. An item
whose body lists independent deliverables — a migration, a function, two
screens, an export — is a section wearing a checkbox.

⚠ **Sections are TOPICS, not areas, and a section's preamble is shared context
for every item beneath it.** Read the preamble before acting on an item, and
file a new item under the section whose preamble already applies. Area lives
in the item's metadata precisely so grouping by topic stays free.

Ids only mean an id **at the start of a line**, right after the checkbox —
every command below anchors with `^`.

## Reading

```bash
sh ${CLAUDE_SKILL_DIR}/scripts/list.sh       # every open item, one row each, sorted
grep -c '^- \[ \] #' TODO.md                 # how many are open
grep -n '^## \|^- \[' TODO.md                # the map: sections + items, in order
git log --oneline -E --grep='#12([^0-9]|$)'  # one item's whole history
```

`list.sh` prints `group  #id  metadata  headline  section`, tab-separated, one
row per open item with wrapped headlines joined. The group is `ready` (no gate
tag), `you` (at least one gate) or `blocked`, and an item sits in exactly one —
blocked wins, then you. Rows run ready → you → blocked, then high → med → low,
then file order, because file order carries sequencing ("slices land in this
order").

Filters — anchor inside the metadata parens so a word in the prose can't match:

```bash
grep -nE '^- \[ \] #[0-9]+ \(api,' TODO.md                  # one area
grep -nE '^- \[ \] #[0-9]+ \([a-z]+, high' TODO.md          # high priority
grep -nE '^- \[ \] #[0-9]+ \([^)]*founder[^)]*\)' TODO.md   # a tag
```

To show one item in full, get its line number, then read that range **plus the
`## ` heading above it** — the preamble is part of the item's meaning.

## Showing the list

Answer "what's open" with a count line and three markdown tables — real
tables, not a code block — in `list.sh` order. Take every number in the count
line from `sh ${CLAUDE_SKILL_DIR}/scripts/list.sh | cut -f1 | sort | uniq -c`
(ready, you, blocked; open is their sum), never by counting rows:

```
**25 open** · 6 ready · 12 need you · 7 blocked

**Ready to pick up**
| #   | Pri | Area | Item                                     |
| --- | --- | ---- | ---------------------------------------- |
| #93 | med | api  | Split the order's freight across suppliers |

**Needs your call**
| #   | Pri  | Area   | Item                              | The call           |
| --- | ---- | ------ | --------------------------------- | ------------------ |
| #74 | high | web    | Finish the live email checks      | run the checks     |
| #82 | med  | agents | Allowance for live model calls    | approve the spend $ |

**Blocked**
| #   | Pri | Item                | Waiting on                 |
| --- | --- | ------------------- | -------------------------- |
| #32 | med | Import a real account | first real customer export |
```

- **Item** is the headline as written; one over 60 characters is shortened to
  about 45 without changing its meaning.
- **The call** is what the item needs from a person, in a few words — the
  question, not the backstory. A decision or a go reads as the choice
  ("approve the spend", "pick the name"); work only a person can do reads as
  `yours:` and the next action ("yours: test it on a device"). A trailing `$`
  marks a gate that spends money.
- **Waiting on** is the blocker, as `#N` when it is an item. A `blocked: #N`
  whose `#N` is gone moves to Ready, marked "unblocked: #N closed".
- Drop an empty group. Nothing around the tables but one closing line, and only
  when something needs attention.

Narrower asks reuse the same tables:

- **What should I pick up** — one sentence naming the pick, the Ready table cut
  to three rows, then one line of twenty words or fewer per row on why: what it
  unblocks, which story it builds, any order its section preamble sets. Close
  with "N more wait on your call," N being the `you` count from that same
  command. Nothing else — alternatives are what the
  full list is for. Offering a gated item as the next move wastes the turn:
  those wait on a decision, not on effort.
- **What needs my call** — the Needs-your-call table alone.
- **Anything blocked** — the Blocked table alone.
- **An area, a priority, a tag** — the full layout, matching rows only.
- **Show #12** — the item in full with its section preamble.

## Adding

1. **Is it already here?** Grep TODO.md for the work's key nouns first. If an
   item covers it, update that item instead — a second id for one outcome
   splits its history and its blockers.
2. **Next id** — `sh ${CLAUDE_SKILL_DIR}/scripts/next-id.sh`. It reads every
   branch's TODO.md and every worktree's working copy, because a checkout's own
   `next-id:` is only as fresh as its branch point. Bump `next-id:` in the same
   edit.
3. **Pick the section** whose preamble already applies. If none does, add a new
   `## ` section **with a preamble** — a heading with no shared context is how a
   file full of orphan items starts. Append at the end of that section.
4. **Write the item the way the repo writes them**: a headline within the rule
   above, then enough context to act without re-deriving the reasoning — what
   was already ruled out and why, the ⚠ that would trip the next agent, the doc
   that holds the full argument. If the repo keeps a `STORIES.md` whose stories
   list the items that build them under `Delivers:`, name the story in the
   prose (`Story S4.`) and add the id to its `Delivers:`.

Never invent metadata to look thorough. If the priority is genuinely unknown,
`low` is the honest default; if you are guessing at a gate, ask instead.

## Starting a backlog

With no `TODO.md` yet, create one with this header. Propose the areas from the
repo's top-level folders and confirm them before the first item; keep the
gates the repo needs and delete the rest.

```markdown
# TODO — engineering backlog

Carry-forward engineering items. Each carries enough context to act on without
re-deriving the reasoning. **Delete items when done** — git history is the archive.

**Item format — operated by `/todo`.** `- [ ] #1 (app, low, founder) headline…`: a stable
`#id`, then AREA (`app` · `api` · `ops` · `docs`), then PRIORITY (`high` · `med` · `low`),
then optional tags in this order — `paid` (spends real money), `founder` (a person owns it
or must say go), `doing` (work has landed and the item is still open), `blocked: <why or
#id>`. A bolded headline of 60 characters or fewer states the task; one item is one
landing. **A section heading and its preamble are shared context for every item under it.**

**next-id: 1.** Ids are never reused, so this counter survives deleting the newest item.
```

## Working an item

For "let's work on #12" or "the todo to…":

1. **Read it whole** — the item, its section preamble, the docs it names, and
   its story if it has one, whose `Accept:` lines are the acceptance.
2. **Respect the gates.** A gate tag means a person's go comes first: name the
   decision and wait. A gate that spends money also falls under whatever
   approval rules the repo's `AGENTS.md` or `CLAUDE.md` sets. `blocked:`: check
   whether the blocker still holds, and stop if it does.
3. **Re-verify what it cites** — paths, migration numbers, counts, "decided"
   facts. Items drift while they wait; correct the item in the same change.
4. **Then the normal flow** — plan, test, land it the way the repo lands work.
   When it lands, done means Closing; partly done means Updating.

## Updating

- **Partial progress** — rewrite the item to what remains, and tag it `doing`.
  What landed belongs in the owning doc or the commit message, not in a running
  log inside the item.
- **A decision** — one dated sentence ("Decided 2026-09-23: …"), only where the
  builder needs it. A decision that outlives the item goes in the owning doc in
  the same commit.
- **Retag or reprioritize** — keep the tag order; add a gate only on the word
  of the person it names.
- **A different outcome** — an id names one outcome. If what remains is other
  work, delete the item and file a new one, moving every `blocked: #N` and
  `Delivers:` that pointed at the old id.
- **A headline over 60 characters** comes within the rule while you are here.

⚠ Never tag `doing` to claim an item. An uncommitted edit to a shared
`TODO.md` makes the whole file another session's (Landing), and every other
session stops landing backlog changes until yours does.

## Closing — `done` or `dropped` means DELETE the item

**Delete items when done — git history is the archive.** A `- [x]` tombstone
costs every future reader the work of deciding whether it still matters.
**Dropping** — deciding the work will not happen — deletes the same way, with
the reason in the commit subject. Decide and move on: a dropped item is cheaper
than one nobody believes.

Before deleting, ask one question: **does this item carry a durable lesson?** A
trap, a measured number, a rejected approach with its reason, a decision. If it
does, that belongs in the repo's docs (amend the doc that owns the topic) or
its agent instructions (`AGENTS.md` or `CLAUDE.md`, only if an agent must know
it to avoid breaking something) in the SAME commit — and only then does the
item go.

If the repo keeps `STORIES.md`, check whether a story claims the item —
`grep -nE 'Delivers:.*#12\b' STORIES.md` — and update it in the same commit:
the story either shipped or merely loses the id.

Last, **surface what it unblocked** — every item whose `blocked:` mentions it,
prose blockers included:
`grep -nE '^- \[ \] #[0-9]+ \([^)]*blocked:[^)]*#12\b' TODO.md`. Drop or
rewrite each hit's `blocked:` in the same commit, and name those items in your
reply.

## Grooming

A consistency pass over the whole file. Report, don't silently fix anything
that needs a judgment call. Open with two or three lines — how many items, what
came back clean, what needs a person — then group the report by check, and
give each finding a proposed fix marked **mechanical** (applied on a go) or
**needs a call**. Run the scripts rather than estimating; a count by eye is
not a finding.

- **Ids** — duplicates, or an id above `next-id:` (both mean two sessions added at once).
- **Malformed metadata** — an area or tag the legend does not define, a missing
  priority, tags out of order.
- **Closed blockers** — a `blocked:` that names `#N` where `#N` is gone: drop or
  rewrite the tag and surface the item (a prose blocker that also names `#N`
  needs a call — the prose may still hold).
- **Dead references** — `sh ${CLAUDE_SKILL_DIR}/scripts/refs.sh` lists cited
  paths under the repo's top-level folders that no longer resolve (a line that
  says the file is in git history is deliberate and skipped). If the repo
  numbers its migrations, also a migration number cited for unlanded work at
  or below the newest one that exists.
- **Stories out of step** — with a `STORIES.md`,
  `sh ${CLAUDE_SKILL_DIR}/scripts/stories.sh` lists an item naming a story
  whose `Delivers:` omits it, a `Delivers: #N` no longer open, and a `doing`
  story with no `doing` item. The fix on the story side is the story's owner's.
- **Shape** — headlines over 60 characters
  (`sh ${CLAUDE_SKILL_DIR}/scripts/list.sh | cut -f2,4 | awk -F'\t' 'length($NF) > 60'`)
  or not verb first: propose a rewrite (mechanical). Items that bundle
  independent deliverables, or two ids that must land together: propose the
  split or merge (needs a call).
- **Progress logs** — an item that narrates what already landed. Propose
  rewriting it to what remains, and move any durable fact it holds to the
  owning doc in the same commit (Updating).
- **Items that outgrew the file** — three paragraphs of argument is a design
  doc wearing a checkbox. Propose a doc and a one-line item pointing there.
- **Keep the backlog small** — a backlog is only useful while someone can hold
  it in their head. Items waiting on a distant event (a prose `blocked:`, not
  `#N`) or untouched for 30+ days (`sh ${CLAUDE_SKILL_DIR}/scripts/age.sh`)
  each get one decision, put to the user as a table: **keep**, **park** (a
  "when X happens" line in the owning doc, then delete the item) or **drop**.
  Never park or drop on your own call.

## Landing the change

TODO.md is shared across sessions and is usually one of the most-edited files
in a repo, so it is the likeliest file in the tree to already hold someone
else's work:

```bash
git diff TODO.md
```

Read the diff. If it contains an item you did not touch, that is another
session's — leave the file for its owner and say so. Otherwise commit it by
explicit path (`git commit TODO.md -m "…"`), never `git add -A`. If the repo has
a landing skill, it is the full ritual when this rides along with code.

**Subjects name the item**, so `git log --grep` is its whole history. A commit
that adds, updates, closes or drops an item names `#N` in its subject; a
TODO-only commit leads with the verb — `Add #95: …`, `Update #87: …`,
`Close #94: …`, `Drop #25: …` — and a code commit that closes one says so
anywhere in the subject ("…, #80 closes").

**A merge conflict on `next-id:`** means both sides took ids: keep the higher
counter. If both took the same id, renumber the branch's item and fix every
`blocked:` and `Delivers:` that points at it.
