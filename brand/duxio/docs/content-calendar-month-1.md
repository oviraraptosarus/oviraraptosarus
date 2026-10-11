# DUXIO content calendar, month 1 (Oct 12 to Nov 15, 2026)

This builds on `content-strategy.md` and uses the brief already on file:
- brand new pages
- faceless with a voiceover
- 5 reels a week plus 1 YouTube video
- no ads, so the reach comes from pain point content edited to hook the fast scrolling crowd

Skills behind each layer of this plan:

| Layer | Skills |
|---|---|
| Month and series story | `storyteller` |
| Every line of copy (written, then run through all seven sweeps and the AI tell check) | `copywriting`, `copy-editing` |
| The character, the beat sheet and the audio pipeline | `story-motion` |
| Reel motion | `hyperframes:motion-graphics`, `hyperframes-animation` |
| Pose ladders, match cuts and masks | `hyperframes-keyframes` |
| The four YouTube videos | `hyperframes:faceless-explainer` |
| House rules | `duxio-brand`, `duxio-vsl`, `make-video` |

**Pre-flight passed on all customer-facing text:**
- zero dashes
- CTA is "Book a Strategy Call", and nothing is offered free
- no price and no "5 spots"
- no client results
- every mock DM, time and number is labelled "Example"
- claims come only from `duxio-brand` §7

---

## 1. The month as one story

The month is one serialized story. Followers who watch week 1 come back to see how it ends.

| Week | Act | Theme | What the viewer should feel by Friday |
|---|---|---|---|
| 0 (Oct 12 to 18) | Prep | Pages, backend, bank of videos | (nothing published except 3 pinned posts on Sat) |
| 1 (Oct 19 to 23) | Act 1: the wound | **Dot goes cold.** Where coaching sales leak | "That's me. I lose people like this." |
| 2 (Oct 26 to 30) | Act 2a: the stakes | **What cold costs.** Math and bad follow up | "This is costing me real money." |
| 3 (Nov 2 to 6) | Act 2b: the fix | **60 seconds later.** The four steps, one per day | "So that's how it should work." |
| 4 (Nov 9 to 13) | Act 3: the return | **Dot books.** Objections, fit, the call, the payoff | "I want this running for me. Book the call." |

**Dot, the recurring character (`story-motion`)**
- Dot is the lead. Every coach knows Dot: someone who asked about the program and waited.
- A character makes a dry B2B topic watchable for the fast scrolling crowd. Coaches see their own lost buyers in Dot.
- Physical form:
  - a small violet DM bubble (`#6F00FF`, glow `#B794FF`)
  - two dot eyes
  - nothing else: no mouth, no limbs, in keeping with the brand's no-blobs look
- Dot appears in about half the reels. The fix and objection reels lean on UI and type.

| State | Look | Keyframes (pose ladder, one wrapper, seek-safe) |
|---|---|---|
| Warm | violet fill, soft glow | idle breathe `scale 1 → 1.02`, every 1.2s; blink every 2.5 to 4s (uneven) |
| Waiting | violet, glow dims 40% | eyes glance at the clock (`x` of the eye group ±6px); breathe slows |
| Cold | fill tweens to `#5B5B66`, glow off, frost specks on the rim | `scale 1 → 0.86` over 0.5s `power2.inOut`; shiver `x ±2px` as a 6-step deterministic keyframe ladder over 0.36s |
| Saved | re-saturates with a light sweep across the bubble | `back.out(1.5)` pop to 1.05, settle to 1; eyes open wider (`scaleY 1 → 1.2 → 1`) |

**Villains (a physical verb each)**
- **The Clock** (status bar time) rolls forward.
- **Seen** stamps down on Dot.
- **The Pile** (an unread badge with stacked bubbles) buries Dot.
- **The Empty Chair** is a call tile with nobody in it.

**Hero**
- The backend is the same single line of violet light used in the VSL.
- It always reaches Dot in under 60 seconds and warms them back up.
- Week 3 pays off week 1's wound, and R20 replays R1 with the line in place.

## 2. Motion and sound system for every reel

