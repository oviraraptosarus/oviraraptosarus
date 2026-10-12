#!/usr/bin/env python3
"""SessionStart hook: print the handoff files so a new session picks up where the last one stopped."""
import json, os, subprocess, sys

root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def read(name, limit=6000):
    try:
        with open(os.path.join(root, name), encoding="utf-8") as f:
            return f.read()[:limit]
    except OSError:
        return f"(missing: {name})"


def git(*args):
    try:
        return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


parts = [
    "RESUME THIS PROJECT. Read these before replying, then continue from 'Next' in CONTEXT.md. Do not ask the owner to re-explain.",
    "=== OWNER-RULES.md ===\n" + read("OWNER-RULES.md"),
    "=== CONTEXT.md ===\n" + read("CONTEXT.md"),
    "=== NEEDS-FROM-OWNER.md (remind the owner of open items) ===\n" + read("NEEDS-FROM-OWNER.md", 3000),
    "=== VIDEO STYLES (short form default = Style 1; full rules in edits/duxio-reel-kit/styles/style-1/STYLE.md, templates via kit/new_reel.py, batch process in edits/duxio-reel-kit/BATCH.md) ===\n" + read("edits/duxio-reel-kit/styles/README.md", 2500),
    "=== git ===\n" + git("status", "-sb") + "\n" + git("log", "--oneline", "-5"),
]
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n\n".join(parts)}}))
