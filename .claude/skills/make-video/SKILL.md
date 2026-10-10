---
name: make-video
description: Single entry point for any content-creation job in this repo: reel, short, paid ad, promo, launch video, VSL, explainer, product demo, tutorial, testimonial, talking-head or podcast edit with B-roll, story, teaser, logo sting, lower thirds, or a launch video of the current project (/brag). Infers goal, format, length, source and tone; picks the right pipeline; builds, reviews against video-craft, renders, and delivers. Use for "make a video", "make an ad/promo/reel/VSL", "edit my footage", "turn this site into a video", "/make-video".
---

# /make-video: the whole content-creation journey

Don't interview. Infer, state your assumptions in one line, then build. Ask only if the subject or the source is missing.

## 1. Load the standard first
1. `video-craft`: the quality bar and the pre-render review. Always.
2. `video-formats`: pick the format; take its structure, length, specs and loudness target.
3. Then the pipeline below.

## 2. Pick the pipeline from what the user gives you

| Input | Pipeline |
|---|---|
| **Their own footage or audio** (talking head, screen recording, podcast, interview) and they want editing and B-roll | `footage-edit` |
| **A website, product page or funnel** to sell or explain | read the site(s) first (WebFetch/browser; if blocked, ask for pasted copy or screenshots), extract offer, funnel steps, proof, brand colours and fonts, then build with the format playbook (VSL, ad, promo, explainer, demo) |
| **The current project/repo itself**, "brag about this" | `/brag` (map "voice", "vertical", "N seconds", a tone, a title to its flags; default `--voice` on) |
| **A topic, script, article or idea with no source** | write the script (`copywriting`, `storyteller`, `marketing-psychology`, `video-content-strategist`), then build in HyperFrames |
| **A PR, music track, deck or Figma file** | the matching HyperFrames workflow (`pr-to-video`, `music-to-video`, `slideshow`, `figma`) |
| **Existing video to improve** | `video-craft` review first, list what is wrong at the principle level, fix it, re-review |

Style: choose from the message and tone (`motion-art-direction`). Character/metaphor storytelling lives in `story-motion`; typography-led, diagram-led and UI-led styles are equally valid and are usually right for sales, finance, B2B and VSLs.

## 3. Build
1. **Brief** (inferred, written to `BRIEF.md`): goal and action, audience, single message, tone, format and channel, length, sources, proof available, brand (colours, fonts, logo).
2. **Script** (VO, on-screen words, CTA) through the copy skills; every claim traceable to the source.
3. **Beat sheet**: time | what the viewer must understand | visual | VO | sound.
4. **Build** in HyperFrames (single paused GSAP timeline; `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`). Vendor GSAP locally in cloud sessions.
5. **Audio**: voiceover (`hyperframes tts`; `pip install kokoro-onnx soundfile` first), brag's bundled music and SFX, voice chain and carve (`hyperframes-audio`), loudness per `video-formats`.
6. **Review** against `video-craft` section 4 using snapshots at every beat. Fix, then render, then re-check the final file's duration, specs and loudness with `ffprobe` and `ebur128`.

## 4. Variants and versions
Always offer (and when it's cheap, produce) the platform versions the format implies: 16:9 master plus 9:16 and 4:5 recuts, hook variants for ads, a 15s cutdown for promos. Reframe by re-composing, not cropping.

## 5. Preflight
- `claude plugin list` shows `brag@brag` and `hyperframes@hyperframes` enabled. If missing, install them (`claude plugin marketplace add latent-spaces/brag` + `claude plugin install brag@brag --scope project`, and the same for `heygen-com/hyperframes`). Read newly installed skill files straight from `~/.claude/plugins/cache/...` instead of asking for a restart.
- `node -v` (22+), `ffmpeg`, `npx hyperframes doctor`.
- Cloud network limits: some hosts (CDNs, model hosts, user websites) may be blocked. Say which, and give the user the exact fix (allow the domain in the environment's network settings, or paste the content).

## 6. Generated media (AI B-roll, images, voices)
Only use a generation provider that is actually connected and signed in. Never fake or imply generated footage. If none is available, build the B-roll as designed motion graphics or use the user's own material, and say so in one line.

## 7. Deliver
Send the mp4 (`SendUserFile`, render), one line on what it is (format, length, voice), plus the script and any variants. Commit the source and render to the session's branch.
