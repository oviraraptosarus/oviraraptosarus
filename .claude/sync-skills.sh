#!/bin/sh
# Run on your LOCAL machine from the repo root. Makes the repo the single source of truth for skills.
# 1) copies skills that exist only in ~/.claude/skills into .claude/skills (never overwrites repo versions)
# 2) lists skills that exist in both places but differ, so you pick one
# Then: git add .claude/skills && git commit && git push
L="$HOME/.claude/skills"; R=".claude/skills"
[ -d "$L" ] || { echo "no $L"; exit 1; }
for d in "$L"/*/; do n=$(basename "$d")
  if [ ! -d "$R/$n" ]; then cp -r "$d" "$R/$n"; echo "added   $n"
  elif ! diff -rq "$d" "$R/$n" >/dev/null 2>&1; then echo "DIFFERS $n  (diff -r $d $R/$n)"
  fi
done
