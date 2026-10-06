#!/bin/bash
# Behavioural checks for dev-workflow/skills/wizard/assets/template.sh, run under the system bash
# (3.2 on macOS) because that is what a user's `bash script.sh` gets.
set -u
TEMPLATE="${1:-$(dirname "$0")/../dev-workflow/skills/wizard/assets/template.sh}"
pass=0; fail=0
ok()  { pass=$((pass+1)); printf '  ok   %s\n' "$1"; }
bad() { fail=$((fail+1)); printf '  FAIL %s\n' "$1"; }

# Library = everything above the STAGES marker; stages are supplied per case.
lib=$(sed -n '1,/^# STAGES:/p' "$TEMPLATE")

run() { # run <dir> <stages-body> <stdin>
  local dir="$1"; printf '%s\n%s\n' "$lib" "$2" > "$dir/w.sh"
  (cd "$dir" && printf '%b' "$3" | /bin/bash w.sh 2>&1)
}
repo() { local d; d=$(mktemp -d); (cd "$d" && git init -q); printf '%s' "$d"; }

STAGES='TOTAL_STAGES=1
banner "Demo"
stage "Keys"
ask PUB "Publishable key:"
ask_secret SEC "Secret key:"
write_env PUB "$PUB"
write_env SEC "$SEC"
finish'

echo "template: $TEMPLATE"

# 1. values land in an ignored .env, once each
d=$(repo); printf '.env\n' > "$d/.gitignore"
out=$(run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\n')
grep -qx 'PUB=pk_test_dummy' "$d/.env" && grep -qx 'SEC=sk_test_dummy' "$d/.env" \
  && ok "writes both values to an ignored .env" || bad "writes both values to an ignored .env"

# 2. the secret value never reaches the terminal
printf '%s' "$out" | grep -q 'SUPERSECRET' \
  && bad "secret value echoed to terminal" || ok "secret value never echoed"

# 3. re-run with Enter keeps values and does not duplicate lines
run "$d" "$STAGES" '\n\n\n' >/dev/null
[ "$(grep -c '^SEC=' "$d/.env")" = 1 ] && grep -qx 'SEC=sk_test_dummy' "$d/.env" \
  && ok "re-run keeps value, no duplicate line" || bad "re-run keeps value, no duplicate line"

# 4. .env NOT ignored: declining the guard writes nothing and says so
d=$(repo)
out=$(run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\nn\n')
if [ ! -s "$d/.env" ] && printf '%s' "$out" | grep -qi 'not ignored by git'; then
  ok "refuses unignored .env when declined"; else bad "refuses unignored .env when declined"; fi

# 4b. .env NOT ignored: accepting the guard writes, and asks only once
d=$(repo)
out=$(run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\ny\n')
if grep -qx 'SEC=sk_test_dummy' "$d/.env" && [ "$(printf '%s' "$out" | grep -c 'anyway?')" = 1 ]; then
  ok "writes unignored .env when confirmed, one prompt"; else bad "writes unignored .env when confirmed, one prompt"; fi

# 5. nothing written at all: finish must not crash under set -u on bash 3.2
d=$(repo)
out=$(run "$d" 'TOTAL_STAGES=1
banner "Empty"
stage "Nothing"
say "no values"
finish' '\n'); rc=$?
[ $rc = 0 ] && ok "empty run exits 0 on system bash" || bad "empty run exits 0 on system bash (rc=$rc: $(printf '%s' "$out" | tail -1))"

echo "$pass passed, $fail failed"; [ $fail = 0 ]
