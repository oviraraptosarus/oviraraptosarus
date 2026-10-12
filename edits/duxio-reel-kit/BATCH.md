# Making several videos at once (framework)

Goal: stop spending about 30 minutes of hands-on time per reel. Two ways to run more than one reel, and they can be combined.

## Where the 30 minutes went (and what this removes)
| Before | Now |
|---|---|
| Writing a new `gen.py` and tuning cue words by hand for each reel | One JSON **spec** per reel (phrases + slides). Cues, slide timing and sound design are compiled from the real voice timings (`kit/compile_ap.py`, `kit/ap_sfx.json`) |
| Element text hardcoded to one topic | Every element takes `props`, so one element serves any topic (`kit/ELEMENTS.md`) |
| Re-asking the same look/voice questions each video | Defaults live in `make-video/preferences.md` ("Short form defaults" + "Voice recipe"); only topic, ending and assets are asked |
| Voice, build, check, snapshots, render, loudness, pitch check one command at a time | `kit/make.py <spec>` does all of it unattended and writes `out/<id>/REPORT.md` |
| One reel per run | `kit/batch.py <spec> <spec> <spec> --jobs 2` runs several at once |

What it does NOT remove: writing the script and picking elements (I do that for all reels in one pass), and **looking at the contact sheets and listening** before anything is sent. Status checks passing does not mean it looks right.

## The flow
1. **Batch intake, one message.** You name N videos. I send ONE plain message with a table, one row per video: topic or angle, objections or beats you want, ending (CTA), assets you will supply (rule 3d), length. Shared answers (voice, look, music, captions) come from the saved defaults, so they are not asked again. "You decide" on a row means I choose.
2. **Specs.** I write `kit/specs/<id>.json` for every video (copy `kit/specs/_template.json`). If a video needs an element that does not exist, I add it to `kit/ap.js` once (see ELEMENTS.md).
3. **Run.** `py -3.12 kit/batch.py kit/specs/a.json kit/specs/b.json kit/specs/c.json --jobs 2` (or `kit/make.py` for one). Voice is cached and only re-rendered when the spoken script changes. `--no-render` stops after the contact sheets for a cheap review pass.
4. **Review.** I read every `out/<id>/snapshots/contact-sheet*.jpg` and `REPORT.md` (pitch of the questions, loudness, check errors). Fixes are edits to the spec, then re-run that one id.
5. **Deliver.** One message with the mp4s, what to confirm per video, and open items. Commit `kit/specs/<id>.json`, `reels/<id>/`, and the mp4.

## Mode A: many reels in one session (cheapest)
One session writes 3 to 5 specs and runs `batch.py`. One context, one set of questions, the renders run in the background while I review the earlier sheets. Recommended for reels in the same niche.

## Mode B: several sessions in parallel (your "not in same session" option)
Use it when the videos are in different niches or you want to keep working on something else (for example a long form video) while reels build. Each session pays for its own context, so it costs more than Mode A.

Rules so the sessions never collide:
1. **One git worktree per session**, so `out/` and `reels/` are separate checkouts:
   ```bash
   git worktree add ../duxio-<id> -b reel/<id> claude/blissful-hawking-xxcdii
   ```
   Open Claude Code in `..\duxio-<id>`.
2. **Own your id.** A session only creates or edits `edits/duxio-reel-kit/kit/specs/<id>.json`, `edits/duxio-reel-kit/reels/<id>/` and `edits/duxio-reel-kit/out/<id>/`. Unique ids per video.
3. **Shared files are frozen** (`kit/*.js`, `kit/*.py`, `kit/*.css`, `kit/ap_sfx.json`, `brand/`, `OWNER-RULES.md`, `CONTEXT.md`). A session that needs a new element writes it in `kit/ap_ext_<id>.js` (the build picks up every `ap_ext_*.js`), and I merge it into `ap.js` later.
4. **Notes go in `reels/<id>/NOTES.md`**, not in `CONTEXT.md`. When a session finishes, one line goes into `CONTEXT.md` from the main session.
5. **Merge:** from the main checkout, `git merge reel/<id>` (only your own folders changed, so there are no conflicts). Then `git worktree remove ../duxio-<id>`.
6. **Machine limits (unverified on this PC):** voice synthesis is CPU heavy and the render uses the GPU. Keep at most 2 renders running at the same moment. Stagger the sessions, or run with `--no-render` and render one at a time.

Paste this at the start of each parallel session:
```
Read OWNER-RULES.md, CONTEXT.md and edits/duxio-reel-kit/BATCH.md. You are session <n>, id <id>. Make this reel: <topic, objections, ending, assets>. Use Mode B rules: own only your id's spec/reels/out folders, notes in reels/<id>/NOTES.md, new elements in kit/ap_ext_<id>.js. Write kit/specs/<id>.json, run py -3.12 kit/make.py on it, review the contact sheets and REPORT.md, then send the mp4 and the open items. Do not render test videos.
```

## Status of this framework (honest)
- **Verified:** `ap` elements take `props`; a spec compiles to the same cues and slide timing as the hand written v2 (checked slide by slide); voice, build and `hyperframes check` run through `make.py` with 0 errors on the v2 spec.
- **Written but not run yet:** the snapshot, render, loudness and question pitch stages of `make.py`, and the parallel runner `batch.py`. The first real batch will exercise them; expect small fixes.
- **Side effect:** testing the cache regenerated the v2 voice files (timings identical). The approved v2 mp4 was not touched.
- **Limits:** the `ap` look is the DUXIO violet look. A new niche needs its own `--acc` colours, logo and element texts via `props` and `look.vars` in the spec; the fonts and gradient rules stay the same.
