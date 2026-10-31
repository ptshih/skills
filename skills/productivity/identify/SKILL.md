---
name: identify
description: Set the current agent's name, conversation title, and Herdr tab label together from a user-supplied name, such as /identify atlas-lead. Use when the user asks to identify or consistently name the current session across these surfaces.
---

# Identify

One request names the current agent, conversation, and enclosing Herdr tab. Apply
only to the current session; examples in a request to create this skill are not
instructions to rename an existing session.

## Derive the names

Use the supplied lower-case, hyphen-separated name as the agent name and tab label.
For the conversation title, replace hyphens with spaces and capitalize each word:

| Input | Agent name | Conversation title | Herdr tab |
| --- | --- | --- | --- |
| `atlas-lead` | `atlas-lead` | `Atlas Lead` | `atlas-lead` |
| `atlas-review-2` | `atlas-review-2` | `Atlas Review 2` | `atlas-review-2` |

Honor an explicitly supplied title instead of deriving one. If the name is missing
or ambiguous, ask one focused question before renaming. Do not invent a project
prefix or silently shorten a name. Pass names as literal CLI arguments or structured
API fields, never executable shell text.

## Apply and verify

1. Identify the current harness/session and, if present, its Herdr pane and parent
   tab. Use current-session IDs and verify their relationship; do not target the
   currently focused pane, a stale note, or another agent selected by its old name.
2. Inspect existing names and supported native controls before changing them. Check
   for an existing agent with the requested name; never take over another agent's
   address. Leave matching values alone so repeating the request is a no-op.
3. Adopt the requested agent identity and set the independent agent-name field
   where supported. In Herdr, use its agent registration below. Outside Herdr, use
   the harness's native agent-name field if it has one. If it has no separate field,
   report the name as a conversational role only; do not claim a durable routing
   alias or overwrite the human-readable title with the slug.
4. Set the conversation title with a native rename tool or supported CLI/API. For
   Codex, read [the native title procedure](references/codex-title.md) at
   `${CLAUDE_SKILL_DIR}/references/codex-title.md`; without that variable, resolve it
   relative to this SKILL.md. For other harnesses, inspect their available native
   controls and current documentation. Do not guess an API or install a rename tool.
5. Rename the enclosing Herdr tab when applicable. Read back every changed field
   using its native metadata API. A terminal escape sequence or tab label is not
   proof the conversation title changed.
6. Report the three resulting names, noting any unavailable or failed surface.
   These are separate metadata operations, not an atomic transaction. Preserve
   successful changes after a partial failure; on retry, read current state and
   change only mismatches. Do not claim all three succeeded without readback.

Do not type into prompt boxes, queue slash commands as agent messages, edit session
storage, restart agents, change models, or bypass a permission denial. Naming does
not grant new task ownership. Keep stable thread IDs for messaging; do not assume
the Herdr agent slug is also a Codex queue alias. An unavailable UI alone does not
prove the native CLI/API is unavailable.

## On Herdr

When `HERDR_ENV=1`, inspect the installed help for `herdr agent rename` and
`herdr tab rename`. Read `herdr agent get "$HERDR_PANE_ID"` and derive the parent
`tab_id` from that result. Confirm it matches `HERDR_TAB_ID` when provided, and
for Codex confirm `agent_session.value` matches `CODEX_THREAD_ID` when available.
If identification conflicts or is unavailable, stop that part and report it.

Use `herdr agent list` to check name collisions. Apply the verified current-pane
and parent-tab targets with `herdr agent rename <pane-id> <agent-name>` and
`herdr tab rename <tab-id> <tab-label>`. Verify with `herdr agent get <pane-id>`
(`name`) and `herdr tab get <tab-id>` (`label`). Do not rename the workspace or
other panes. If the parent tab contains multiple agents, confirm shared-tab intent
before changing its label. Outside Herdr, skip the tab operation and say so.
