#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [[ -f scripts/check_dependencies.py ]]; then
    /usr/bin/python3 scripts/check_dependencies.py
fi

exec /usr/bin/python3 app.py "$@"
