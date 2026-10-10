---
name: story-motion
description: House standard for every motion graphics / promo / explainer / "show off" video in this repo. Use whenever asked to make, redo or improve a video (HyperFrames or otherwise), even with no reference. Defines the creative caliber (character-driven story, metaphor, match cuts), the edit rhythm, the type/color system, and the full audio pipeline (voiceover + SFX on every action + music bed), plus a self-review loop. Use alongside /hyperframes; this skill wins on taste and pacing.
---

# Story-motion: the caliber bar

The exemplar is `motion-reel-src/` (render: `motion-reel.mp4`). Open its `index.html` before building. Match its **caliber**, never its layout: new story, new metaphor, new palette every time.

A video that only animates text and shapes fails this bar. Every video needs a **story told by a character through physical metaphor, cut to sound**.

## 0. Companion skills (vendored in `.claude/skills/`, MIT, see each SOURCE.md)

Load the ones that match the job. This skill stays the boss on caliber. Their code samples are often Remotion/React or After Effects, so translate the *principles* into the HyperFrames/GSAP timeline; never switch frameworks.

| Phase | Load | Use it for |
|---|---|---|
| Concept and story | `storyteller`, `marketing-psychology` | arc, emotional stakes, tension and release, persuasion triggers behind the hook |
| Script / VO / on-screen copy | `copywriting`, then `copy-editing` (sweep the script) | specific, benefit-first lines, customer language, cutting filler words |
| Ads / promos | `ad-creative` | hook angles, variants, CTA |
| Reels / TikTok / Shorts | `short-form-video`, `video-content-strategist` | 0–1s hook, an open loop closed last, pattern interrupts every 2–3s, loop endings, 9:16 safe areas |
| Captions / name tags | `caption-animation`, `lower-thirds` | word-by-word captions synced to the VO (reels need them; most viewers watch muted) |
| Art direction | `motion-art-direction`, `color-motion`, `shot-composition` | pick one motion personality and commit; palette, focal point, grid |
| Animation feel | `animation-principles`, `motion-design` | easing and duration tables, Disney principles, choreography and stagger |
| Edit rhythm | `beat-sync-editing` | cuts on beat phrases, `frames_per_beat=(60/BPM)*fps`, speed ramps into hits, match / J / L cuts |
| Logo / backgrounds | `logo-animation`, `motion-background` | brand sting at the end, living backgrounds |

**Platform defaults.** If the user says reel, TikTok, short or story, render 1080×1920 (9:16), keep text inside the safe area, add word-synced captions, and make the first frame itself a hook (no logo intro). Otherwise use 1920×1080.

## 1. Concept first (before any code)

Write these into `BRIEF.md` yourself; do not interview the user unless the subject is unknown.

1. **Protagonist object**: turn the abstract subject into one physical, lovable thing (money → a glossy orange ball with eyes; time → a clock; data → a droplet; bugs → a beetle). It must be able to *suffer and recover*: squash, melt, get bitten, shrink, blink, sigh.
2. **Villains / forces**: 2–4 secondary characters, each a distinct color plus shape (purple monster, blue flame, cardboard box). Each one *does a physical verb* to the protagonist (eat, burn, take), and the damage stays visible (bites accumulate).
3. **Arc** (scale beats to length; for 15s each beat is 1.5–3s):
   - Hook: a provocative lie or claim ("Your dashboard is LYING. to you.")
   - Setup: the protagonist with the claimed number
   - Twist: the truth, shown physically (melt)
   - Villains: one per beat, same rhythm, rule of three
   - Low point: a **contrast scene** with a different world (dark, stars, midnight, slow)
   - Resolution: the clear answer as a hero UI or object, annotated by hand (circle, REAL stamp)
   - Sign-off: brand plus a payoff line ("Every single frame.")
4. **Script**: VO lines of 3–8 words each, one per beat, conversational, with pauses ("You actually kept… four twelve."). On-screen text echoes the VO's key word; it never duplicates the whole line.

## 2. Visual system

- **Type pairing**: heavy grotesk (800–900, tight `-0.03em` to `-0.05em`) for statements, plus **serif italic in the accent color for the one emotional word** per line (*actually*, *today.*, *midnight.*). This pairing does most of the "designed" feel.
- **Color**: one hero accent (saturated) on warm off-white (`#f1efed` with a radial vignette), plus one villain color per villain. Use one full-bleed accent scene and one dark scene for contrast. Never use more than ~5 hues total.
- **Depth without 3D**: radial-gradient spheres (highlight at 34% 28%, darker rim, inset shadow, soft drop shadow), pearl spheres, soft UI cards with large blurred shadows. Add ambient floating particles in the accent color around the edges.
- **Real UI moments**: a dashboard card, an overview screen, a notification, or a chip like "The real one." Counters always *count* (`onUpdate` textContent).

