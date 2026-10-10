---
name: duxio-vsl
description: "Write, storyboard, build or review any DUXIO video (the VSL (16:9, faceless, AI or recorded voiceover), its 1:57 cutdown, Instagram reels, shorts and ads). Holds the multi-influencer persuasion framework (Hormozi, Gadzhi, Suby, Tai Lopez, selectivity), faceless production rules, the DUXIO video look, the word-for-word master VSL script with visuals, cutdown and reel structures, and the video pre-flight. Use with make-video for production. Not for the website (use duxio-website)."
---

# DUXIO VSL and video

Load order: `duxio-brand` (rules every asset obeys) → this skill (what DUXIO videos say and look like) → `make-video` (how to produce them to an editor's standard). Website work lives in `duxio-website`; never mix the two.

## 1. Persuasion framework (use all five; each has one job)
| Lens | Job in the video |
|---|---|
| **Hormozi:** value = (dream outcome × likelihood) / (time delay × effort) | Remove all client effort. Sell the end of typing on a phone for three hours every night, not features. Use the rescued-client math (illustrative, labelled). |
| **Iman Gadzhi:** new vehicle beats improvement | Manual DMing and notes apps are the old way: they turn the coach into a low-paid messaging employee. DUXIO is the new backend. |
| **Sabri Suby:** bleeding neck in 10 seconds | Open on the pain: waking up to missed DMs and a hot buyer gone cold because you were coaching or asleep. |
| **Tai Lopez:** authenticity over polish | Show how the machine works, as a plain breakdown rather than a pitch. Kill the bot fear early: it's a natural reply in the coach's own voice, not a spam bot dropping links. |
| **Selectivity / high standards** | Desperation kills high ticket sales. Say who it's not for (no offer, nobody reaching out). The call is an honest check of fit. |

## 2. Faceless production rules
1. No face on camera. No webcam, selfie or ring-light shots.
2. Visual format, one of:
   - **A (default):** editorial motion graphics, black on white in Plus Jakarta Sans, cut with fast, accurately rebuilt UI moments (inbox notifications, a 45s reply, a calendar invite, the 2-step form).
   - **B:** a screen recording of a diagram being drawn on a blank canvas (Excalidraw, Miro or Figma).
3. **Voice for the VSL:** deep, calm, authoritative; an operations partner across a desk, not a radio host.
   - ElevenLabs: Adam or Marcus (or the owner's "serious" voice), Multilingual v2. Stability 65%, similarity 75%, style 0%, speaker boost on.
   - **Voice for reels and ads:** the opposite. Energetic and warm, female by default, using the `short-form-video` house rules (stability 30 to 45%, style 25 to 45%, speed 1.05 to 1.15). Never use the serious VSL voice for a reel.
   - If no file is supplied, ask for it once. Otherwise fall back to Kokoro (`am_michael` for the VSL, `af_heart` for reels) and say so.
4. No pricing in any video. The CTA sends people to the short form and a **Strategy Call**.
5. Calm voice, tight edit. The delivery is unhurried, but the cut never waits: follow the `make-video` editing standard (no dead air, a visual change every 2 to 4s, no slow fades).

## 3. The DUXIO video look (derived from the brand tokens)
- **VSL base (owner direction, 2026-10-10): Apple Keynote dark.**
  - Obsidian `#0D0E12` canvas with a faint radial lift.
  - White `#F5F5F7` type in Plus Jakarta Sans 800 (tracking -0.03 to -0.035em); support lines `#9A9AA5`, 500 to 600.
  - Subtle glass panels: `rgba(255,255,255,.04 to .06)` fill, a 1px `rgba(255,255,255,.1)` border, 28px radius.
  - Big type, wide margins, one idea per frame.
- **Website-style moments inside a video** (the form, the page) are shown light, exactly as the site looks.
- **Reels and ads** may use the dark base or a light editorial base (`#FFFFFF`, ink `#111113`). Pick one per piece.
- The full shot-by-shot build sheet, with motion, SFX and attention mechanics, is `brand/duxio/docs/vsl-v4-motion-sound-spec.md`; follow it for any VSL rebuild.
- **Violet `#6F00FF`:** only the CTA button, the active step, glows, and the one highlighted phrase per line (on dark use `#B794FF` for violet text).
- **Red `#F1283A`:** only problems, leaks, missed revenue, "too late".
- UI is drawn the way the real thing looks: an Instagram DM thread, an iOS notification, a calendar invite, the real form. Thin `rgba(0,0,0,.08)` borders and soft shadows.
- **Banned:** purple-pink gradient blobs, neon glassmorphism, floating particles, generic SaaS card grids, grey-on-grey text, zoom-as-filler. Subtle glass panels are fine; neon blobs are not.
- Logo:
  - `brand/duxio/logo/svg/duxio-wordmark-ink.svg` on light, `-white.svg` on dark.
  - For a build-up animation use `duxio-wordmark-parts.svg`: the four X arms (`x-tl x-tr x-bl x-br`) converge, then `d u i o` follow.
  - It lands on the final hit, never as an intro.
- Sound effects: `brand/duxio/sfx/`. Voice: `brand/duxio/voice/`. Fonts and tokens: `brand/duxio/fonts/`, `brand/duxio/tokens/tokens.css`.
- Before a new video, check `brand/duxio/docs/content-library.md` so nothing gets rebuilt that already exists.

## 4. Master VSL script (word for word; voiced by the owner as v4, 2:36 at about 3 words/s, file `brand/duxio/voice/elevenlabs-vsl-v4-serious.mp3`)
The v4 recording differs slightly from the text below: "while you were in a client call or asleep", "stop losing the ones who are already trying to talk to you", "Most buyers do not book on day one. We run a three week sequence ... real client stories so qualified people stay warm", and it ends "Fill out the form below and let us talk." Treat the recording as the source of truth.

Zero dashes, zero jargon, zero freebies. Visual notes are for the build only.

**[0:00 to 0:40] Bleeding-neck hook**
VO: "Every coach watching this has lost sales this month for one simple reason. Someone reached out while you were busy or asleep. You took three hours to reply. By the time you answered, they were already gone. Or you spent forty five minutes on Zoom, only to discover at the very end that they were never qualified in the first place."
Visuals: unread DM badges and an email notification, fast. Clock hands spin 2:00 PM → 5:00 PM. A message "Hey, how much is your coaching?" → a long gap → the lead goes cold (red).

**[0:40 to 1:15] Old way vs the backend**
VO: "Most people tell you to post more content, buy expensive ads, or spend three hours every evening glued to your phone manually messaging prospects. That is the old way, and it turns you into a full time messaging employee inside your own business. You do not need more leads. You need a backend that stops losing the ones you already have."
Visuals: split screen. Left, "The Old Way": a messy phone with 40 unread chats. Right, "The DUXIO Backend": one lead moving cleanly into a calendar slot.

**[1:15 to 2:40] The 4-step engine**
VO: "Here is how the DUXIO system works in four steps.
Step one is immediate speed. When someone reaches out, they get a reply in under sixty seconds. This is not a spam bot dropping links. It is a natural, conversational response in your tone of voice, so your prospects feel heard right away.
Step two is filtering. Before anyone gets to your calendar, the system asks three short, respectful questions. Prospects who are not ready get directed to your free content. Serious buyers get invited to book a time.
Step three is follow up and attendance. Qualified leads receive short, helpful check ins and proof stories over three weeks. Once they book, automated reminders ensure they show up on time and prepared to talk business.
Step four is reactivation. Once a month, cold contacts receive a short, human message that quietly restarts conversations with people who were not ready sixty days ago."
Visuals: four connected blocks revealed one at a time:
1. Lead arrives → a 45s reply → the lead answers.
2. Three filter cards (Goal, Experience, Readiness) get green ticks.
3. A 21-day timeline with 24h, 2h and 10m reminder pings.
4. A lead from 60 days ago tagged "Re-engaged" books a call.

**[2:40 to 3:25] The math**
VO: "The math is very simple. If eighty people reach out over the next month and this backend rescues just one or two sales that would have slipped away, that single difference adds thousands of dollars of profit directly to your business. You did not spend more on advertising, and you did not waste hours typing replies on your phone."
Visuals: type-led arithmetic: 80 inquiries → 2 rescued clients → thousands in profit, zero extra ad spend. Labelled "Example".

**[3:25 to 4:10] Fit and the Strategy Call**
VO: "This system is not for beginners with zero offer and no audience. It is built for active coaches and consultants who already have people reaching out, but do not have a dedicated backend to capture and close them. Below this video is a short sixty second form. Fill it out. If your business looks like a fit, you can pick a time for a Strategy Call. We will inspect your current lead flow, pinpoint where sales are leaking, and show you exactly how this backend runs. Fill out the form below, and book your call."
Visuals: the real 2-step form filled in, a cursor clicks "Book a Strategy Call", end card with the logo and the button.

## 5. Other DUXIO video formats (same rules, same look)
- **1:57 cutdown (16:9):** hook (0 to 15s) → old way vs backend (15 to 35s) → the four steps (35 to 85s, about 12s each) → math (85 to 100s) → fit and CTA (100 to 117s). About 290 words max.
- **Reel / short (9:16, 30 to 60s):** a hook line and the pain visual on frame 0 → the HBR stat or the old way → the four steps as four fast beats → "you just show up to calls" → "Book a Strategy Call, link in bio" → loop back to frame 0. About 3 words/s. Captions on everything.
- **Paid ad (9:16 or 4:5, 15 to 30s):** three hook variants (missed DM at night / "you don't need more leads" / the HBR stat), one mechanism beat, the CTA.
- The mechanism is always the four steps; never invent a fifth.

## 6. Video pre-flight (block delivery on any failure)
1. `duxio-brand` §9 on the VO script **and** every on-screen word, caption and button (zero dashes, banned words, no freebies, no income gate, four steps, allowed claims).
2. No price anywhere in the video.
3. The CTA is "Book a Strategy Call", spoken and on screen.
4. The look follows §3: light base, violet and red used only for their jobs, no blobs or glass.
5. Example names, messages and numbers are labelled "Example". The HBR stat is cited on screen.
6. The `make-video` editing standard and the `video-craft` review pass (pacing, sound, typography, detail).

## 7. Earlier deliverables (repo history; fix these if reused)
- `edits/duxio-vsl-v4/`: the current VSL (2:41), built on the v4 recording to the spec sheet. Apple-dark, four steps, Book a Strategy Call.
- `edits/duxio-vsl-v3/`: the VO says "five-stage" (it's four steps), "48-hour sequence" (it's 24h, 2h, 10m) and "exactly forty seconds" (under sixty). Its on-screen text uses hyphens.
- `edits/duxio-reel/`: violet aurora with glass cards (now off-brand per §3), "Re-engage", "re-opened", "high-ticket", "follow-up", "check-in" (dashes), and a five-pill rail.
