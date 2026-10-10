# DUXIO VSL v4: motion, sound and attention spec

This is the build sheet for the VSL on the owner's ElevenLabs recording (`brand/duxio/voice/elevenlabs-vsl-v4-serious.mp3`, 2:36 of voice). Times are voice time; the video adds 0.3s of lead-in and a 5s end card, about 2:41 in all.

**Look:** Apple Keynote dark.
- Canvas: obsidian `#0D0E12` with a faint radial lift behind the hero (no blobs).
- Type: white `#F5F5F7`, Plus Jakarta Sans 800 at -0.03em, support lines in `#9A9AA5`.
- Violet `#6F00FF` for fills, glows and the CTA, with `#B794FF` for violet text on dark. Red `#F1283A` only for loss.
- Glass panels: `rgba(255,255,255,.04)` fill, 1px `rgba(255,255,255,.09)` border, 28px radius, a soft long shadow.
- One idea per frame.

**Motion grammar**
- Entrances: `expo.out`, 0.45 to 0.6s.
- Landings: `back.out(1.4)`, overshooting 2 to 5% then settling.
- Exits: `power2.in`, 0.25s.
- Camera glides: `power2.inOut`, 0.9 to 1.2s.
- Nothing sits still for more than about 1.2s. An active element always has a micro move: a breathing glow, typing dots, a cursor blink, or a 0.5% drift.

**Sound grammar (calm, never cheesy)**
- Ambient synth bed, about 24dB under the voice, with three sections:
  - dark pad under the pain
  - a soft arpeggio added for the four steps
  - the pad opening up for the math and the CTA
- Every SFX is low-passed at about 9kHz. Bright, harsh sound lowered likes and comments in a TikTok ad study, so the clicks stay warm.

## Attention mechanics (the slot-machine lessons, used honestly)
| Mechanic | What the research says | How it shows up here |
|---|---|---|
| **Anticipation beats the reward** | Dopamine neurons ramp up while an outcome is uncertain, most at 50/50 (Fiorillo, Tobler & Schultz, *Science* 2003) | 0.4 to 0.8s of build before each reveal: a node charges, a riser plays, digits spin. The answer always arrives a beat after the question |
| **Rolling reels that decelerate** | Variable outcomes keep attention; a slowing spin creates suspense | Every number rolls like a reel and slows into its value with ticks that space out, then lands with a soft thunk and a 3% overshoot. Used on the clock (2:14 → 5:14), the reply timer (0:42), the Zoom timer (45:00) and the 80 leads |
| **Variable reward spacing** | Variable-ratio schedules hold behaviour longer than fixed ones | Big hits (an impact plus a visual flip) land at uneven gaps of 6 to 14s: 11s, 21s, 38s, 44s, 63s, 77s, 95s, 116s, 142s, 152s. Small rewards (ticks, checks) fill the gaps |
| **Ascending pitch ladder** | Rising pitch reads as progress or winning (the slot "win ladder") | Checks inside one build rise in pitch (C5 → E5 → G5 → C6): the three questions, the three reminders, the fit list |
| **Near miss / loss framing** | Almost-wins and almost-losses raise arousal | The lead goes cold three hours too late (red pulse); the call timer reaches 45:00 and then "Not a fit" |
| **Juice in proportion** | 2 or 3 feedback channels per event, more only for big events | Small: a 2% pop and a click. Medium: pop, glow and a chime. Big: a flip, light sweep, sub thump and music swell |
| **Open loop and completion** | Unfinished sequences pull attention (Zeigarnik) | The 01 to 04 track stays on screen and fills step by step; the CTA closes the loop |

**Guardrails:** no fake scarcity, no fake wins. Every number is the voice's number or labelled "Example".

## Shot list
### 1. Hook (0.0 to 22.5)
| Time | Visual and micro-movement | Sound |
|---|---|---|
| 0.0 | Frame 0: an iPhone on the right third, lock screen at 2:14 PM, slow 0.5% float. Left headline "Every coach lost sales this month." (*lost sales* in red) builds word by word | pad in |
| 0.4 | An Instagram notification springs down: "Hey, how much is your coaching?" (squash 4%, settle) | haptic thump + soft ping |
| 5.0 | Headline swaps to "While you were on a call." then "or asleep." Two status chips (camera icon, moon icon) light in turn | soft whoosh, tick |
| 8.7 | The status-bar clock rolls 2:14 → 5:14 like a reel, slowing; a red "3 hours unanswered" counter rolls in under the notification | accelerating ticks, then a decelerating land and a low thunk |
| 11.0 | "Already gone.": the notification greys out, a red glow pulses once and the lead chip flips to "Cold" | dull low thud, pad dips |
| 15.1 | The phone glides left and shrinks. A Zoom-style call tile slides in; its timer rolls 00:00 → 45:00 | glass whoosh, rolling ticks |
| 20.8 | On "never a fit": the tile freezes and desaturates; a red "Not a fit" pill drops onto it (3% overshoot) | impact thud + sub |

