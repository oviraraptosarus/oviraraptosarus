#!/bin/sh
# Run once on your LOCAL machine (Mac/Linux). Schedules sync-daily.sh every day at 09:00 via cron.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LINE="0 9 * * * /bin/sh $REPO/.claude/sync-daily.sh $REPO >> $HOME/.claude/skill-sync.log 2>&1"
( crontab -l 2>/dev/null | grep -v sync-daily.sh; echo "$LINE" ) | crontab -
echo "scheduled: $LINE"; /bin/sh "$REPO/.claude/sync-daily.sh" "$REPO"
