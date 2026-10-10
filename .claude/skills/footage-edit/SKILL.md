---
name: footage-edit
description: Workflow for when the user supplies raw footage (talking head, screen recording, podcast, interview) and wants AI to do the editing and the B-roll: ingest, transcript, cut dead air and filler, story-driven edit, B-roll plan from the transcript with each shot built from the tools in this repo (designed motion graphics, registry blocks, stock, screen captures, the user's own material), captions and overlays, audio cleanup and music, colour, reframing for each platform, QC. Use for any request that starts from the user's own video or audio files.
---

# Footage edit: user's footage, AI's B-roll and editing

The user is the talent and director; you are editor, motion designer and sound mixer. Output quality is judged by `video-craft`; structure and specs come from `video-formats`.

## 1. Ingest
- `ffprobe` every file (duration, resolution, fps, audio). Extract audio to wav.
- Look at the picture: sample frames (`fps=0.5` contact sheets) to understand the setting, framing, lighting, speaker position and any on-screen text.
- Note the deliverables (format, length, platforms) and infer the rest.

## 2. Transcript
- Use `npx hyperframes transcribe <file>` (word-level timestamps). In restricted cloud sessions the model host can be blocked. If so: ask the user for an SRT/transcript, or use a local fallback (`pocketsphinx`, rough timing only) and say that the timing is approximate.
- The transcript is the edit's source of truth. Work on text first, then apply it to picture.

## 3. Story edit (cut)
- Decide the spine: hook line (the most compelling claim moved to the top if needed), promise, body beats, payoff, CTA.
- Remove dead air (`ffmpeg silencedetect`), filler words, false starts and retakes. Keep natural breathing so it doesn't sound robotic.
- Tighten to the target length. Cut on action or on a breath; use J/L cuts (audio leads or trails picture) to hide joins.
- Build an edit decision list (source in/out, → timeline in/out) before rendering anything.

## 4. B-roll plan (the creative core)
For every sentence or beat, write what it should *show*, using these questions: what is being claimed, what is the most concrete image of that, and does a viewer need it to understand? Not every line needs B-roll; a talking face is fine for emotion and trust. Cover any stretch of 8s with no visual change.

B-roll is **built, not generated.** The toolset here is enough; don't ask for or wait on any AI video or image generator. Source order for each shot:
1. **Designed motion graphics in HyperFrames** (the default, fully on-brand): diagrams, UI mockups and product flows, charts and counters, kinetic text, maps, timelines, checklists, line-drawn illustrations, device frames, animated icons, shape-based scenes and characters. Build them with GSAP, SVG, CSS, canvas or Three.js, and start from the registry (`hyperframes-registry`: ~400 ready blocks for charts, terminals, maps, transitions and effects) before hand-building.
2. **The user's own material**: screen recordings, product shots, earlier videos, photos, logos. Treat them with `media-use` (grade, reframe, background removal, privacy blur).
3. **Stock and assets** via `media-use` / the registry when something actually matches (icons, brand logos, images, textures, LUTs).
Never leave a gap because a "generated clip" isn't available. If a line is abstract, build it as a diagram or kinetic typography.

Rules for B-roll: it illustrates the *exact words being spoken*, enters on the key word, leaves before the thought ends, and keeps the same palette, grade and motion language as the rest. Alternate it with the speaker so the face returns every 5–8s. Don't use zoom in or out as a stand-in for B-roll.

## 5. Overlays and graphics
- Captions: word-synced, 4–7 words per line, safe zones (see `caption-animation`). Highlight the key word.
- Lower thirds for names/roles, chapter cards for long videos, callouts for numbers and terms, source or proof chips.
- HyperFrames workflows `talking-head-recut` (designed overlays over untouched footage) and `embedded-captions` (captions behind or around the subject) can be used directly.

## 6. Sound
- Dialogue first: `hyperframes-audio` voice-clean chain (rumble cut, mud cut, compressor, clarity, limiter). If the room is noisy, flag it. Gating only hides it between sentences.
- A music bed that fits the tone, carved under the voice (`carve.mjs`), dropped or softened on the key claim, lifted at the payoff.
- SFX only for meaningful actions (graphic arrivals, transitions, numbers landing); never over a spoken punchline.
- Master to the target loudness in `video-formats`.

## 7. Picture polish
- Consistent exposure and white balance between cuts. Apply a grade through `media-use` treatments rather than ad-hoc filters. Keep skin tones natural.
- Reframe for each aspect ratio by re-composing (move the crop to follow the speaker), not by letterboxing. Check captions and graphics against each platform's safe zones.

## 8. QC and delivery
- Snapshot every cut and every graphic and run the `video-craft` review. Watch for jump-cut jitter at joins, B-roll that doesn't match the words, clipped captions, audio pops.
- Deliver the master plus each platform cut, the transcript or SRT, and the edit decision list. Commit the project (not the raw footage) to the branch and send the files.
