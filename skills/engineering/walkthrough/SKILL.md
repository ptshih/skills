---
name: walkthrough
description: Write a linear walkthrough that explains how code runs, step by step in execution order, with every code excerpt pulled from the files by a command rather than retyped. Use for "walk me through this", "walkthrough", "how does this work", "explain this change", "explain this feature/module/codebase", after a large agent-written change lands, or before reviewing code you did not write.
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

With no target named, use the uncommitted changes, or the last commit when the tree is clean.
Ask once only when two readings would produce different walkthroughs.

## 2. Read before writing

Read every file in scope, then trace the execution path: what calls what, with which data, and
what state changes. Plan the sections in **execution order** (input to effect), not file order
or diff order. For a change, explain the new path, and note what the old path did only where the
difference matters.

## 3. Write it

Number the sections in execution order. Each section has a few sentences of plain explanation
followed by the excerpt that shows it. Cover along the way:

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
finishing, re-run the extraction for each excerpt, or `grep -nF` its first line, to confirm it
still matches the file.

If `uvx showboat --help` works, you may build the file with `showboat note` for prose and
`showboat exec` for extraction commands, which records each command beside its output.

## 5. Deliver it

Save the walkthrough as Markdown with a unique name such as `walkthrough-<topic>-<date>.md`. Use
the repository's private scratch location when its instructions name one (for example
`.agents/tmp/`), otherwise the OS temporary directory. Do not commit it unless asked.

In chat, give a short plain-English summary of the flow (a few sentences), the risks or gaps you
flagged, and the absolute path to the file.

Based on the linear walkthrough pattern in [Simon Willison's Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/).