- **Canvas and type:**
  - 1080×1920, obsidian `#0D0E12`
  - Plus Jakarta Sans 800 at -0.03em
  - support text `#9A9AA5`
  - one Instrument Serif italic word per reel at most (the emotional word)
  - safe area: the centre 900×1400
- **Frame 0 is the hook.** Text and sound are already on screen, with no fade in. The first visual change comes by 0.8s, then a new visual every 1.5 to 2.5s.
- **Easing family:**
  - Entrances: `expo.out` over 0.45s.
  - Landings: `back.out(1.4)`.
  - Exits: `power2.in` over 0.25s.
  - Moves: `power2.inOut`.
- **Transitions:** use match cuts and masks only.
  - An iris `clip-path: circle()` collapses from a full-screen colour into Dot.
  - A mask wipe moves in the direction of travel.
  - Dot becomes a node on the four-step track.
  - No zoom filler. A punch-in is allowed only on a reveal: one wrapper, a set or a 0.2s tween.
- **Counters roll like slot reels.** They decelerate (`power3.out`) and land on the exact number. Use the `apple-money-count` registry block or `rules/counting-dynamic-scale`.
- **Lines draw on** (`rules/svg-path-draw`) and checks draw on.
- **Captions:** 2 to 4 words, with an active-word pop, hidden where the headline already says the line.
- **Voice:** energetic female via ElevenLabs (stability 30 to 45, style 25 to 45, speed 1.05 to 1.15). Kokoro `af_heart` is the fallback.
- **Sound:**
  - `hookhit` plus air at frame 0.
  - About 1 SFX per second from `brand/duxio/sfx/`.
  - SFX sit 7 to 8 dB under the voice, measured with stems.
  - No chimes; use wooden plucks for ladders.
  - Music 14 to 18 dB under the voice, 110 to 130 BPM.
  - Master to -14 LUFS.
- **End and loop:** the last frame matches the first.
- **CTA rotation:**
  - "Comment REPLY": our backend answers in under 60s, as a live demo.
  - "Send this to a coach who…": builds reach.
  - "Book a Strategy Call. Link in bio.": converts.

Each reel's Instagram caption follows the same pattern. The first line repeats the hook, then 1 or 2 lines of payoff, the CTA, and 4 hashtags from this set: `#coachingbusiness #highticketcoaching #onlinecoach #salesforcoaches #businesscoach #consultingbusiness`.

---

## 3. Week 0: prep (Oct 12 to 18)

| Day | Task | Who |
|---|---|---|
| Mon 12 | Instagram professional account, Facebook page linked, YouTube channel created. Name field `DUXIO | Follow Up for Coaches`, bio and avatar from `brand/duxio/logo/social/` | Owner |
| Mon 12 | Pick or design the energetic female ElevenLabs voice for reels (one voice for the whole month) | Owner |
| Tue 13 | **Our own backend on our own page:** comment keyword REPLY, DM within 60s, three questions, 21 day follow up, booking link. Every CTA depends on this | Owner + backend |
| Tue 13 | Add the real booking link (still missing from the brand kit) | Owner |
| Wed 14 to Fri 16 | Build the Dot rig once as a reusable HyperFrames component. Build the 3 pinned posts. Build R1 to R5 and YT1 | Claude |
| Sat 17 | Publish the 3 pinned posts (P1, P2, P3) so the grid isn't empty when R1 lands. Upload VSL v4.1 to YouTube as the channel trailer | Owner schedules |
| Sun 18 | Approve week 1. Schedule it in Meta Business Suite and YouTube Studio | Owner (30 min) |

**Pinned posts**
- **P1 · VSL cutdown, 75s, 9:16.** A restack of `edits/duxio-vsl-v4/`, reframed by restacking the layout, never by cropping. VO is the calm male voice from the VSL. Hook: "Every coach lost sales this month."
- **P2 · How it works in 4 steps, 25s.** The four-node track fills. On screen:
  1. "Every lead gets an answer."
  2. "Serious buyers get sorted."
  3. "21 days of follow up and reminders."
  4. "Quiet leads reopened."

  End card: "Book a Strategy Call. Link in bio."
