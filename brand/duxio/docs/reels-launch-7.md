# DUXIO launch week: 7 reels on trending formats

Each reel opens with value and points to us once, softly. The CTA is always "comment a word and I'll DM you". The DM gives the promised thing first. A Strategy Call comes up only after the person shows they have leads.

## Format research (October 2026)

| Format | Source | Status |
|---|---|---|
| "Getting robbed": the person filming stays glued to their phone while their bag gets taken; a text overlay explains the distraction | Ramdam and Later, October 2026 roundups | Current trend |
| "Yes… but": split screen, the good on one side and the catch on the other | SocialBee, Oct 7 2026 | Current trend |
| "Which one are you?": self-identification, where viewers comment their type and get a tailored answer by DM | Creatorflow, 2026 DM playbook | Proven comment driver |
| "Loading %": starts at 0%, the percentage climbs with every cut until the finished result | Later, Oct 2 2026 ("Daily GRWM loading") | Current trend |
| "Message From A": an embarrassing moment with a shady note signed "A" | New Engen, Oct 1 2026 | Current trend |
| Blind ranking: items appear one at a time and must be placed in a slot before you see the next | Manychat, 2026 trends roundup | Ongoing game format |
| "Comment to get": show the resource, tease it, give one piece of it away on screen, then the keyword | Creatorflow, 2026 | Proven DM funnel |

**Why these, for us**
- Instagram ranks Reels on watch time and sends. Sends matter most for reaching non-followers (Mosseri, per 2025 to 2026 algorithm guides).
- Every reel below is short, loopable, and built to be sent to "a coach who does this".

**Sources are marketing blogs. Check in the app before posting:**
- **Trending audio:** business accounts only get the commercial sound library.
- **What to do:** if the trend's sound is there, lay it 18 to 20 dB under the voice. If not, use our bed.

## Shared settings

- **Voice:** energetic female ElevenLabs voice (the same one all week).
  - **Eleven v3:** use the audio tags in [brackets] as written, stability "Natural".
  - **Multilingual v2:** drop the tags and set stability 35, similarity 75, style 35, speed 1.08, speaker boost on.
- **Script marks:**
  - Words in CAPS get stress (write them lowercase in ElevenLabs and stress them with the tag or by regenerating).
  - "/" is a short breath, about 0.2s. "//" is a held beat, 0.4 to 0.6s.
- **Look:** obsidian `#0D0E12`, Plus Jakarta Sans 800, violet `#6F00FF` / `#B794FF`, red `#F1283A` only for loss, 1080×1920.
- **Captions:** 2 to 4 words, with an active-word pop, inside the centre 900×1400. Every mock DM, number and name is labelled "Example".
- **Sound:** a hit at frame 0, about 1 SFX per second, SFX 7 to 8 dB under the voice, no chimes. Master to -14 LUFS.
- **Build:** `/make-video` builds every reel to `editing-standard.md`. The last frame loops into the first.
- **Posting:**
  - One a day.
  - The same video goes to Facebook Reels and YouTube Shorts with the same keyword.
  - The comment automation (our own backend) must be live before reel 1.
