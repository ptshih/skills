# Third-party notices

`SKILL.md`, `AGENTS.md`, `README.md` and the `rules/` files are adapted from
[Vercel's react-best-practices skill](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md).
Changes: the description and "When to Apply" limit the skill to reported performance problems,
measured regressions and explicit optimization reviews, matched to the project's framework
version, with measurements before and after and added complexity only when the problem justifies
it; the Quick Reference rule index is removed in favour of finding rules by category prefix and
reading only the relevant ones, and `AGENTS.md` is reference material for a requested
comprehensive review. `SKILL.md` locates `rules/` and `AGENTS.md` through `${CLAUDE_SKILL_DIR}`;
three links in `AGENTS.md` point into `rules/`, where the linked files live; `README.md` notes
that the build tooling stays upstream; `metadata.json` is omitted; `agents/openai.yaml` is new.

The upstream repository declares the MIT License in its `README.md` and in this skill's
frontmatter (`license: MIT`, `author: vercel`) but ships no `LICENSE` file or copyright notice,
so none is reproduced here. The standard MIT License text follows.

```text
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