- **P3 · Who this is ideal for, 20s.** Uses R18's script below.

---

## 4. The 20 reels

Format for each: hook on screen at frame 0 · VO (word for word) · story beat · visual and motion · sound · CTA · Shorts title.

### Week 1 · Dot goes cold (the Leak)

**R1 · Mon Oct 19 · "The 3 hour reply" · about 15s**
- **Frame 0:** an iPhone lock screen. Dot arrives as a DM notification: "Hey, how much is your coaching?" Label: Example.
- **VO:** "Someone just asked about your coaching. You were on a call. You replied three hours later. They had already booked with someone else. This is where most coaching sales leak out."
- **Story:** opens in the middle of the action. Dot is warm, waits, then goes cold.
- **Motion:**
  - The notification springs down (4% squash, settle).
  - The status bar clock rolls 2:14 → 5:14 like a slot reel, decelerating.
  - Dot glances at the clock, then runs the full cold ladder.
  - "Seen" stamps down (scale 3.5 → 1, rotate -6°).
  - On "leak", an iris collapses onto the grey Dot.
- **Sound:** `hookhit` + `haptic` at frame 0, `ping`, rolling ticks, a low `thud` on cold.
- **CTA:** "Send this to a coach who replies at midnight."
- **Shorts title:** Why coaching leads go cold in your DMs

**R2 · Tue Oct 20 · "The Pile" · about 16s**
- **Frame 0:** a red unread badge reading "41".
- **VO:** "Forty one unread messages. One of them is ready to buy. You'll find it on Sunday. They found another coach on Thursday. Your next client might already be in your inbox, waiting for an answer."
- **Story:** the villain buries the hero.
- **Motion:**
  - The badge rolls 12 → 27 → 41 (two decelerating reel spins, a 3% overshoot on each land).
  - Bubbles stack into a column. Dot is in the middle with a violet glow and gets pushed down as new bubbles land.
  - A calendar chip flips Thu → Sun (rotationX card flip).
  - Dot's glow fades under the pile.
- **Sound:** a tick per badge step, soft `card-place` per stacked bubble, `switch2` on the flip.
- **CTA:** "Follow for the fix."
- **Shorts title:** 41 unread DMs and one of them was a client

**R3 · Wed Oct 21 · DM Rewrite: "The worst first reply" · about 18s**
- **Frame 0:** a chat bubble reading "Check the link in my bio." under a red "Worst first reply" label.
- **VO:** "Someone asks how your coaching works. You send: check the link in my bio. They never click. A better first reply is about them. What made you look into this right now? One question keeps the conversation going. Comment REPLY and see how fast we answer you."
- **Story:** a before and after, with Dot reacting.
- **Motion:**
  - Bad reply: Dot's eyes half close (`scaleY 1 → 0.4`) and Dot drifts off frame left.
  - A red strike draws through the bubble (`svg-path-draw`).
  - Mask wipe right. Typing dots, then the good reply lands with `back.out`.
  - Dot slides back in and leans forward (`rotation 4°`, `scale 1.04`).
  - All DMs are labelled Example.
- **Sound:** `drop_002` on the bad reply, a `swish` strike, `keypress` patter, `send`.
- **CTA:** Comment REPLY.
- **Shorts title:** The worst first reply a coach can send

**R4 · Thu Oct 22 · "The Empty Chair" · about 16s**
- **Frame 0:** a video call tile with an empty chair, and a timer reading 00:07.
- **VO:** "They booked the call. Then they didn't show. Usually they just forgot. A call booked days out needs reminders. Twenty four hours before. Two hours before. Ten minutes before. Send this to a coach staring at an empty call."
- **Story:** a near miss, then a rewind.
- **Motion:**
  - The timer rolls 00:07 → 10:00 (waiting).
  - `rewind.wav` plays while the timeline visibly scrubs back: a fast reverse of the same keyframes, with a VHS-free white flash line.
  - Three reminder notifications stack (24h, 2h, 10m), each landing on its spoken word.
  - Dot pops into the chair as Saved.
