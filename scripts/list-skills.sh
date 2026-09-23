#!/usr/bin/env bash
set -euo pipefail

# Prints every SKILL.md in the repository, one path per line.
REPO="$(cd "$(dirname "$0")/.." && pwd)"

cd "$REPO"
find . -name SKILL.md -not -path '*/node_modules/*' | sed 's|^\./||' | sort
