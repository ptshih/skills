---
name: summarize
description: Summarize documents, plans, diffs and results in plain English at the requested level of detail.
disable-model-invocation: true
---

# Summarize

Lead with the main point and include the material details the reader needs to understand or
act. Follow the user's reply preferences. Default to a concise summary under 150 words unless
the user asks for more detail; do not expand a routine summary into a report.

## Pick the subject

Resolve "it" from the conversation or the supplied path or reference. Ask one focused question
only when ambiguity materially changes what needs summarizing.

Read the source needed for the requested scope. A whole-document summary requires the whole
document; an excerpt supports only a summary of that excerpt. Reuse material already fully in
context. For a diff, read enough surrounding code to understand the change. State access or
coverage gaps instead of guessing.

## Write the summary

- Use plain English and explain technical terms only when they help the reader.
- Cover the main outcome, material changes, decisions and significant caveats. Preserve
  important uncertainty even in a short summary.
- Attribute claims to the source. Clearly label any inference or judgment you add.
- Choose prose, a short list or a table according to the material and the requested format.
- Link to relevant sources instead of copying large sections. Include file or function names
  only when useful.
- Omit secrets and irrelevant personal information.

## When detail is requested

Expand the substantive points, relevant background, alternatives, changes from earlier versions
and evidence limits. Use the source's organization when it helps, without forcing a fixed outline
or a fixed fraction of its length.

Give a confidence assessment only when asked. Add recommendations only when requested, and
distinguish them from what the source says. Deliver in chat unless the user requests another form.
