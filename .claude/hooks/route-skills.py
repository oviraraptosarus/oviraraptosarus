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

video = has(r"videos?", r"vids?", r"reels?", r"vsl", r"shorts?", r"tiktoks?", r"ads?", r"promos?", r"explainers?", r"motion graphics?",
            r"b-?roll", r"footage", r"animations?", r"animate", r"voice ?over", r"vo", r"captions?", r"clips?", r"youtube", r"yt",
            r"instagram", r"ig", r"stories", r"story", r"podcasts?", r"webinar", r"testimonial", r"mp4", r"render", r"storyboard",
            r"thumbnail", r"sfx", r"sound effects?", r"intro", r"outro", r"logo sting", r"teasers?", r"trailers?", r"cutdowns?",
            r"content", r"edit(ing)? (my|this|the|a) \w+")
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
    msg += (" MANDATORY for every NEW video, short or long: make-video auto-selects the specialist skills, then asks "
            "the user, in one AskUserQuestion round, for every required brief field the prompt, the conversation, "
            "make-video/preferences.md and the brand kit did not already answer (type, platform and length, style, "
            "voice, CTA, plus the short-form or long-form extras). Do not start building before that round, unless the "
            "user said 'you decide', 'no questions' or 'just do it'. Skip the round for a revision of a video already "
            "built in this conversation. After the user answers, append the answers to make-video/preferences.md so "
            "the next video asks fewer, sharper questions.")
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))
