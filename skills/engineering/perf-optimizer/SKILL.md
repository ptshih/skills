---
name: perf-optimizer
description: "Identify and eliminate performance bottlenecks: database N+1 queries, un-indexed lookups, accidental O(N²) loops, redundant React re-renders, and memory leaks."
license: MIT
metadata:
  version: "1.0.0"
---

# Perf-Optimizer: Bottleneck Elimination & Query Tuning

Audit and optimize runtime performance across database queries, algorithms, and rendering loops.

## Measure First

No measurement, no optimization. Before changing code, measure the slow path: a profile, a query
plan (`EXPLAIN ANALYZE`), the React Profiler, or a timed run. Change only what the measurement
implicates, measure again after, and report both numbers. The areas below are where to look, not
changes to apply everywhere; adding a dependency (a windowing library, a dataloader) needs a
measured reason.

## Optimization Areas

### 1. Database & ORM Tuning
- **N+1 Query Elimination:** Replace iterative single-record queries inside loops with batch fetching (`IN (...)`, `with: { ... }`, or dataloaders).
- **Index Verification:** Assert columns used in `WHERE`, `ORDER BY`, and `JOIN` clauses have corresponding database indexes.
- **Selective Projections:** Replace `SELECT *` with explicit column selections to avoid serializing unneeded blobs or large text fields.

### 2. Algorithmic Complexity (CPU & Memory)
- **O(N²) Loop Flattening:** Replace nested array scans (`arr1.filter(a => arr2.some(b => b.id === a.id))`) with `Set` or `Map` lookups for O(N) performance.
- **Lazy Evaluation:** Use iterators/streams for processing large files instead of loading entire datasets into RAM.
- **Avoid Repeated Parsing:** Cache compiled regexes, JSON schema validators, and parsed date formatters outside hot loops.

### 3. Frontend & Rendering Performance
- **React Re-renders:** Memoize expensive calculations with `useMemo`; stabilize callback references with `useCallback` when passed to memoized children.
- **Virtualization:** Virtualize long lists (> 100 items) using windowing libraries instead of rendering 5,000 DOM nodes.
- **Dynamic Imports:** Code-split heavy dependencies (charts, rich-text editors, syntax highlighters) using dynamic `import()`.
