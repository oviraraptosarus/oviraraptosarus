# Move this workspace to your own machine

The workspace is this git repo. Everything (skills, hooks, brand kit, reel kit, voice and music tools) is in it.

1. Install: git, Node 22, Python 3.11+, ffmpeg (with rubberband), then `pip install kokoro-onnx soundfile numpy scipy librosa pyworld`.
0. Run `sh bootstrap-local.sh` after cloning (checks and installs the tools).
2. `git clone https://github.com/oviraraptosarus/oviraraptosarus.git && cd oviraraptosarus && git checkout claude/blissful-hawking-xxcdii`
3. Open the folder in Claude Code. `.claude/settings.json` registers the hooks and plugins automatically.
4. Kokoro voice files: the voice tool expects them at `~/.cache/hyperframes/tts/` (running `npx hyperframes tts` once downloads them).
5. Optional: `.claude/install-sync-schedule.sh` keeps `~/.claude/skills` and the repo in sync daily.
6. Your uploaded videos and large audio are not in git. Put them in `input/`.
