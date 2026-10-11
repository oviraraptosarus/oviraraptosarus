# DUXIO content system: handoff

Paste the block under "Prompt for the new session" into a fresh session. Everything else in this file is the detail it points to.

---

## Prompt for the new session

```
You are continuing an existing project. Treat this as the same session, not a new one.

Repo: oviraraptosarus/oviraraptosarus. Branch: claude/blissful-hawking-xxcdii (develop, commit and push only there). PR: https://github.com/oviraraptosarus/oviraraptosarus/pull/1 (already open, do not create another).

Do this first, in order, before replying:
1. Read /home/user/oviraraptosarus/HANDOFF.md fully.
2. Read CLAUDE.md, then brand/duxio/README.md and brand/duxio/docs/facts-and-owner-answers.md.
3. Read the skills: .claude/skills/duxio-brand, duxio-vsl, duxio-website, make-video (SKILL.md, editing-standard.md, attention-mechanics.md, preferences.md), short-form-video, video-craft.
4. Run `git log --oneline | head` and `git status -sb` to confirm you are on the branch and clean.

Who I am: the owner of DUXIO, a done-for-you follow-up backend for high ticket coaches. You are my video and content tool, not my colleague. Do the task. Do not add opinions, options or lectures. Keep replies short.

Rules that never change:
- Skill routing is automatic (hook in .claude/hooks/route-skills.py). Any video job loads make-video; DUXIO work loads duxio-brand; DUXIO video also duxio-vsl; DUXIO site also duxio-website. The site and the videos stay separate.
- For every NEW video, short or long, ask the missing brief questions once, in one AskUserQuestion round, then build without further check-ins. Skip the round if I say "you decide", "no questions" or "just do it", and for revisions of a video already built in the conversation. Save my answers to .claude/skills/make-video/preferences.md.
- CTA is always "Book a Strategy Call". Never a free audit. No price, no "5 spots", no client results, no guarantees in videos.
- Zero dashes (hyphens, en dashes, em dashes) in customer-facing text. Plain human words ("estimate", never "forecast"). Heading is "Who this is ideal for".
- No AI-generated video or images. No zoom filler. Apple-style type and spacing, sales-tight pacing, a sound for every action.
- Sound: the voice is the hero. SFX at least 7 to 8 dB under the voice (measure with voice-only and SFX-only stems), no chimes or bell ladders, a cinematic hook at frame 0. Reels and ads use an energetic female voice; VSLs a calm authoritative male voice. Never flat.
- Use brand/duxio/ for logos, fonts, tokens, SFX, voice, facts. Never ask me for them again.

Current state: VSL v4.1 is finished and pushed (edits/duxio-vsl-v4/). I told you I would send reference videos later. When they arrive, study their pacing, sound and motion and fold what you learn into the skills (make-video/attention-mechanics.md, editing-standard.md, short-form-video, duxio-vsl). The unfinished list is in HANDOFF.md section 6. Wait for my next instruction; do not start any of it unprompted.

Reply with one line confirming you have read everything and are on the branch, then wait.
```

---

## 1. Project in one paragraph

DUXIO builds and runs the follow-up that turns interested leads into booked sales calls for coaches and consultants selling high ticket offers. This repo is the owner's content factory: a HyperFrames (HTML to video) setup with a brand kit, a set of skills that auto-load by prompt, and the videos made so far. The owner wants to start a content creation arc (Instagram reels, a VSL, ads) and wants Claude to know the brand and taste without being told again.

## 2. The DUXIO blueprint (full source in `brand/duxio/`)

| Item | Value |
|---|---|
| Hero line | "Turn interested leads into paying clients." |
| CTA | "Book a Strategy Call" (short form "Book a Call"). Never a free audit, never a freebie |
| Mechanism (always these four) | 1. Every lead gets an answer. 2. Serious buyers get sorted. 3. 21 day follow up and call reminders. 4. Quiet leads reopened |
| Offer (website only) | $397 one time setup, then $300 to $800 a month. Not in videos |
| Reminders | 24 hours, 2 hours, 10 minutes before the call |
| Reopen | a short human check-in every month, reopened for 90 days |
| Control | messages written in the coach's voice, approved by the coach; built inside the coach's own accounts; the coach owns it |
| Fit | active coaches and consultants with leads reaching out and no backend to capture and close them. Heading: "Who this is ideal for." No income gate. Beginners with no offer and no audience are not a fit |
| Proof | no client results yet. Only the HBR 2011 lead-response stat (cite it on screen). Example numbers are always labelled "Example" |
| Site | https://duxio-website-for-coaches.vercel.app/ (repo `oviraraptosarus/duxio-website-for-coaches`, TanStack Start, Tailwind v4, Supabase `public.lead_applications`, Vercel) |
| Look | Apple Keynote dark for video: obsidian `#0D0E12`, white `#F5F5F7`, Plus Jakarta Sans 800 at -0.03em, support text `#9A9AA5`, violet `#6F00FF` (fills) and `#B794FF` (violet text on dark), red `#F1283A` only for loss. Glass panels `rgba(255,255,255,.04)`, 1px border `rgba(255,255,255,.09)`, 28px radius. One idea per frame. No blobs |

