---
name: investigate-first
description: Diagnose ambiguous failures before editing, using evidence to rank and test plausible causes.
disable-model-invocation: true
---

# Investigate first

Gather evidence before changing product code. No fix without root cause: if you cannot state a
testable claim about why it is broken, keep investigating.

## Collect

- Read the actual error in full: whole message and stack trace, not someone's summary.
- Reproduce when possible. For an intermittent failure, collect triggering conditions, state,
  timing and available errors.
- Separate observed facts from inferred causes.
- Check what changed: recent commits on affected paths, working-tree and staged diffs. In a
  shared working tree, another agent session may have changed the code a minute ago.
- Read the definition, not only the call site.
- Trace inputs, state transitions, ownership boundaries and failure output.

## Scope

- Name the narrowest area that could hold the cause; say why before editing outside it.
- Keep temporary instrumentation narrow, track it, remove it before finishing.
- Never log secrets, tokens or credentials.
- A reproduction that spends money or changes an external system needs authorization.

## Test

- Rank hypotheses by evidence and cheap falsification value.
- State each as a falsifiable claim: `<thing>` is wrong because `<mechanism>`, which causes
  `<symptom>`.
- Test it before fixing: focused assertion, safe instrumentation or existing evidence.
- Do not edit until one credible mechanism explains the evidence.
- After three failed hypotheses, stop and reassess: summarize what was rejected and why, revisit
  the model of the system, gather fresh evidence. Do not cycle through unsupported guesses.
- Ask the user only when missing information or authority blocks the next useful step; say what
  is needed and why.
- Stop when evidence names the cause or the exact blocker. Report an unresolved failure honestly.

## Fix, when authorized

- Fix the cause at its source, not the symptom where it surfaces.
- Remove all temporary instrumentation.
- Add a regression test where behavior can regress.
- Write what was learned where the next agent will meet it.

Report cause and proof. Make no fix unless task authorizes implementation.
