# DUXIO reel 4: "Loading %" (launch week)
- 1080x1920, 30fps, 30.5s, -14.3 LUFS, -1.4 dBTP. Script: `brand/duxio/docs/reels-launch-7.md` (Reel 4). Comment word: LOADING.
- Voice: Kokoro `af_heart` (fallback; no ElevenLabs key in the session). To swap in an ElevenLabs voice, replace `src/assets/vo/vo.wav`, rerun `python3 src/tools/asr.py src/assets/vo/vo.wav src/words.json`, update the time table in `src/tools/build.py`, then `python3 src/tools/build.py`.
- Build: `python3 src/tools/build.py && npx hyperframes render src -o raw.mp4`, then master with `loudnorm=I=-14:TP=-1.5,alimiter=limit=0.84:level=false`.
- Music bed is synthesized (`build.py`); no licensed track. Check the app's trending audio before posting.
