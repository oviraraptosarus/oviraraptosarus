# Editing standard: pacing, motion, sound, typography, detail

The bar is a senior editor who cuts sales videos for a living. Sales-worthy means the viewer never waits and never strains. Too slow loses them, and so does anything that delays the point. This file is mandatory for every video built through `/make-video`, together with `attention-mechanics.md` (anticipation, rolling reels, variable payoffs, pitch ladders, idle life). Brand skills (e.g. `duxio-vsl`) can change colours and fonts, never these standards.

## 1. Pacing: no waiting, no rushing
**Voice rate**

| Format | Words per second |
|---|---|
| Reel / ad | 3.0 to 3.4 average, varied: about 3.6 in lists, about 2.4 on the key line |
| VSL | 2.4 to 2.7 |
| Explainer | 2.2 to 2.5 |

A calm voice is fine; a slow edit is not.

**Gaps between VO lines**
- 0.10 to 0.35s inside a thought; 0.4 to 0.7s at a section turn.
- Never more than 0.8s of dead air, unless a silence beat is deliberate (at most one per minute).

**Visual change**
- Reels and ads: every 1.5 to 3s.
- VSL: every 2.5 to 5s.
- Nothing sits fully still for more than about 1.2s: give it a counter, a highlight, a progress fill or a secondary move.
- Uneven intervals read as momentum; a metronome reads as boring.

**Openings and timing**
- The hook is on screen at frame 0. No fade from black, no logo intro, no "hey guys".
- The first spoken word comes within 0.1 to 0.3s.
- **Lead the voice, don't trail it.** A visual lands 0 to 120ms before its word. The key word, the visual hit and the SFX share one frame.

**Entrances and exits**
- Entrances 0.35 to 0.6s. Exits 0.2 to 0.3s, always faster than entrances.
- Scene transitions 0.25 to 0.45s.
- Never wait for an exit to finish before the next thing enters: overlap them by 0.1 to 0.2s.

**Holds and payoffs**
- A key line holds long enough to read twice: about words ÷ 3 + 0.5s.
- The CTA holds at least 2.5s with no competing motion.
- **Cut the delay, not the beat.** Remove pre-roll, throat-clearing and any setup the viewer can infer. But give the payoff (the number, the logo, the CTA) its full hold.

## 2. Motion: designed, motivated, one system
**One easing family per video**
- Entrances: `expo.out` / `power3.out`.
- Exits: `power2.in`.
- Moves on screen: `power2.inOut`.
- Overshoot (`back.out(1.3 to 1.7)`) only for things that land: chips, buttons, check marks.

**Hierarchy in motion**
- One primary move at a time. Secondary elements stagger 40 to 90ms behind.
- Everything else stays still.

**Text**
- Mask reveals: words rise from an overflow-hidden line, synced to their spoken word.
- No typewriter for headlines, no letter-by-letter on long lines.

**Transitions**
- Use match cuts and continuity: a shape becomes the next shape, a wipe goes in the direction of travel, a line draws into the next diagram.
- Crossfades only at the very end.
- No zoom or pulse as filler. Camera moves only when they mean something (focus, reveal).

**State changes and verbs**
- Show a state change through the thing that changed (colour, strike, fill, break), not a label.
- Counters count. Lines draw. Checks draw on.
- Verbs are performed: "cut" cuts, "drop" drops, "book" books.

## 3. Sound: half the video
**Voice**
- Chain: high-pass 75Hz → mud cut 250Hz -2.5dB → compressor (3:1) → presence +2dB at 3 to 4kHz → light air → limiter -1dB.
- The voice is always the loudest, clearest thing.

**SFX**
- One sound for every meaningful visual event: whoosh for a transition, pop or click for a chip, tick for counters, soft impact or sub for a reveal, ping or haptic for a notification, key clicks for typing, swish for strikes, a riser into the payoff, an impact plus sub on the logo or CTA.
- Sit 6 to 12dB under the voice.
- Never stack more than 2 or 3 sounds within 100ms.
- Vary the samples, so repeats don't sound looped.

**Music**
- Carved under the voice (`hyperframes-audio` carve, strength about 0.6). It sits 18 to 24dB under the voice while words play.
- Structure matters:
  - a lowpass or drop at the low point
  - a riser into the reveal
  - a full hit on the logo or CTA
  - a clean ending (a 0.3 to 0.6s fade, or end on a downbeat)
- Cut music beats to the edit: big reveals within about 0.15s of a strong beat.

**Silence and loudness**
- Silence is a tool: 0.2 to 0.4s of music dropout right before the biggest reveal.
- Masters:

| Channel | Integrated loudness | True peak |
|---|---|---|
| Social | about -14 LUFS | -1 dBTP or lower |
| YouTube / web / VSL | about -16 LUFS | -1 dBTP or lower |

  Verify with `ebur128`, then transcribe the final mix to prove the voice reads through.

## 4. Typography and spacing (Apple-style)
**Typeface**
- SF-like grotesk: Inter or SF Pro, or the brand font (DUXIO: Plus Jakarta Sans).
- At most one accent face, used for one emotional word per line (e.g. a serif italic), and only if the brand allows it.

**Display type**
- 80 to 140px at 1080 wide, weight 700 to 800.
- Tracking -0.03 to -0.045em, line-height 1.0 to 1.08.
- Balanced lines, at most 2 lines and 6 to 8 words.

**Support type**
- 32 to 48px, weight 500 to 600, tracking -0.01 to -0.02em, line-height 1.3 to 1.45, in the secondary colour.

**Eyebrows**
- 24 to 30px uppercase, weight 600 to 650, tracking +0.08 to +0.14em, muted.

**Numbers**
- Tabular figures for counters and times. Counters land on the exact spoken value.

**Spacing**
- 8px grid.
- Generous margins: 90 to 120px on the sides at 1080 wide, 96 to 160px at 1920.
- One idea per frame, with a lot of air around the hero.

**Contrast and colour**
- Body contrast 4.5:1 or better, display 3:1 or better.
- At most 2 font weights per frame.
- At most 4 or 5 hues in the whole video.

## 5. Attention to detail (the checklist an editor runs before export)
**Safe areas**
- 9:16: keep text inside the centre 900×1400, clear of the top 120px, the bottom 320px and the right 120px.
- 16:9: about 5% on every side.

**Alignment**
- Centre with layout (flex or measured bounds), never with guessed offsets.
- Check every centred element's rendered centre numerically (logo, headline, button).

**Text quality**
- No clipped descenders in masks: give a line-height of at least 1.25 × the font size, or pad the mask.
- No widows or orphans in headlines.
- No text overlapping text, including captions over the hero or a UI card.

**Truthful data**
- Times, dates and numbers on screen agree with the voice and with each other.
- Example data is labelled "Example".
- Counters end on the spoken number.

**Joins**
- At every cut, check the frame before and after: no flash of an empty frame, no element popping in or out, no leftover from the last scene, no double headline.

**Consistency and loop**
- One corner-radius scale, one shadow direction, one stroke weight.
- The same icon style throughout.
- Reels: the last frame matches the first, for a clean loop.

**Captions**
- Word-synced, 4 to 7 words a line, never covering the hero.
- Hidden where the on-screen headline already says the same line.

**Final pass**
- Watch at 1x with sound, then muted, then with eyes closed.
- Fix anything that made you wait, squint or wonder.
