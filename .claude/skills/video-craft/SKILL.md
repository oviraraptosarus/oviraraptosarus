---
name: video-craft
description: The quality standard for ALL video work in this repo: motion graphics, ads, promos, reels, VSLs, explainers, product demos, footage edits with B-roll. Defines what makes a motion graphic good or bad from principles (meaning-first motion, coherence of message, metaphor and design, hierarchy, restraint, truthful visuals, information order, pacing, sound), a pre-render review, and how to learn from feedback. Load for every video task, before planning and again before rendering.
---

# Video craft: the standard

A video is good when a viewer understands and feels the message with no effort, and nothing on screen is there for any other reason. Everything below is a consequence of that.

## 1. Core idea: motion is meaning

Every element, movement, colour and sound must carry the message. Test any element: remove it. If the story loses nothing, it was decoration, so cut it. Motion is a language, so each move must say something (this appears, this matters, this causes that, this is now gone).

## 2. What makes a motion graphic good

**Coherence (the three must agree).** The *message* (what is said), the *metaphor* (what is shown) and the *style* (how it looks and moves) must tell the same story. When one drifts, the video feels "off" even if every frame is polished. Most "I can't say why it's bad" feedback is a coherence break. Check the three against each other before building, and again on the finished frames.

**Truthful visuals.** What's on screen does what the words say. Verbs are performed, not decorated: if the voice says "cut", something is cut. States are shown with design (colour, shape, grey-out, break, glow), not by captioning them. A metaphor character must have the means for its verb. Numbers add up and claims trace to the source material.

**Represent things the way professionals in that field do.** Dashboards look like dashboards (large, layered, in perspective, believable data). A breakdown looks like a bill or waterfall. A funnel looks like a flow with real stages. A timeline looks like a timeline. A message thread looks like a chat UI. Audiences read these conventions instantly; a toy stand-in reads as amateur.

**Hierarchy.** One hero per moment. Rank everything by size, contrast, colour, position and motion; the hero gets the boldest of these and everything else is demoted (smaller, lighter, slower, dimmed or removed). If two things compete for the eye, the frame has failed. Viewers skim, so the one key thing must survive a 1-second glance.

**Information order.** Reveal in the order the viewer needs it: context, tension, payoff. Never pre-announce the payoff (show the "before" state first and flip on the trigger word). Build complex ideas progressively, one new thing at a time. Put the key number or claim last in a build and let the support step back when it lands. The viewer reads at roughly 3 words per second on top of watching, so don't make them read what they don't need.

**Restraint.** Great motion design is mostly subtraction. No ambient filler without meaning (no floating shapes, particles or confetti "for balance"). Ambient texture, if any, is subliminal. Fewer, simpler elements read as premium; many elements read as cheap.

**One visual system.** A fixed palette, type pairing, corner radius, easing family and transition family used everywhere. Every scene, including contrast scenes (night, error, empty), carries the brand's colours so the piece reads as one object. Transitions are motivated by continuity (a shape becomes the next shape, a wipe in the direction of travel), not random.

**Craft.** Alignment on a shared grid and centre lines. Lockups optically aligned. Spacing consistent. Text readable (size, contrast, hold time long enough to read it aloud twice). Easing consistent: anticipation before a strike, overshoot and settle on arrival, exits quicker than entrances. Believable physics. Safe margins for the platform. Cameras and scale moves (zoom, push, pulse) only when they communicate something. Never as default filler.

**Tone fit.** Pick the register (calm premium, kinetic playful, urgent, authoritative) and keep every choice inside it: pacing, ease, colour, copy, music. Retail-promo cliches (starbursts, stamps, "SALE"-style badges, shouting colours) are wrong for a premium or trust tone.

**Sound is half the video.** A clear, well-mixed voice. Music with structure (a drop at the low point, a hit at the payoff). A sound for every meaningful action, and silence used on purpose. The video must work with the voice alone and with captions alone.

**Platform fit.** Aspect ratio, length, hook window, captions, safe areas, loop and CTA follow the delivery channel (see `video-formats`).

## 3. What makes it bad (smells)

Decoration with no meaning. Message, metaphor and style out of sync. Text where a visual belongs ("LYING." in big letters instead of a visibly broken number). A character that can't do its verb. Toy stand-ins for real things. Everything moving at once, or nothing ever settling. Uniform pacing. More than about five colours. Different design language scene to scene. Zoom or pulse as filler. Spoiling the reveal early. Labels that contradict the content (a "midnight" clock showing 11:47). Misaligned lockups. Unreadable or too-brief text. Claims with no proof. Features listed instead of outcomes. AI-sounding copy. A final frame that doesn't say what to do next.

## 4. Pre-render review (mandatory, in this order)

Render snapshots at every beat and inspect them. Fix violations before showing anything to the user.

1. **One-sentence test.** State the video's single message in one sentence. If you can't, the video isn't ready.
2. **Coherence.** Do message, metaphor and style agree in every scene?
3. **Verb and truth.** For each spoken claim, does the picture perform it? Do the numbers add up? Does every claim trace to the source?
4. **Hero.** Squint at each frame: is the hero obvious and the rest clearly secondary?
5. **Remove-it.** List every element that could go without losing meaning, and cut it.
6. **Order and leaks.** Is anything shown before its moment? Is the payoff the last thing in its build?
7. **System.** Palette, type, easing, transitions and audio vocabulary are consistent, including contrast scenes.
8. **Read time.** Is each text on screen long enough to read aloud twice?
9. **Mute test and audio-only test.** Does it make sense with sound off (captions) and with picture off (voice)?
10. **Craft pass.** Alignment, safe areas, clipped text, awkward seams, mix levels, loudness target.
11. **Platform test.** Does it match the format spec in `video-formats`?

## 5. Learning from feedback

When the user or anyone else critiques a video, don't patch only that video. Extract the principle behind the critique, state it generally, and add it to "Learned principles" below (one or two lines, no scene-specific detail). Keep the list short and general, merging duplicates. Never record literal quotes or one-off fixes.

### Learned principles
- A mismatch between what is said and what is shown is the most damaging flaw. Fix it by changing whichever side is weaker.
- Show a state change through the thing that changed (colour, shape, break), not through a label.
- The audience should never need to read the whole screen. Design for the one number or word that matters.
- Reveal order is part of the design: the cause before the effect, the "before" before the "after".
- A video is weakest at the joins between scenes. Check that the story, the visuals and the audio agree at each cut.
- Prefer motivated, designed motion over camera tricks. Don't use zoom in/out as a default effect.
- Align by layout, never by guessed pixel offsets: centre with flex or measured bounds, then check every centred element's rendered centre numerically (logo, headline, button) before delivering.
- Slow is a defect in sales video: cut every delay before the point (pre-roll, fades, waiting on exits), but give the payoff its full hold.
- When the brief leaves out style, platform, voice or CTA, ask once up front rather than guess; a guessed style is the main source of generic output.
- The voice is the hero of the mix. If any effect competes with it, the mix is wrong; measure voice and SFX stems instead of trusting the ear in a dense timeline. Cheap-sounding chimes are a tell; prefer weighty, warm, low sounds.
- Sound energy is judged as hard as visuals: a beautiful reel with a flat narrator fails. Match the voice's energy to the platform (energetic and varied for reels, calm authority for VSLs) and give the audio its own rewards (hits, ladders, drops).
