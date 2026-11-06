# Review, landing and reporting

## Review

- Give reviewers the exact revision and known findings. Map older findings onto current code,
  then send one consolidated fix list with file and line references.
- Repeat review only when fixes add risk or leave consequential findings open; further rounds
  need new evidence. For a small fix after a second review, read the diff yourself.
- A reviewer reads a detached snapshot (`git worktree add --detach`) so the builder never waits;
  move it with `git checkout --detach <new head>`, which keeps its probe scripts for a re-check.
- Verify check evidence against the revision being landed; re-run checks for changed code.
- Check that a reported failure is reachable before ranking it. For logic that reconciles reads
  over time, check event identities, boundaries and what was already seen.
- Design documents get independent review when consequential assumptions need checking.
- A landing others build on (a schema, a wire shape, a specification): written proposal first,
  reviewed against the specification, before any code.
- When a fix adds machinery and the next review finds a race in it, ask whether the product can
  live without the machinery. When a fix introduces a defect, clarify the rule before editing.
- When your own shell refuses a check, do not rephrase it to get through: the reviewer's run is
  the evidence, and your report says you did not run it.

## Outside services

- Exercise any path to an outside service once with real credentials right after the deploy;
  a health check is not that.
- When a fix relies on a property of the hosted database or platform (a session setting, a
  pooler, a timeout, function lifetime), ask the real one, read-only, before the fix is built.

## Landing

- A shared checkout has one index: two agents committing at once collide. Never stage another
  teammate's file into someone else's commit.
- Order a multi-commit assignment so the part that stands alone comes first, with a message at
  that commit: it can be reviewed and land alone.
- `git merge-tree --write-tree main <branch>` shows conflicts without touching anything.
  `git merge -F -` does not read stdin: write the message to a file.
- Many commits as one: `git merge --squash <branch>`, commit with `-F <file>`, then
  `git diff --quiet HEAD <branch>` proves the tree matches what was reviewed.
- When main has moved, `git cherry-pick <base>..<head>` and prove it on the owned paths with
  `git diff --quiet HEAD <head> -- <paths>`. A stacked branch lands the same way after its base.
- After a merge, grep for stragglers of any repo-wide change the branch predates. Branches that
  each delete neighbouring sections of a shared note conflict: remove all of them.
- Before replacing a section of a shared backlog by slicing between headings, list its items.
- Deleting a directory deletes its `.gitignore`: run `git status` after, and do not stage what
  reappears.
- A check failing in the main checkout right after a fast-forward may be stale installed
  packages: compare with the lockfile, and never reinstall under the user's running dev server.
- A preview serves whatever was last built in its worktree: while anyone checks it, the builder
  holds branch switches and builds there.
- `secret-scrubber` reads only the uncommitted or staged diff. For a committed branch, pipe
  `git diff main <branch>` into its exported `scanDiff` from a short Bun script run with
  `bun --no-env-file` outside the repo.
- "Land and push" said before the verdict: hold it, say so, carry it out on a clean verdict;
  on any finding, come back.

## Migrations

- An applied migration never changes: wording fixes go in before landing, and the expected
  journal hash changes with them.
- Around a scheduled job: read-only baseline, wait for its lease to clear, apply, compare, and
  explain every count that moved.

## Vercel

- `vercel inspect <domain> --scope <team>` names the deployment a domain serves. `vercel ls`
  writes to stderr. A project deployed by hand is not built by a push: list its deployments.
- A sensitive variable cannot be read back (`[SENSITIVE]`): re-enter the full value with
  `vercel env update <name> production` from a trusted source, then
  `vercel redeploy <deployment> --target production --non-interactive`.

## Reporting and product checks

- Report outcomes with exit codes and what was not verified.
- Show a builder's screens by copying them to a stable folder; another session's scratchpad is
  not usable, and a signed-in localhost preview would replace the user's cookie. For a live look,
  the builder runs a small proxy on its own port that adds a synthetic account's session.
- A user on a phone cannot open a local path: publish options as a private page, one line per
  choice, recommendation marked.
- A width-only breakpoint also catches a sideways phone: ask what short screens get, and add
  those sizes to the preview checks.
- Before designing what a product should notice, ask how it reaches the user today and, on their
  word, take a counts-only read of their real account.
- Take every time you write into a state file from `date`.
