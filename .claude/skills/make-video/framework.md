# The Masterpiece Framework (from the owner's 7 reference reels, 2026-10-12)

Mandatory for every video, short or long, through `/make-video`. The goal is to look and sound like a professional editor made it, never like AI. Where this file and `editing-standard.md` disagree, this file wins (see §8). Brand overlays (§9) win over both.

Evidence labels: **[measured]** = ffmpeg/ebur128/scene-score/Whisper on the files; **[watched]** = read off frame-by-frame contact sheets. v1's transcript is only reliable to about 28s (Hinglish); its middle and end are judged from visuals.

## 0. The references

| # | What it is | Length, shape | What makes it work |
|---|---|---|---|
| v1 | Personal story (creator, Hinglish) | 97s 16:9 | Secret plus sacrifice hook, own phone footage of his real life, red slab type, a silence beat before the climax, "is your story worth telling?" |
| v2 | Talking head, "30 reasons your site looks vibecoded" | 33s 9:16, one shot | Pure utility, a numbered list that fills as he talks, example cards pop beside each item, save bait "give this to claude/chatgpt" |
| v3 | Editing agency ad | 12s square | Frosted light UI, text resolving out of blur, a search bar typing the viewer's own question, "Apply" morphs into "Booked" |
| v4 | Poetic brand piece | 20s 4:3 | Pixel icon loop on paper texture, heat-map silhouettes, music led, only 4 spoken lines with long air |
| v5 | AI news explainer (AirLLM) | 28s 9:16 | Clay diorama with a mascot, a taped headline per beat, a rolling star counter, $0.0x vs $0.00 cards, "comment AIR" |
| v6 | Documentary on one person's motive | 76s 16:9 | Paradox hook, a "they said / he did" ladder, 0.47s montage, serif italic captions, film grain, a scale comparison, a callback ending |
| v7 | Confession (feeling behind on AI) | 68s 9:16 | Monochrome line-art windows with one red accent, one continuous camera with no hard cuts, repeated stacked words, a self twist, a question CTA typed into an input box |

## 1. The five senses (my framework, not an industry standard)

A screen reaches only two senses directly: sight and hearing. A professional edit makes the viewer *feel* the other three through cues. Every video must hit all five on purpose.

| Sense | How the edit reaches it | Shown in |
|---|---|---|
| **Sight** | One visual world, one accent colour, one idea per frame, the frame changes state every 1.5 to 3s | v7 (mono plus red), v5 (clay set), v6 (grain plus serif) |
| **Hearing** | The voice leads, music never stops being felt, a sound for every action, silence as a weapon | v7 (big dynamic range), v1 (drop before the climax), v5 (dense ticks and pops) |
| **Touch** | Texture and weight: film grain, paper, clay, glass, vignette; impacts with low end; objects that land, bounce, settle; foley (taps, paper, keys) | v4 (paper, pixel), v5 (clay, tape), v6 (grain, retro TV) |
| **Taste and smell** | Evoked through **specific real details that trigger memory**: a childhood photo, a city street at night, a phone screen at 2am, Central Park. Specific beats generic every time | v1 (childhood photos, his room, train, family), v6 (Central Park scale), v7 (one window, one blinking cursor) |
| **The gut (what the four add up to)** | One emotion per video, named before scripting: envy, fear of missing out, vindication, relief, awe | v7 (shame then honesty), v6 (defiance), v1 (sacrifice then rebirth) |

Rule: write the target for each sense into `CONCEPT.md` before the script. If a sense has no plan, the video is not ready to build.

## 2. The hook (first 1.5s)

