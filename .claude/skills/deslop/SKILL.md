---
name: deslop
description: Scan the current branch's git diff for AI-generated code patterns (debug logs, obvious comments, needless try-catch, etc.) and remove them. Use when asked to deslop, clean up AI code, or check the slop score.
---

Install if missing: `command -v deslop || (git clone --depth 1 https://github.com/dabit3/deslop /tmp/deslop && npm install -g /tmp/deslop)`

1. Run `deslop -v -b <base>` (base defaults to `main`) from the repo root.
2. Fix each flagged line in the diff: remove debug `console.log`s, obvious comments, empty/log-only catch blocks, redundant checks and wrappers. Don't touch lines outside the diff.
3. Re-run `deslop score` and report the before/after score.

Other commands: `deslop patterns` (list rules), `deslop -j` (JSON), `deslop -a` (scan all lines).
