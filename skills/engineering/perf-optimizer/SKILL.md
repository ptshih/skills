---
name: perf-optimizer
description: "Investigate reported performance problems, measured regressions or explicit optimization requests. Measure the affected path, change the demonstrated bottleneck and compare before and after results."
license: MIT
metadata:
  version: "1.0.0"
---

# Perf-Optimizer: Bottleneck Elimination & Query Tuning

Investigate the performance problem within the requested scope. Do not turn ordinary code
changes into an optimization audit or change unrelated paths.

## Measure First

No measurement, no optimization. Before changing code, measure the slow path: a profile, a query
plan (`EXPLAIN ANALYZE`), the React Profiler, or a timed run. Change only what the measurement
implicates, measure again after, and report both numbers. The areas below are where to look, not
changes to apply everywhere; adding a dependency (a windowing library, a dataloader) needs a
measured reason.

## Optimization Areas

### 1. Database & ORM Tuning
- **N+1 Query Elimination:** Replace iterative single-record queries inside loops with batch fetching (`IN (...)`, `with: { ... }`, or dataloaders).
- **Index Verification:** Use the affected query's plan and workload to assess index needs; do not add indexes just because a column appears in a clause.
- **Selective Projections:** Replace `SELECT *` with explicit column selections to avoid serializing unneeded blobs or large text fields.

### 2. Algorithmic Complexity (CPU & Memory)
- **O(N²) Loop Flattening:** Replace nested array scans (`arr1.filter(a => arr2.some(b => b.id === a.id))`) with `Set` or `Map` lookups for O(N) performance.
- **Lazy Evaluation:** Use iterators/streams for processing large files instead of loading entire datasets into RAM.
- **Avoid Repeated Parsing:** Cache compiled regexes, JSON schema validators, and parsed date formatters outside hot loops.

### 3. Frontend & Rendering Performance
- **React Re-renders:** Memoize expensive calculations with `useMemo`; stabilize callback references with `useCallback` when passed to memoized children.
- **Virtualization:** Use windowing only when measured rendering cost justifies the added complexity.
- **Dynamic Imports:** Code-split heavy dependencies (charts, rich-text editors, syntax highlighters) using dynamic `import()`.
