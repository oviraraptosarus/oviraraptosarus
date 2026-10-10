---
name: make-video
description: "The one command for any video job: VSL, reel, short, TikTok, paid ad, promo, launch video, explainer, demo, tutorial, testimonial, footage edit with B-roll, podcast clip, logo sting, motion graphic. It asks the questions the request left out (type, platform and length, style, voice, CTA) in one quick round, auto-selects and loads the right specialist skills for that type of video (no slash commands needed), then scripts, builds, sound-designs, reviews and renders to a senior editor's standard. Use for 'make a video/reel/ad/VSL', 'edit my footage', 'turn this into a video', '/make-video'."
---

# /make-video: one command, the right skills, no AI slop

The user never has to type other skill names. This skill picks and loads them, asks once for what's missing, and holds the work to `editing-standard.md`.

## Step 1. Intake: ask what's missing, once

1. Read the request, the conversation, attachments and the repo. Fill this brief:

| Field | Examples | Required? |
|---|---|---|
| Type | VSL, reel, ad, promo, explainer, demo, footage edit, logo sting | yes |
| Platform, aspect, length | IG reel 9:16 ≤60s; YouTube/site 16:9; feed ad 4:5 | yes |
| Visual style | see the style list below | yes |
| Voice | uploaded ElevenLabs/mic file; built-in male/female TTS; none (music + captions) | yes |
| CTA | the exact words and the action ("Book a Strategy Call", "link in bio") | yes |
| Brand | logo, colours, fonts, a brand skill (DUXIO → `duxio-brand` + `duxio-vsl`) | infer |
| Script source | user script, a site to read, or write it | infer |
| Music mood | calm premium, upbeat, cinematic, none | default by type |
| Proof | real results or testimonials (never invented) | infer; assume none |
| Reference | a video they like | optional |

2. Anything already answered by the message, the conversation or a brand skill counts as answered. **Don't re-ask it.**
3. For every **required** field still unknown, ask with **one** `AskUserQuestion` call (up to 4 questions; 2 to 4 options each; put the recommended option first, marked "(Recommended)"; use `preview` to show what a style looks like). If more than 4 are missing, ask the 4 that change the build most and default the rest.
4. Skip the questions entirely when the user says "you decide", "just do it", "no questions", or the brand skill fixes everything. Then pick sensible defaults and state them in one line.
5. Write the brief to `BRIEF.md` in the build directory. No further check-ins on routine choices: build.

**Style options to offer** (pick the 3 or 4 that fit the type):
- **Editorial light (Apple-like):** white canvas, near-black type, one accent, big type with generous spacing. Best for VSLs, B2B, premium.
- **UI and diagram-led:** real-looking app screens, notifications, flows drawn on. Best for SaaS, services, demos.
- **Kinetic typography:** word-driven, beat-cut, bold. Best for reels and hooks.
- **Cinematic dark:** deep backgrounds, light type, one accent glow. Best for launches and drama.
- **Character and metaphor (`story-motion`):** a lovable object tells the story. Best for explainers and playful brands.
- **Footage-led:** the user's clips with B-roll, captions and lower thirds.

## Step 2. Auto-select the skills

Load these with the Skill tool (or read their `SKILL.md`) before planning. Always load: `video-craft`, `video-formats`, this skill's `editing-standard.md`, and `hyperframes` + `hyperframes-core` + `hyperframes-animation` + `hyperframes-audio` for any HyperFrames build.

| Video type | Also load |
|---|---|
| VSL / sales video | `copywriting`, `marketing-psychology`, `storyteller`, `copy-editing`, `motion-art-direction`, `shot-composition`, `animation-principles`, `caption-animation`, `beat-sync-editing` |
| Reel / short / TikTok | `short-form-video`, `video-content-strategist`, `storyteller`, `copywriting`, `caption-animation`, `beat-sync-editing`, `motion-design`, `shot-composition` |
| Paid ad | `ad-creative`, `copywriting`, `marketing-psychology`, `short-form-video` (if vertical), `caption-animation`, `copy-editing` |
| Promo / launch | `motion-art-direction`, `beat-sync-editing`, `logo-animation`, `color-motion`, `motion-design`; `/brag` if it's about this repo |
| Explainer | `storyteller`, `animation-principles`, `motion-design`, `shot-composition`; `story-motion` if the character style was picked |
| Product demo / tutorial | `shot-composition`, `lower-thirds`, `caption-animation`, `media-use` (screen captures) |
| Footage edit / talking head / podcast clip | `footage-edit`, `caption-animation`, `lower-thirds`, `beat-sync-editing`, `media-use` |
| Testimonial / case study | `footage-edit`, `lower-thirds`, `caption-animation`, `storyteller` |
| Logo sting / brand piece | `logo-animation`, `motion-design`, `color-motion` |
| Any piece with an animated backdrop | `motion-background` (subtle, and never against a brand's "no blobs" rule) |
| Free-form / montage | `general-video`, `hyperframes-creative` |

**Brand overrides (load first, they win on conflicts):** a DUXIO job loads `duxio-brand` and `duxio-vsl`. The brand's look, words and CTA replace the generic style choice.

Say in one line which skills were loaded, then go.

## Step 3. Build
1. **Script** through the copy skills (or the user's script, cleaned with `copy-editing`). Every claim traces to a source; no invented proof.
2. **Beat sheet:** time | what the viewer must understand | visual | VO | SFX | music cue. Plan to `editing-standard.md` pacing.
3. **Build** in HyperFrames: one paused GSAP timeline at `window.__timelines.main`, scenes as absolute layers. Vendor GSAP and fonts locally (CDNs are blocked in cloud sessions).
4. **Voice:**
   - If the user uploaded a voiceover, use it, and transcribe it for word timings.
   - Otherwise use `npx hyperframes tts` (Kokoro, after `pip install kokoro-onnx soundfile`): `am_michael` for male, `af_heart` for female.
   - Align visuals to word timestamps, so each key word lands on its visual action.
5. **Sound:**
   - Real SFX and music beds first: brag's bundled assets (`~/.claude/plugins/cache/brag/.../assets`), then synth.
   - Voice chain, SFX bus, music carve under the voice (`hyperframes-audio`).
   - Master to the platform loudness.
6. **Captions:** word-synced on every social cut, inside the safe area.

## Step 4. Review, render, verify
1. `npx hyperframes check`: 0 errors.
2. Snapshot every beat and read the contact sheets. Run the `video-craft` §4 review and the `editing-standard.md` checklist. Fix, then repeat.
3. Render, then check:
   - duration, resolution and fps with `ffprobe`
   - loudness and true peak with `ebur128`
   - a 1fps contact sheet of the whole video
   - a transcription of the final mix, to prove the voice is intelligible
4. Platform cuts the format implies (9:16 / 4:5 recuts, hook variants for ads). Reframe by restacking, never by cropping.

## Step 5. Deliver
- `SendUserFile` the mp4 (render), plus the script.
- One short message: format, length, voice, and anything the user must confirm (example data, music licence, claims).
- Commit the source and the render to the session branch.

## Preflight (once per session)
- `node -v` (22+), `ffmpeg`, `npx hyperframes doctor`.
- `brag@brag` and `hyperframes@hyperframes` enabled (see `.claude/settings.json`).
- Name any blocked host and the exact fix.
