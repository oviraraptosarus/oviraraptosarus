# DUXIO VSL v4 (2:41, 1920×1080, 30fps)

Built on the owner's ElevenLabs recording of the master script to `brand/duxio/docs/vsl-v4-motion-sound-spec.md`.

**Look:** Apple Keynote dark: obsidian canvas, white Plus Jakarta Sans, violet for the active step and the CTA, red only for loss.

**Beats:**
1. Hook:
   - phone lock screen at 2:14
   - an Instagram DM springs in
   - the clock reels to 5:14 with "3 hours unanswered"
   - the lead goes cold
2. A Zoom timer reels to 45:00, then "Not a fit".
3. The old way:
   - three advice cards
   - the manual panel (unread badge 41, endless typing dots, "Coach" flips to "Full time messaging employee")
4. "You do not need more leads" → split screen: the manual way vs the DUXIO backend (a beam of light books the slot).
5. The DUXIO logo assembles from its X; the 01 to 04 rail fills as the camera glides through:
   - Answer: reply timer reels to 0:42, spam bubble rejected, "in your tone of voice"
   - Sort: Goal, Timeline, Readiness checks on a rising pitch ladder; routed to free content or a calendar slot
   - Follow up: 21-day timeline pings, booked invite, 24h/2h/10m reminders, "Joined"
   - Reopen: a Day 60 lead lights up violet
6. The math: 80 → 1 or 2 → Thousands, with a light sweep. Labelled as an example.
7. Fit list.
8. The page tilts down to the real 2-step form, a cursor fills it, and "Book a Strategy Call" is pressed.
9. End card.

**Sound:**
- Synth ambient bed (`src/tools/synth.py`): a dark pad, an arpeggio for the steps, and it opens for the math and the CTA. It sits about 22dB under the voice.
- Warm low-passed SFX: reel ticks with landing thunks, a C-E-G-C pitch ladder, confirm chimes, glass whooshes and sub hits.
- Master: about -15.7 LUFS, -1.9 dBTP.

**Rebuild:**
1. Convert the VO mp3 to `src/assets/vo/vo.wav`.
2. Run `python3 src/tools/synth.py` for the bed and SFX.
3. Run `python3 src/tools/build.py` (paths point at the build directory), then `npx hyperframes render`.

The music and VO wavs aren't committed because of their size.
