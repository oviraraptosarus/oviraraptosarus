# DUXIO design system (video and web)

Source of truth for how DUXIO looks. Built only from `tokens/tokens.json`, `tokens/tokens.css`, `docs/owner-spec-parts-1-to-5.md` and the owner's feedback. If something isn't here, ask; don't invent. Brand rules (words, claims, CTA) live in `.claude/skills/duxio-brand`.

## Colour
| Token | Value | Job |
|---|---|---|
| canvas | `#FFFFFF` | web page background |
| canvas-subtle | `#F9FAFB` | alternate web sections |
| ink | `#111113` | text on light |
| secondary / muted | `#4B5563` / `#6B7280` | support text on light |
| violet | `#6F00FF` | primary CTA, active state, the one highlighted phrase |
| violet (on dark text) | `#B794FF` | violet text on dark backgrounds |
| red | `#F1283A` | problems, leaks, missed revenue only |
| obsidian | `#0D0E12` | video frame and one contrast scene |
| video white | `#F5F5F7`, support `#9A9AA5` | text on obsidian |
| border | `rgba(0,0,0,.08)` / `.12` | web lines |

Glass panels in video: fill `rgba(255,255,255,.04)`, 1px border `rgba(255,255,255,.09)`, 28px radius. No blobs.

## Type
Plus Jakarta Sans 400 to 800. Display weight 800, tracking about -0.03em on video (-0.02em on web). Eyebrows uppercase, tracking +0.08em. Instrument Serif italic for one accent word at most. Inter variable for UI.

## Shape and space
Radius 10 / 16 / 24 and pill. 8px grid. One idea per frame, generous margin.

## Logo
`logo/svg/` (ink, white, violet, gradient wordmark; parts file for animation), `logo/original/monogram-metal.png` (hexagon D×X, also the favicon), `logo/social/` profile pictures.

## Voice and sound
Reels: energetic female (Kokoro `af_heart`, unconfirmed). VSLs: calm authoritative male. SFX under the voice; no chimes or bell ladders.

## Imagery
No AI generated images or video. Real photos, own footage, licensed stock or hand-built vector art. Source approval is an open item in `NEEDS-FROM-OWNER.md`.

## Video look and the references
Videos follow `.claude/skills/make-video/framework.md` and `visual-breakdown.md` (the owner's 7 reference reels): layered, textured, one world, a character or recurring object, a travelling camera. DUXIO's world is dark obsidian with violet as the active colour and red only for loss. **Open decision:** the character or mascot for DUXIO (owner wants one eventually).

## Never
Zero dashes in customer-facing text. No price, results or guarantees in videos. CTA is "Book a Strategy Call". Heading "Who this is ideal for". "Estimate", never "forecast".