- **Sound:** a clock `tick` bed, `rewind`, `tap1` to `tap3` on a rising wooden pluck ladder, `join`.
- **CTA:** "Send this to a coach staring at an empty call."
- **Shorts title:** Why your sales calls don't show up

**R5 · Fri Oct 23 · "The 1 hour rule" · about 18s**
- **Frame 0:** a huge "7×" in white with "Harvard Business Review, 2011" in small grey type.
- **VO:** "Harvard Business Review studied how fast companies answer new leads. The ones who tried within an hour were nearly seven times as likely to qualify that lead. Wait a full day, and the odds drop more than sixty times. Most coaches answer when they get a free minute. Follow, so you catch part two."
- **Story:** the evidence that makes week 1 real.
- **Motion:**
  - A horizontal time bar draws 0h → 1h → 24h.
  - At 1h, "7×" rolls 1 → 7.
  - At 24h the bar turns red and "60×" rolls in with a low `thud`.
  - Dot sits at the start of the bar and freezes cold at 24h.
- **Sound:** a `riser` along the bar, `land` on 7×, `hookhit` (at 0.4 volume) on 60×.
- **CTA:** Follow.
- **Shorts title:** The 1 hour rule for coaching leads (Harvard study)

### Week 2 · What cold costs (Coach Math and DM Rewrite)

**R6 · Mon Oct 26 · Coach Math: "80 messages" · about 18s**
- **Frame 0:** a grid of 80 small dots and the line "80 people messaged you."
- **VO:** "Say eighty people message you this month. You answer the quick ones. The rest wait a day. If one or two of them were ready for a three thousand dollar offer, that's three to six thousand dollars sitting in your inbox. Example. Your numbers will vary. Comment REPLY and feel what a fast answer is like."
- **Motion:**
  - The 80 dots fill row by row (`stat-bars-and-fills`, staggered 0.012s).
  - Most dots go grey in a wave. Two stay violet and glow.
  - A money counter rolls $0 → $6,000 with coin ticks that slow, then a register land and a 7% pop.
  - Label: "Example. Just an estimate."
- **Sound:** soft taps for the fill, `coin` ticks slowing down, `cash`.
- **CTA:** Comment REPLY.
- **Shorts title:** What 80 coaching DMs are really worth (example math)

**R7 · Tue Oct 27 · DM Rewrite: "Rating follow ups" · about 17s**
- **Frame 0:** a follow up bubble reading "Just checking in!" with a score dial.
- **VO:** "Rating coach follow ups. Just checking in. Two out of ten. It asks for their time and gives them nothing. Saw this and thought of you, with a short video that answers their exact question. Eight out of ten. Every follow up should give something before it asks. Send this to a coach who just checks in."
- **Motion:**
  - The score dial spins like a slot reel and lands on 2 (red), then later on 8 (violet), each with a 4% overshoot.
  - The second bubble shows a play-button thumbnail.
  - Dot reacts: bored at 2, leans in at 8.
- **Sound:** reel ticks, `land`, `drop_003`.
- **CTA:** Send.
- **Shorts title:** Rating coach follow up messages

**R8 · Wed Oct 28 · POV: "On a client call" · about 15s**
- **Frame 0:** "POV: you're coaching a client" over a split screen.
- **VO:** "You're coaching a client. Your phone buzzes four times. Each one is someone asking about your program. You can't answer for an hour. By then, two of them have gone quiet. That hour is the one we cover. Book a Strategy Call. Link in bio."
- **Motion:**
  - Left: a calm call tile with a running timer.
  - Right: a phone where four notifications stack, each a mini Dot.
  - Two go cold and drift off the top.
  - On "we cover", the violet line sweeps across the phone and catches the two before they leave (they re-saturate).
- **Sound:** `haptic` ×4 at uneven spacing, a low thud when they go cold, a light `swish` with a `confirm2` at 0.3 volume as the line catches them.
- **CTA:** Book a Strategy Call.
- **Shorts title:** POV: four leads message you mid call

