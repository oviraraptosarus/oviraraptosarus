# Attention mechanics: micro-movements and sound that hold attention

Load with `editing-standard.md` for every video. These are the slot-machine and game-feel lessons, translated into honest motion design. They make watching feel rewarding; they never fake a result, a number or scarcity.

## The evidence (what is solid, what is a hypothesis)
| Finding | Source | Strength |
|---|---|---|
| Dopamine neurons show a sustained ramp while an outcome is uncertain, strongest at 50/50 uncertainty, separate from the reward hit itself | Fiorillo, Tobler & Schultz, *Science* 299:1898 (2003) | Peer reviewed |
| Variable-ratio schedules (rewards after an unpredictable number of actions) produce high, persistent responding | Skinner; standard behavioural psychology | Classic |
| Speech rate, pitch and loudness have an inverted-U relation with engagement: moderate-high wins, flat or extreme loses. Positive emotional valence helps, linearly | Douyin study of 6,152 short videos (2025, *Int. J. Hospitality Mgmt*) | Peer reviewed |
| Faster speech rate raised shares on TikTok ads; brighter, harsher audio (high spectral centroid) lowered likes and comments | TikTok field study of short video ads | Peer reviewed |
| Audio arousal and visual change work best when they match (congruence) | Yang et al., *JTAER* 20(2):69 (2025) | Peer reviewed |
| Game feel: anticipation, squash and stretch, small overshoot (2 to 5%), 100 to 200ms micro-feedback, 2 or 3 feedback channels per event, stronger effects only for important events | Game-feel practice (Swink; Jonasson & Purho "juice") | Practitioner consensus |
| A cut or visual change every 2 to 3s, and the hook in the first 0.5 to 1s | Platform and creator guides | Directional; check against your own retention curve |

## The mechanics
1. **Anticipation before every reveal.** Build 0.4 to 0.8s of uncertainty before each payoff: a node charges, digits spin, a riser plays, typing dots run. Let the answer land a beat after the question. Never reveal on the same frame the question is asked.
2. **Rolling reels that slow down.** Numbers, times and counters spin like slot reels and decelerate (`power3.out`) into the value. Ticks space out as they slow, then a soft thunk and a 3 to 4% overshoot settle.
   - Use realistic strips: a clock's minute-tens digit only shows 0 to 5.
   - Land exactly on the spoken number.
3. **Variable reward spacing.** Big payoffs (a flip, light sweep, sub thump, music swell) land at uneven intervals: 6 to 14s in a VSL, 3 to 6s in a reel. Small rewards (ticks, checks, pops) fill the gaps every 1 to 3s. A metronome kills it.
4. **Ascending pitch ladder.** Items inside one build sound on rising notes (C, E, G, C) so the list feels like progress, or winning. Reset the ladder for each new build.
5. **Near miss and loss framing.** Show the almost-loss: the lead going cold three hours later, the timer hitting 45:00 and then "Not a fit". Then show the save. Loss lands harder than gain, so set it up before the solution.
6. **Juice in proportion.** Every interactive-looking event gets feedback on 2 or 3 channels (motion + sound + light):
   - Small: a 2% pop and a click.
   - Medium: pop, glow and a chime.
   - Big: a flip, light sweep, sub and music.
   - Never put big juice on routine events.
7. **Idle life.** Nothing is fully still for more than about 1.2s: a breathing glow on the active element, typing dots, a cursor blink, a 0.5% drift. Keep it subliminal, never filler zoom.
8. **Open loop and completion (Zeigarnik).** A visible progress structure (a step rail, a counter, a checklist) stays on screen and fills. The final step or CTA closes it with the biggest payoff.
9. **Match sound energy to the cut.** Faster sections get denser SFX and a busier bed; reflective lines get air. Audio arousal and visual change move together.
10. **Warm, not harsh.** Low-pass SFX at about 9kHz. Prefer soft clicks, thunks and bells over bright clicks and white-noise hits. Harsh highs lower likes.

## Owner feedback that refines the above
- Ladders use **soft, low wooden plucks** (C4 → C5, short decay, quiet), never bright bells. Bells and chimes stick out over the voice and read as cheap.
- The **hook needs weight**:
  - A sub impact and air on frame 0.
  - A low pulse under the tension.
  - A swell into the turn, then a hit.
  - A small chime is not a hook.
- **Money is a counter**, not a word: count up from $0 with coin ticks that slow down, then land with a soft register "cha-ching" and a 7% pop.
- **Measure, don't guess:** render voice-only and SFX-only passes. Then compare 400ms loudness. During speech, every SFX must sit at least 7 to 8dB under the voice median. Only the frame 0 hook hit may come closer.

## Guardrails
- No fake scarcity, fake countdowns, fake wins or invented numbers. Example data is labelled "Example".
- Don't flash or strobe, and don't use more than 3 SFX within 100ms.
- The voice always wins the mix. SFX sit 6 to 12dB under the voice; music sits 18 to 24dB under while words play.
