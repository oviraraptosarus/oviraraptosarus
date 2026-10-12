#!/usr/bin/env python3
"""Fail fast on a spec before any voice or render: refs resolve, element cue counts fit, slides are in time order.

  py -3.12 kit/check_spec.py kit/specs/a.json [more.json ...]     (also run automatically by make.py)

Uses estimated phrase timings when the real voice does not exist yet, so it is safe and instant.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from compile_ap import compile_spec

NEED = {"call": 2, "typing": 1, "chat": 4, "qual": 6, "appr": 4, "badge": 3, "lock": 4, "notready": 2, "route": 2, "report": 2, "handset": 2, "logo": 2, "cta": 2}


def need(slide):
    x, P = slide.get("x"), slide.get("props", {})
    if x == "notifs": return len(P.get("rows", [0, 0, 0]))
    if x == "age": return len(P.get("times", [0] * 5))
    if x == "cal": return 1 + len(P.get("reminders", [0, 0, 0]))
    return NEED.get(x)


def fake_timings(spec):
    t, out = 0.04, []
    for p in spec["voice"]["phrases"]:
        d = 0.33 * len(p["t"].split()) + 0.3
        out.append({"start": round(t, 3), "end": round(t + d, 3)}); t += d + p.get("pause", 300) / 1000
    return out


def validate(spec, tm=None):
    problems = []
    kinds = set(json.load(open(os.path.join(HERE, "ap_sfx.json"), encoding="utf-8"))) - {"_comment", "_slide", "_hl"}
    phrases = spec["voice"]["phrases"]
    for i, s in enumerate(spec["slides"]):
        if s.get("x") and s["x"] not in kinds: problems.append(f"slide {i}: unknown element {s['x']!r}")
        n = need(s)
        if n is not None and len(s.get("xw", [])) != n: problems.append(f"slide {i} ({s.get('x')}): needs {n} element cues in xw, has {len(s.get('xw', []))}")
        if len(s.get("hw", [])) != len(s.get("hl", [])): problems.append(f"slide {i}: hw has {len(s.get('hw', []))} refs for {len(s.get('hl', []))} headline lines")
        if not 0 <= s.get("p", 0) < len(phrases): problems.append(f"slide {i}: p={s.get('p')} is not a phrase")
        for ln in s.get("hl", []):
            if ln.count("*") % 2: problems.append(f"slide {i}: unbalanced * in {ln!r}")
            if len(ln.replace("*", "")) > 25: problems.append(f"slide {i}: headline line {ln!r} is {len(ln.replace('*', ''))} chars, over 25 and will not fit one line")
    try:
        reel, starts = compile_spec(spec, tm or fake_timings(spec))
    except Exception as e:
        return problems + [f"compile: {e}"]
    if starts != sorted(starts): problems.append("slides are not in time order: " + str([round(x, 1) for x in starts]))
    bt = reel["beats"][0]
    for i, s in enumerate(bt["props"]["slides"]):
        if "hl" in s and s["hl"] and any(not x for x in s["hl"]): problems.append(f"slide {i}: empty headline line")
    return problems


if __name__ == "__main__":
    bad = 0
    for f in sys.argv[1:]:
        sp = json.load(open(f, encoding="utf-8")); pr = validate(sp)
        print(("OK   " if not pr else "FAIL ") + os.path.basename(f) + (f"  ({len(sp['slides'])} slides, {len(sp['voice']['phrases'])} phrases)" if not pr else ""))
        for p in pr: print("   -", p)
        bad += bool(pr)
    sys.exit(1 if bad or len(sys.argv) < 2 else 0)
