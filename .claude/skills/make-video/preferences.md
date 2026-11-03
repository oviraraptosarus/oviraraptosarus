# Learned video preferences

make-video reads this before asking questions and appends the user's answers after each intake. Newest last. Anything here counts as already answered.

## Standing (from the owner's feedback)
- Voice: reels and ads use an energetic female voice; VSLs a calm, authoritative male voice. Never flat.
- Sound: SFX at least 7 to 8 dB under the voice, no chimes or bells, a real cinematic hook at frame 0.
- Look: Apple-style type and spacing, tight sales pacing, no zoom filler, no AI-generated video or images.
- CTA: "Book a Strategy Call". Never a free audit. No price or scarcity in videos.
- Words: plain and human ("estimate", not "forecast"). Zero dashes in customer-facing text.

## Short form defaults (owner approved reel `cold-call-ai-v2`, 2026-10-12: "awesome, i love it")
**These defaults are packaged as Style 1 (Glass): `edits/duxio-reel-kit/styles/style-1/STYLE.md`, with ready templates and `kit/new_reel.py`. Start there.** Apply to every reel, short and TikTok unless the owner says otherwise. Reference build: `edits/duxio-reel-kit/reels/cold-call-ai-v2/`, scene library `kit/ap.js`.
- **Show, don't just say:** every beat has a built visual element (iOS notifications, call screen, chat bubbles, toggles, calendar, lock screen, progress bars, counters), not only text. Think Apple. Reels of text only are rejected.
- **Type:** Inter variable (display 760, light 250 for big numbers) plus Instrument Serif italic on the highlighted words. Eyebrow labels small, uppercase, tracked. Not Plus Jakarta Sans.
- **Gradient only on highlight words** (violet; red for loss words). Body type stays solid. Soft violet bloom behind the frame, glass cards, grain, slow camera push, blur whips between beats.
- **Questions must sound like questions:** objection lines are real questions and the voice ends on a rising pitch (`q` in the voice script, about 8 semitones). Check the pitch contour after rendering the voice.
- **Outcome first** (`duxio-brand` §0): money, call quality, show rate, time back. Not "saving leads". Objection then answer, each answered with an element.
- **Length and sound:** under 60 s (35 s worked well), energetic female `af_heart`, music "thugs" ducked under the voice, an SFX on every visible action, a short silence before the CTA, word synced captions in a dark pill at the bottom, nothing important under the caption zone (y 1452).
- **Voice recipe (use this exact setup for every reel voice):** Kokoro `af_heart` through `voiceover-pacing/director.py`, run with `py -3.12` (pyworld needs 3.12; build.py does it when launched with 3.12). Script file `voice.vo.json`: `base_speed` 1.12, `takes` 6 (best of 6 cleanest takes), `seed` 21, `lead_ms` 40, `pause_max` 900, `pause_scale` 1.0, no `shape` flag (clean path, no resynthesis). Per phrase: `speed` 1.0 to 1.12 (statements 1.06 to 1.12, hook 1.08), hand placed `pause` in ms (150 to 440; longer after answers), energy `e` 0.5 to 0.95 (hook and CTA 0.95, questions 0.55), one idea per phrase, numbers written as words in `t` with a digit version in `cap` for the captions. **Questions** get `"q": 8, "q_tail": 0.45` and speed 0.98: the director re-synthesises only the last 0.45 s with a rising pitch glide so the line ends like a question; verify with the f0 contour (look for a rise at the end, don't trust the ear-less assumption). Music: library "thugs", seed 7, ducked by `music-director`; SFX on every action. Final loudness about -14 to -15 LUFS, peak under -1 dBFS.
- **Assets:** the owner supplies visuals and photos; ask by name every video. With none supplied, vector elements built in code, labelled "Example" where names, messages or numbers are illustrative.
- **Process:** "you decide" means skip the questions and concept approval, build once, check frames, render once.

## Log
- 2026-10-11 · VSL 16:9 · ElevenLabs voice supplied · Apple dark look · CTA: Book a Strategy Call
- 2026-10-11 · content strategy · pages brand new (0 to 100) · faceless with voiceover · 5 reels + 1 YouTube a week · no ads: pain point content for coaches and consultants, edited to also hook the fast scrolling Instagram crowd · plan in brand/duxio/docs/content-strategy.md
- 2026-10-11 · reels · owner direction: script on the formats trending right now (research them first), think like a pro creator: value first, one soft mention of us, never salesy · CTA is "Comment WORD and I'll DM you" with a written DM that delivers the promised thing first, a question second, a Strategy Call invite only after they show lead volume · never the word "free" · example set: brand/duxio/docs/reels-launch-7.md

- 2026-10-11 · all reels · Ideation is mandatory before scripting (`reel-ideation` + `adhd`). Concept Card first. Generic dark UI cards, flat stand-in voices shipped as final, and lint-only reviews are rejected. Owner wants kid-like, playful, scroll-stopping ideas.
- 2026-10-12 · short form · owner loved cold-call-ai-v2 and asked to remember it: Apple style UI elements, Inter + Instrument Serif italic, gradient on highlight words only, rising tone on questions, outcome first, 35 s · saved as 'Short form defaults' above
