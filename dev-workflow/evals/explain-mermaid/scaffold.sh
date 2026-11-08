#!/usr/bin/env bash
# Seed the agent's working directory with this case's fixture directories.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
for d in "$here"/*/; do
  case "$(basename "$d")" in graders) continue ;; esac
  cp -R "$d" "./$(basename "$d")"
done
