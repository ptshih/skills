---
name: design-review
description: Review visual design, interaction quality and component polish against the project's design system. Use for requested design reviews, after substantial UI changes, or when design-system compliance is uncertain.
---

# Design Review

Review a feature against the project's design system through three lenses, then consolidate
the findings into one prioritized report. Small UI changes get a focused diff and headless
browser check in the main session.

Apply three lenses: visual compliance, interaction quality, and component robustness.

## When to Use

- The user requests a design review
- Substantial UI changes or new component patterns are ready for review
- When design system compliance is uncertain

## Prerequisites

1. **DESIGN.md** (or equivalent) must exist in the repo — the agents need a spec to review against
2. Know which files changed — the agents need a focused file list

## How to Run

### 1. Gather context

```bash
# Find changed UI files on the branch
git diff main --name-only -- '*.tsx' '*.ts' '*.css'
```

Read the design system before reviewing. Include the relevant guidance in any delegated brief.

### 2. Apply the three review lenses

Apply these lenses yourself by default. Merely selecting this skill does not authorize
spawning agents. If the user or project instructions authorize delegation, use the smallest
read-only review team that fits the change; a three-lens review need not mean three agents.
Use only the selected harness's supported tools and load its launch instructions only then.

**Visual Design:**
- Color token compliance (no hardcoded hex)
- Typography scale usage (correct text-* tokens)
- Spacing grid alignment (8px base unit or project-specific)
- Border radius scale
- Semantic color states (success/warning/error/info)
- Surface/background token usage

**Interaction/UX:**
- Animation easing and duration vs spec
- Loading states and transitions
- Auto-scroll behavior
- Panel/modal enter/exit motion
- Empty states
- Focus management and keyboard support
- Responsive behavior at breakpoints
- Error state graceful degradation

**Component Polish:**
- Text truncation/overflow handling
- Empty array/missing data edge cases
- Schema validation strictness
- Memoization correctness
- Accessibility (aria attributes, semantic HTML, contrast)
- Key prop stability (no array index keys)
- TypeScript type safety

### 3. For delegated review, brief each agent with

- The full design system spec (colors, typography, spacing, motion, etc.)
- The exact file list to review (8-12 files max per agent)
- A checklist of what to check (from the lists above)
- Instruction: "Report findings as a structured list with file:line references"
- Instruction: "Read only: do not edit, and do not run tests, builds, dev servers, migrations
  or anything else that writes files or reaches a database"

### 4. Consolidate into severity table

When the review is complete, merge findings into one report:

| Severity | Criteria |
|----------|----------|
| **P0 Critical** | Crashes, data loss, fundamentally broken patterns |
| **P1 High** | Layout breaks, overflow, missing responsive handling |
| **P2 Medium** | Spacing off-grid, missing transitions, a11y gaps |
| **P3 Low** | Minor polish, color contrast edge cases, naming |

Include a "What's already great" section — review should validate good work too.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Agents review too many files | Cap at 8-12 files per agent — focused review beats broad scan |
| No design spec provided | Agents can't review without a reference — read DESIGN.md first |
| Findings lack line numbers | Brief agents explicitly: "include file:line references" |
| Missing severity triage | Raw findings are noise — always consolidate with P0/P1/P2/P3 |
| Skipping "what's working" | Validating good patterns prevents future regression |

## On Herdr

When `HERDR_ENV` is `1` and delegation is authorized, reviewers can be separate sessions
in their own tabs:

1. Write each reviewer's brief (step 3) to a file.
2. Follow the orchestrator skill's "Routing" section to start each selected harness in a
   read-only session without taking focus. A new Codex session receives the brief path as
   its CLI startup prompt argument; every follow-up uses its inbox, never pane typing.
   For another harness, use its inbox when reachable; pane input requires a freshly
   inspected empty prompt and no dialog. Verify that the assignment began before waiting.
3. Wait for the reviewers with `wait-all-idle.sh` from the orchestrator skill's "Take over", read
   each report with `herdr agent read <name> --source recent-unwrapped`, then consolidate.
4. After collecting the reports, close only the completed reviewer sessions created for
   this task, using the selected harness's documented exit procedure.
