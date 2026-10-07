#!/usr/bin/env bash
# Seed the working directory with the textkit fixture as a fresh git repo.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cp -R "$here/textkit" ./textkit
cd textkit
git init -q
git -c user.name=dev -c user.email=dev@example.com add -A
git -c user.name=dev -c user.email=dev@example.com commit -qm "Initial textkit"
git config user.name dev && git config user.email dev@example.com
