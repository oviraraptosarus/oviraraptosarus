#!/bin/sh
# Two-way skill sync, run on your LOCAL machine (daily via install-sync-schedule.sh).
#   cloud -> local: git pull, then repo skills are copied into ~/.claude/skills (repo wins)
#   local -> cloud: skills only on your machine are copied into the repo, committed and pushed
# Usage: sync-daily.sh /path/to/repo
REPO="${1:-$(cd "$(dirname "$0")/.." && pwd)}"; BR="claude/blissful-hawking-xxcdii"
L="$HOME/.claude/skills"; R="$REPO/.claude/skills"; mkdir -p "$L"
cd "$REPO" || exit 1
git fetch -q origin "$BR" && git checkout -q "$BR" && git pull -q --no-edit origin "$BR"
for d in "$L"/*/; do n=$(basename "$d"); [ -d "$R/$n" ] || { cp -r "$d" "$R/$n"; echo "local->repo $n"; }; done
for d in "$R"/*/; do n=$(basename "$d"); rm -rf "$L/$n"; cp -r "$d" "$L/$n"; done   # repo version wins
git add .claude/skills
if ! git diff --cached --quiet; then git commit -qm "Daily skill sync from local machine" && git push -q origin "$BR"; fi
echo "synced $(date)"