## 3. Motion and editing rules

- **A new visual idea every 1–2.5s.** Nothing holds still longer than ~0.6s without a secondary motion (float, blink, flicker).
- **Match cuts over fades**: the shape of scene A *becomes* scene B (an orange full screen collapses via `clip-path: circle()` into the ball; the clock face expands into the next scene). Other transitions: wipe, slide-up panel, circle iris. Fade only at the very end.
- **Physics**: anticipation before a hit (lunge back, then forward), squash and stretch on landing, overshoot (`back.out`, `elastic.out`), shake on impact, crumbs or particles flying from impacts. Stagger everything that comes in groups (0.04–0.1s).
- **Character acting**: eyes appear late (a reveal), a blink sells life, and a "(sigh)" in gray serif italic beats any words.
- **Text entrances**: mask-reveal (`yPercent` 110→0 inside an overflow-hidden line), letters falling with random rotations for slams, a stamp scaling from 3.5→1 with a rotation.
- **Hand-drawn annotation**: an SVG path stroke-dash draw (circle around the answer, sparkline).

## 4. Audio pipeline (mandatory; a silent video fails)

Every video ships with voiceover, SFX and music.

1. **Voice**: `pip install kokoro-onnx soundfile` first (the CLI needs it), then one file per line:
   `npx hyperframes tts "line" -v af_heart -s 1.2 -o audio/voN.wav`
   - Default voice: `af_heart` (expressive female), speed 1.15–1.3. Use `am_michael` only when asked for male.
   - Measure every file with `ffprobe`, then set `data-start` so the **key word lands on its visual action** (bite, stamp, reveal). VO clips on one track must not overlap.
2. **SFX**: `python3 .claude/skills/story-motion/tools/sfx.py audio/`. **Every visual event gets a sound**: slam for letters, boing for landings, slide whistle for melts, bloops for drips, blink, two-bite chomp, pop for numbers, tick for clocks, ding for reveals, riser before the resolution, stamp, scribble while drawing, sparkle for the logo, whoosh on transitions, glitch on "lies". Expect ~2–3 SFX per second of video. Give each SFX type its own `data-track-index`.
3. **Music**: `python3 .claude/skills/story-motion/tools/music.py audio/ --dur <len> --bpm 128-145 --drop <lowpoint_start>,<lowpoint_end> --hit <logo_time>`. The drums drop out during the low-point scene, a riser leads back in, and a final hit lands on the logo.
4. **Mix**: VO `data-volume` 1.0, SFX ~0.55, bed ~0.28. Target about −16 LUFS integrated, peak below −1 dBFS. Check with `ffmpeg -i out.mp4 -af ebur128=peak=true -f null -`.
5. Every `<audio>` needs an `id`. If a HeyGen login or a music/SFX connector is available, prefer real stock BGM/SFX via `/media-use` over the synth kit.

## 5. Build and self-review loop

1. Write the beat sheet (time | visual | VO line | SFX) before coding.
2. Build one monolithic `index.html` (single paused GSAP timeline, scenes as absolute layers toggled with `tl.set(opacity)`).
3. `npx hyperframes check` must pass with 0 errors.
4. `npx hyperframes snapshot --at <one time per beat>`, then **read the contact sheet**, then fix and repeat. Reject a frame if:
   - text is clipped (mask height too small for descenders; use ≥1.25× font size)
   - an off-screen element peeks in (park it ≥900px away)
   - a frame is empty or just a fade
   - a beat has no character or physical action
   - two consecutive beats look alike
5. Render, then extract frames at 1fps (`ffmpeg ... fps=1,tile=5x3`) and review the whole flow once more.
6. Deliver the mp4 with a short beat list.

## 6. Environment gotchas

- jsDelivr is blocked in cloud sessions, so vendor GSAP: copy a `gsap.min.js` from the hyperframes skill assets (`find / -name gsap.min.js`) and use `<script src="gsap.min.js">`.
- The lint rejects tweening `letterSpacing`/layout properties. Use transforms (x, scale, scaleX) instead.
- HuggingFace and the Whisper model hosts are blocked, so `hyperframes transcribe` fails. Use `pip install pocketsphinx` for a rough transcript of a reference video.
- To analyze a reference video: `ffmpeg fps=2,tile` contact sheets for visuals; `librosa` (pyin pitch, beat_track tempo, hpss + onset_detect for SFX density) for audio.
