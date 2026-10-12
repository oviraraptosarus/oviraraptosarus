# Owner rules and mistake log (read this first, every session)

The owner (VRK) runs more than one channel: DUXIO now, faceless content in other niches soon, and maybe a YouTube automation channel. The look, topic, voice and ending change per video. Nothing is assumed from the last video.

## 1. Ask like a curious kid, every single video
Before any new video, send **one message with all questions in plain text. No popups.** Short questions, plain words. Never skip it, never reuse last video's answers without saying "last time you said X, same again?". Questions to cover, skipping only what the owner already said in this message:

1. Which channel or niche is this for? (DUXIO, another niche, a new one)
2. What is the topic, and who is it for?
3. What should they feel at the end? What should they do? (the ending changes by channel: DUXIO ends on its own call to action, others differ)
4. Length (reels under 60s; longer for YouTube)
5. Which reference look to copy: v1 slab-type story, v3 frosted UI ad, v4 pixel on paper, v5 clay diorama, v6 documentary, v7 line-art windows, or a new one they send
6. Mascot or character? If yes, what is it like?
7. Voice (female `af_heart`, male, or none) and voice energy
8. Captions? What style?
9. Music: do they have a track? If not, the licensed library
10. Where the pictures come from: they download the best images, or footage they supply, or I draw vector art. **I never use AI generated images or video**
11. On camera or faceless? (most content is faceless)
12. Anything they hate, or want to copy from something they saw?

Be honest about anything missing. Never invent answers.

## 2. Missing data goes in NEEDS-FROM-OWNER.md and I remind them
`NEEDS-FROM-OWNER.md` lists what I can't do without them. At the start of every video job I show the open items in 2 to 4 lines and ask again. I only remove an item when they give it. Never say "TBD" and carry on silently.

## 3. Cost and speed: stop stalling
The owner has seen a full video cost about $4 with a strong result. That is the bar: **do the work, don't stall.**
- No more than one round of questions, then build.
- Don't measure, transcribe or re-render things that don't change a decision.
- No renders before the concept card is approved. One render, one check, deliver.
- No subagents unless the job needs them. Never fan out many agents for a short reel.
- Don't narrate options, don't re-explain, don't write long reports. Short answer first.
- Don't redo a delivered video unless asked. "Don't redo it" means don't.
- Concept card first, kept short. Wait for approval, then build.

## 3b. Keep the files current
After every step, update `CONTEXT.md` before replying. Log new mistakes in §5 as they happen. Update `NEEDS-FROM-OWNER.md` whenever an item opens or closes. Each brand has a `DESIGN.md`.

## 3c. Feedback becomes a rule, immediately (from the Christian Peverelli walkthrough, 2026-10-12)
Every note the owner gives on a video is written into the right file in the same turn: a numbered rule in the matching skill (`make-video/framework.md`, `editing-standard.md`, a brand `DESIGN.md`) or a line in §5. Say "saved as rule N" in one short line. Start with small clips (the hook first), tune the sound on its own, and keep a library of reusable reel elements (animations, characters, scenes) that grows each time one is used. Use the strongest model for setup and planning, a cheaper one for routine builds.

## 3d. The owner supplies the assets, I always ask (2026-10-12)
Visuals, images, footage, screenshots, music, logos and similar assets come from the owner: "ill provide them no worries". For every video I name exactly which assets the concept needs (a short list with a size or shot description each) and ask for them in the same one-message question round. I never invent, scrape or silently source them, and never use AI generated images or video. If an asset is missing I build the rest and flag the gap in `NEEDS-FROM-OWNER.md`. Where the owner sends nothing, I may only draw simple vector art in code and say so.

## 3e. Several videos at once: framework first, no test videos (2026-10-12)
The owner wants to make many videos, in one session or several. Build the process before any video: `edits/duxio-reel-kit/BATCH.md` (batch intake table in one message, JSON specs, `kit/make.py` and `kit/batch.py`, worktrees for parallel sessions). Do not render test videos to prove tooling; verify with syntax checks, compile comparisons and `hyperframes check`, and let the first real batch exercise the rest. The owner pays for time and session limit, so say plainly what is verified and what is not.

## 4. Quality bar
- Output must look like the 7 reference reels: layered, textured, one world, a character or recurring object, a travelling camera, sound on every action. A reel made only of text and boxes on a dark gradient is rejected. See `.claude/skills/make-video/visual-breakdown.md` and `framework.md`.
- Built for the Instagram algorithm: strong hook in the first second, short pacing, a reason to watch to the end. Not a stack of slides.
- The result must not look AI made. Real, specific details beat generic ones.

## 5. Mistake log (add a line after every owner reaction)
- 2026-10-12 · Reel "Dots That Stopped": reused an old concept and the existing kit, delivered flat UI cards on dark. Rejected. The reference videos barely influenced the look.
- 2026-10-12 · Spent session budget on analysis, measuring and a render before asking the owner anything. The owner wants questions first and a cheap, fast build.
- 2026-10-12 · Showed a popup question round. The owner wants all questions in one plain message.
- 2026-10-12 · Reel "cold-call-ai" framed DUXIO mostly as answering and following up leads. Owner: sell the outcome (more money, better lead quality, other industry pains), not just saving leads. Saved as `duxio-brand` §0 (and pre-flight check 8).
- 2026-10-12 · Reel "cold-call-ai" v1 was giant text only. Owner liked their earlier 59s `duxio-reel` (Apple style UI elements, Inter + Instrument Serif italic) better and asked for visual elements instead of text like "2 AM", gradient only on highlight words, more premium fonts, and questions that sound like questions. Saved as `brand/duxio/DESIGN.md` "Reel look, owner rules" 1 to 5 and the `ap` scene.
- 2026-10-12 · Owner reminded me: always ask them for visuals and other assets (they will provide). Saved as rule 3d.
- 2026-10-12 · Assumed DUXIO and a 10 second format. The owner's content varies by niche; ask every time.
