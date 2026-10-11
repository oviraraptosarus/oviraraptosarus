# Where the audio and motion assets come from

Only GitHub is reachable from the cloud session (freepd.com, kenney.nl and archive.org are blocked by the egress proxy). Everything below was cloned from GitHub and its license checked.

| Asset | Source | License | Where it lives |
|---|---|---|---|
| Music library (5 excerpts) | https://github.com/tannerhelland/free-music | CC BY 4.0 (credit in the caption) | `brand/duxio/music/library/`, credits in `CREDITS.md` |
| SFX: riser, reverse whoosh, 3 whooshes, swoosh, glitch, boom, drone, shutter, pop, click, success, magic reveal, notification, error | https://github.com/crafter-station/elements (`public/sfx`) | MIT repo (sound origin not stated; treat as MIT plus check before a paid ad) | `brand/duxio/sfx/elements/` |
| 125 GLSL scene transitions plus a skill | https://github.com/gl-transitions/gl-transitions | MIT | `.claude/skills/gl-transitions/` |
| Divergent ideation | https://github.com/UditAkhourii/adhd | MIT | `.claude/skills/adhd/` |
| Existing SFX | brand kit and the brag plugin | see their folders | `brand/duxio/sfx/`, plugin cache |

**Reference only (not installed):** LottieFiles/awesome-lottie and inlife/awesome-ae for motion presets and ideas; heygen-com/hyperframes (already installed as a plugin); Remotion's skills if a Remotion build is ever needed.

**Still missing:** a large CC0 pack of cinematic hits, bass drops and designed whooshes. None exists on GitHub. `music-director` synthesizes risers, impacts, kicks, claps and hats, and the elements pack covers whooshes and glitches. If the owner buys or downloads a pack (Epidemic, Artlist, Envato or a free CC0 pack from freesound), drop it into `brand/duxio/sfx/` and the tool will use it.
