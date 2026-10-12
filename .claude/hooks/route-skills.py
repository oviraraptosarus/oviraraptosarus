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
vsl = has(r"vsls?", r"video sales letters?", r"sales video", r"sales script", r"sales letter", r"hook", r"epiphany", r"offer stack")
if site:
    load.append("site-design-gate")
if vsl:
    load.append("vsl-script-writing")
short = has(r"reels?", r"shorts?", r"tiktoks?", r"ads?", r"hooks?", r"b-?roll", r"stories", r"clips?", r"ideas?", r"brainstorm", r"ideate", r"ideation", r"concepts?")
unhappy = has(r"suck", r"sucks", r"bad", r"boring", r"generic", r"shit", r"crappy", r"ugly", r"cringe", r"flat", r"meh")
if video and (short or unhappy):
    load.append("reel-ideation")
audio = has(r"music", r"songs?", r"tracks?", r"beats?", r"sfx", r"sound effects?", r"soundtrack", r"audio", r"voice ?over", r"vo")
if video and audio:
    load.append("voiceover-pacing")
    load.append("music-director")
longform = has(r"long ?form", r"youtube", r"yt", r"tutorials?", r"raw footage", r"talking head", r"podcasts?", r"webinar", r"chapters?",
               r"youtube automation", r"faceless youtube", r"dead air", r"jump ?cuts?", r"walkthrough", r"screen recording", r"recording")
if video:
    load.append("make-video")
if longform:
    load.append("long-form-video")

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
    msg += (" MANDATORY for every NEW video, short or long: read OWNER-RULES.md and CONTEXT.md, then make-video auto-selects "
            "the specialist skills and the owner is asked ONE plain-text message of kid-style questions (niche, topic, "
            "ending, length, reference look, character, voice, captions, music, image source, face or faceless), with the "
            "open items from NEEDS-FROM-OWNER.md. NO popups, no AskUserQuestion. Do not build before the owner answers "
            "or says 'you decide', 'no questions' or 'just do it'. Skip the round for a revision of a video already "
            "built in this conversation. Then show a short Concept Card, build cheaply, and save the answers to "
            "make-video/preferences.md.")
if "reel-ideation" in out:
    msg += (" IDEATION GATE: reel-ideation runs BEFORE any script or build. Keep it cheap: 2 isolated branches for a quick reel (adhd skill), "
            "not a big fan-out; the owner watches the session budget. Use the adhd skill's method for hook, story and per-beat visuals, apply the gates, write the Concept Card, and "
            "only then build. Never ship a stand-in voice as final, and review real frames and playback, not just lint.")
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}}))
