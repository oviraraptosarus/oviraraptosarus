# DUXIO reel kit

A config in, a renderable HyperFrames project out. You describe a reel as data; the kit does voice, music, SFX, captions and scenes.

1. Write `reels/<name>/voice.vo.json` (performance script, see `voiceover-pacing`) and `reels/<name>/reel.json` (beats). `reels/_example-e2-draft/` shows the format. Nothing here has been built or rendered.
2. `python3 kit/build.py reels/<name>/reel.json` renders the voice, mixes the music, resolves SFX and writes `out/<name>/`.
3. `npx hyperframes check`, `snapshot`, `render` inside `out/<name>/`. Review real frames before sending.

Scenes (`kit/scenes.js`): statement, stack, clock, msg, phone, wall, stamp, dots, chain, tier, compare, cta, plus the caption engine. Cues are phrase relative, so a new voice retimes the reel. SFX names live in `kit/sfx-map.json`. Add a scene by adding one function to `scenes.js`.
