#!/usr/bin/env python3
"""UserPromptSubmit hook: picks the skills a prompt needs so the user never types skill names.

Reads the hook JSON on stdin and prints additionalContext telling Claude which skills to load.
Prints nothing when the prompt is unrelated or already names a skill.
"""
import json, re, sys

try:
    prompt = json.load(sys.stdin).get("prompt", "")
except Exception:
    sys.exit(0)
p = prompt.lower()
if p.lstrip().startswith("/"):
    sys.exit(0)  # the user already invoked a skill or command

def has(*words):
    return any(re.search(r"\b" + w + r"\b", p) for w in words)

video = has(r"videos?", r"reels?", r"vsl", r"shorts?", r"tiktok", r"ads?", r"promo", r"explainer", r"motion graphics?",
            r"b-?roll", r"footage", r"animation", r"animate", r"voice ?over", r"captions?",
            r"edit(ing)? (my|this|the) (clip|video|footage)", r"logo sting", r"teaser", r"trailer", r"cutdown")
site = has(r"website", r"site", r"landing page", r"web ?page", r"hero section", r"homepage", r"navbar", r"header",
           r"form", r"calculator", r"funnel page", r"frontend", r"lovable", r"tanstack", r"tailwind", r"pricing section")
copy = has(r"script", r"copy", r"headline", r"caption for", r"email", r"dm script", r"sales letter", r"offer")
duxio = has(r"duxio", r"my business", r"my agency", r"my offer", r"strategy call", r"coaches?")

load = []
if duxio:
    load.append("duxio-brand")
    if site:
        load.append("duxio-website")
    if video:
        load.append("duxio-vsl")
if video:
    load.append("make-video")

seen, out = set(), []
for s in load:
    if s not in seen:
        seen.add(s); out.append(s)
if not out:
    sys.exit(0)

msg = ("Skill router: before doing anything else, load these skills with the Skill tool, in order: "
       + ", ".join(out) + ".")
if duxio:
    msg += " DUXIO brand kit (logos, fonts, tokens, SFX, voice, spec, facts): brand/duxio/README.md."
if "make-video" in out:
    msg += (" make-video will auto-select the specialist skills for this type of video and ask, in one "
            "AskUserQuestion round, for any required brief field the prompt left out (type, platform/length, "
            "style, voice, CTA), unless the user said to decide for them.")
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))
