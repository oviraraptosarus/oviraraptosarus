---
name: music-director
description: "Gives a reel's music an arc and real intensity: picks the most energetic stretch of a track on the beat grid, adds synthesized drums, risers and impacts that follow the voice's energy curve, sweeps the filter, ducks under the voice and masters. Use for every reel, ad or VSL soundtrack, after the voiceover exists. Includes the track library and credit rules."
---

# Music director: make the track drive the reel

A bed that plays at one level reads as wallpaper. Instagram music is felt as a shape: a hit on frame 0, a drop to nothing for the sting, a build, then full drive on the CTA.

## Workflow
1. Voiceover first (`voiceover-pacing`). Give every phrase an energy `e` from 0 to 1 in the `.vo.json`:
   - hook and CTA: 0.9 to 1.0
   - normal lines: 0.5 to 0.7
   - gravity and stakes lines: 0.2 to 0.4 (the music tucks away and the voice owns the room)
   - the line before a reveal: dip low, then jump
2. Pick a track from `brand/duxio/music/library/` (credit in `CREDITS.md`), or the brag default. Audition 3 candidates on the same voice, as the owner decides by ear.
3. Run `python3 .claude/skills/music-director/director.py track.mp3 vo.wav vo.timings.json bed.wav --mix preview.mp3`. It prints the tempo, the cut point and the grid.
4. Add scene SFX from `brand/duxio/sfx/` (whooshes on cuts, a pop per element, `riser` and `boom` where the picture reveals). SFX sit 7 to 8 dB under the voice. No chimes.
5. In the final HyperFrames build use `bed.wav` as the music bus and keep the voice sidechain (the mix in the tool shows the levels).

## What the tool does
- **Cut:** finds the loudest stretch for the reel length and starts on a bar line.
- **Drums:** a synthesized kick, clap and hats locked to the detected beats. Density follows the energy: below 0.3 no kick, above 0.5 claps, above 0.8 sixteenth hats.
- **Hit and builds:** an impact at frame 0; a riser and impact before every pause of 550 ms or more, or every jump of 0.3 in energy.
- **Filter:** a low pass that opens with energy and closes under gravity lines.
- **Duck:** the music drops about 9 dB plus a sidechain whenever the voice speaks.
- **Master:** -14 LUFS, true peak under -1.5.

## Honest limits
- Tempo and beat tracking can misread (it read one track at double time). Check the printed tempo against the track.
- The synthesized drums are clean but generic. A real drum stem would sound better. They are tuned to sit under a voice.
- I cannot hear the result. I check loudness, peak and whether the transcript stays intelligible. The owner decides by ear.

## Lessons log
- 2026-10-11: the owner said the synthesized pad was "so bad" and the default tracks lacked intensity. Fix: real tracks plus this arc and drum layer.
