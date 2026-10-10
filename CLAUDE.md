# Video work in this repo

For any video request, start with `/make-video` (`.claude/skills/make-video/SKILL.md`): it picks `/brag` or story-motion. Otherwise load the `story-motion` skill (`.claude/skills/story-motion/SKILL.md`) together with `/hyperframes`. It sets the required caliber: a character-driven story, match cuts, a voiceover, SFX on every action, and a music bed. The reference implementation is `motion-reel-src/`.

`story-motion` section 0 routes to the vendored companion skills in `.claude/skills/` (MIT, with sources in each `SOURCE.md`):
- **Story:** storyteller, marketing-psychology
- **Copy:** copywriting, copy-editing, ad-creative
- **Reels:** short-form-video, video-content-strategist, caption-animation, lower-thirds
- **Motion:** motion-art-direction, animation-principles, motion-design, beat-sync-editing, shot-composition, color-motion, logo-animation, motion-background

## Plugins (auto-installed from `.claude/settings.json`)
- `hyperframes@hyperframes` (heygen-com/hyperframes): the HTML-to-video framework and its skills.
- `brag@brag` (latent-spaces/brag): `/brag` turns the current project into a ~20s launch video (`--voice`, `--tone`, `--format vertical`). It also bundles real music and SFX that `story-motion` uses.
