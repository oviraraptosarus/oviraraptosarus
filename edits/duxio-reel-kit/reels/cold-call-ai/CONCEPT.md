# cold-call-ai (24.9s, 9:16)

Owner brief 2026-10-12: "how AI replaces cold calling, how DUXIO does it, common objections answered, supreme typography, DUXIO design rules." Owner then said "you decide on everything, use giant type, just do it", so the concept card step was skipped by instruction.

**Angle (my pick):** cold calling chases people who never asked, AI answers the people who did. Chosen because the DUXIO brand rules describe an inbound follow up backend (reply under 60 seconds, 3 questions, 21 day follow up, monthly check in). Nothing in the brand rules says DUXIO dials strangers, so the reel does not claim it. "AI" appears in one line only; the brand says DUXIO does not sell chatbots. **Confirm that wording.**

**Objections (my list, NOT verified against real calls):** sounds like a robot, I already follow up myself, what if they are not ready. Answers use only claims allowed in `duxio-brand` §7 (coach's voice, coach approves every message, 21 days, quiet leads get a monthly check in).

**Blocks used (visual-breakdown.md):** giant slab type as the picture, travelling camera (push in, drift, blur whips), material (grain, vignette, ghost word parallax), one recurring object (a hand drawn handset: rings and is hung up in slide 1, comes back violet in the CTA). Character: none (the handset is the recurring object).
**Assets:** none supplied by the owner. Handset is vector drawn in code, wordmark is `brand/duxio/logo/svg/duxio-wordmark-white.svg`, no photos or AI imagery.

**Spine:** Hook (Stop calling strangers) > who actually asked (inbox) > 60 seconds > 3 objections with answers > Cold calling chases, DUXIO answers > Book a Strategy Call.
**Sound:** Kokoro `af_heart` at 1.14, music "thugs" ducked under the voice, one SFX on every word slam, strike, pill and the countdown bar, a 0.4s silence before the CTA. Loudness -13.9 LUFS, peak -1.4 dBFS.
**Rebuild:** `python reels/cold-call-ai/gen.py` (word cues come from the voice timings), then `py -3.12 kit/build.py reels/cold-call-ai/reel.json`.

**Not verified:** the voice and the final audio by ear; the objection list; the "AI" wording; no booking link on screen (the ending is "Book a Strategy Call" with no link, pending `NEEDS-FROM-OWNER.md` item 1).