- Words on screen and voice from the first frame. No logo, no fade from black, no greeting. In all 7, speech starts within about half a second **[watched]**.
- The first line is one of these seven proven shapes:
  1. **Paradox question:** "X has everything. Then why is he spending billions on this one building?" (v6)
  2. **Confession:** "I use Claude every day, and every day I feel more behind." (v7)
  3. **Secret with stakes:** "At 17 I learned this universe has a dark secret." (v1)
  4. **Number plus utility:** "30 reasons your site looks vibecoded." The full list is visible from frame 1 (v2)
  5. **The viewer's own question:** "Still looking for an editor?" (v3)
  6. **Big question, quiet answer:** "How do you show you're changing? You don't." (v4)
  7. **Surprising fact plus proof number:** "Someone open sourced X and it's already past 35,000 stars." (v5)
- The hook visual moves fast even when the video later slows: v6's first 3s holds about 10 different images, one per word or two **[watched]**.
- Within 3s, open a loop the viewer needs closed: a why, a twist, a list to finish, a number to land.

## 3. Story spines (pick one per video)

| Spine | Beats | Ref |
|---|---|---|
| **Motive documentary** | Paradox → origin sentence → quote → "this isn't about X" reframe → "They said A. He did it" ×2 → scale proof → the real inner motive → callback to the origin line | v6 |
| **Confession** | Admit the feeling → "somebody, somebody, somebody" comparison → the hidden truth nobody says → twist on yourself → no fake fix → a question to the viewer | v7 |
| **Transformation** | Secret plus stakes → twist (the sacrifice is me) → years of struggle montage → silence beat → the new self → "is your story worth telling?" | v1 |
| **News explainer** | Fact plus proof number → name it → one everyday analogy (a book read one page at a time) → bigger proof → who it is for → comment keyword | v5 |
| **Utility list** | Promise plus count → rapid items with a visual per item → save or follow ask | v2 |
| **Question → show** | Viewer's question → short answer → show it working → one action | v3, v4 |

Every spine has one **turn** (a reframe or twist) in its middle third, and one **callback** at the end that echoes the hook.

## 4. Visual world (this is what makes it look professional)

- **One world per video, held from first frame to last.** Pick a material and keep it: line-art windows (v7), clay diorama (v5), pixel on paper (v4), film documentary (v6), frosted glass UI (v3), slab type plus phone footage (v1). Never a different template per scene.
- **One accent colour that means something.** v7's only colour is the red AI character, so your eye always finds it.
- **Captions belong to the world.** v5 uses paper tags, v6 serif italic with a glow, v7 typed system text, v1 small word pops. Never default subtitle styling.
- **Caption beats are 1 to 3 words**, synced to the word, and placed where the eye already is.
- **Repetition as design:** stacking "somebody. somebody. somebody." (v7) and the "They said" card (v6) turn a sentence into a visual rhythm.
- **Scale and comparison made physical:** 100M sq ft shown as blocks next to Central Park (v6), $0.0x vs $0.00 cards (v5), a star counter rolling 0 to 35,988 (v5).
- **A quirk in every video:** one specific, slightly odd, human element the viewer remembers. Examples: the mascot (v5), the scrawled "17" (v1), "loser" typed in red (v7), the retro TV (v6). Without the quirk it is just competent.
- **Human texture over clean perfection:** grain, vignette, paper, slight imperfection, real phone footage. Perfect gradients and glossy cards read as AI.
- **Real over generated:** own footage, real photos, licensed stock, hand-built illustration and motion graphics. **No AI-generated images or video**, even though v1 and v6 use some. Get the same effect from real photos styled into one look.

## 5. Pacing (measured)

| Mode | Measured in refs | Rule |
|---|---|---|
| Montage (story, documentary) | median shot 0.47s (v6), 1.22s (v1), 0.77s (v4) **[measured]** | 0.4 to 1.3s per shot, faster in the hook and in lists, slower on the key line |
| One-take motion design | 0 hard cuts in 68s (v7), 1 in 12s (v3) **[measured]** | No cuts needed if the camera and elements keep travelling and the frame changes state every 1.5 to 3s |
| Talking head | 1 shot for 33s (v2) **[measured]** | Allowed only when the overlay does the work: a filling list, popping examples |

