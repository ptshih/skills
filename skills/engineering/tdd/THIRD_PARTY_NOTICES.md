# Third-party notices

`SKILL.md`, `tests.md`, `mocking.md` and `agents/openai.yaml` are adapted from
[Matt Pocock's tdd skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md).
Changes: a seam is confirmed with the user only when it is new or unclear; the seam definition
follows the `codebase-design` vocabulary; `tests.md` allows call counts on a boundary fake when
the count is the rule, and direct checks of stored state when that state is the contract; the
Codex label says "red-green loop". The following notice is preserved from the
[upstream repository](https://github.com/mattpocock/skills/blob/main/LICENSE).

```text
MIT License

Copyright (c) 2026 Matt Pocock

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