- **IG caption pattern:** a keyword-rich first sentence (that's how Instagram search reads it), one line of value, the CTA, then 2 or 3 hashtags.

---

## Reel 1 · Mon · "Getting robbed" · about 22s · keyword LEAK

**Format beats:**
1. The viewer's eye locks on a phone in the foreground.
2. Behind it, something gets taken.
3. A text overlay names the distraction.
4. Turn into the lesson.

| Time | On screen | VO and direction |
|---|---|---|
| 0.0 | Close on a phone: a reel editor, the cursor dragging a caption. Overlay: **"Me perfecting my 4th reel this week"** | [deadpan, dry] "Me. Perfecting my FOURTH reel this week." |
| 2.2 | Blurred background comes into focus: violet DM bubbles with tiny eyes walk out of an open door, each holding a small bag tagged "$3,000 · Example". The phone stays sharp in front | [still deadpan, slower] "Meanwhile… / six people who asked about my coaching / are walking out the back door." |
| 6.5 | Hard cut to clean type: **"Before you post today"** | [warm, faster, leaning in] "Here's the fix. // Before you post ANYTHING today, / open your DMs." |
| 9.5 | The inbox list. Three threads tick green one by one: "asked 2 days ago", "asked yesterday", "asked this morning" | "Answer every person who asked a question in the last forty eight hours. / THEN post." |
| 13.5 | Split: content brings them in (arrow into the inbox) · replies keep them (the bubbles turn around and walk back in) | [smiling] "Content brings them in. / Replies are what keep them." |
| 17.0 | Keyword card: **Comment LEAK** | [bright, friendly] "Comment LEAK / and I'll send you the three messages we use to bring cold leads back." |

- **Motion:**
  - A rack focus between the phone layer and the background layer (blur 0 ↔ 8px, one wrapper each).
  - The bubbles walk with a 2-frame bob cycle.
  - The return walk is the same keyframes reversed: same subjects, no crossfade.
- **SFX:** `hookhit` at 0, a soft `keypress` patter while editing, quiet footstep taps per bubble, `swish` on the hard cut, a pluck per green tick.
- **IG caption:**
  > Coaches lose leads in their DMs while they're busy making content. Clear your inbox first, then post. Comment LEAK and I'll send you the 3 messages we use to bring cold leads back.
  > #coachingbusiness #onlinecoach

## Reel 2 · Tue · "Yes… but" · about 20s · keyword YES

**Format beats:** a split screen. The left side says "Yes" and shows the win. The right side says "But" and shows the catch. Three fast rounds, then a calm resolve.

| Time | Left: YES | Right: BUT | VO and direction |
|---|---|---|---|
| 0.0 | "You got 40 DMs this week" (counter rolls 0 → 40) | "You replied to 12" (40 rolls down to 12, red) | [upbeat, quick] "Yes, you got forty DMs this week. / But you replied to TWELVE." |
| 4.0 | "9 people booked a call" | "4 showed up" (five empty chairs grey out) | "Yes, nine people booked a call. / But FOUR showed up." |
| 7.8 | "Your content is working" | "Nobody heard from you after day 1" (a 21 day line with only Day 1 lit) | "Yes, your content is working. / But nobody heard from you after day ONE." |
| 11.8 | The split closes into one centred line: **"The leads are already there."** | | [slower, warm, sincere] "The leads are already there. // They just need to hear back from you." |
| 15.8 | Keyword card: **Comment YES** | | [bright] "Comment YES / and I'll send you the exact follow up schedule we run for coaches." |

- All numbers carry a small "Example" tag.
- **Motion:**
  - The centre divider slams in at 0.
  - Each "But" side lands 0.1s after its word.
  - Counters roll and decelerate.
  - On "already there" the divider slides away (one wipe, toward the right).
- **SFX:** `hookhit` + `swish` at 0; a tick roll on each counter, with a low `thud` on each "But" (quiet); a pluck on the resolve.
- **IG caption:**
  > Most coaches already have enough leads. The sales get lost in slow replies and no follow up. Comment YES and I'll send you the follow up schedule we run for coaches.
  > #coachingtips #salesforcoaches

## Reel 3 · Wed · "Which one are you?" · about 24s · keywords GHOST, LINK, MIDNIGHT, ONCE

**Format beats:**
1. Name a mistake everyone makes.
2. Show 4 types fast.
3. Ask viewers to comment their type.
4. Each type gets its own DM.

It's October, so type 1 wears the sheet-ghost costume to ride the season.

| Time | On screen | VO and direction |
|---|---|---|
| 0.0 | Four face-down cards, numbered 1 to 4. Title: **"Which coach are you in the DMs?"** | [playful, curious] "There are four kinds of coaches in the DMs. / Which one are you?" |
| 3.0 | Card 1 flips: **The Ghost**. A DM bubble in a little sheet, with a timestamp "3 days later": "So sorry, just seeing this!" | [teasing] "Number one. The GHOST. / Replies three days later with: so sorry, just seeing this." |
| 8.0 | Card 2 flips: **The Link Dropper**. "Check the link in my bio." The conversation greys out | [dry] "Number two. The Link Dropper. / Check my bio. // Conversation over." |
| 12.0 | Card 3 flips: **The Midnight Replier**. 11:48 PM, a moon icon, bed sheets | [sympathetic laugh] [laughs softly] "Number three. The Midnight Replier. / Answers everything at eleven p.m. from bed." |
| 16.0 | Card 4 flips: **The One and Done**. One follow up sent, then a 21 day line stays dark | "Number four. The One and Done. / Follows up once. / Then never again." |
| 19.5 | All four cards fanned out. **"Comment your type"** with the four keywords under the cards | [warm, inviting] "Comment your type / and I'll send you the fix for it." |

- **Motion:**
  - Cards flip on `rotationY` with real perspective.
  - Each lands with `back.out(1.4)` and a 3% overshoot.
  - The previous card slides left and stacks, so all four stay visible (an open loop that completes).
- **SFX:** `hookhit` at 0, `card-slide` + a pluck per flip on a rising ladder (C4, E4, G4, C5), a soft "boo" whoosh on the Ghost (quiet).
- **IG caption:**
  > The 4 types of coaches in the DMs, and the one habit that fixes each. Comment GHOST, LINK, MIDNIGHT or ONCE and I'll send you the fix for your type.
  > #coachingbusiness #businesscoach

## Reel 4 · Thu · "Loading %" · about 26s · keyword LOADING

**Format beats:** a percentage counter starts at 0% and climbs with every cut. Each cut is one stage, and 100% is the finished result.

| % | On screen | VO and direction |
|---|---|---|
| 0% | Title: **"Turning a DM into a client. Loading…"** A DM lands: "How much is your coaching?" (Example) | [excited, fast] "Turning a DM into a client. / Loading. // Zero percent. Someone asks how much your coaching is." |
| 15% | A ring timer lands on 0:42 (Example). The reply bubble shows "written in your voice" | "Fifteen. / You answer in under a minute, / in your own words." |
| 35% | Three chips check: Goal · Situation · Timing | "Thirty five. / Three quick questions. / What they want, / where they are, / how soon." |
| 50% | Calendar slot locks: "Pick a time" → Booked | "Fifty. / They pick a time." |
| 70% | Reminder stack: 24 hours · 2 hours · 10 minutes | "Seventy. / Reminders. A day before, / two hours before, / ten minutes before." |
| 85% | Call tile, the chair fills, timer starts | [delighted] "Eighty five. / They actually SHOW UP." |
| 100% | A calm call tile. Text: **"Now it's just a good conversation."** | [relaxed, smiling, slower] "One hundred. // Now it's just a good conversation." |
| end | Keyword card: **Comment LOADING** | [bright] "Comment LOADING / and I'll send you the whole flow, step by step." |

- **Motion:**
  - The % counter sits top centre at all times and rolls between stages, slot-style and decelerating, landing exactly on each number.
  - Every stage enters with one mask wipe upward (the same direction as the climb).
  - At 100% everything settles and holds 1.5s with only a breathing glow.
- **SFX:** `hookhit` at 0, a tick roll per % step that slows down, a pluck that rises one step per stage (a 7 note ladder, C4 to C5), `join` at 85%, and a soft pad open at 100%.
- **IG caption:**
  > How a DM turns into a client, stage by stage: a fast reply, three questions, a booked time, three reminders. Comment LOADING and I'll send you the whole flow.
  > #onlinecoach #highticketcoaching

## Reel 5 · Fri · "Message From A" · about 18s · keyword SORRY

**Format beats:**
1. Show a mildly embarrassing moment.
2. A shady handwritten note signed "A" appears over it.
3. Add our reveal: who A is.
4. Then the fix.

The brand allows zero dashes, so the signature is "A." on its own line.

| Time | On screen | VO and direction |
|---|---|---|
| 0.0 | Screen recording style: a DM inbox, the cursor typing "Hey!! So sorry, just seeing this" to a message from 6 days ago (Example) | (no VO for 2s, just keyboard taps and the trend's sound if licensed, low) |
| 2.0 | A handwritten note slides on, slightly rotated: **"saw you send 'so sorry, just seeing this' for the 4th time this week."** with **"A."** on its own line | [sing-song, teasing] "Saw that." |
| 5.0 | The note flips over: **"A. = your abandoned leads"** | [laughs] [warm] "Love, / your abandoned leads." |
| 7.5 | Clean type: **"10 minutes. Same time every day."** A clock at 8:50 AM, inbox to zero | [helpful, steady] "If you send that more than once a week, / here's a two minute fix. // Pick ONE time a day, before your first session, / and clear every DM. / Same time. Every day." |
| 14.0 | Keyword card: **Comment SORRY** | [bright] "Comment SORRY / and I'll send you the replies we use, / so it never has to sound like an apology." |

- **Motion:**
  - The note drops with a paper flutter (a 3 stop rotation ladder: 8°, -4°, 2°, then 0).
  - The flip is a card `rotationY`.
  - The inbox count rolls down to 0 decelerating, then lands with a 3% pop.
- **SFX:** `keypress` taps, a paper `swish`, a light `thud` for the reveal, a tick roll, `confirm2` at 0.25 volume on inbox zero (no bells).
- **IG caption:**
  > If "so sorry, just seeing this" is your most sent DM, this is for you. A ten minute daily habit that keeps leads warm. Comment SORRY and I'll send you the replies we use instead.
  > #coachinglife #coachingtips

## Reel 6 · Sat · Blind ranking · about 26s · keyword RANK

**Format beats:**
1. Five empty slots.
2. Items reveal one at a time, and each must be placed before the next appears.
3. The best one lands in the slot that was luckily left open.

| Time | On screen | VO and direction |
|---|---|---|
| 0.0 | Title: **"Blind ranking first replies to: how much is your coaching?"** Slots 1 to 5 empty | [game show energy, quick] "Blind ranking first replies to: / how much is your coaching?" |
| 3.0 | Card: "Check the link in my bio." → dropped into slot **4** | [unimpressed] "Check the link in my bio. / That's a four." |
| 6.5 | Card: "Great question! Let's hop on a call!" → slot **3** | "Great question, let's hop on a call. / Too fast. / Three." |
| 10.0 | Card: a grey bubble, "Seen 3 days ago" → slot **5** | [deadpan] "Seen. No reply. // Bottom. Five." |
| 13.0 | Card: "It's $3,000." → slot **2** | [wince] "It's three thousand dollars. / Ouch. / I'll give it a two." |
| 16.5 | Card: "Depends! What are you hoping to change right now?" → slot **1** glows violet | [relieved, delighted] "Depends. / What are you hoping to change right now? // THAT'S the one. Number one." |
| 21.0 | Small type under the board: **"A price with no context scares people off. A question keeps them talking."** | [teaching, warm] "A price with no context scares people off. / A question keeps them talking." |
| 23.5 | Keyword card: **Comment RANK** | [bright] "Comment RANK / and I'll send you our first reply script." |

- All replies are labelled "Example".
- **Motion:**
  - Each card drops from the top and snaps into its slot with `back.out(1.5)`.
  - A tiny camera shake (2px, 3 frames) on the slot 5 placement.
  - Slot 1 gets a light sweep.
- **SFX:** `hookhit` at 0, `card-place` per drop, a buzzer-like low `thud` for slot 5 (soft), a rising pluck on slot 1.
- **IG caption:**
  > Ranking 5 ways coaches reply to "how much is your coaching?" The best first reply asks a question before giving a price. Comment RANK and I'll send you our first reply script.
  > #salesforcoaches #coachingbusiness

## Reel 7 · Sun · "Comment to get" · about 22s · keyword REMIND

**Format beats:**
1. Call out who it's for.
2. Show the resource with most of it blurred.
3. Give one piece away fully on screen.
4. Then the keyword.

This reel uses the coaches' own phrase from the Reddit research, "something came up".

| Time | On screen | VO and direction |
|---|---|---|
| 0.0 | A booked call tile with "Something came up, can we reschedule?" (Example) landing on it | [knowing, a little playful] "If people book calls with you, / and then, something came up… / this is for you." |
| 4.0 | Three message cards stacked, labelled 24 hours · 2 hours · 10 minutes, text blurred | [clear, helpful] "These are the three reminders we send before every call." |
| 7.0 | Card 1 un-blurs | "Twenty four hours before. / A short note on what you'll cover, / so they come prepared." |
| 10.5 | Card 2 lifts slightly (still blurred) | "Two hours before. / A quick, see you soon." |
| 13.0 | Card 3 lifts (still blurred) | "Ten minutes before. / The link, ready to tap." |
| 15.0 | Card 1 full screen, readable (see text below) | [warm] "Here's the first one, word for word." (hold 2.5s so it can be read) |
| 19.0 | Keyword card: **Comment REMIND** | [bright] "Comment REMIND / and I'll send you all three." |

- **Card 1 text (on screen, Example):**
  > Hey Sam, looking forward to tomorrow at 2pm. We'll look at where you are now and what you want next. Anything you'd like me to know before we talk?
- **Motion:**
  - The blur animates from 12px to 0 on card 1 only.
  - The cards lift with `y -16` and a soft shadow grow.
  - The reschedule message slides in like a notification and squashes 4% on landing.
- **SFX:** `haptic` + `ping` on the notification, `card-slide` per card, a soft `whoosh` on the un-blur.
- **IG caption:**
  > The 3 reminders we send before every sales call so people actually show up: 24 hours, 2 hours and 10 minutes before. Comment REMIND and I'll send you all three.
  > #discoverycall #coachingbusiness

---

## The DMs (what the comment triggers)

Every DM follows the same three steps:
1. **Message 1 (instant):** deliver exactly what was promised.
2. **Message 2 (2 minutes later):** one honest question.
3. **Message 3 (only if they answer and clearly have leads):** a soft invite.

Never pitch in message 1.

### Message 1, by keyword

**LEAK**
> Here you go. Three messages for leads who went quiet.
> 1. "Hey Sam, you asked about coaching a while back. Is this still something you're working on?"
> 2. "Saw this and thought of you. [one short tip or video on their exact problem]"
> 3. "No pressure at all. If now isn't the time, just say later and I'll check back next month."
> Send them a few days apart, never all at once.

**YES**
> Here's the follow up schedule we run for coaches.
> Day 1: answer within a minute and ask one question about them.
> Day 3: a short tip on their problem.
> Day 7: a quick story about why you coach what you coach.
> Day 14: an answer to the question most people ask before buying.
> Day 21: a simple invite to book a call.
> Once they book: reminders 24 hours, 2 hours and 10 minutes before.

**GHOST**
> Fix for the Ghost: pick one time a day to clear your DMs, and reply to new questions within the hour when you can. Leads contacted within an hour are far more likely to turn into a real conversation (Harvard Business Review, 2011).

**LINK**
> Fix for the Link Dropper: answer their question with a question first. "Depends! What are you hoping to change right now?" Send the link only after they've told you what they want.

**MIDNIGHT**
> Fix for the Midnight Replier: batch replies to one daytime slot, and have a short first reply ready for when you can't. "Hey! Saw this, I'm with a client right now. What made you reach out today?" It buys you time and starts the conversation.

**ONCE**
> Fix for the One and Done: one follow up is rarely enough. Spread four or five short, helpful check ins over three weeks: a tip, a story, an answer, then an invite.

**LOADING**
> Here's the whole flow.
> 1. Answer in under a minute, in your own words.
> 2. Ask three questions: what they want, where they are, how soon.
> 3. Ready? Send your calendar. Not yet? Send something useful and follow up.
> 4. Follow up for 21 days.
> 5. Remind them 24 hours, 2 hours and 10 minutes before the call.
> 6. Check back once a month with anyone who said not yet.

**SORRY**
> Replace "so sorry, just seeing this" with one of these.
> "Hey! Thanks for waiting. Quick question so I can actually help: what made you reach out?"
> "Good timing, I just finished with a client. What are you working on right now?"
> Neither one apologises. Both move the conversation forward.

**RANK**
> Our first reply script, for "how much is your coaching?":
> "Depends on what you need! What are you hoping to change right now?"
> Then: "Got it. And how soon do you want that sorted?"
> Then share the price with context: what it includes and who it's for.

**REMIND**
> All three reminders.
> 24 hours: "Hey Sam, looking forward to tomorrow at 2pm. We'll look at where you are now and what you want next. Anything you'd like me to know before we talk?"
> 2 hours: "See you at 2pm! Here's the link so it's handy: [link]"
> 10 minutes: "Starting in 10. Jump on whenever you're ready: [link]"

### Message 2 (all keywords, about 2 minutes later)

> Quick question so I can point you the right way: roughly how many people message you about your coaching each month?

### Message 3 (only if they answer with real lead volume)

> That's a solid flow. Most coaches at that level lose a few every month just to timing.
> We build and run this whole follow up for coaches, in their own voice, inside their own accounts. If you want, I can show you how it would look for you on a quick Strategy Call. Here's the link: [booking link]

If they say they have few or no leads, stay helpful and don't invite them to the call (`duxio-brand` §6).

## Pre-flight

- [x] Zero dashes in the VO, on-screen text, captions and DMs (the "A" signature is written "A.")
- [x] No price for DUXIO (the $3,000 in reel 6 is an example of a coach's own price, labelled Example)
- [x] No results, no "5 spots", no guarantees
- [x] Claims stay within `duxio-brand` §7 (the HBR stat in GHOST is cited)
- [x] One soft mention of us per reel ("we use", "we run", "we send")
- [x] No "free" anywhere
- [ ] Owner: the booking link, and the comment automation live for LEAK, YES, GHOST, LINK, MIDNIGHT, ONCE, LOADING, SORRY, RANK, REMIND
