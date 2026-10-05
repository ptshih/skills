---
name: ast-grep
description: "Perform syntax-aware AST search, code outlining, and structural refactoring using ast-grep. Use when exploring code structures, functions, classes, imports, or searching complex syntax patterns."
license: MIT
metadata:
  version: "1.0.0"
---

# AST-Grep: Structural Code Search & Outline

Use `ast-grep` for syntax-aware code exploration instead of dumping large files or parsing noisy regex grep output.

## High-Leverage Commands

### 1. Symbol Outlining
Inspect all functions, classes, interfaces, and methods in a file without loading the entire source:
```bash
ast-grep outline path/to/file.ts
```

### 2. Pattern Matching
Search for exact syntactic constructs using `$VAR` (single node) and `$$$VAR` (zero or more nodes):
```bash
# Find all function declarations
ast-grep run -p 'function $NAME($$$ARGS) { $$$BODY }' <dir>

# Find all route handlers
ast-grep run -p 'router.$METHOD($PATH, $$$HANDLERS)' <dir>

# Find React hooks
ast-grep run -p 'useEffect($$$ARGS)' <dir>
```

### 3. Structural Replacement
Rewrite code safely preserving indentation and formatting:
```bash
ast-grep run -p 'oldFunc($$$ARGS)' -r 'newFunc($$$ARGS)' --update-all
```
