# `ap` element catalog

Each slide in a spec = one headline (2 lines, `*word*` = serif italic gradient highlight) + one element. `xw` lists the words in the voice where the element's cues fire, in the order below. Every text is overridable with `props`; the defaults are the DUXIO cold calling reel. Names, messages, times and numbers in elements are illustrative: keep the word "Example" on screen (a `tag` or `sub` prop) for DUXIO.

| `x` | Looks like | `xw` cues, in order | `props` (all optional) |
|---|---|---|---|
| `call` | iOS call screen, ringing then declined | 0 card appears, 1 decline pressed | `glyph`, `name`, `sub`, `sub2` |
| `notifs` | 1 to 3 stacked iOS notifications | one cue per card | `rows [[icon,app,name,text]]`, `when`, `tag` |
| `age` | one notification that ages and greys out | 0 card in, 1..n each time label | `app`, `name`, `text`, `icon`, `chip`, `times [..]` |
| `chat` | 60 second ring, incoming bubble, reply, "Replied" | 0 ring and incoming bubble, 1 ring starts, 2 reply (ring ends), 3 chip | `num`, `unit`, `inText`, `outText`, `done`, `tag`, `arcLeft` |
| `qual` | avatar, 3 question chips ticking, "Serious buyer", text alert | 0 avatar, 1 to 3 chips, 4 ready, 5 text alert | `letter`, `questions [3]`, `badge`, `smsApp`, `sms` |
| `cal` | calendar card "Booked" plus 3 reminder bells | 0 card, 1 to 3 reminders | `day`, `date`, `title`, `sub`, `badge`, `reminders [3]` |
| `typing` | big "?" behind three bouncing dots | 0 appears | `glyph` |
| `appr` | "Approve before sending" toggle, draft bubble | 0 card, 1 toggle on, 2 draft bubble, 3 note | `label`, `draft`, `note` |
| `badge` | app icon with a counting red badge | 0 icon and count start, 1 chip, 2 count ends | `icon`, `count`, `caption`, `chip` |
| `lock` | lock screen clock, notification, dot grid filling | 0 clock, 1 notification, 2 dots start, 3 dots end | `time`, `mode`, `app`, `title`, `body`, `caption`, `dots` |
| `notready` | grey avatar with a dashed spinning ring, chip | 0 avatar, 1 chip | `letter`, `chip` |
| `route` | two glass cards (what happens next) | 0 first card, 1 second card | `cards [[icon,label,text]]`, `letter`, `ping` |
| `report` | weekly report card with progress bars | 0 card, 1 bars fill | `title`, `tag`, `rows [[label, 0..1]]` |
| `handset` | big phone handset ringing, then struck out | 0 appears, 1 strike | `color` |
| `logo` | wordmark on the violet flash, big serif word | 0 wordmark, 1 word | `logo` (asset path), `word` |
| `cta` | gradient button with a tap ripple | 0 button, 1 tap | `label`, `icon` |

Icons for `icon` and `rows`: send, mail, form, bell, check, x, moon, play, cal, phone, msg, link, user, star, heart, trend, dollar.

## Adding an element
1. Write `E.name = (tl, inn, X, END, P) => {...}` in `kit/ap.js`. `X(k)` is the time of cue k, `END` the slide end, `P` the props. Use only GSAP tweens (no timers, no `tl.call`), absolute positioning inside the 1080 by 1920 frame, nothing important below y 1420 (the caption zone).
2. Add its default sounds to `kit/ap_sfx.json`.
3. Add a row to this table. Use it in a spec with `"x": "name"`.

## Layout rules that keep it clean
- Headline sits at y 330 to 520. Element zone is y 640 to 1420. Captions are y 1452 and up.
- One idea per slide, 1.5 to 4 seconds. Cue words so each visual lands on the word that names it.
- Questions get their own slide (`typing`, `notready` or `badge`) and the answer gets the next one.
