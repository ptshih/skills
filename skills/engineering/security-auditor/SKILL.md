---
name: security-auditor
description: "Review security-sensitive changes to authentication, authorization, secrets, trust boundaries or untrusted input, and explicit security audit requests. Check the affected code for injection, traversal, SSRF, access-control flaws and related vulnerabilities."
license: MIT
metadata:
  version: "1.0.0"
---

# Security-Auditor: Zero-Trust Code & Vulnerability Review

Review the security-relevant parts of the requested change. Apply the checklist to affected
trust boundaries and report concrete findings with file and line references. Preserve unrelated
work and any project-required security checks.

## Vulnerability Checklist

### 1. Injection Attacks
- **SQL Injection:** Queries must use parameterized placeholders or ORM query builders. Never concatenate user strings into raw SQL (`"SELECT * FROM users WHERE id = '" + id + "'"`).
- **Command Injection:** Never pass un-sanitized user input into `child_process.exec()`, `spawn("sh", ["-c", cmd])`, or `os.system()`.
- **Path Traversal:** Resolve the target with `fs.realpath()` (which follows symlinks), then require `path.relative(root, target)` to be neither absolute nor starting with `..`. A bare `target.startsWith(root)` is not enough: it accepts `/srv/app-evil` for root `/srv/app`.

### 2. Web & Client Vulnerabilities
- **Cross-Site Scripting (XSS):** Never use `dangerouslySetInnerHTML` or `innerHTML` with user-supplied content without sanitization via DOMPurify.
- **Server-Side Request Forgery (SSRF):** When fetching URLs provided by users, validate against a strict domain allowlist. Resolve the host and block private, loopback and link-local addresses (`127.0.0.0/8`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `169.254.0.0/16`, `::1`, `fc00::/7`, `fe80::/10`), checking the address actually connected to so DNS rebinding cannot swap it after validation. Do not follow redirects without re-checking.
- **Open Redirects:** Disallow redirecting to arbitrary user-supplied URLs without domain verification.

### 3. Authentication & Authorization
- **Insecure Direct Object Reference (IDOR):** Every query fetching or mutating a resource must scope by the authenticated `userId` / `orgId`, not just the resource `id`.
- **Timing Attacks:** Use constant-time comparison (`crypto.timingSafeEqual`) when validating API keys, HMAC signatures, or password hashes.

### 4. ReDoS (Regular Expression Denial of Service)
- Avoid nested quantifiers on user-supplied input: `(a+)+$`, `([a-zA-Z]+)*$`.
- Use linear-time regex engines or length bounds before regex evaluation.