**R9 · Thu Oct 29 · Leak: "Before you spend more on ads" · about 17s**
- **Frame 0:** an ad spend counter climbing in red.
- **VO:** "Before you spend more on ads, scroll back through last month's messages. Count the people who asked a question and never heard from you after the first reply. They already raised their hand. Following up with them costs you nothing extra. Follow to see how we do it."
- **Motion:**
  - The spend counter climbs, then hard stops.
  - A mask wipe downward reveals a DM list scrolling (one wrapper, `y` travel, with `ease: "none"` during the scroll and `power2.out` to stop).
  - Each forgotten conversation gets a small raised-hand icon. A tally counter rolls to the final count.
  - Label: Example.
- **Sound:** a cash-register tick per spend step (low volume), a scroll `swish`, `tap` on each hand.
- **CTA:** Follow.
- **Shorts title:** Check your DMs before you spend more on ads

**R10 · Fri Oct 30 · Coach Math: "One saved sale" · about 15s**
- **Frame 0:** "1,000 new followers" next to a weightless counter.
- **VO:** "A thousand new followers feels good. One saved sale pays you. At a three thousand dollar offer, one lead you would have lost is three thousand dollars back. Example. Just an estimate. Fix the follow up before you chase more reach. Send this to a coach chasing followers."
- **Motion:**
  - The follower counter spins 0 → 1,000 fast and floats up like a balloon (`y -40`, slight sway).
  - One violet coin drops onto a balance scale. The scale tips hard (`rotation`, `back.out`), with squash on the coin as it lands.
- **Sound:** a fast tick roll, a light `whoosh`, `coin`, then a heavy `thud`.
- **CTA:** Send.
- **Shorts title:** One saved sale vs 1,000 followers

### Week 3 · 60 seconds later (the Fix, one step a day)

The four-node track (01 Answer · 02 Sort · 03 Follow up · 04 Reopen) stays at the top of every week 3 reel and fills one node per day. This is the open loop.

**R11 · Mon Nov 2 · Step 1: "Every lead gets an answer" · about 17s**
- **Frame 0:** a cold grey Dot with a ring timer at 0:00.
- **VO:** "Step one. Every lead gets an answer in under sixty seconds. On Instagram, on your form, by email. Even while you sleep or coach. It's written in your voice, and you approve every message before anything goes out. Comment REPLY and time us."
- **Story:** the hero arrives. The violet line reaches Dot and Dot warms up. This pays off R1.
- **Motion:**
  - The ring timer rolls to 0:42 and lands (Example).
  - The reply bubble lands with a delivered check that draws on.
  - Dot goes through the full Saved ladder.
  - Node 01 fills.
- **Sound:** `rtick` slowing down, `land`, `send`, a soft wooden pluck.
- **CTA:** Comment REPLY.
- **Shorts title:** What should happen 60 seconds after a lead DMs you

**R12 · Tue Nov 3 · Step 2: "Serious buyers get sorted" · about 17s**
- **Frame 0:** three chips: Goal · Situation · Timing.
- **VO:** "Step two. Three short questions. What do you want, where are you now, and how soon do you want it fixed. Not ready yet? They get pointed to your free content. Serious? They get a time on your calendar, and you get a text."
- **Motion:**
  - The chips check in turn on a rising wooden pluck ladder (C4 · E4 · G4).
  - Two dots split along forked paths (path travel, `ease: "none"`): a grey dot to a folder, and Dot to a calendar slot that locks with a 3% overshoot.
  - A phone buzzes with "Someone serious just came in."
  - Node 02 fills.
- **Sound:** plucks, a low slide, `click3` lock, `haptic`.
- **CTA:** Follow.
- **Shorts title:** 3 questions that sort buyers from browsers

