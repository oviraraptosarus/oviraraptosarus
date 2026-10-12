# Style 1: Glass (Apple UI, violet)

**Status:** approved by the owner on 2026-10-12 ("i like that reel very much", "awesome, i love it"). **Default for all short form** (reels, shorts, ads) unless the owner names another style.
**Reference build:** `edits/duxio-reel-kit/reels/cold-call-ai-v2/` (35.8 s). **Ancestor the owner liked first:** `edits/duxio-reel/` (the 59 s reel).
**How to use it:** pick a template in `templates/`, run `py -3.12 kit/new_reel.py <template> <id>`, rewrite the slots, run `kit/make.py` or `kit/batch.py` (see `../../BATCH.md`). A new session reads this file and the registry `../README.md` and carries on.

## The principles (what makes it Style 1)
1. **Show, don't just say.** Every beat has a built visual element, not only text: iOS notifications, a call screen, chat bubbles, toggles, a calendar, a lock screen, progress bars, a counting badge. Think Apple. Giant text only was tried and rejected.
2. **Two typefaces.** Inter variable for everything (headline weight 760, small labels 650, big numbers weight 250 for the light Apple look) and Instrument Serif italic for the one highlighted word per line.
3. **Gradient only on highlight words.** Violet gradient `--grad` (loss words use red `--gradr`). Everything else is solid. A soft violet bloom sits behind the frame (as in the liked reel); no other gradients on text.
4. **One idea per slide, 1.5 to 4 seconds.** A two line headline plus one element. Each visual lands on the word that names it.
5. **Questions sound like questions.** Objections are real questions with a rising voice tone; the answer gets the next slide and a different element.
6. **Outcome first.** Money, call quality, show rate, time back (`duxio-brand` §0), then the mechanism, then the Strategy Call. Never "saving leads".
7. **Sound on every action.** A tick, pop, notify or snap for each visible event, a hook hit at frame 0, a short silence before the CTA.

## Look tokens
| Thing | Value |
|---|---|
| Frame | 1080 x 1920, 30 fps, 9:16, obsidian base `#07060b` |
| Bloom | three radial blobs (violet `rgba(115,0,240,.5)`, indigo `rgba(80,40,220,.38)`, lilac `rgba(190,90,255,.2)`) drifting slowly; grain and a vignette over everything |
| Glass card | `linear-gradient(180deg, rgba(255,255,255,.11), rgba(255,255,255,.05))`, 1.5px border `rgba(255,255,255,.14)`, big radius (46 to 52), deep soft shadow |
| Accent | violet `#7300f0` (var `--acc`), light violet `#b98cff` and `#c9adff`, green `#30d158` for success, red `#ff453a` for loss |
| Headline | Inter 760, 92 px, line height 1.04, tracking -.045em, white `#f5f5f7`, two lines max, centered at y 330 |
| Highlight word | Instrument Serif italic at 1.13 em, `--grad` text gradient (95deg `#8a3dff`, `#b98cff`, `#f1e8ff`); red `--gradr` for loss |
| Eyebrow | 30 px, 650, uppercase, tracking .14em, `#b3b3bd`, y 262 |
| Big numbers | Inter weight 250, tracking -.05em (the 60 ring, the 2:04 clock) |
| Captions | dark pill `rgba(10,8,16,.55)`, Inter 680 at 46 px, word synced, 4 word chunks, y 1452 |
| Layout zones | headline y 330 to 520, element y 640 to 1420, captions y 1452 and below. Nothing important under y 1420 |

## Motion
- Slide change: the new slide blurs and scales in over 0.32 s (`power3.out`), the old one fades out over 0.18 s.
- Camera: every slide slowly pushes in (scale 1.035) and drifts up 12 px; the background blobs travel the whole reel.
- Headline: each word rises out of a mask, 0.5 s `power4.out`, 0.06 s stagger.
- Elements enter with `back.out(1.4)` from 44 px below at 94 percent scale. Nothing hard cuts.

## Voice and sound
Voice recipe (Kokoro `af_heart`, `director.py`, rising tail on questions) is in `make-video/preferences.md` "Voice recipe". Music: library track "thugs" ducked under the voice. SFX are chosen per element by `kit/ap_sfx.json`. Loudness -14 to -15 LUFS, true peak under -1 dBFS.

## Elements
16 ready made elements, all with editable `props`: `kit/ELEMENTS.md`. New ones are added to `kit/ap.js` (or `kit/ap_ext_<id>.js` in a parallel session).

## Templates (plug and play)
| Template | Length | Use it for | Elements used |
|---|---|---|---|
| `objection-answers` | about 36 s | outcome first, then 3 objections each answered | call, notifs, age, chat, qual, cal, typing, appr, badge, lock, notready, route, report, handset, logo, cta |
| `how-it-works` | about 28 s | showing the mechanism step by step | notifs, chat, qual, cal, lock, route, report, cta |
| `lead-leak` | about 22 s | the pain of a lead going cold, then the fix | notifs, age, chat, lock, cta |
| `one-question` | about 16 s | one objection, one answer, one proof, CTA | typing, appr, report, cta |

Each template file lists its `_slots` (the text you rewrite). Word cues use relative refs (`first`, `mid`, `last`, `40%`, `word:strangers`, `end-0.12`), so they keep working when the sentence changes.

## Rules when filling a template
- Copy rules: `duxio-brand` (zero dashes, banned words, no freebies, claims from §7 only, price never in a reel). Names, messages, times and numbers shown in elements are illustrative: keep "Example" on screen.
- Phrases end with a full stop or a question mark; numbers are spoken as words, with the digits in `cap`.
- Ask the owner for the assets (rule 3d). Style 1 needs none by default; photos or screen recordings, if supplied, are shown inside an element (a future element), never as full frame stock.
- Write the sentences first, then the headline lines (shorter than the sentence, the highlight word is the idea), then pick elements.

## Before sending (checklist)
1. Contact sheet: no overlapping text, nothing under y 1420, every slide has a built element, highlight words carry the gradient, nothing else does.
2. `REPORT.md`: no check errors, loudness -16.5 to -12.5 LUFS, peak under -1 dBFS, every question shows a positive pitch rise.
3. Listen to the voice and the questions (the pitch check is a measurement, not a listen).
4. `duxio-brand` pre-flight (§9): dashes, banned words, claims, CTA wording.
5. Write the owner's reaction into `OWNER-RULES.md` §5 and, if it changes the look, into this file (bump the version below).

## Known limits
- Look is DUXIO violet. Another niche or brand changes `--acc`, `--acc2`, `--grad`, the logo asset and the wording through `look.vars` and `props`; the principles, fonts and layout stay.
- Elements are UI mockups, not footage. For real footage, photos or screen recordings a new element (a phone or window frame that plays a clip) must be built first.
- Not yet run: the first batch through `make.py` and `batch.py` (render, loudness and parallel runner stages).

## Version
- v1 (2026-10-12): captured from `cold-call-ai-v2` after owner approval.
