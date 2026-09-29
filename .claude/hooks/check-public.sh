#!/usr/bin/env bash
# PreToolUse hook: public repo に出してはいけない内容が staged diff に無いか検査する。
# exit 2 で commit を止め、stderr の内容が Claude に返る。
set -euo pipefail

cmd=$(jq -r '.tool_input.command // ""')
# settings.json で if を付けないのは、`git add … && git commit` のような連結コマンドも拾うため
grep -Eq 'git[[:space:]]+commit' <<<"$cmd" || exit 0
cd "${CLAUDE_PROJECT_DIR:-.}"

# hook は add より先に走るので、同じコマンド内で add された分は検査から漏れる
if grep -Eq '(^|[;&|[:space:]])git[[:space:]]+add([[:space:]]|$)' <<<"$cmd" ||
   grep -Eq 'git[[:space:]]+commit([[:space:]].*)?[[:space:]](-a|--all|-[a-zA-Z]*a[a-zA-Z]*)([[:space:]]|$)' <<<"$cmd"; then
  echo "公開チェック: git add と git commit を別々のコマンドで実行してください (commit -a も不可)。staged diff を検査してから commit します。" >&2
  exit 2
fi

added=$(git diff --cached --no-color -U0 | grep -E '^\+' | grep -Ev '^\+\+\+ ' || true)
[ -z "$added" ] && exit 0

hits=""
secret_re='AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{36}|xox[abprs]-[A-Za-z0-9-]+|sk-[A-Za-z0-9_-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
hits+=$(grep -Eno "$secret_re" <<<"$added" || true)

denylist=.claude/public-check.local.txt
if [ -f "$denylist" ]; then
  terms=$(grep -Ev '^[[:space:]]*(#|$)' "$denylist" || true)
  if [ -n "$terms" ]; then
    hits+=$'\n'$(grep -Fnoi -f <(printf '%s\n' "$terms") <<<"$added" || true)
  fi
fi

hits=$(sed '/^$/d' <<<"$hits")
if [ -n "$hits" ]; then
  echo "公開チェック: staged diff に public repo に出せない可能性がある文字列があります。" >&2
  echo "$hits" | sort -u >&2
  echo "削除するか、問題ない場合はユーザーに確認してください。" >&2
  exit 2
fi
