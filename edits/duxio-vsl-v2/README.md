# DUXIO VSL v2 (faceless, 1:57)

`duxio-vsl-v2.mp4`: 1920×1080, 30fps, exactly 117.0s, −16 LUFS, −1.4 dBTP.

- **Script:** `../duxio-vsl/script-v2.md`
- **Visual plan:** `../duxio-vsl/visual-treatment.md`
- **Concept:** follow one lead, Maya, through the coach's current process (she goes cold), then rewind and run the same DM through the Lead-to-Call System (she books).
- **Type:** Inter Display (variable, optical sizing) with Apple-style spacing.
- **Look:** iPhone and macOS-style interfaces. The pain section is in night mode and daylight returns after the rewind.
- **Sound:**
  - Phone sounds: notification, haptic, typing, send, chime, call join.
  - Rewind effect, a sub hit on −$3,000, and a riser into the end card.
  - Music: a filtered dark bed that cuts to silence on "nothing", then a bright bed that lands on the downbeat after the rewind. Both are carved under the voice.
- **Voice:** Kokoro `af_heart`, word-aligned with Parakeet so every visual lands on its word.
- **Captions:** karaoke style, hidden while the headline already says the line.
- **Rebuild:** `src/tools/words2.py` → `plan2.py` → `build2.py`, then `npx hyperframes render`.
- **Music licence:** brag bundled tracks (vol-12, vol-9); the licence is unverified upstream.
