---
name: site-design-gate
description: Anti vibecoded design gate for any website, landing page, UI, app screen, slide or web design work. Lists the 30 tells that make a site look AI generated and the replacement for each, with a pre-ship audit. Use before and after designing or reviewing any page, hero, section, component, pricing, testimonial or visual style, in addition to duxio-website for the DUXIO site.
---

# Site design gate: 30 vibecoded tells and the fix

Source: the owner's reference reel "30 reasons your site looks vibecoded" (@aj.on.ai), transcribed and turned into rules. Run the audit BEFORE building (pick the replacements) and AFTER (grep and look). One tell is a style choice; three or more and the page reads as AI.

| # | Tell | Do instead |
|---|---|---|
| 1 | Harsh gradients | Flat brand colour; if a gradient, one hue, low contrast, used once |
| 2 | Lucide icons everywhere | Few icons, drawn or chosen to the brand, or none; type and real imagery carry the meaning |
| 3 | Pure white `#fff` background | Warm or tinted off white from the brand tokens, with a defined surface ladder |
| 4 | Rainbow colouring | One accent colour plus neutrals; colour means something |
| 5 | Drop shadows on everything | Borders or tonal surface steps; one shadow level reserved for overlays |
| 6 | Three feature cards in a row | Vary the layout: a list, a split with a real visual, a numbered flow, one big statement |
| 7 | Emojis as design | Never in UI or headlines |
| 8 | Liquid glass / glassmorphism | Opaque surfaces, no blur panels |
| 9 | Em dashes | Zero dashes in copy (DUXIO rule); rewrite the sentence |
| 10 | Inter, Geist or Space Grotesk by default | The brand fonts in `brand/duxio/fonts`; otherwise choose a pairing on purpose |
| 11 | Coloured left stripe on cards and callouts | Spacing and weight make hierarchy, not a stripe |
| 12 | Fake testimonials | Only real, verified ones with permission; otherwise a section of real process, never invented names or numbers |
| 13 | Bento grids | Only when the content is genuinely uneven; never as a default section |
| 14 | Terminal window mockups | Show the real product or a real screenshot |
| 15 | "It's not X, it's Y" copy | Say the claim directly; no reveal structure |
| 16 | Check mark bullets | Plain sentences or numbered steps; use a mark only for a true yes/no table |
| 17 | Three pricing tiers by reflex | Match the real offer (DUXIO: a single engagement, no public price) |
| 18 | No real product demo | Real screens, a recorded walkthrough or the actual flow |
| 19 | Soft rounded corners on everything | Pick a radius system (sharp, small or one deliberate round) and apply it consistently |
| 20 | Purple and black | Brand palette only |
| 21 | No skeleton loaders | Skeletons or a considered loading state for every async region |
| 22 | Radial orbs in the background | Plain backgrounds or real imagery |
| 23 | Dot grids and grid backgrounds | Cut them |
| 24 | Sparkle icons | Cut them |
| 25 | Animated arrows on buttons | Static, clear buttons |
| 26 | No terms of service | Terms page linked in the footer |
| 27 | No privacy policy | Privacy page linked in the footer and at every form |
| 28 | Hover animation on everything | Hover only on things that are clickable, with one consistent subtle state |
| 29 | Neon colours | Brand colours at normal saturation |
| 30 | Basic pastel colours | A deliberate palette from the brand tokens |

## Audit (run on the built page)
1. `grep -rniE "—|–|lucide|sparkle|backdrop-filter|blur\(|radial-gradient|linear-gradient|#fff\b|#ffffff|Inter|Geist|Space Grotesk|✓|✔|✨|[\x{1F300}-\x{1FAFF}]" src` and justify every hit.
2. Count layouts: no section may repeat the same card row twice in a row, and no three equal feature cards.
3. Check the footer for Terms and Privacy, and a skeleton or loading state for each async region.
4. Take desktop and mobile screenshots and look at them. Does it still feel like a template? If yes, change the layout, not the colours.
5. List the tells found and fixed in the reply.

## Working principles
- Start from the brand tokens and real content, not from a component library's defaults.
- Fewer, stronger decisions: one accent, one radius, one shadow level, two type sizes of emphasis.
- Real over decorative: real screens, real proof, real copy. Remove anything that exists only to look like a modern site.
