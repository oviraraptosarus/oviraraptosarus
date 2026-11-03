# Kept: 20s vertical reel (1080×1920)

A 9:16 remake of `motion-reel-src/`. It applies these skills:
- **story-motion** for the house caliber.
- **storyteller** for the arc: lie → truth → three thieves → midnight low point → the real number → sign-off → loop.
- **short-form-video** for:
  - a hook on frame 0 with no fade-up
  - an uneven pattern interrupt every 1–3s
  - word-synced captions inside the 900×1400 safe box
  - a loop seam where the last frame returns to the opening dashboard, now showing the truth
- **animation-principles**: anticipation before every bite, squash and stretch, and exits shorter than entrances.
- **brag**: its CC0 Kenney SFX, plus the "Happy Beats vol. 11" bed (music license unverified upstream). Every story beat sits on the track's cue map (1.6, 3.7, 6.86, 7.38, 8.44, 9.5, 12.65, 17.91s).
- **hyperframes-audio**, with three groups:
  - `voiceover`: highpass, mud cut, compressor, clarity boost, limiter
  - `sfx`: highpass, limiter
  - `music`: a voiceover carve (`carve.mjs`, strength 0.6) plus a midnight lowpass sweep and a volume dip
- **hyperframes-creative**: bass from the bed (`audio-data.js`) breathes the ambient dots, and treble warms the pill glow.

The render was mastered to about −15 LUFS with a −0.6 dBTP peak, using `loudnorm` followed by `alimiter`.
