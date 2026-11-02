---
name: find-skills
description: Find or install agent skills when the user asks for a skill or a search of the skills ecosystem. Answer ordinary coding and how-to requests directly.
---

# Find Skills

Identify the requested capability and check existing installed skills before searching for new
ones. Use connected discovery tools when suitable, or search with the Skills CLI:

```sh
npx skills@latest find <query>
```

A request such as "find a skill for React performance" calls for discovery. "Make this React
page faster" calls for working on the page, not a skill search.

Evaluate a candidate's actual `SKILL.md`, relevant references and scripts before recommending
or installing it. Check task fit, scope, tool and network requirements, delegated work and
external actions. Popularity and stars are context, not evidence of safety or suitability.
Prefer a small, relevant skill over a broad overlapping bundle.

Present the best fit with its source link and any material requirements. Offer alternatives
only when they represent a useful trade-off. Do not invent install counts or endorsements.

Install only the concrete skill and scope the user selected, including an unambiguous approval
of a presented recommendation. A search request alone does not authorize installation, and
ambiguous assent to several options needs one focused clarification. Reuse settled approval.
Use project scope unless the user requested global availability or established that preference
for this installation. Do not update or install unrelated skills.

```sh
# Project scope; add -g only for an authorized global installation.
npx skills@latest add <owner/repo> --skill <skill-name>
```

After installing, verify the actual installed instructions, discovery location and requested
scope. Report the result and any meaningful behavior the skill adds. Do not run its scripts
or workflows merely because installation succeeded.

If no suitable skill is found, say so briefly. Continue the underlying task when it is already
requested and authorized; do not install a weak match just to produce a result.