Where each thing lives:
- `brand/duxio/README.md`: index and quick facts.
- `brand/duxio/logo/` (svg, png, original, social), `fonts/`, `tokens/`, `sfx/` (with `LICENSES.md`), `voice/`.
- `brand/duxio/docs/`: `owner-spec-parts-1-to-5.md` (the owner's master spec, verbatim), `facts-and-owner-answers.md` (every claim must trace here), `site-copy.md`, `website.md`, `content-library.md`, `vsl-v4-motion-sound-spec.md`, `content-strategy.md` (the IG, FB and YouTube plan).
- `brand/duxio/source-material/`: raw research, VSL script library, Reddit pain phrases, objections.

## 3. The skills and what each does (`.claude/skills/`)

| Skill | Job |
|---|---|
| `make-video` | The one entry point for any video. Mandatory one-round intake, auto-selects specialist skills, builds, reviews, renders. Files: `SKILL.md`, `editing-standard.md` (pacing, motion, sound, type, detail checklist), `attention-mechanics.md` (slot-machine and game-feel mechanics, research table, owner feedback), `preferences.md` (learned choices) |
| `duxio-brand` | Voice, zero-dash rule, banned and anti-AI vocabulary, plain words over stiff ones, the 4 steps, offer rules, allowed claims |
| `duxio-vsl` | All DUXIO videos: persuasion lenses, faceless rules, the Apple dark look, the master VSL script, reel structure, voice settings, sound rules, pre-flight |
| `duxio-website` | The site and funnel: design hierarchy, copy, 2-step form, DB schema, calculator, launch checklist. Kept separate from videos |
| `short-form-video` | Reels, shorts, TikTok. "House rules" section: HyperFrames not Remotion, energetic female voice by default, sound at frame 0, about 1 SFX a second, a visual change every 1.5 to 2.5s, 2 to 4 word captions |
| `video-craft` | Quality standard and pre-render review, plus learned principles (slow is a defect, voice is the hero of the mix, measure stems, no cheap chimes) |
| `video-formats`, `footage-edit`, `story-motion` | Format playbooks, footage-plus-B-roll workflow, character storytelling and build pipeline |
| Companion skills | storyteller, marketing-psychology, copywriting, copy-editing, ad-creative, video-content-strategist, caption-animation, lower-thirds, motion-art-direction, animation-principles, motion-design, beat-sync-editing, shot-composition, color-motion, logo-animation, motion-background |
| Plugins | `hyperframes@hyperframes`, `brag@brag` (auto-installed from `.claude/settings.json`) |
| Router | `.claude/hooks/route-skills.py`, registered as a `UserPromptSubmit` hook; it tells Claude which skills to load and enforces the intake round |

## 4. The owner's taste (learned from feedback, in order)

1. Wants stunning, original visual design for short form, not the same UI twice. Uses the logo.
2. The first reel looked great but sounded flat and "depressed". Needs an energetic female voice, enthusiasm, and pacing variation that fits the Instagram algorithm. Fixed in the skills; the old reel has not been rebuilt.
3. Wants slot-machine micro-movement psychology used honestly: anticipation before reveals, decelerating rolling counters, uneven reward spacing, rising pitch ladders, near-miss framing. Backed by research (Fiorillo 2003 and others, in `attention-mechanics.md`).
4. SFX must never dominate the voice. The chime sounds were the worst offender. Use soft thunks, taps and wood plucks, never bright bells.
5. Wants a real hooking sound at frame 0 (sub impact, pulse, swell, hit), not a small chime.
6. Words: "estimate" not "forecast"; "Who this is ideal for" not "who this is for"; plain human language, no AI tells.
7. "Thousands" should be a money counter, $0 to $6,000, with coin ticks and a register land.
8. The form demo price must feel accessible: "$1,000 to $3,000" offer option, not high-ticket only.
9. Hates chatter. Wants the tool to execute, not opine. Wants questions only at the start of a new video, then autonomous work.
10. Wants auto skill selection so they never type skill names.

## 5. Everything changed so far (commit trail on this branch)

| Commit | What |
|---|---|
| `3701a53` | First DUXIO Instagram reel, 59s 9:16 (`edits/duxio-reel/`) |
| `5d41c88` | Brand, website and VSL skills; `make-video` becomes an auto-routing intake with an editing standard; the prompt hook |
| `652615e` | Full brand kit in `brand/duxio/` (logos as vector and PNG, social avatars, monogram, fonts, tokens, SFX, voice, spec, facts, site copy, content library, research) |
| `c898325` | VSL v4 on the owner's ElevenLabs voice (Apple dark, attention mechanics), motion and sound spec, short-form house rules, `attention-mechanics.md` |
| `b1efad3` | VSL v4.1: SFX rebalanced under the voice (measured with stems), cinematic hook audio, no chime ladders, $0 to $6,000 money counter, "estimate", "Who this is ideal for", $1,000+ form option; rules recorded in the skills |
| `2dd2762` | Routing hook catches more video phrasing; intake mandatory for short and long videos; answers learned into `preferences.md` |

Deliverable details, VSL v4.1 (`edits/duxio-vsl-v4/`): `duxio-vsl-v4.mp4`, 2:41, 1920x1080, 30fps, -15.7 LUFS, -2.0 dBTP; `captions.srt`, `script.md`, `README.md`; `src/` has `index.html`, `T.json`, `words.json`, assets and `tools/` (`template.html`, `build.py`, `synth.py`, `asr.py`). The build directories under `/tmp` are gone in a new session; rebuild from `src/` and `tools/`.

Technical lessons worth keeping (also in the skills):
- HyperFrames composition: one paused GSAP timeline at `window.__timelines.main`; run `npx hyperframes check` then `snapshot` then `render`.
- Automation lane volume values are absolute gains that override `data-volume`. Scale the lane values themselves.
- Measure the mix: render voice-only and SFX-only passes (320x180, `--fps 5`), compare 400 ms windows, SFX at least 7 to 8 dB under the voice during speech. Only the frame 0 hit may come closer.
- Master with `loudnorm=I=-15.4:TP=-2:LRA=11,alimiter=limit=0.79:level=false` (lands near -15.7 LUFS); verify with ebur128, then transcribe the final mix (sherpa-onnx parakeet) to prove the voice reads through.
- ElevenLabs settings: VSL stability 65, similarity 75, style 0, speaker boost on (Adam or Marcus). Reels: energetic female, stability 30 to 45, style 25 to 45, speed 1.05 to 1.15.
- Avoid same-time conflicting `tl.set` calls at 0; guard `VIS` helpers with `t0>0`.

## 6. What is left unfinished

Waiting on the owner:
1. **Reference videos.** The owner said they will send videos to learn from. Study pacing, sound and motion, then update `attention-mechanics.md`, `editing-standard.md`, `short-form-video` and `duxio-vsl`.
2. **Missing brand facts** (listed in `brand/duxio/README.md`): the real booking calendar link, the Instagram handle, any permissioned client result or testimonial, a licensed music track.

Offered, not yet requested (do only when asked):
3. **Rebuild the Instagram reel** to the current rules: energetic female ElevenLabs voice, no hyphens, four steps (the old one has a five-step rail), hook audio, measured SFX, money counter. Needs an energetic female VO file from the owner, or Kokoro `af_heart` / `af_bella` as a fallback.
4. **Fix the live site** (`duxio-website-for-coaches`): the chatbot `SalesChatbot.tsx` uses "Growth Expert", an emoji, "lead generation", "custom blueprint" and a placeholder Calendly link. Needs the real booking link.
5. **Replace VSL v3 with v4.1 on the site** (v3 says "five stage", "48 hour sequence", "forty seconds" and has hyphens).
6. **Cutdown and other formats** of the VSL (1:57 cutdown, ads, more reels) once the reel rebuild sets the short-form standard.
7. **Execute the content strategy** (`brand/duxio/docs/content-strategy.md`): profile setup copy, our own comment keyword backend, the first 10 banked reels from the hook bank, YouTube #1 and #2. Nothing built yet.
8. Not verified end to end: the updated routing hook has been tested on sample prompts only, not on a live new-video request with the intake round.

Older assets and their status are in `brand/duxio/docs/content-library.md` (v1 to v3 and the first reel are older or off-brand; v4.1 is current).

## 7. How to behave

- Minimal chatter. Execute. Report in a few lines: what was made, where it is, anything the owner must confirm.
- Send finished videos with `SendUserFile`. Commit and push to the branch after each deliverable. No new PR; PR #1 already exists and updates on push.
- Ask questions only through the make-video intake round for new videos. Never narrate options for routine choices.
- Never invent proof, scarcity, prices, or numbers. Example data is labelled "Example".
