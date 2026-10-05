---
name: summarize
description: Summarize a document, plan, diff, report, thread or result in detail, in plain English, for a reader who did not watch the work. Use for /summarize, "summarize it", "summarize in plain english", "walk me through it", "what does this say", or when a plan or proposal needs a plain-English summary before approval.
---

# Summarize

Give a complete, plain-English account of one thing so the reader can decide or act on
it without opening the source. Detail means coverage, not length: every substantive point
survives, the padding does not.

## Pick the subject

"It" is the most recent deliverable, document, plan, diff, report or thread in the
conversation. `/summarize <path or reference>` names it directly. If two candidates are
equally recent, ask one line and stop.

Read the whole source before writing, never a preview, an excerpt or your memory of it.
If the source is already fully in context, do not reread it. For a diff, read enough of
the changed files to know what the change does. For a thread or session, reread the
turns the summary covers.

## Register

Plain English overrides caveman and any other compressed mode for the summary itself.
Complete sentences of about 20 words or fewer, one idea each. Sentence case. Concrete
nouns. Expand every acronym the first time. No em-dashes, semicolons, parentheticals,
metaphors or coined terms. Name a file, function or flag only when the reader must go
there. Keep the source's own words for terms that matter, quoted when they are a label.

Report, do not opine. Keep the source's claims as its claims: "the document says", "the
plan proposes". If you add an inference or a judgment, mark it as yours in one clause.
Keep every caveat, unknown and "not verified" the source carries. Never fill a gap with
a guess.

## Shape

1. **What it is**, in two or three sentences: the kind of thing, who made it, why, and
   what the reader is expected to do with it.
2. **The starting point** the source assumes, only when the reader needs it.
3. **The substance**, in the source's own order and grouping. Parallel items with
   attributes (options, findings, rules, decisions) go in a table with one row each.
   Sequential or causal material stays in prose. Every numbered or named item in the
   source appears; if you merge two, say so.
4. **What changed, was dropped or was narrowed** against an earlier plan, spec or
   version, with the reason the source gives.
5. **Decisions the reader owns**, with the options the source offers for each.
6. **Evidence limits**: what the source did not check, could not verify, or estimates
   without measurement.

Headers only when the summary passes about 500 words, and at most three. Length scales
with the source: about a tenth to a fifth of it, rarely past 900 words. If the reader
asked for "brief", "short" or "one paragraph", drop items 2, 4 and 6 and keep the rest
to a paragraph.

## Close

End with one confidence line for the summary itself: a percentage, then one line per
point you could not confirm from the source (an ambiguous passage, a term you had to
interpret, a section you skimmed). Say verified, inferred or unread; never blur them.

## Do not

- Summarize from a file's first screen, a search hit or an earlier summary.
- Add recommendations the source does not make.
- Reorder the source into your own framework when its own order is clear.
- Restate what is already in the conversation or a linked document; point to it.
- Include secrets, credentials or personal data from the source.
