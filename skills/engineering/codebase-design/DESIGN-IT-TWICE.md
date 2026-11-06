# Design It Twice

When the user wants to explore alternative interfaces for a chosen deepening candidate, compare designs within that scope. Work in the main session unless delegation is already authorized. Based on "Design It Twice" (Ousterhout): your first idea is unlikely to be the best.

Uses the vocabulary in [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**, **leverage**.

## Process

### 1. Frame the problem space

Briefly frame the chosen candidate using what is already known:

- The constraints any new interface would need to satisfy
- The dependencies it would rely on, and which category they fall into (see [DEEPENING.md](DEEPENING.md))
- A rough illustrative code sketch to ground the constraints, not a proposal, just a way to make the constraints concrete

Reuse existing investigation and settled constraints. Ask only when missing intent materially affects the design.

### 2. Compare alternatives

Develop materially different interfaces in the main session, using only as many alternatives as the decision needs. If delegation is authorized and useful, give each subagent a distinct design brief and a fresh context window. Loading this reference does not itself authorize delegation.

For each alternative, use the relevant file paths, coupling, dependency category from [DEEPENING.md](DEEPENING.md), and implementation responsibilities. Possible design constraints include:

- Minimal surface: "Minimize the interface: aim for 1–3 entry points max. Maximise leverage per entry point."
- Required variation: "Support the known variations without adding speculative extension points."
- Common caller: "Optimise for the most common caller: make the default case trivial."
- Ports and adapters, when relevant: "Design around ports & adapters for cross-seam dependencies."

Use the project's existing vocabulary and relevant concepts from [SKILL.md](SKILL.md); read a project glossary only when one exists and helps the task.

For each alternative, describe:

1. Interface (types, methods, params, plus invariants, ordering, error modes)
2. Usage example showing how callers use it
3. What the implementation hides behind the seam
4. Dependency strategy and adapters (see [DEEPENING.md](DEEPENING.md))
5. Trade-offs: where leverage is high, where it's thin

### 3. Present and compare

Present a concise comparison scaled to the decision. Contrast by **depth** (leverage at the interface), **locality** (where change concentrates), and **seam placement**.

After comparing, give your own recommendation: which design you think is strongest and why. If elements from different designs would combine well, propose a hybrid. Be opinionated: the user wants a strong read, not a menu.
