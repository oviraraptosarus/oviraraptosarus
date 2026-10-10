# Content creation in this repo

## Automatic skill routing
A `UserPromptSubmit` hook (`.claude/hooks/route-skills.py`, registered in `.claude/settings.json`) reads each prompt and tells Claude which skills to load. The user never has to type skill names. Follow its instruction before anything else. Without the hook, route the same way:
- any video job → `make-video`
- DUXIO anything → `duxio-brand` first
- DUXIO video → plus `duxio-vsl`
- DUXIO website → plus `duxio-website` (the website and the videos stay separate)

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
- Ask once, up front, for missing brief fields (via the `make-video` intake). After that, work autonomously and show results; don't narrate options or ask for approval on routine choices.
- Pacing is sales-tight: no dead air, no slow fades, nothing that delays the point. Apple-style type and spacing, a sound for every action. See `make-video/editing-standard.md`.
- Exemplars: `motion-reel-v2-src/` (16:9 story piece) and `kept-reel-src/` (9:16 reel).

## DUXIO (the owner's business)
- `duxio-brand`: shared rules. Voice, zero dashes in customer-facing text, banned words, no freebies (CTA is "Book a Strategy Call"), no income gate, the 4-step mechanism, the claims that may be made.
- `duxio-vsl`: all DUXIO videos (VSL, cutdown, reels, ads).
- `duxio-website`: the site and funnel.
