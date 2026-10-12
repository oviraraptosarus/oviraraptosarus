---
name: long-form-video
description: "Long form video pipeline (YouTube videos, tutorials, explainers, talking-head or screen footage, faceless YouTube automation, anything over 60 seconds). Use for 'long form', 'YouTube video', 'raw footage', 'edit my recording', 'cut the dead air', 'tutorial', 'YouTube automation', 'chapters', 'B-roll proof'. Runs free local tools: faster-whisper transcript and cut list, creator measurement and taste rules via the NextWork plugins, Hyperframes motion graphics, real screenshot B-roll, music and SFX, FFmpeg finish. Loads after make-video's question round and obeys OWNER-RULES.md."
---

# Long form video (free local stack)

Sits on top of `make-video`. Its question round, `OWNER-RULES.md` and the quality bar still apply: ask the kid-style question round in one plain message first, show open items from `NEEDS-FROM-OWNER.md`, no popups, no renders before the concept is approved. Also load `make-video/framework.md` and `visual-breakdown.md` for hooks, spines and the look. No AI generated images or video.

## Tool chain (all free)
| Job | Tool | Status here |
|---|---|---|
| Orchestrator | Claude Code | running |
| Transcribe, word timestamps | `faster-whisper` (use `py -3.12`; decode audio to 16 kHz wav with ffmpeg first, then pass samples, because the `av` decoder crashes) | installed |
| Measure a creator, build a style | NextWork `creator-teardown` plugin | installed (user scope) |
| Cut raw talking-head footage, style it, remember corrections | NextWork `ai-editor` plugin: `setup`, `start`, `cut`, `style-edit`, `taste`, `motion-design`, `clips`, `improve` | installed, **not set up or tested**. Run its `setup` skill once; it renders captions and cards with Remotion |
| Motion graphics, titles, stat cards | Hyperframes (`npx hyperframes`) and our reel kit | installed |
| Real screenshot and scroll B-roll as proof | Playwright MCP or Chrome, saving real pages (a real tweet, doc or repo page, never a mock) | available, untested here |
| Music and SFX | `brand/duxio/music/library/`, `brand/duxio/sfx/`, then `music-director`. Pixabay audio is allowed if the licence is recorded. **StreamBeats licence for monetised YouTube is unverified; check before use** | |
| Finish | FFmpeg: cut, loudness, black frame check, final render | installed |
| Screen recorder with auto zoom (and webcam, for face content) | OpenScreen v1.5.0 (MIT, siddharthvaddem/openscreen), installed at `%LOCALAPPDATA%\Programs\Openscreen\Openscreen.exe` (SHA-256 checked; the silent installer crashed, the normal installer worked) | installed, not opened or tested |

## Which route
- **Owner supplies talking-head, face or screen footage (face content works too):** `ai-editor` (`start` → `cut` → `style-edit`), with `taste` saving every correction. Our additions: Hyperframes overlays instead of Remotion where the look matters, our loudness master, our framework hooks.
- **Faceless or generated YouTube (the common case for the owner):** no footage to cut. Script (copy skills) → voice (`voiceover-pacing`) → scenes in Hyperframes with real screenshot and licensed imagery → chapters → music and SFX → FFmpeg. Same framework, longer.
- **Copy a creator's pacing:** run `creator-teardown` on their videos, save the numbers as a style, feed `style-edit` or our beat sheet.

## Pipeline (each step is short; skip nothing that changes a decision, skip everything that doesn't)
1. **Brief and concept card** (question round, one plain message). Long form adds: the viewer's starting belief, the end action, chapters or one flow, voice pace, whether a cutdown is wanted.
2. **Cut list from transcript** (footage jobs): word timestamps, remove pauses over about 1.0s, false starts, repeated takes (keep the last clean one). Write `cuts.json`; never overwrite the raw file.
3. **Structure:** hook in the first 5s, a chapter title every 1 to 3 minutes, a visual change at least every 3 to 5s (a state change counts, not only a cut), a pattern interrupt about every 30 to 45s. Framework hook shapes and spines apply.
4. **Proof B-roll:** for every factual claim, a real capture of the real source. Highlight the line, then zoom. Record the URL and date next to the clip.
5. **Motion graphics:** Hyperframes titles, stat cards, lower thirds from the brand `DESIGN.md`. `npx hyperframes check` before rendering.
6. **Sound:** music about 18 to 24 dB under speech, SFX at least 7 to 8 dB under the voice, a sound on every visual event, one silence beat.
7. **Finish:** FFmpeg assemble and normalise to about -16 LUFS for YouTube (-14 for shorts cutdowns), true peak -1 dBTP or lower. Check duration, black frames and A/V sync.
8. **Deliver:** the mp4, the transcript, chapter timestamps, and one line on anything the owner must confirm. Then save every note the owner gives as a numbered rule (`OWNER-RULES.md` §3c or the `ai-editor` `taste` file).

## Known bad commands (from pasted guides, do not use)
- `npm install -g @heygen/hyperframes-cli`: the package doesn't exist. Use `npx hyperframes`.
- `npx playwright screen capture`: not a real command.
- `github.com/nextwork/ai-video-editor`: 404. The real repo is `nextwork-projects/ai-video-editor`.
- "GitHub Actions secret mission": invented. Rendering is local.
