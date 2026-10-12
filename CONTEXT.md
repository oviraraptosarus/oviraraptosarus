# CONTEXT: where we are (read second, after OWNER-RULES.md; rewritten after every step)

**Rule:** after every finished step, edit this file (state, last done, next, open questions) before replying. If a new session starts, this file is the handoff. `HANDOFF.md` is older history; this file wins.

## Right now
- **Repo / branch:** `oviraraptosarus/oviraraptosarus`, branch `claude/blissful-hawking-xxcdii`, PR #1 open (don't open another). Local clone: `C:\Users\sriva\Desktop\CLAUDE\oviraraptosarus`.
- **Owner:** VRK. Runs DUXIO now, plans faceless channels in other niches and maybe a YouTube automation channel. Reels under 60s, longer for YouTube.
- **Mode:** the owner wants me to ask the question round (one plain message) before every video, then build cheaply. See `OWNER-RULES.md`.

## Done so far (newest first)
- 2026-10-12 Long form: installed NextWork `creator-teardown` + `ai-editor` plugins (user scope, NOT set up or tested; run the `ai-editor` setup skill once before first use), added `.claude/skills/long-form-video` (auto-routed by `route-skills.py` on YouTube, long form, raw footage, tutorial prompts). Face content covered: ai-editor already fully set up (doctor says Ready) and OpenScreen v1.5.0 installed (normal installer; silent mode crashed). Nothing tested. Router no longer uses popups. Bad commands in the pasted guides are listed in the skill.
- 2026-10-12 Studied Christian Peverelli's "I Fully Automated My Video Editing Using Claude Code" (YouTube HzXD4GVqXwM). Real cost there is about $24 to $27 per video, not $4. Takeaways saved in `OWNER-RULES.md` §3c: feedback becomes a numbered rule at once, tune sound separately, keep a reusable element library, strong model for setup and cheaper for routine builds.
- 2026-10-12 Session update setup: `CONTEXT.md`, session-start hook, `brand/duxio/DESIGN.md`, `brand/_template/DESIGN.md`.
- 2026-10-12 `OWNER-RULES.md` (question round, cost rules, quality bar, mistake log) and `NEEDS-FROM-OWNER.md`.
- 2026-10-12 `make-video/visual-breakdown.md`: what the 7 reference reels are built from.
- 2026-10-12 `make-video/framework.md`: five senses, hook shapes, story spines, pacing, sound.
- 2026-10-12 First 10s reel "Dots That Stopped" built and delivered (`edits/duxio-reel-kit/out/dots-10s/`). The owner said the look is wrong (flat UI cards); **do not redo it**, learn from it.
- 2026-10-11 Local setup on the owner's Windows PC: brag installed (plugin + `.claude/skills/brag*`, uncommitted), Python 3.12 has pyworld, reel kit built.

## Next
0. Start an element library (`edits/duxio-reel-kit/library/`: reusable scenes, characters, textures) once the first reference-style reel is built.
1. Wait for the owner to name the next video. Send the question round (OWNER-RULES §1), show open items from `NEEDS-FROM-OWNER.md`.
2. Build asset capability for the references' look: drawn characters and sets (SVG), textures, travelling camera. Not started.
3. Image source: still unanswered (the owner downloads images, supplies footage, or I draw vector art).

## Known facts to keep
- Reel kit: `edits/duxio-reel-kit/` (`kit/build.py`, `scenes.js`, `kit.css`). Voice tool: `.claude/skills/voiceover-pacing/director.py`, run with `py -3.12`.
- Voice: Kokoro `af_heart` (female), not yet confirmed by ear. No ElevenLabs.
- No AI generated images or video. Zero dashes in customer-facing DUXIO text. DUXIO CTA "Book a Strategy Call".
- Owner's cost bar: a full video for about $4, so no stalling, no extra measuring, no renders before an approved concept.

## Uncommitted (don't sweep in by accident)
- `.claude/skills/brag/` (17 MB), `.claude/skills/brag-slim/`, `edits/duxio-vsl-v4/src/assets/music/` and `vo/`.
