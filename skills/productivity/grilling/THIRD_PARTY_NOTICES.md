# Third-party notices

`SKILL.md` and `agents/openai.yaml` are adapted from
[Matt Pocock's grilling skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md).
Changes: the skill is user-invoked (`disable-model-invocation: true` and
`policy.allow_implicit_invocation: false`) with a shorter description; the interview stays within
the requested scope and asks one focused question at a time through the harness's question tool,
with a recommendation and the meaningful alternatives, instead of numbered rounds covering the
whole decision frontier; facts are looked up in the main session, with delegation only when
already authorized; routine details are decided rather than asked; the interview stops when the
requested critique is complete and does not itself authorize implementation. The following
notice is preserved from the [upstream repository](https://github.com/mattpocock/skills/blob/main/LICENSE).

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
