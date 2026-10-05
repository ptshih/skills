---
name: browser-verify
description: "Verify web UI, layout, and frontend rendering headlessly using Playwright. Captures screenshots and accessibility trees. Use when modifying web pages, components, or verifying local web server output."
license: MIT
metadata:
  version: "1.0.0"
---

# Browser-Verify: Headless Frontend & Visual Inspection

Verify web interfaces and server rendering headlessly without blind guessing. Follows `AGENTS.md > Browser automation` (headless by default, hidden tabs, session reuse).

## Verification Procedure

### 1. Check running dev server
Before starting any server, check if port already listens (required by `AGENTS.md`):
```bash
lsof -nP -iTCP:3000 -sTCP:LISTEN
```
Never kill or restart a running dev server.

### 2. Playwright CLI session (Pi / any terminal agent)
`playwright-cli` is headless unless `--headed` is passed; reuse one named session per task.
Open the session from a scratch directory, never inside a checkout: it writes `.playwright-cli/`
snapshot files into the directory it was opened in, for the session's whole life.
```bash
cd <scratch dir> && playwright-cli -s=verify open http://localhost:<port>/<route>
playwright-cli -s=verify snapshot   # accessibility tree: verify text/buttons exist
playwright-cli -s=verify screenshot --filename=/tmp/agent-artifacts/ui-<timestamp>.png
playwright-cli -s=verify close
```
Inspect the screenshot with `read` or an image tool to verify styling and layout.

### 3. One-shot Playwright (Claude Code / Codex / Terminal)
```bash
# Capture full page screenshot
npx -y playwright screenshot --viewport-size="1280,800" http://localhost:3000 /tmp/agent-artifacts/shot.png

# Test end-to-end user interaction headlessly
npx -y playwright test
```

### 4. Fast API / Status Check
For JSON endpoints and SSR response verification:
```bash
curl -is http://localhost:3000/api/health | head -n 20
```
