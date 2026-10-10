---
name: make-video
description: One entry point for making any video in this repo. Use when the user says "/make-video", "make a video", "make a reel", "launch video", "brag about this", "promo", "explainer", or "motion graphic". Picks between /brag (a launch video of the current project) and story-motion + HyperFrames (any other custom video), maps plain-language asks to the right flags, checks the plugins are present, and reports where the output lands.
---

# /make-video

Turn the user's ask into the right video pipeline. Don't interview the user; infer, then go.

## 1. Pick the pipeline

| The ask is about… | Use |
|---|---|
| **the current project/app/repo itself** ("brag about this", "launch video for what I built", "show off this app") | `/brag` (§2) |
| **anything else**: a topic, a product story, a reel, an ad, an explainer, a motion piece, "show what you can do" | `story-motion` + `/hyperframes` (§3) |
| Unclear | If the repo contains an app or website, use `/brag`; otherwise use story-motion. |

## 2. /brag route

Translate the user's words into flags, then invoke the `brag` skill (plugin `brag@brag`) with them:

| User says | Flag |
|---|---|
| voice, narration, voiceover, "talk over it" | `--voice` |
| reel, TikTok, Shorts, story, vertical, phone | `--format vertical` |
| square, Instagram post | `--format square` |
| N seconds | `--duration N` |
| chaotic / polished / deadpan / cinematic / App Store / YC parody, or any vibe ("fake Series A launch") | `--tone <that>` |
| a product name | `--title "<name>"` |
| no music / no sound effects | `--no-music` / `--no-sfx` |

- **Default to `--voice`** unless the user says silent. On Opus 5.5, plain `/brag` switches to brag-slim, which has no voiceover; `--voice` keeps the full workflow.
- Output goes to `brag-output/brag.mp4` (or `brag-output-<timestamp>/`), plus `brag.jpg` and share copy. Send the mp4 to the user when done.

## 3. story-motion route

Load `.claude/skills/story-motion/SKILL.md` and follow it end to end, with HyperFrames as the framework:

- concept → script → beat sheet → build → `npx hyperframes check` → snapshot review → render
- companion skills per its section 0 table
- audio: voiceover, plus brag's bundled music and SFX first, plus the synth kit as fallback
- format: vertical 1080×1920 for reels/TikTok/Shorts, otherwise 1920×1080

## 4. Preflight (both routes)

1. **Plugins.** Run `claude plugin list`. Both `brag@brag` and `hyperframes@hyperframes` must be enabled. If either is missing:
   ```bash
   claude plugin marketplace add latent-spaces/brag --scope project && claude plugin install brag@brag --scope project
   claude plugin marketplace add heygen-com/hyperframes --scope project && claude plugin install hyperframes@hyperframes --scope project
   ```
   Plugin skills load at session start. If you just installed them, read the skill file straight from `~/.claude/plugins/cache/<plugin>/<plugin>/<version>/skills/<skill>/SKILL.md` and follow it, rather than asking the user to restart.
2. **Tools.** Check `node -v` (22+), `ffmpeg -version` and `npx hyperframes doctor`. For `--voice`, run `pip install kokoro-onnx soundfile` if `hyperframes tts` complains.
3. **Cloud sandbox.** jsDelivr is blocked, so vendor `gsap.min.js` locally (see story-motion §6).

## 5. Deliver

- Send the mp4 with `SendUserFile` (`display: render`).
- Give one line on what was made: route, length, format, voice on or off.
- If the work lives in a git repo, commit the source (not `node_modules` or render caches) and push to the session's branch.
