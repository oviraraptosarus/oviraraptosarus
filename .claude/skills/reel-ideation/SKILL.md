---
name: reel-ideation
description: "Mandatory ideation gate before any reel, short, ad hook or b-roll plan is scripted or built. Runs the ADHD divergent method (parallel isolated frames, then a critic) on the hook, the story and the visual of every beat, and ends in a one page Concept Card the owner can read in 30 seconds. Use before writing any script, before building any scene, and when the owner says a video looks bad, generic or boring."
---

# Reel ideation: no build without a Concept Card

Why this exists. Reel 4 ("Loading %") failed because the first idea was built: a counter plus small UI cards on a dark background, a narrator listing steps, a flat stand-in voice. Nothing was explored, nothing was tested against a scroller, and the pre-render review was lint plus loudness. This skill makes exploration the first step and a watched playback the last.

Read first: `.claude/skills/adhd/SKILL.md` (the divergent method, vendored from GitHub), `make-video/attention-mechanics.md`, and for DUXIO `brand/duxio/docs/content-calendar-month-1.md` (Dot and the series) plus `brand/duxio/docs/content-strategy.md`.

## Step 1. Trend and reference pull (5 minutes of work, not skipped)
- The month's trending formats: `brand/duxio/docs/reels-launch-7.md` §formats, refreshed with a search when older than 30 days. Mark them "unverified, check in app".
- The owner's reference videos (if any were sent) and the exemplars `kept-reel-src/`, `edits/duxio-vsl-v4/`. Describe what each does visually in two lines. Never design without one named reference.
- Pain source: `brand/duxio/source-material/coach-pain-points-reddit.md`. The hook starts from a pain, in the coach's own words.

## Step 2. Diverge with `adhd` (isolated parallel Agent calls, never serial)
This counts as an explicit `/adhd` invocation: skip the adhd pre-flight and go straight to Phase 1.
Run the `adhd` loop three times, one per layer. Frames come from `frames.md` (reel frames) plus the originals. Branches never see each other.
1. **Hook layer:** 5 frames x 6 hooks. The first three obvious hooks are banned.
2. **Story layer:** 5 frames x 6 shapes for the 15 to 30 seconds (character, stakes, turn, payoff).
3. **Visual layer, per beat:** 5 frames x 6 visual metaphors for each beat. A beat is any line that changes the picture.

## Step 3. Converge with the gates
Score every survivor 0 to 10 on novelty, viability, fit, then run the hard gates. An idea that fails a gate is cut, however clever.

| Gate | Pass condition |
|---|---|
| Stop the scroll | The frame 0 image plus first 1.5 seconds make a stranger ask "what happens?" without sound. State the open question. |
| Pain first | The hook is a coach's pain or a curiosity gap from the pain file, not a feature or a process name. |
| One idea | The whole reel can be said in one sentence. |
| Value | A coach could use the content tomorrow without DUXIO. DUXIO appears once, softly. |
| Visual variety | Every beat has a different visual treatment. No two adjacent beats use the same layout. |
| Motion density | Something meaningful changes on screen at least every 1.0 to 1.5 seconds. |
| Hero visual | Each beat has one big hero element at 40% or more of the frame width or height. Small floating cards are banned as the hero. |
| No dead zone | No empty region larger than a third of the frame for more than 1 second. |
| Sound | Every on-screen action has a named sound. Voice is the hero. |
| Rules | `duxio-brand` pre-flight: zero dashes, no "free", no price, no results, no guarantees, CTA "Comment WORD and I'll DM you". |
| Not generic | Cannot be described as "UI cards on a dark background". If it can, redo the visual layer. |

## Step 4. The Concept Card (written to `edits/<name>/CONCEPT.md`, shown to the owner for reels over 30 seconds or any new format)
- **Hook** (exact line and frame 0 image)
- **Story in one sentence**
- **Reference** (the named video or format it follows, and what it borrows)
- **Beat table:** time | VO line | hero visual | motion | sound
- **Why a stranger stays** (the loop or open question that holds until the end)
- **Rejected ideas** (top 3, one line each, so the owner sees the range)
- **Voice:** the exact voice file or "BLOCKED: need the ElevenLabs file". A stand-in voice is never shipped as final. Say so and stop.

## Step 5. Build, then watch
- Build only from the Concept Card. A change of idea means a new card.
- Before delivery: render, extract a 3 fps contact sheet, check every gate again on real frames, and play the audio against the picture word by word. Report any gate that fails. "Passes lint" is not a review.
- Deliver only what passes. If the voice is a stand-in, label the file `DRAFT_standin_voice` and say it is a draft.

## Lessons log (append after every owner reaction)
- 2026-10-11 · Reel 4 "Loading %": rejected as "looks like shit". Cause: first idea built, generic UI cards, empty frame, flat Kokoro voice shipped as if final, only lint and loudness reviewed. Rule added: Concept Card and the gates above.
- 2026-10-12 · Budget rule from the owner: ideate lightly (2 branches for a quick reel, no more than 3 agents), get the Concept Card approved, then build once. See `OWNER-RULES.md` §3.
