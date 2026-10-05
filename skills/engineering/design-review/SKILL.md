---
name: design-review
description: Use when a feature is visually complete and needs design review — checks visual compliance, interaction quality, and component polish against the design system using parallel agent teams
---

# Design Review

Dispatch a parallel agent team to review a feature against the project's design system. Three agents run simultaneously, each focused on a different dimension. Results are consolidated into a single prioritized report.

**Core principle:** Design review is three lenses applied at once — visual compliance, interaction quality, and component robustness.

## When to Use

- Feature is visually complete and ready for review
- Before merging UI-heavy PRs
- After implementing new component patterns
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

Read DESIGN.md fully before briefing agents — you need to include the spec in each agent's prompt.

### 2. Launch three agents in parallel

Run three read-only reviewers at once, one per lens below, each told not to edit. Use your
harness's way of running agents in parallel:

- **Claude Code:** the Agent tool with a read-only reviewer type (`fsd:reviewer` when it is
  installed, otherwise `general-purpose` told not to edit) and `run_in_background: true` for all
  three. Not `Explore`: it locates code from excerpts and does not review it.
- **Codex, Pi or another harness:** its own subagent or background-agent feature, when it has one.
- **No parallel agents:** apply the three lenses yourself, one after another, and still
  consolidate them in step 4.

**Agent 1 — Visual Design:**
- Color token compliance (no hardcoded hex)
- Typography scale usage (correct text-* tokens)
- Spacing grid alignment (8px base unit or project-specific)
- Border radius scale
- Semantic color states (success/warning/error/info)
- Surface/background token usage

**Agent 2 — Interaction/UX:**
- Animation easing and duration vs spec
- Loading states and transitions
- Auto-scroll behavior
- Panel/modal enter/exit motion
- Empty states
- Focus management and keyboard support
- Responsive behavior at breakpoints
- Error state graceful degradation

**Agent 3 — Component Polish:**
- Text truncation/overflow handling
- Empty array/missing data edge cases
- Schema validation strictness
- Memoization correctness
- Accessibility (aria attributes, semantic HTML, contrast)
- Key prop stability (no array index keys)
- TypeScript type safety

### 3. Brief each agent with

- The full design system spec (colors, typography, spacing, motion, etc.)
- The exact file list to review (8-12 files max per agent)
- A checklist of what to check (from the lists above)
- Instruction: "Report findings as a structured list with file:line references"

### 4. Consolidate into severity table

When all agents complete, merge findings into one report:

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

When `HERDR_ENV` is `1`, the three reviewers can be separate sessions in their own tabs, which
works in any harness and lets the user watch them:

1. Write each reviewer's brief (step 3) to a file.
2. Per reviewer, open a tab at the repository root and start a read-only session (Claude Code
   `--permission-mode plan`, Codex `--sandbox read-only`):
   `herdr tab create --workspace "$HERDR_WORKSPACE_ID" --cwd <repo root> --label <lens>-review --no-focus`,
   then `herdr agent start <name> --kind <claude|codex|pi> --pane <root pane> -- <read-only flags>`.
   Read the screen for an empty prompt and no dialog, then send one line naming the brief and
   asking for the findings as the final reply: `herdr agent prompt <name> "<line>"`.
3. Wait for all three with `wait-all-idle.sh` from the orchestrator skill's "Take over", read
   each report with `herdr agent read <name> --source recent-unwrapped`, then consolidate.
4. Exit each session with `herdr agent send-keys <name> ctrl+c ctrl+c` and close its tab.
