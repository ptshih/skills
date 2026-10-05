---
name: test-synthesizer
description: "Generate adversarial, boundary, and property-based test cases to eliminate happy-path bias. Tests extremes: nulls, empty collections, unicode, huge payloads, and network timeouts."
license: MIT
metadata:
  version: "1.0.0"
---

# Test-Synthesizer: Adversarial & Boundary Test Generation

Force test suites beyond happy paths by testing boundary conditions, invalid formats, and adversarial inputs.

The vectors below are a menu, not a quota. Test through the seams agreed for the code (see the
`tdd` skill), and pick only the vectors that match an input the code really accepts and a risk it
really has; large payloads and 10,000-item collections belong only where size is a real risk.

## Test Boundary Vectors

### 1. Numeric Inputs
- Zero: `0`, `-0`, `"0"`.
- Negatives: `-1`, `-999999`.
- Limits: `Number.MAX_SAFE_INTEGER`, `Number.MIN_SAFE_INTEGER`, `Infinity`, `-Infinity`.
- Floats: `0.1 + 0.2`, `1e-7`, division by zero.
- Invalid: `NaN`, non-numeric strings passed to numeric parsers.

### 2. String & Text Inputs
- Empty string: `""`.
- Whitespace only: `"   "`, `"\t\n\r"`.
- Unicode & special symbols: multi-byte emojis (`🚀👨‍👩‍👧‍👦`), RTL markers, null bytes (`\0`).
  Put invisible, bidirectional and look-alike characters (a Cyrillic a inside a Latin word) into source as code points, not typed characters or escapes: a `\uXXXX` passed through a tool's parameters can land in the file as the literal character, invisible, and a raw U+2028 or U+2029 ends a JavaScript line. Build them with `String.fromCodePoint(0x202e)` and check each changed file with `LC_ALL=C grep -n '[^ -~]'` or `od -c`.
- Dangerous strings: SQL injection payloads, `<script>alert(1)</script>`, template injections (`{{7*7}}`).
- Near misses for a text filter: whenever a rule widens, add accept cases for the closest legitimate inputs, such as a hyphenated name that contains the trigger (`always-deploy`), a two-letter symbol from another script (a Greek delta-t), a negation before the trigger word (`aren't allowed to push`) and a list that the negation does not cover.
- Large strings: 1MB/10MB string payloads to test buffer overflow and memory bounds.
- Regex backtracking: for every regular expression, time a 20,000-character run of the characters two neighbouring repetitions can both match (a keyword repeated inside one identifier run such as `x-token-x-token-…`, `a.a.a.…`, `hooks/hooks/…`). Run the timing in a child process with a hard timeout, so a pattern that backtracks fails the test instead of hanging the suite.

### 3. Collections & Data Structures
- Empty: `[]`, `{}`.
- Single item: `[x]`.
- Large scale: 10,000 items (test memory and execution timeout).
- Duplicates: arrays with identical keys/elements.
- Sparseness & undefined: arrays with holes (`[1, , 3]`), missing object keys.

### 4. Async & Failure Modes
- Slow networks: artificial delays and abort controller timeouts.
- Server errors: HTTP 500, 502, 504 responses.
- Partial failures: batch operations where 1 out of 10 items throws.
