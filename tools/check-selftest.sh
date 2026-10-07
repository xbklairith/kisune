#!/usr/bin/env bash
# Proves every check in check.py can fail. A guard that cannot fail is
# decoration. Seeds one fault at a time, asserts check.py rejects it naming
# the right check, then restores the file byte-for-byte.
set -u
cd "$(dirname "$0")/.."
pass=0; fail=0

try() { # try <check-name> <file> <sed-expr>
  local want="$1" file="$2" expr="$3" tmp
  tmp=$(mktemp); cp "$file" "$tmp"
  sed -i '' "$expr" "$file" 2>/dev/null || sed -i "$expr" "$file"
  if out=$(python3 tools/check.py 2>&1); then
    echo "  NOT PROVEN [$want]: seeded fault in $file but check.py passed"; fail=$((fail+1))
  elif printf '%s' "$out" | grep -q "\[$want\]"; then
    echo "  ok [$want] fails as designed"; pass=$((pass+1))
  else
    echo "  WRONG CHECK [$want]: failed, but not via [$want]:"; printf '%s\n' "$out" | sed 's/^/      /'; fail=$((fail+1))
  fi
  cp "$tmp" "$file"; rm -f "$tmp"
}

trysh() { # trysh <check-name> <file> <shell-mutation>; <file> may not exist yet
  local want="$1" file="$2" cmd="$3" tmp="" existed=1
  if [ -e "$file" ]; then tmp=$(mktemp); cp "$file" "$tmp"; else existed=0; fi
  eval "$cmd"
  if out=$(python3 tools/check.py 2>&1); then
    echo "  NOT PROVEN [$want]: seeded fault in $file but check.py passed"; fail=$((fail+1))
  elif printf '%s' "$out" | grep -q "\[$want\]"; then
    echo "  ok [$want] fails as designed"; pass=$((pass+1))
  else
    echo "  WRONG CHECK [$want]: failed, but not via [$want]:"; printf '%s\n' "$out" | sed 's/^/      /'; fail=$((fail+1))
  fi
  if [ "$existed" = 1 ]; then cp "$tmp" "$file"; rm -f "$tmp"; else rm -f "$file"; fi
}

echo "proving each check can fail:"
# Seeds are pattern-based on purpose: a seed that hardcodes today's version or
# count silently stops seeding anything the next time either changes, and the
# selftest then reports a check as unprovable rather than as broken.
try versions   .claude-plugin/marketplace.json            's/"version": "[0-9][0-9.]*"/"version": "9.9.9"/'
try counts     CLAUDE.md                                  's/### Dev-Workflow Plugin ([0-9][0-9]* skills/### Dev-Workflow Plugin (999 skills/'
try index      dev-workflow/skills/using-kisune/SKILL.md   's/^| `review` |/| `no-such-skill` |/'
try references dev-workflow/skills/post-mortem/SKILL.md    's/They are the index\./They are the index. See `explain-in`./'
# Skill-authoring rules from Anthropic's skill best-practices guide.
SK=dev-workflow/skills/review/SKILL.md
try name        $SK 's/^name: review$/name: Review_Skill/'
try description $SK 's/^description: /description: <b>x<\/b> /'
trysh description $SK "sed -i '' 's/^description: /description: $(printf 'x%.0s' $(seq 1030)) /' $SK"
try when        $SK '/^description:/s/\. Use .*$/./'
trysh length    $SK "seq 520 >> $SK"
trysh toc       dev-workflow/skills/more-creativity/references/long.md "seq 120 > dev-workflow/skills/more-creativity/references/long.md"
trysh links     $SK "printf '\\n[x](references/a/b.md)\\n' >> $SK"
trysh links     $SK "printf '\\n[x](references\\\\x.md)\\n' >> $SK"

echo
if ! python3 tools/check.py >/dev/null 2>&1; then
  echo "RESTORE FAILED — tree is dirty, run: git diff"; exit 1
fi
echo "tree restored clean; $pass proven, $fail not proven"
[ "$fail" -eq 0 ]
