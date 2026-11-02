---
name: walkthrough
description: Explain code step by step in execution order using excerpts from the source.
disable-model-invocation: true
---

# Linear walkthrough

Explain how the code in scope actually runs, in order, so the reader understands it without
reading every file. The walkthrough is a reading aid, not a review: describe what the code does
and why, and flag risks you notice, but do not change code.

## 1. Settle the scope

Resolve the target from the request:

- **A change:** uncommitted work (`git diff`, `git diff --cached`), a commit (`git show <rev>`),
  a range (`git diff <base>..<head>`), or a branch against its base (`git diff <base>...<branch>`).
- **A feature or flow:** start from its entry point (route, command, event handler, exported
  function) and follow the calls.
- **A module or codebase:** start from its public entry points.

Resolve an unnamed target from the conversation. Use the working changes or last commit only
when the request points there. Ask once when ambiguity would produce different walkthroughs.

## 2. Read before writing

Read the code needed to trace the requested execution path: what calls what, with which data, and
what state changes. Plan the sections in **execution order** (input to effect), not file order
or diff order. For a change, explain the new path, and note what the old path did only where the
difference matters.

## 3. Write it

Explain the flow in execution order. Use numbered steps and short source excerpts when they
help, at the level of detail requested. Cover the relevant parts of:

- why the code is shaped this way, taken from comments, commit messages and docs (cite them);
- invariants, edge cases and error paths;
- which tests exercise this path, and what is untested;
- anything surprising, risky or inconsistent, marked as such.

Say which claims you verified (read or ran) and which you inferred.

## 4. Excerpts come from commands, never from memory

Never type or paraphrase code into an excerpt. Produce each one with a command and paste its
output verbatim:

- working tree: `sed -n '<start>,<end>p' <path>` (or `nl -ba <path> | sed -n '<start>,<end>p'`
  for line numbers);
- another revision: `git show <rev>:<path> | sed -n '<start>,<end>p'`;
- a change: `git diff <range> -- <path>`.

Head each fenced block with its source, like `path/to/file.ts:40-58` or `git show abc123:path`.
Keep excerpts short (about 25 lines); show two excerpts rather than eliding inside one. Before
delivery, recheck excerpts if the source has changed since extraction.

## 5. Deliver it

Deliver in chat by default. Create a separate file only when requested. For a requested file,
use the chosen destination or the repository's private scratch location; otherwise use a unique
name in the OS temporary directory. Link to it in chat and do not commit it unless asked.

Based on the linear walkthrough pattern in [Simon Willison's Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/).