**R13 · Wed Nov 4 · Step 3: "21 days of follow up" · about 18s**
- **Frame 0:** a 21 day timeline with Day 1 reading "Not yet".
- **VO:** "Step three. Plenty of people need more than one conversation before they book. So for twenty one days they get short, helpful check ins. Then reminders twenty four hours, two hours and ten minutes before the call. We write every message. You write none of it."
- **Motion:**
  - The 21 day line draws on (`svg-path-draw`).
  - Pings ripple at Day 3, 7, 14 and 21.
  - A calendar invite lands "Booked".
  - Three reminder chips stack, then "Joined" turns green.
  - Node 03 fills.
- **Sound:** four soft pings rising, `card-slide`, taps, `join`.
- **CTA:** "Send this to a coach who gives up after one message."
- **Shorts title:** 21 days of follow up you never have to write

**R14 · Thu Nov 5 · Step 4: "Quiet leads reopened" · about 15s**
- **Frame 0:** a dusty grey card reading "Day 60".
- **VO:** "Step four. Someone told you not yet, two months ago. Once a month, they get a short, human check in. Hey, are you still looking to solve this? Some of them were waiting for someone to ask. Follow for the full system."
- **Motion:**
  - Dust specks drift off the card as the message sends.
  - The card relights grey → violet with a light sweep.
  - The reply "Yes. Can we talk?" lands (Example).
  - Node 04 fills, and the whole track glows once.
- **Sound:** `send`, a warm low pad swell, a pluck.
- **CTA:** Follow.
- **Shorts title:** How to reopen leads who went quiet

**R15 · Fri Nov 6 · "All four in 20 seconds" · about 20s**
- **Frame 0:** the full track lit, plus the line "The whole backend in 20 seconds."
- **VO:** "Every lead gets an answer. Serious buyers get sorted. Twenty one days of follow up and call reminders. Quiet leads reopened. We build it inside your own accounts, we run it daily, and it's live in under forty eight hours. Book a Strategy Call. Link in bio."
- **Motion:**
  - Dot rides the violet line through all four nodes. Each node pops as Dot passes, as a match cut from node to node.
  - Logo hit at the end, using `duxio-wordmark-parts.svg` with the X arms snapping in.
- **Sound:** a `pulse` bed, a pluck per node, `bighit` on the logo.
- **CTA:** Book a Strategy Call.
- **Shorts title:** The follow up system for coaches in 20 seconds

### Week 4 · Dot books (objections, fit, the call, the payoff)

**R16 · Mon Nov 9 · "Will it sound like a robot?" · about 15s**
- **Frame 0:** a stiff grey bubble reading "Hello. Thank you for your inquiry." with a robot icon.
- **VO:** "Will this sound like a robot talking to your people? Every message is written in your voice. You read and approve all of it before anything goes out. Your reputation stays yours. Comment REPLY and judge our replies yourself."
- **Motion:**
  - The robot bubble glitches once (2 frames, no strobe), then morphs into a warm violet bubble in a natural tone (shape interpolation, one subject kept).
  - An "Approved" stamp lands.
- **Sound:** a short muted glitch, `swish`, a stamp `thud`.
- **CTA:** Comment REPLY.
- **Shorts title:** Does automated follow up sound like a robot?

**R17 · Tue Nov 10 · "Why not hire an assistant?" · about 16s**
- **Frame 0:** two columns: Assistant | Backend. It is 11:48 PM.
- **VO:** "Why not just hire an assistant? An assistant sleeps. They forget. And they cost more every month. This answers in under a minute, day or night, and keeps following up for twenty one days. Send this to a coach about to hire one."
- **Motion:**
  - Assistant column: a moon icon and an "Offline" chip. A DM waits as Dot goes cold.
  - Backend column: the line answers at 0:42 (Example) and Dot stays warm.
  - A 21 day bar fills under the backend column only.
- **Sound:** a quiet night ambience, `ping`, `send`, taps.
- **CTA:** Send.
- **Shorts title:** Assistant vs follow up system for coaches

**R18 · Wed Nov 11 · "Who this is ideal for" · about 17s** (also pinned post P3)
- **Frame 0:** the headline "Who this is ideal for."
- **VO:** "Who this is ideal for. Active coaches and consultants. People already reaching out, commenting or asking about your help. And no backend to capture and close them. If you haven't launched yet and nobody is messaging you, start there first. Book a Strategy Call. Link in bio."
- **Motion:**
  - Three violet checks draw on, each on its spoken words.
  - A grey line with an x shows "Not launched yet, nobody messaging".
  - Dot sits beside the checks, warm.
