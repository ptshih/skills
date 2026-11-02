---
name: browser-verify
description: "Verify rendering, layout and browser interactions affected by UI changes, or fulfill explicit browser-verification requests. Use a headless browser and focused screenshots or accessibility snapshots."
license: MIT
metadata:
  version: "1.0.0"
---

# Browser verification

Check the browser behavior affected by the request. Reuse the task's existing browser session
and stay headless unless the user requests a visible browser or an essential interaction needs
one; explain that need first.

## 1. Find the running application

Read the project's server instructions and check its actual port before starting a server:

```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN
```

Never kill or restart an existing dev server.

## 2. Use the available browser tools

Prefer an available browser integration when it covers the task. Use Playwright CLI when
requested or when the available integration cannot perform the needed interaction.

For CLI work, reuse the task's named session. If a new session is needed, open it from a private
scratch directory outside the checkout: Playwright CLI writes `.playwright-cli/` snapshots there.
Keep artifacts in the requested destination or the task's temporary directory.

```bash
cd <scratch-directory>
playwright-cli -s=<task-session> open http://localhost:<port>/<route>
playwright-cli -s=<task-session> snapshot
playwright-cli -s=<task-session> screenshot --filename=<artifact-path>.png
```

Reuse that session throughout the task. Close only sessions created for this task when finished.

## 3. Check the affected behavior

Exercise the changed route and interactions. Use accessibility snapshots for controls and text;
inspect screenshots with an image tool before claiming layout or styling is correct. Check
console or network errors when relevant. A successful HTTP response alone does not verify UI.

Use the existing project toolchain. Run relevant checks and required project gates; this skill
does not require downloading tooling, creating test files or running an unrelated full test suite.

## 4. Report the evidence

Briefly state what was exercised, the result and any unverified behavior. Include the route and
viewport when they matter to the finding.
