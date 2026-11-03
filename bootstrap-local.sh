#!/bin/sh
# One-time setup on your own machine (Mac or Linux). Run from the repo root: sh bootstrap-local.sh
set -e
need(){ command -v "$1" >/dev/null 2>&1 || { echo "MISSING: $1  ->  $2"; MISSING=1; }; }
need git "install git"; need node "install Node 22 (nodejs.org)"; need python3 "install Python 3.11+"; need ffmpeg "brew install ffmpeg / apt install ffmpeg"
[ -n "$MISSING" ] && exit 1
ffmpeg -hide_banner -filters 2>/dev/null | grep -q rubberband || echo "WARN: your ffmpeg has no rubberband filter (pitch nudge). Mac: brew install ffmpeg; Linux: apt install ffmpeg librubberband2"
python3 -m pip install --user kokoro-onnx soundfile numpy scipy librosa pyworld
npx -y hyperframes tts --help >/dev/null 2>&1 || true   # fetches the voice models into ~/.cache/hyperframes on first real use
echo "Done. Open this folder in Claude Code. Reel flow:"
echo "  python3 edits/duxio-reel-kit/kit/build.py edits/duxio-reel-kit/reels/<name>/reel.json"
echo "  cd edits/duxio-reel-kit/out/<name> && npx hyperframes check && npx hyperframes render"