- **Sound:** a `thud` under the headline, a pluck ladder on the checks.
- **CTA:** Book a Strategy Call.
- **Shorts title:** Who a follow up system is ideal for

**R19 · Thu Nov 12 · "What happens on the call" · about 18s**
- **Frame 0:** a "Book a Strategy Call" button with a cursor hovering.
- **VO:** "Here's what happens on a Strategy Call. We pull up your current lead flow. We find where sales are leaking. We show you exactly how we'd run this for you. If it makes sense for both of us, we start. If not, you leave knowing where your leads drop off. Link in bio."
- **Motion:**
  - The cursor presses the button (scale 0.96 → 1, violet ripple).
  - The two step form fills: Name and Instagram, then the "$1,000 to $3,000" chip is picked.
  - Three rows check: inspect, pinpoint, show.
- **Sound:** keypress patter, `mouseclick1`, `click3`, pluck checks.
- **CTA:** Book a Strategy Call.
- **Shorts title:** What happens on a DUXIO Strategy Call

**R20 · Fri Nov 13 · "Same lead, new backend" (the series finale) · about 20s**
- **Frame 0:** R1's exact first frame: lock screen, the same notification.
- **VO:** "Remember the lead who waited three hours? Here's the same message with a backend behind it. Answered in forty two seconds. Three questions. Booked. Reminded. They showed up. Same lead and the same coach, with a backend running the follow up. Book a Strategy Call."
- **Story:** the return. Dot ends where week 1 broke them, now warm.
- **Motion:**
  - `rewind` plays as R1's cold ladder visibly reverses.
  - The violet line enters from frame right.
  - Each step lands on its word: the 0:42 ring (Example), the three chips, a "Booked" invite, reminders, "Joined".
  - The last frame matches R1's first frame, but with Dot violet, so the loop rewatches as a before and after.
- **Sound:** `rewind`, `hookhit` (at 0.6 volume) as the line enters, a pluck per step, a `bighit` end.
- **CTA:** Book a Strategy Call.
- **Shorts title:** Same coaching lead, answered in 42 seconds

---

## 5. The four YouTube videos (Saturdays, faceless explainers)

- **Build:** `hyperframes:faceless-explainer`. Make `frame.md` from the DUXIO Apple dark tokens (`brand/duxio/tokens/`), not a stock preset palette.
- **Script:** each beat in `STORYBOARD.md` is tagged with a blueprint id from `hyperframes-animation/blueprints-index.md`.
- **Voice and pace:** calm male (ElevenLabs Adam or Marcus, stability 65, style 0) at 2.4 to 2.7 words per second, about 8 minutes and 1,250 words.
- **SEO:** the keyword goes in the first 60 characters of the title, the first 2 lines of the description, and the first 30s of speech. Chapters are on.
- **End screen:** VSL v4.1.
- **Description CTA:** "Book a Strategy Call" with the link.
- **Thumbnail:** built as a HyperFrames still, no AI images. Dot plus 3 to 4 words of Plus Jakarta 800 on obsidian, with one violet or red accent.
- **Reuse:** every video feeds 2 or 3 Shorts for month 2.

**YT1 · Sat Oct 24 · "Why Your Coaching Leads Ghost You After the First DM"**
- **Keyword:** coaching leads ghosting
- **Thumbnail text:** "They left at 3h"
- **Chapters:**
  - 0:00 The DM that went cold
  - 0:40 What a lead is thinking in the first hour
  - 2:10 The 1 hour rule (HBR 2011)
  - 3:40 Three replies that end conversations
  - 5:20 What a good first reply does
  - 6:40 Where follow up should start
  - 7:30 How we run this for coaches
- **Description first lines:** "Most coaching leads go quiet after the first DM. Here's why it happens and what a good first reply does instead."

