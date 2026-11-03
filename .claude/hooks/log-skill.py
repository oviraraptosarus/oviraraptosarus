#!/usr/bin/env python3
"""PostToolUse hook for the Skill tool: appends 'time<TAB>session<TAB>skill' to .claude/skills-used.log."""
import json, os, sys, time
try:
    d = json.load(sys.stdin)
    name = (d.get("tool_input") or {}).get("skill")
    if name:
        root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
        open(os.path.join(root, ".claude", "skills-used.log"), "a").write(f"{int(time.time())}\t{d.get('session_id','')}\t{name}\n")
except Exception:
    pass
