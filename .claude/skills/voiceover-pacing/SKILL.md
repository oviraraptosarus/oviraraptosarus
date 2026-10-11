---
name: voiceover-pacing
description: "How a voiceover must be paced and performed so it sounds human, not AI: breaths, pauses, number reading, stress, falling landings, gravity on stakes lines, pitch variation. Includes director.py, which turns a marked up performance script into an mp3 plus caption timings (local Kokoro voice, WORLD pitch shaping). Use for every reel, ad or VSL voiceover that is not a real recorded or ElevenLabs file, and to direct an ElevenLabs take."
---

# Voiceover pacing: write it like a person breathes

A real ElevenLabs or recorded voice always beats this tool. When one exists, use it, and use this page to write and direct the script. `director.py` is the best local fallback and a draft-quality guide track, never a final voice you pass off as human.

## Why the AI voice gave itself away
1. **One speed.** Every line ran at the same tempo.
2. **Same gap after every sentence.** A person pauses long before a reveal and barely at all inside a list.
3. **Flat pitch.** Nothing was stressed, nothing landed, and statements did not fall at the end.
4. **Numbers read like text.** "2:07" or "7:50" came out as one flat blob.
5. **No weight.** The scary line sounded as bright as the hook.

## The rules (human language)

**Breath = phrase.** Write a reel in breaths of 3 to 7 words. Each phrase is one line of the performance script.

**Silences carry the meaning.**
- Inside a list or between joined thoughts: 60 to 200 ms.
- Between two sentences: 200 to 350 ms.
- Before a reveal or after the line that stings: 600 to 800 ms. Say nothing. The viewer fills it.
- Never the same gap twice in a row. Wobble each by about 10 percent.
- No silence over 0.8 s in a reel unless the picture is doing the work.

**Speed is emotion.**
- Hook and CTA: fast and bright, 1.1 to 1.2x, starting a little high and settling.
- Normal lines: 1.0 to 1.06x.
- Stakes and the sting: slower, 0.86 to 0.95x, lower in pitch by 1 to 2 semitones, and the last word falls hard. That is gravity.
- Alternate short punches ("And hit send.") with longer lines. Never three lines of the same length.

**One stress per phrase.** Lift the important word by about 1 semitone and make it a touch louder. Everything around it relaxes.

**Land the end.**
- Statements fall on the last word.
- Questions rise.
- A line that continues ("Send it at seven fifty,") ends level or slightly up so the listener knows more is coming.
- Triplets: first two rise or stay level, the last falls.

**Numbers are said the way people say them.**
- Times: "two oh seven", "seven fifty". Never "two colon zero seven".
- Chunk long numbers with a 60 to 90 ms gap.
- Write every number as words in the performance script.
- Spell out initials: "D M", "A M".

**Pace for Instagram.**
- The first word lands within 0.3 s of frame 0.
- About 2.7 to 3.2 words per second including pauses.
- 20 to 25 percent of the runtime is silence and breaths.
- Cut anything that does not earn its seconds.

## Using the director
1. Write `scripts/<name>.vo.json`. Each phrase has the text and these optional dials:
   - `speed`: relative tempo.
   - `st`: register shift in semitones, negative for gravity.
   - `reset`: bright start that decays.
   - `fall` / `rise`: how much the end bends down or up.
   - `gain`: dB.
   - `pause`: ms of silence after the phrase.
2. Top level dials:
   - `voice`: a Kokoro voice name, or a blend like `{"af_kore":0.55,"af_jessica":0.45}`.
   - `base_speed`, `k` (pitch range, keep 1.1 to 1.2), `strength` (how hard the bends hit), `seed`, `wobble`.
3. Run `python3 .claude/skills/voiceover-pacing/director.py script.vo.json out.mp3 --report`.
4. It writes the mp3, a wav, and `out.timings.json` (start and end of every phrase) for captions and the video kit. The report prints words per second, pitch spread and the list of pauses.
5. Check the transcript with `edits/duxio-vsl-v4/src/tools/asr.py`. Numbers, "D M" and names must read right.

**Honest limits.** The pitch tool cannot make Kokoro an actress. I cannot listen: the report proves structure (varied pauses, a controlled pitch range, intelligibility), not taste. The owner's ear decides. Keep `k` at 1.1 to 1.2 and `strength` at 0.7 or less: past that the vocoder starts to buzz.

## Lessons log
- 2026-10-11: owner said the voice had no pitch variation, no natural pauses and no gravity, and that number readings sounded robotic. Cause: one speed, a fixed gap, no stress, text style numbers. Fix: this page and `director.py`.