### 2. Old way vs backend (22.5 to 43.5)
| Time | Visual | Sound |
|---|---|---|
| 22.5 | Three advice cards stack in on their words: "Post more content", "Run expensive ads", "3 hours a night in your DMs" | three card slides, rising pitch |
| 31.6 | "The old way": the cards fade, and a chaos panel ("The Manual Way") fills: an unread badge rolls 12 → 27 → 41, scribbled notes lines, typing dots that never stop | badge ticks, muted keyboard patter |
| 34.0 | A name badge flips from "Coach" to "Full time messaging employee" | card flip |
| 37.6 | Big centred type: "You do not need more leads." | music drops to the pad, a beat of air |
| 39.7 | Split screen. Left: the manual panel greys. Right: "The DUXIO Backend", where a single line of violet light carries a lead dot into a calendar slot that turns green ("Confirmed") | light swish, then a confirm chime |

### 3. Four steps (43.5 to 105.5)
| Time | Visual | Sound |
|---|---|---|
| 43.5 | Logo lockup, then the track: four nodes 01 to 04 (Answer, Sort, Follow up, Reopen) draw across; the camera glides to 01 | arpeggio enters, node pops ascend |
| 47.5 | **01 Answer.** An incoming bubble lands; a ring timer rolls to 0:42 and lands; the reply bubble lands with a delivered check (Example label) | ticks, land, send swoosh, check |
| 53.6 | "Not a spam bot": a ghost bubble with a link appears, gets a red strike and slides out | strike swish |
| 55.9 | "Your voice" chip glows; typing dots, then "That makes sense. Tell me more?" | soft typing, pop |
| 62.7 | Glide to **02 Sort.** A glass card: three chips (Goal, Timeline, Readiness) check in turn | pitch ladder C, E, G |
| 71.4 | Routing: a grey dot slides to a "Free content" folder; a violet dot unlocks a calendar slot ("Pick a time") | low slide, then lock click and chime |
| 77.3 | Glide to **03 Follow up.** A 21-day line draws; Day 1 reads "Not yet" | draw swish |
| 82.4 | Check-in pings ripple at Day 3, 7, 14, 21 | four soft pings, rising |
| 89.2 | A calendar invite lands "Booked"; reminders stack: 24 hours, 2 hours, 10 minutes; then "Joined" in green | chime; three ticks rising; join tone |
| 94.9 | Glide to **04 Reopen.** A grey "Day 60" card; on "check in" the message sends: "Hey, are you still looking to solve this?" | send |
| 101.0 | The card lights grey → violet; a reply lands "Yes. Can we talk?" (Example) | warm chime + small sub |

### 4. The math (105.5 to 125.1)
| Time | Visual | Sound |
|---|---|---|
| 105.5 | Pure black. "Think about the math." | music thins out (uncertainty beat) |
| 107.3 | "80" rolls up like a reel: *leads reach out* | rolling ticks, land |
| 111.0 | Arrow → "1 or 2" *rescued sales* | riser |
| 114.5 | Arrow → "+$3,000 to $6,000" with a violet light sweep; small label "Example at a $3,000 offer. Not a forecast." | big hit: sub + sparkle, music swells |
| 118.7 | Two rows check: "$0 more on ads", "0 evenings typing" | two checks rising |

### 5. Fit and CTA (125.1 to 161)
| Time | Visual | Sound |
|---|---|---|
| 125.1 | Fit list: "Beginners with no offer and no audience" in grey with an x; then "Active coaches and consultants", "People already reaching out", "No backend to capture and close them" check in violet | thud; ladder of three checks |
| 137.9 | The camera tilts "down the page": below a video frame sits the 2-step form | glass whoosh down |
| 140.9 | A cursor fills step 1 (Name, Instagram), clicks Next, picks step 2 chips | soft key clicks, clicks |
| 141.6 | "Book a Strategy Call" button presses (scale 0.96 → 1) with a violet ripple | click + haptic thump |
| 145.4 | Three rows beside the form check: "We inspect your lead flow", "We pinpoint the leaks", "We show you how it runs" | checks rising |
| 152.8 | End card: the logo, "Book a Strategy Call", "For coaches and consultants selling high ticket offers", "Below this video" with a gentle bouncing arrow, held 5s | logo hit + pad resolve |
