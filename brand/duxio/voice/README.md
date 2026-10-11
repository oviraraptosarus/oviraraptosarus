# Voice
- `elevenlabs-vsl-v4-serious.mp3`: the owner's ElevenLabs "serious" recording of the v4 master VSL script (2:36). Used in `edits/duxio-vsl-v4/`.
- **Reels need a different voice:** energetic and warm, female by default (see the `short-form-video` house rules for the ElevenLabs settings). Don't reuse the serious VSL voice for reels.
- `elevenlabs-serious-flat-masterclass.mp3`: the owner's ElevenLabs recording (v4, "serious_flat" voice) of the "Masterclass" VSL script, 1:47 raw. Used, with one sentence cut, in `edits/duxio-vsl-v3/`. Its text is in `../source-material/elevenlabs-masterclass-and-ai-scripts.md`. Note that it says "five stage", "48 hour" and "free pipeline audit", which the current rules no longer allow.
- Preferred voice for new videos: ElevenLabs, deep and calm (Marcus or Adam), or this same "serious_flat" voice for continuity. The owner records in ElevenLabs and uploads the file.
- Fallback when no file is supplied: local Kokoro TTS, `am_michael` (male) or `af_heart` (female), via `npx hyperframes tts`.


## ElevenLabs configuration (2026-10-11)
Settings live in `.claude/skills/voiceover-pacing/elevenlabs.json`; `eleven.py` renders a performance script with them once `ELEVENLABS_API_KEY` is set and `api.elevenlabs.io` is allowed in the environment.
- **Male, VSLs and YouTube:** Marcus (fallback Adam). Multilingual v2, Stability 65, Similarity 75, Style 0, Speaker boost on.
- **Female, reels and ads:** Jessica first (bright, warm, conversational), then Laura or Aria. Multilingual v2, Stability 38, Similarity 75, Style 35, Speed 1.08. Eleven v3 is the option for more emotion (audio tags such as [excited]).
- Voice names are resolved at run time from the account and the shared library, so confirm the pick by ear and tell Claude which one stays.