**YT2 · Sat Oct 31 · "The Real Cost of Slow Replies for Coaches (Example Math)"**
- **Keyword:** speed to lead for coaches
- **Thumbnail text:** "$6,000 in your inbox"
- **Chapters:**
  - 0:00 80 messages, one month
  - 1:00 Where they drop off
  - 2:30 The math with example numbers
  - 4:00 Ads vs follow up
  - 5:30 The cheapest sales you'll ever make
  - 7:00 How to check your own inbox this week
  - 7:45 Book a Strategy Call
- **On screen:** every number is labelled "Example. Just an estimate."

**YT3 · Sat Nov 7 · "What Should Happen 60 Seconds After a Lead DMs You"**
- **Keyword:** instagram dm sales for coaches
- **Thumbnail text:** "The first 60 seconds"
- **Chapters:**
  - 0:00 The clock starts
  - 0:50 Step 1 Answer
  - 2:20 Step 2 Sort
  - 3:50 Step 3 Follow up and reminders
  - 5:30 Step 4 Reopen
  - 6:50 Your voice, your accounts
  - 7:40 Book a Strategy Call
- **Visual spine:** the four-node track carries the whole video. Dot travels it chapter by chapter.

**YT4 · Sat Nov 14 · "How to Reduce No Shows on Sales Calls: The 24h, 2h, 10m Rule"**
- **Keyword:** reduce no shows sales calls
- **Thumbnail text:** "Nobody reminded them"
- **Chapters:**
  - 0:00 The empty call
  - 0:45 Why people forget
  - 2:00 The three reminders and what each one says
  - 4:00 The short note that makes them arrive warm
  - 5:30 Rebooking the ones who miss
  - 6:45 How we run this
  - 7:30 Book a Strategy Call
- **Source:** the reminder note follows the site FAQ ("plus a short note on how you work, so they arrive warm").

## 6. Stories (daily, 2 to 3 frames)

| Day | Story |
|---|---|
| Mon | Poll: "How fast do you reply to DMs?" Under an hour / Same day / When I can |
| Tue | Reshare the reel, plus a question sticker: "What's your worst follow up moment?" |
| Wed | This or that: two first replies, vote for the better one (Example) |
| Thu | Quiz: "When do most no shows forget?" ties into R4, R13 and YT4 |
| Fri | Reshare the reel, plus a "Comment REPLY on the reel" pointer |
| Sat | "New video" link sticker to the YouTube upload |
| Sun | Off (batch day) |

Poll and question answers feed next month's hooks: copy the coaches' exact words into `brand/duxio/source-material/`.

## 7. Weekly operating loop

- **Sunday batch:**
  - Claude builds the next 5 reels and 1 YouTube video through `/make-video` and posts them for approval as one set.
  - The owner approves, records or generates the VO if using their own ElevenLabs, and schedules.
- **Daily, 30 to 45 min (the engine without ads):**
  - Comment on 15 to 20 posts from coaches with 2,000 to 50,000 followers.
  - Reply to every comment within the hour.
  - Send warm DMs to coaches who engaged.
  - Founding offer details live only in DMs and calls.
- **Sunday review** (per reel: skip rate, average watch %, sends per 1,000 reach, comments from coaches, REPLY comments, link clicks, calls booked):
  - A reel at 2× the median sends gets a sequel in the next batch, with the same format and a new hook.
  - A format below median on watch % three times is dropped from month 2.
  - Hooks with the lowest skip rate go into `content-strategy.md` §7 as proven.

**Month 1 targets [assumed; replace with real data after week 2]:**
- 20 reels and 4 YouTube videos published on schedule
- our own REPLY backend answering every keyword comment in under 60s
- at least 30% of comments from coaches by week 4
- first Strategy Calls booked from DMs started by the reels

## 8. What's needed from the owner before Oct 17

1. The real booking link. Every "Link in bio" depends on it.
2. The Instagram handle and page names.
3. The REPLY keyword automation live on our own page.
4. One energetic female ElevenLabs voice for the reels. If none is ready, Claude uses Kokoro `af_heart`.
