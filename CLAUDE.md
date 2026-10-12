# Content creation in this repo

**Session start:** a hook prints `OWNER-RULES.md`, `CONTEXT.md` and `NEEDS-FROM-OWNER.md`; continue from `CONTEXT.md` "Next" without asking the owner to re-explain. **After every finished step, update `CONTEXT.md`** (state, done, next) and any other living file you touched (`NEEDS-FROM-OWNER.md`, the mistake log in `OWNER-RULES.md`, `brand/<name>/DESIGN.md`). New brand or niche: copy `brand/_template/DESIGN.md`.

**Read `OWNER-RULES.md` every session** (how to ask, cost limits, quality bar, mistake log) and show the open items in `NEEDS-FROM-OWNER.md` at the start of every video job.

**Short form videos use Style 1 by default** (owner approved, 2026-10-12): `edits/duxio-reel-kit/styles/style-1/STYLE.md` has the principles, tokens and checklist; ready templates are in `styles/style-1/templates/` (start one with `py -3.12 kit/new_reel.py <template> <id>`); the registry of styles is `styles/README.md`; making several videos at once is `edits/duxio-reel-kit/BATCH.md`. A new style is added by copying the folder, never by editing Style 1.

## Automatic skill routing
A `UserPromptSubmit` hook (`.claude/hooks/route-skills.py`, registered in `.claude/settings.json`) reads each prompt and tells Claude which skills to load. The user never has to type skill names. Follow its instruction before anything else. Without the hook, route the same way:
- any video job (short or long) → `make-video`, which always asks the missing brief questions first (one round), then logs the answers in `.claude/skills/make-video/preferences.md` so later videos ask less
- reel, short, ad, hook, b-roll, or the owner saying a video looks bad → `reel-ideation` first (vendored `adhd` divergent skill, gates, Concept Card), then `make-video`
- any music, soundtrack or SFX → `music-director` (after the voiceover); asset sources in `brand/duxio/docs/asset-sources.md`
- machine learning, neural networks, deep learning, PyTorch, transformers → `deep-learning` (refs: nn-zero-to-hero, LLMs-from-scratch; more via fetch-more.sh)
- any voiceover → `voiceover-pacing` (human pacing rules + `director.py`)
- VSL, sales video, sales script, hook → `vsl-script-writing` (Brunson frame plus the 10 tips; DUXIO rules override it)
- DUXIO anything → `duxio-brand` first
- DUXIO video → plus `duxio-vsl`
- any website, page, UI or web design → `site-design-gate` (30 vibecoded tells + audit)
- DUXIO website → plus `duxio-website` (the website and the videos stay separate)

## Skill selection and reporting
- `route-skills.py` handles the fixed routes; `skill-select.py` then scores every local skill (project, `~/.claude/skills`, plugins) against the prompt and suggests the best fits. If nothing local fits, check cloud skills with `ListSkills` / `SearchSkills`.
- It learns from the owner's words and saves to `.claude/skill-prefs.json`: "always use X", "never use X", "stop using X", "use X for <topic>".
- `log-skill.py` logs each Skill load (`.claude/skills-used.log`, not committed). End every finished task with one line: `Skills used: a, b, c`.

- Skills on the owner's local machine are not visible in cloud sessions. The repo's `.claude/skills/` is the single source of truth: run `.claude/sync-skills.sh` locally, then commit and push.

## Video
Entry point for any video, motion graphic, ad, promo, reel, VSL, explainer, demo, testimonial, footage edit or B-roll job: `/make-video` (`.claude/skills/make-video/SKILL.md`). It runs a one-round intake, asking only for the brief fields the request left out (type, platform and length, style, voice, CTA). It auto-selects the specialist skills for that video type, and holds every build to `make-video/editing-standard.md` (pacing, motion, sound, Apple-style typography, detail). It loads:
- **`video-craft`**: the quality standard, from principles (what makes a motion graphic good or bad, the pre-render review, how to learn from feedback). Always applied.
- **`video-formats`**: playbooks and specs for each deliverable (reel, ad, promo, VSL, explainer, demo, testimonial, long-form, clips, stories, brand pieces).
- **`footage-edit`**: the workflow when the user supplies footage and AI does the editing and the B-roll.
- **`story-motion`**: the character and metaphor storytelling style plus the build and audio pipeline.

Companion skills in `.claude/skills/` (MIT, sources in each `SOURCE.md`):
- **Story and copy:** storyteller, marketing-psychology, copywriting, copy-editing, ad-creative, video-content-strategist
- **Reels and captions:** short-form-video, caption-animation, lower-thirds
- **Motion and design:** motion-art-direction, animation-principles, motion-design, beat-sync-editing, shot-composition, color-motion, logo-animation, motion-background

## Plugins (auto-installed from `.claude/settings.json`)
- `hyperframes@hyperframes` (heygen-com/hyperframes): the HTML-to-video framework and its skills.
- `brag@brag` (latent-spaces/brag): `/brag` makes a launch video of the current project. It also bundles real music and SFX.

## User preferences for video
- B-roll and visuals are built with the tools in this repo (HyperFrames motion graphics, registry blocks, the user's own material, stock via media-use). No AI-generated video or images.
- Don't use zoom in/out as default filler. Use designed motion graphics and motivated moves only.
- Ask the full question round in one plain message (no popups) before every new video, then build cheaply. Rules and the list of questions: `OWNER-RULES.md`. After the concept card is approved, work autonomously; don't narrate options.
- Pacing is sales-tight: no dead air, no slow fades, nothing that delays the point. Apple-style type and spacing, a sound for every action. See `make-video/editing-standard.md`.
- Exemplars: `motion-reel-v2-src/` (16:9 story piece) and `kept-reel-src/` (9:16 reel).

## DUXIO (the owner's business)
- **Brand kit: `brand/duxio/`** (start at its README). It holds logos, fonts, tokens, SFX, voice, the master spec, facts, live site copy, the content library and research. Use it; don't ask the owner for these again.
- `duxio-brand`: shared rules. Voice, zero dashes in customer-facing text, banned words, no freebies (CTA is "Book a Strategy Call"), no income gate, the 4-step mechanism, the claims that may be made.
- `duxio-vsl`: all DUXIO videos (VSL, cutdown, reels, ads).
- `duxio-website`: the site and funnel.
