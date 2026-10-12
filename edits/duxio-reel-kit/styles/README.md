# Video styles registry

A style = a `STYLE.md` (the principles, tokens and rules), ready templates, and the kit scenes it uses. A new session reads this file, finds the default, and carries on.

| Id | Name | Status | Default for | Path |
|---|---|---|---|---|
| style-1 | Glass (Apple UI, violet) | approved 2026-10-12 | all short form (reels, shorts, ads), DUXIO | `style-1/STYLE.md`, templates in `style-1/templates/` |

## Using a style (plug and play)
```bash
py -3.12 kit/new_reel.py objection-answers my-new-reel     # copies the template to kit/specs/my-new-reel.json
# rewrite the slots in the spec (voice phrases, headlines, element props), then:
py -3.12 kit/make.py kit/specs/my-new-reel.json            # one reel
py -3.12 kit/batch.py kit/specs/a.json kit/specs/b.json    # several at once
```
Run from `edits/duxio-reel-kit`. Review `out/<id>/snapshots/contact-sheet*.jpg` and `REPORT.md` before sending.

## Adding Style 2 (or a style for another brand or niche)
1. Copy `style-1/` to `style-2/`; change the name, status and tokens in `STYLE.md`.
2. Colours and fonts go through `look.vars` in the spec (`--acc`, `--acc2`, `--grad`, `--gradr`, `--fd`, `--fs`). A different layout or element set means a new scene file next to `kit/ap.js` and a new entry in `build.py`.
3. Add a row to the table above, record the owner's approval and date, and point `OWNER-RULES.md` and `CONTEXT.md` at it.
4. Never delete or edit Style 1 to make Style 2: the owner approved Style 1 as it is. Bump its version only for approved changes.
