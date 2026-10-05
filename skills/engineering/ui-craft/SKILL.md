---
name: ui-craft
description: "Build polished, responsive, and accessible web interfaces. Avoid generic AI templates by applying strict spacing grids, design tokens, interactive states, and WCAG accessibility standards."
license: MIT
metadata:
  version: "1.0.0"
---

# UI-Craft: High-Craft Web UI & Aesthetics

Build modern, production-grade frontend interfaces that look designed by a human product designer. Avoid generic, purple-tinted AI cards.

The project's own design system comes first: its tokens, spacing scale, components and rules
(theme files, `DESIGN.md`, `AGENTS.md`). The Tailwind classes and colours below are defaults for
a project that has none; never add a palette class or raw colour a project's tokens replace.

## Design Principles

### 1. Spacing & Rhythm
- Use an 8pt grid scale: `p-2` (8px), `p-4` (16px), `p-6` (24px), `gap-4`, `gap-6`.
- Keep generous whitespace between sections; avoid cramped layouts.
- Mobile-first responsive hierarchy: layout columns stack on mobile, expand with `md:grid-cols-2 lg:grid-cols-3`.

### 2. Color & Hierarchy
- Define neutral scale with CSS variables or design tokens (zinc, slate, or neutral).
- Maximum 1 primary brand accent color; use subdued neutral shades for surfaces, borders, and secondary text.
- Maintain WCAG AA contrast ratio (min 4.5:1 for normal text).
- Avoid raw pure black (`#000`) on white; use soft dark neutrals (`#09090b` or `#18181b`).

### 3. Interactive Polish
- Every clickable element must define:
  - Hover state: subtle background shift (`hover:bg-accent/80`).
  - Active state: slight scale down or darker tone (`active:scale-[0.98]`).
  - Focus state: keyboard-accessible ring (`focus-visible:ring-2 focus-visible:ring-ring`).
  - Disabled state: reduced opacity and `cursor-not-allowed`.
- Fast, smooth transitions: `transition-colors duration-150 ease-in-out`.

### 4. Accessibility & States
- Use semantic elements: `<button>`, `<nav>`, `<main>`, `<dialog>`, not `<div onClick>`.
- Icon-only buttons must carry `aria-label`.
- Loading states: use skeleton placeholders matching content shape, not generic centered spinners.
- Empty states: include clear messaging, secondary explanation, and a call-to-action button.