**Voice rate [measured, rough, from Whisper]**

| Use | Words per second |
|---|---|
| News, explainer, list | 3.0 to 4.3 (v5 4.3, v2 about 3.0 to 4.0) |
| Story, documentary | 3.3 to 3.5 (v6 3.44, v1 3.27) |
| Confession, intimate | about 2.7 with many short breaths (v7) |
| Poetic, brand | about 1.6 with long air (v4) |

Rate must **vary inside the video**. Every ref moves between about 2 and 4.5 words per second across 3s windows. A flat rate is a defect.

## 6. Sound

- **Loudness [measured]:** all 7 sit at -13.8 to -14.5 LUFS integrated. Social masters go to **-14 LUFS, true peak -1 dBTP or lower**. YouTube and the site stay at about -16.
- **Music is always under the story**, carved under the voice and shaped to it: it drops out before the reveal and hits on the turn.
- **Silence is a beat.** v1 drops to about -38 dB for a second on a black frame before the climax line **[measured]**. v7 runs about 33 dB of dynamic range: quiet confession, then a lift **[measured]**. Use one deliberate silence per video.
- **Dense, tactile foley in explainers:** v5 is busy and tightly compressed (about 11 dB range) **[measured]**. Pops, ticks, paper, taps on every element.
- **Story pieces breathe:** wider dynamics, fewer but heavier hits.
- **Every action has a sound.** The voice stays at least 7 to 8 dB above SFX during speech (the existing measure-the-stems rule stands).

## 7. Endings

- Close the loop opened in the hook, ideally with a **callback** line (v6: "not the guy who says five years").
- **One action**, matched to the platform:
  - a question that invites a comment (v7: "What do you feel behind on?", typed into an input box)
  - a comment keyword (v5: "comment AIR")
  - save or follow (v2)
  - book (v3)
- Then a short handle or logo sting (v1, v2, v6), or a loop back to frame 1.

## 8. What this changes in the existing rules

| Old rule (`editing-standard.md`, `short-form-video`) | Now |
|---|---|
| "Visual change every 1.5 to 3s" (implied cuts) | The **frame changes state** every 1.5 to 3s. Cuts are optional (v7). Montage mode cuts every 0.4 to 1.3s |
| Captions "4 to 7 words a line" | **1 to 3 word beats**, styled to the video's world |
| Reel voice 3.0 to 3.4 wps | Story 3.3 to 3.5, explainer up to 4.3, confession 2.7, always varied |
| Social master "about -14" | **-14 LUFS, -1 dBTP**, confirmed by all 7 refs |
| (missing) | Five-senses plan, one visual world, one quirk, one silence beat, a callback ending |

## 9. DUXIO overlay (wins on any conflict)

- Look: Apple dark (obsidian, white, violet accent, Plus Jakarta Sans). The "one world" is DUXIO's glass-and-dark world, and the quirk lives inside it.
- Spines that fit DUXIO best:
  - Confession (in the coach's voice: "I had 40 DMs and booked 2 calls")
  - Motive documentary (why leads go cold)
  - News explainer (the HBR stat)
  - Question → show (the follow-up running)
- CTA in videos is "Book a Strategy Call". The comment keyword is allowed in reels once the comment-to-DM automation exists.
- Never in videos: prices, client results, guarantees, scarcity, AI imagery, or any dash in customer-facing text.
- Specifics for taste and smell come from the coach's real world: the phone at 11pm, the DM left on read, the calendar with gaps.

## 10. Pre-build checklist (add to `CONCEPT.md`)

1. Hook shape (one of §2) and the first-frame visual.
2. Spine (§3), its turn and its callback.
3. The world: material, accent colour, caption style.
4. The quirk.
5. The five senses: one line each.
6. Pacing mode (montage, one-take or talking head) and the voice rate per section.
7. Silence beat placement, and the music shape (drop, turn, hit, end).
8. The single action at the end.
