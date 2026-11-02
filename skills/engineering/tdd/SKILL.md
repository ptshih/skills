---
name: tdd
description: Test-driven development through behavioral interfaces, one red-green-refactor cycle at a time.
disable-model-invocation: true
---

# Test-Driven Development

TDD is the red → green loop. Use the guidance relevant to the current change: what a good test
is, where it belongs, and which testing mistakes to avoid. Reuse established project conventions.

When exploring the codebase, read `CONTEXT.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Seams: where tests go

A **seam** is where a module's interface lives (the term is defined in `codebase-design`): the place where you observe behavior without reaching inside. Tests go through a module's interface, never against its internals. A deep module may also have internal seams used by its own tests; test at one only when the agreed seams include it.

Choose the test boundary from the behavior under test and the project's existing interfaces.
Decide routine test structure without a per-test announcement or confirmation. Ask only when
missing intent about expected behavior or the public interface materially affects the result.
Focus coverage on the change's important behavior and risks.

When interface design is part of the task, consult `codebase-design` as needed. It is a reference,
not a separate workflow to run for every test.

## Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database when the interface could show the result). When stored state is itself the contract, such as a migration or a rule about what is stored, checking it directly is the test. The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological**: the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec.
- **Horizontal slicing**: writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead: one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Keep refactoring in scope.** A TDD cycle does not authorize unrelated cleanup or an additional review workflow.
