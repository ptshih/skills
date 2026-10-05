# Demo GIF

The GIF answers "what does using this look like?" in under a minute, without sound and
without the reader clicking. Decide first whether it will be a recording or an
illustration, because the caption has to say which.

## Recording or illustration

Record when the flow runs in under a few minutes, costs nothing meaningful (no paid API
calls the user has not approved), and a recorder is installed: `vhs` (tape → GIF,
needs `ttyd` + `ffmpeg`), `asciinema` + `agg`, or a screen capture of a real session.
Check with `command -v vhs ttyd ffmpeg asciinema agg`.

Illustrate when the real flow needs live infrastructure, a human in the loop, paid calls,
or tens of minutes (multi-agent coordination, deploys, anything with approvals). Draw the
storyboard from material the repo already documents: worked examples, role or prompt
files, CLI output pasted in docs, test names. Invent as little as possible and keep
invented specifics generic (a file called `src/parser.ts`, not a line number). The caption
then reads like: *Illustration of the [review loop](…): one builder, then a fresh reviewer.
Drawn from the role files, not screen-recorded; for a real trace see the [worked example](…).*

## Storyboard shape

Thirty to forty-five seconds, looping, ending on a four to five second hold of the final
state. A good arc:

1. The user's input, typed (one or two lines).
2. Setup the tool does on its own (three to five lines, one per frame).
3. The work, visible in whichever pane does it. Show one failure or check that turns
   green; readers trust a tool that shows verification.
4. Wake / result / verification back in the main pane.
5. Cleanup and a one-line closing status.

Layout by role: one wide pane for the thing the user talks to, and one stacked pane per
concurrent worker or process on the right. Two workers make the "each in its own
terminal" point far better than one.

## Rendering with the bundled script

`scripts/render_terminal_gif.py SPEC.json OUT.gif --frames DIR` renders a JSON
storyboard (schema in the script's docstring; complete example in
`assets/example-spec.json`). Rules of thumb that came from real renders:

- **Fit lines to the pane.** At Menlo 13px a character is ~7.8px, so a 556px pane holds
  ~67 characters and a 360px pane ~42. The script prints chars-per-line per pane and
  exits 1 listing any overflow; shorten or split the line rather than shrinking the font.
- **Multi-line commands appear in one frame.** Use `cmd` with `cont` for continuation
  lines. It reads naturally and, because a scrolling pane redraws fully on every frame,
  fewer frames is the main lever on file size (a three-pane 41s GIF landed at 1.7MB; two
  panes at 32s was under 1MB).
- **Check glyphs.** Menlo has no ⏰ or ⟵; it does have ← → » ▸ ● ◆ ✓ ├ └ ❯. The script
  detects missing glyphs by comparing against the font's .notdef box and exits 1.
- **Long panes scroll.** Capacity is computed from height; older lines fall off the top
  like a terminal. Put the lines that must be visible together (a report) at the end of
  that pane's sequence, and clear worker panes when their tab closes.
- **Palette.** 64 colours with no dither is enough for a dark terminal and keeps size
  down; the defaults are GitHub's dark theme.
- **Look at the frames.** The script writes five PNG samples; read them as a first-time
  visitor would. Clipped text, tofu boxes and misaligned prompts are only visible this way.

## Placing in the README

```md
![ALT: what the animation shows, in one sentence](assets/demo.gif)

*Caption: recorded or illustrated, from what, linking to the source material.*
```

Keep the GIF under about 2MB and 1000px wide (GitHub renders README content at
~830–1000px). A relative `assets/` path renders on GitHub and lets a repo link checker
validate the file exists; use an absolute `raw.githubusercontent.com` URL only if the
README is also shown somewhere that does not ship the asset (npm, a package registry).
