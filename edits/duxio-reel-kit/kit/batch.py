#!/usr/bin/env python3
"""Make several reels at once from spec files. Run with Python 3.12.

  py -3.12 kit/batch.py kit/specs/a.json kit/specs/b.json kit/specs/c.json [--jobs 2] [--no-render] [--redo-voice]

Each spec runs through kit/make.py in its own process (own out/<id> folder, own log in kit/batch-logs/).
Voice synthesis is CPU heavy and rendering is GPU/CPU heavy, so --jobs 2 is the safe default on one PC.
Prints a summary table at the end; open each out/<id>/snapshots/contact-sheet*.jpg to review before sending.
"""
import json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.dirname(HERE)


def main():
    a = sys.argv[1:]
    jobs = int(a[a.index("--jobs") + 1]) if "--jobs" in a else 2
    flags = [f for f in ("--no-render", "--redo-voice") if f in a]
    specs = [os.path.abspath(x) for x in a if x.endswith(".json")]
    if not specs: sys.exit(__doc__)
    logs = os.path.join(KIT, "batch-logs"); os.makedirs(logs, exist_ok=True)
    queue, running, done = list(specs), [], []
    t0 = time.time()
    while queue or running:
        while queue and len(running) < jobs:
            sp = queue.pop(0); rid = json.load(open(sp, encoding="utf-8"))["id"]
            f = open(os.path.join(logs, rid + ".log"), "w", encoding="utf-8")
            p = subprocess.Popen([sys.executable, os.path.join(HERE, "make.py"), sp, *flags], stdout=f, stderr=subprocess.STDOUT, text=True)
            running.append((rid, p, f, time.time())); print(f"started {rid}")
        for item in list(running):
            rid, p, f, ts = item
            if p.poll() is not None:
                f.close(); running.remove(item); done.append((rid, p.returncode, time.time() - ts)); print(f"finished {rid} (exit {p.returncode}, {time.time() - ts:.0f}s)")
        time.sleep(2)
    print(f"\n=== batch of {len(done)} done in {time.time() - t0:.0f}s ===")
    for rid, code, secs in done:
        rp = os.path.join(KIT, "out", rid, "REPORT.json")
        r = json.load(open(rp, encoding="utf-8")) if os.path.exists(rp) else {"problems": ["no report, see log"]}
        print(f"{rid}: exit {code} | {r.get('duration')}s | {r.get('lufs')} LUFS | problems: {len(r['problems'])} | {os.path.join(KIT, 'out', rid)}")
        for pr in r["problems"]: print("   -", pr[:200])


if __name__ == "__main__":
    main()
