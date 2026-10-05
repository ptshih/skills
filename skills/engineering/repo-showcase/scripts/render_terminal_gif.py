#!/usr/bin/env python3
"""Render a terminal-style demo GIF from a JSON storyboard.

Usage:
  render_terminal_gif.py SPEC.json OUT.gif [--frames DIR] [--colors 64]

The storyboard describes one or more panes (columns of stacked panes) and a list of
steps that append lines to them. Each step that changes what is visible produces one
frame; `silent` steps change state without a frame so that a multi-line command can
appear at once. See ../assets/example-spec.json for a complete storyboard and
../references/demo-gif.md for the storyboarding rules.

Spec (all keys except columns/steps optional):
{
  "title": "text centred in the window bar",
  "width": 960, "height": 620,
  "font": "/System/Library/Fonts/Menlo.ttc", "font_size": 13, "line_height": 20,
  "colors": {"fg": "#c9d1d9"},               # override any palette name
  "columns": [
    {"width": 0.6, "panes": [{"id": "L", "header": "coordinator"}]},
    {"panes": [{"id": "B", "header": "worker 1"}, {"id": "V", "header": "worker 2"}]}
  ],
  "steps": [
    {"type": "L", "prefix": [["❯ ", "prompt", true]], "text": "typed text", "hold": 500},
    {"line": "L", "segs": [["bold purple", "purple", true], " plain", ["dim", "dim"]], "ms": 600},
    {"cmd": "L", "text": "git status", "cont": ["    --more-args"], "tail": [["  → ok", "dim"]], "ms": 500},
    {"silent": "B", "segs": "appears with the next frame"},
    {"blank": "L"},
    {"header": "B", "text": "new header"},
    {"clear": ["B", "V"], "header": "no tab"},
    {"hold": 1000}
  ]
}
A segment is a string (default colour) or [text, colour, bold]. Colours are palette
names (fg dim white green yellow red blue purple prompt) or "#rrggbb".

Exit status 1 when a line overflows its pane or a glyph is missing from the font, so
the problem is noticed before the GIF is published. The GIF is still written.
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

PALETTE = {
    "bg": "#0d1117", "pane": "#161b22", "border": "#30363d",
    "fg": "#c9d1d9", "dim": "#8b949e", "white": "#f0f6fc",
    "green": "#3fb950", "yellow": "#d29922", "red": "#f85149",
    "blue": "#58a6ff", "purple": "#bc8cff", "prompt": "#7ee787",
}
DEFAULT_FONTS = [
    "/System/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]
TITLE_H, PAD, GUTTER, HEADER_H = 36, 14, 12, 26


def hex_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


class Pane:
    def __init__(self, pid, x, y, w, h, header, line_h):
        self.id, self.x, self.y, self.w, self.h = pid, x, y, w, h
        self.header, self.lines, self.cursor = header, [], False
        self.capacity = max(1, (h - HEADER_H - 20) // line_h)


class Renderer:
    def __init__(self, spec):
        self.spec = spec
        self.W = spec.get("width", 960)
        self.H = spec.get("height", 620)
        self.line_h = spec.get("line_height", 20)
        size = spec.get("font_size", 13)
        font = spec.get("font") or next((f for f in DEFAULT_FONTS if os.path.exists(f)), None)
        if not font:
            sys.exit("No monospace font found; set \"font\" in the spec")
        self.reg = ImageFont.truetype(font, size, index=0)
        try:
            self.bold = ImageFont.truetype(font, size, index=1)
        except OSError:
            self.bold = self.reg
        self.title_font = ImageFont.truetype(font, max(size - 1, 10), index=0)
        self.cw = self.reg.getlength("M")
        self.colors = {k: hex_rgb(v) for k, v in {**PALETTE, **spec.get("colors", {})}.items()}
        self.panes = {}
        self.layout()
        self.frames, self.durations, self.overflow = [], [], []
        self.glyph_cache = {}
        self.notdef = self.glyph_bytes(chr(0x0378))  # unassigned code point renders the .notdef box
        self.missing = set()

    def glyph_bytes(self, ch):
        if ch not in self.glyph_cache:
            w = max(1, int(self.reg.getlength(ch))) + 4
            im = Image.new("L", (w, self.reg.size + 8), 0)
            ImageDraw.Draw(im).text((2, 0), ch, font=self.reg, fill=255)
            self.glyph_cache[ch] = im.tobytes()
        return self.glyph_cache[ch]

    def layout(self):
        cols = self.spec["columns"]
        inner_w = self.W - 2 * PAD - GUTTER * (len(cols) - 1)
        fixed = sum(c.get("width", 0) for c in cols)
        free = [c for c in cols if "width" not in c]
        share = (1 - fixed) / len(free) if free else 0
        x = PAD
        top, bottom = TITLE_H + PAD, self.H - PAD
        for col in cols:
            w = round(inner_w * col.get("width", share))
            n = len(col["panes"])
            h = (bottom - top - GUTTER * (n - 1)) // n
            y = top
            for p in col["panes"]:
                self.panes[p["id"]] = Pane(p["id"], x, y, w, h, p.get("header", ""), self.line_h)
                y += h + GUTTER
            x += w + GUTTER

    def color(self, name):
        if not name:
            return self.colors["fg"]
        return hex_rgb(name) if name.startswith("#") else self.colors[name]

    def segs(self, value):
        if value is None:
            return [("", self.colors["fg"], False)]
        if isinstance(value, str):
            value = [value]
        out = []
        for s in value:
            if isinstance(s, str):
                s = [s]
            text = s[0]
            for ch in text:
                if not ch.isspace() and self.glyph_bytes(ch) == self.notdef:
                    self.missing.add(ch)
            out.append((text, self.color(s[1] if len(s) > 1 else None), bool(s[2]) if len(s) > 2 else False))
        return out

    def render(self):
        im = Image.new("RGB", (self.W, self.H), self.colors["bg"])
        d = ImageDraw.Draw(im)
        for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
            d.ellipse([PAD + i * 20, 12, PAD + i * 20 + 12, 24], fill=c)
        title = self.spec.get("title", "")
        d.text(((self.W - self.title_font.getlength(title)) / 2, 11), title, font=self.title_font, fill=self.colors["dim"])
        for p in self.panes.values():
            d.rounded_rectangle([p.x, p.y, p.x + p.w, p.y + p.h], radius=6, fill=self.colors["pane"], outline=self.colors["border"])
            d.text((p.x + 12, p.y + 7), p.header, font=self.reg, fill=self.colors["dim"])
            d.line([p.x, p.y + HEADER_H, p.x + p.w, p.y + HEADER_H], fill=self.colors["border"])
            visible = p.lines[-p.capacity:]
            body = Image.new("RGB", (p.w - 2, p.capacity * self.line_h + 12), self.colors["pane"])
            bd = ImageDraw.Draw(body)
            y = 9
            for li, line in enumerate(visible):
                x = 11
                for text, color, bold in line:
                    f = self.bold if bold else self.reg
                    bd.text((x, y), text, font=f, fill=color)
                    x += f.getlength(text)
                if x > p.w - 12:
                    self.overflow.append((p.id, "".join(t for t, _, _ in line)))
                if p.cursor and li == len(visible) - 1:
                    bd.rectangle([x + 1, y + 2, x + self.cw - 1, y + self.line_h - 4], fill=self.colors["fg"])
                y += self.line_h
            im.paste(body, (p.x + 1, p.y + HEADER_H + 1))
        return im

    def frame(self, ms):
        self.frames.append(self.render())
        self.durations.append(int(ms))

    def run(self):
        for step in self.spec["steps"]:
            if "type" in step:
                p = self.panes[step["type"]]
                prefix = self.segs(step.get("prefix", []))
                text, stride, ms = step["text"], step.get("step", 4), step.get("ms", 55)
                p.lines.append(list(prefix))
                p.cursor = True
                for i in range(stride, len(text) + stride, stride):
                    p.lines[-1] = prefix + self.segs(text[:i])
                    self.frame(ms)
                p.lines[-1] = prefix + self.segs(text)
                self.frame(step.get("hold", 500))
                p.cursor = step.get("keep_cursor", False)
            elif "cmd" in step:
                p = self.panes[step["cmd"]]
                p.cursor = False
                p.lines.append([("$ ", self.colors["dim"], False)] + self.segs(step["text"]) + (self.segs(step["tail"]) if "tail" in step else []))
                for extra in step.get("cont", []):
                    p.lines.append(self.segs(extra))
                self.frame(step.get("ms", 500))
            elif "line" in step:
                p = self.panes[step["line"]]
                p.cursor = False
                p.lines.append(self.segs(step.get("segs")))
                self.frame(step.get("ms", 600))
            elif "silent" in step:
                self.panes[step["silent"]].lines.append(self.segs(step.get("segs")))
            elif "blank" in step:
                self.panes[step["blank"]].lines.append(self.segs(""))
            elif "header" in step and "clear" not in step:
                self.panes[step["header"]].header = step["text"]
            elif "clear" in step:
                ids = step["clear"] if isinstance(step["clear"], list) else [step["clear"]]
                for pid in ids:
                    self.panes[pid].lines = []
                    if "header" in step:
                        self.panes[pid].header = step["header"]
            elif "hold" in step:
                self.frame(step["hold"])
            else:
                sys.exit(f"Unknown step: {step}")

    def save(self, out, colors, frames_dir):
        if frames_dir:
            os.makedirs(frames_dir, exist_ok=True)
            n = len(self.frames)
            for i in sorted({0, n // 4, n // 2, (3 * n) // 4, n - 1}):
                self.frames[i].save(os.path.join(frames_dir, f"frame_{i:03d}.png"))
        pal = [f.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE) for f in self.frames]
        pal[0].save(out, save_all=True, append_images=pal[1:], duration=self.durations, loop=0, optimize=True, disposal=1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("out")
    ap.add_argument("--frames", help="directory for five sample PNG frames to inspect")
    ap.add_argument("--colors", type=int, default=64, help="GIF palette size (default 64)")
    args = ap.parse_args()
    with open(args.spec) as fh:
        spec = json.load(fh)
    r = Renderer(spec)
    r.run()
    r.save(args.out, args.colors, args.frames)
    for p in r.panes.values():
        print(f"pane {p.id}: {p.w}px, ~{int((p.w - 24) / r.cw)} chars/line, {p.capacity} visible lines")
    print(f"frames={len(r.frames)} total_ms={sum(r.durations)} size={os.path.getsize(args.out)} bytes")
    status = 0
    if r.overflow:
        status = 1
        print("OVERFLOW (shorten or split these lines):")
        for pid, text in dict.fromkeys(r.overflow):
            print(f"  [{pid}] {text}")
    if r.missing:
        status = 1
        print("MISSING GLYPHS in font (replace these characters): " + " ".join(f"U+{ord(c):04X} {c}" for c in sorted(r.missing)))
    sys.exit(status)


if __name__ == "__main__":
    main()
