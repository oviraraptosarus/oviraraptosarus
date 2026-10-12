# Visual breakdown of the 7 reference reels (what they are built from)

Companion to `framework.md`. The framework says what rules to follow; this file says what the references are physically made of, and what we can and can't build. Source: frame-by-frame contact sheets, 2026-10-12. Everything here is **[watched]**. Anything about tools or sources is **unverified** until checked.

## The rule this exists for
A reel built only from CSS boxes, rounded bubbles and text on a dark gradient is a **generic UI card reel** and is rejected (Reel 4, and the 2026-10-12 "Dots That Stopped" cut). Every reel needs at least **three** of the building blocks below, from different rows.

## Building blocks seen in the references

| Block | Where | What it is | We can build it? |
|---|---|---|---|
| **Real photo or footage layers** | v1, v6 | Childhood photos, phone selfies, street footage, news clips, cut to the beat | Only with the owner's own footage or properly licensed stock. Never AI generated |
| **Photo cutouts and collage** | v1 (the "17" tag, sunglasses strip), v6 (stacked cutouts) | A person cut out and layered over type, strips of another image sliced through | Yes, with real photos and masks in HyperFrames |
| **Giant slab type as the picture** | v1 | Red or black full-frame condensed type that is the scene | Yes |
| **Illustrated object world** | v4 (pixel icons on paper), v5 (clay diorama, mascot), v7 (line-art windows, one red character) | A small cast of drawn objects with weight and personality, living in one set | Yes if hand-built as SVG or sprite sheets. This is the big gap |
| **Material and texture** | v4 paper, v5 clay and tape, v6 grain and retro TV, v7 glow and reflection | Surfaces that feel like something. Grain, paper, soft shadow, reflection on a floor | Yes: grain, paper textures, shadows, reflections, glow |
| **Camera that travels** | v7, v3, v6 | The world moves, windows fly past, push-ins, blur whips between ideas | Yes: GSAP 3D transforms and blur, no hard cuts needed |
| **Type resolving out of blur** | v3 | Words sharpen into place, with a frosted UI behind | Yes |
| **A character** | v5 (the pink mascot), v7 (the red pen character) | One thing the viewer follows and feels for | Yes if drawn as SVG. Needs real design work |
| **Heat-map or silhouette treatment** | v4 | People as warm orange silhouettes on black | Needs real source footage. Unverified |
| **Scale shown physically** | v6, v5 | A building footprint beside Central Park, star counter rolling, price cards | Yes |
| **Typed or system text** | v7 | Terminal text, an input box that becomes the CTA | Yes (already in the kit) |

## What a reel must have
1. At least **3 blocks from different rows** (for example photo layer + material + travelling camera).
2. **One character or one recurring object** with a name and a behaviour.
3. **A set, not a screen.** The viewer sees a place (a desk, a shelf, a window stack), not a UI.
4. **Texture on everything:** grain, shadow and light, so nothing looks like a flat vector.
5. **A camera move** between ideas, so the picture travels instead of swapping.

## Where imagery comes from (no AI generated images or video, ever)
1. The owner's own footage and photos (put in `input/`).
2. Properly licensed or free-to-use stock, with the licence recorded in the repo. Source list to be agreed with the owner.
3. Hand-built vector art and sprite sheets made in this repo (SVG, drawn in code or from licensed icon sets).
4. Screen recordings of real apps, where the reel is about that app.

## Process change (applies from now on)
1. **Study first.** Name the reference(s) and list which blocks above they use. Cheap, from existing frames.
2. **Ideate with divergence** (`reel-ideation` + `adhd`). The first idea is never built. Scale the branch count to the budget: for a quick reel run 2 isolated branches, not 15.
3. **Concept Card to the owner before building**, listing the blocks used and where each asset comes from.
4. **Build, then check real frames** at about 3 fps. Reject it if it can be described as "UI cards on a dark background".
5. **Spend little.** No renders until the concept is approved. Prefer one subagent over many. Measure only what changes the decision.
