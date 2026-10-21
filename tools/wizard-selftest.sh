#!/bin/bash
# Behavioural checks for dev-workflow/skills/wizard/assets/template.sh, run under the system bash
# (3.2 on macOS) because that is what a user's `bash script.sh` gets.
set -u
# A pre-commit hook exports GIT_DIR (and friends); left set, the temp repos' `git init`
# would write to the real repo's config (e.g. core.bare=true).
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_PREFIX GIT_OBJECT_DIRECTORY
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
ignored() { local d; d=$(repo); printf '.env\n' > "$d/.gitignore"; printf '%s' "$d"; }
mode() { stat -f %Lp "$1" 2>/dev/null || stat -c %a "$1"; }
sourced() { (cd "$1" && /bin/bash -c 'set -a; . ./.env; printf %s "$'"$2"'"'); } # sourced <dir> <KEY>

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
grep -qx "PUB='pk_test_dummy'" "$d/.env" && grep -qx "SEC='sk_test_dummy'" "$d/.env" \
  && ok "writes both values, single-quoted, to an ignored .env" || bad "writes both values, single-quoted, to an ignored .env"

# 2. the secret value never reaches the terminal
printf '%s' "$out" | grep -q 'sk_test_dummy' \
  && bad "secret value echoed to terminal" || ok "secret value never echoed"

# 3. re-run with Enter keeps values and does not duplicate lines
run "$d" "$STAGES" '\n\n\n' >/dev/null
[ "$(grep -c '^SEC=' "$d/.env")" = 1 ] && grep -qx "SEC='sk_test_dummy'" "$d/.env" \
  && ok "re-run keeps value, no duplicate line" || bad "re-run keeps value, no duplicate line"

# 4. .env NOT ignored: declining the guard writes nothing and says so
d=$(repo)
out=$(run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\nn\n')
if [ ! -s "$d/.env" ] && printf '%s' "$out" | grep -qi 'not ignored by git'; then
  ok "refuses unignored .env when declined"; else bad "refuses unignored .env when declined"; fi

# 4b. .env NOT ignored: accepting the guard writes, and asks only once
d=$(repo)
out=$(run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\ny\n')
if grep -qx "SEC='sk_test_dummy'" "$d/.env" && [ "$(printf '%s' "$out" | grep -c 'anyway?')" = 1 ]; then
  ok "writes unignored .env when confirmed, one prompt"; else bad "writes unignored .env when confirmed, one prompt"; fi

# 5. nothing written at all: finish must not crash under set -u on bash 3.2
d=$(repo)
out=$(run "$d" 'TOTAL_STAGES=1
banner "Empty"
stage "Nothing"
say "no values"
finish' '\n'); rc=$?
[ $rc = 0 ] && ok "empty run exits 0 on system bash" || bad "empty run exits 0 on system bash (rc=$rc: $(printf '%s' "$out" | tail -1))"

# 6. a value with a quote, spaces, # and $ sources back unchanged, and a re-run
#    that keeps it (Enter) still does: bash 3.2 must not turn it's into it\'s
VAL='it'"'"'s a #$x "q"'
d=$(ignored)
run "$d" "$STAGES" "\n$VAL\nsk_test_dummy\n" >/dev/null
[ "$(sourced "$d" PUB)" = "$VAL" ] && ok "awkward value sources back unchanged" || bad "awkward value sources back unchanged (got: $(sourced "$d" PUB))"
run "$d" "$STAGES" '\n\n\n' >/dev/null
[ "$(sourced "$d" PUB)" = "$VAL" ] && ok "awkward value survives a re-run" || bad "awkward value survives a re-run (got: $(sourced "$d" PUB))"

# 7. a new .env is created owner-only; an existing one keeps its mode
d=$(ignored)
run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\n' >/dev/null
[ "$(mode "$d/.env")" = 600 ] && ok "new .env is 0600" || bad "new .env is 0600 (got $(mode "$d/.env"))"
d=$(ignored); printf 'OTHER=1\n' > "$d/.env"; chmod 640 "$d/.env"
run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\n' >/dev/null
[ "$(mode "$d/.env")" = 640 ] && ok "existing .env keeps mode 0640" || bad "existing .env keeps mode 0640 (got $(mode "$d/.env"))"

# 8. a symlinked .env stays a symlink, and the value lands in its target
d=$(ignored); : > "$d/real.env"; ln -s real.env "$d/.env"
run "$d" "$STAGES" '\npk_test_dummy\nsk_test_dummy\n' >/dev/null
if [ -L "$d/.env" ] && grep -qx "SEC='sk_test_dummy'" "$d/real.env"; then
  ok "symlinked .env stays a symlink"; else bad "symlinked .env stays a symlink"; fi

# 9. EOF at a prompt stops the wizard instead of saving an empty value
d=$(ignored)
run "$d" "$STAGES" '\n' >/dev/null; rc=$?
if [ $rc != 0 ] && ! grep -q '^PUB=' "$d/.env" 2>/dev/null; then
  ok "EOF at a prompt stops the wizard"; else bad "EOF at a prompt stops the wizard (rc=$rc)"; fi

# 10. no browser opener: the human is told to open the URL by hand
d=$(ignored)
out=$(run "$d" 'command() { return 1; }
open_url "https://example.test/keys"' '')
printf '%s' "$out" | grep -q "couldn't open a browser" \
  && ok "warns when no browser opener exists" || bad "warns when no browser opener exists"

# 11. write_env also sets $KEY for later stages
d=$(ignored)
out=$(run "$d" 'write_env K "v1"
say "K is $K"' '')
printf '%s' "$out" | grep -q 'K is v1' && ok "write_env sets \$KEY" || bad "write_env sets \$KEY"

# 12. a plain dotenv double-quoted value is offered back without its quotes
d=$(ignored); printf 'PUB="hello world"\n' > "$d/.env"
run "$d" "$STAGES" '\n\nsk_test_dummy\n' >/dev/null
grep -qx "PUB='hello world'" "$d/.env" && ok "re-reads a double-quoted dotenv value" || bad "re-reads a double-quoted dotenv value (got: $(grep '^PUB=' "$d/.env"))"

# 13. the shipped template is parsed whole before the first prompt: a line
#     appended to the file mid-run never executes
d=$(ignored)
INJECT='command() { return 1; }; printf "echo INJECTED\n" >> "$0"'
while IFS= read -r l; do printf '%s\n' "$l"; [ "$l" = 'banner "Stripe setup"' ] && printf '%s\n' "$INJECT"; done < "$TEMPLATE" > "$d/w.sh"
out=$(cd "$d" && printf '\npk_test_dummy\nsk_test_dummy\n' | /bin/bash w.sh 2>&1); rc=$?
if [ $rc = 0 ] && ! printf '%s' "$out" | grep -q INJECTED; then
  ok "edits made mid-run never execute"; else bad "edits made mid-run never execute (rc=$rc)"; fi

echo "$pass passed, $fail failed"; [ $fail = 0 ]
