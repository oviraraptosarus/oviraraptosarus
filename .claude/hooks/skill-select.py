#!/usr/bin/env python3
"""UserPromptSubmit hook (runs after route-skills.py): auto-picks skills the fixed routes miss, learns from the user's
words, and keeps the 'Skills used' report honest.

1. Scans every local skill (project, ~/.claude/skills, plugin caches), matches the prompt to skill descriptions.
2. Applies .claude/skill-prefs.json: always / never / learned phrase -> skill. Updated when the user says
   'always use X', 'never use X', 'use X for <words>', 'stop using X'.
3. Reminds Claude to end each finished task with 'Skills used: ...' (from the log written by log-skill.py).
"""
import json, re, os, sys, glob, time

root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
prefs_path = os.path.join(root, ".claude", "skill-prefs.json")
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
prompt = data.get("prompt", "")
sid = data.get("session_id", "")
p = prompt.lower()

def load_prefs():
    try:
        return json.load(open(prefs_path))
    except Exception:
        return {"always": [], "never": [], "learned": []}
prefs = load_prefs()

def index():
    dirs = [os.path.join(root, ".claude/skills"), os.path.expanduser("~/.claude/skills")]
    dirs += glob.glob(os.path.expanduser("~/.claude/plugins/**/skills"), recursive=True)
    out = {}
    for d in dirs:
        for f in glob.glob(os.path.join(d, "*", "SKILL.md")):
            name = os.path.basename(os.path.dirname(f))
            try:
                txt = open(f, errors="ignore").read(2500)
            except Exception:
                continue
            m = re.search(r"^description:\s*(.+?)(?:\n\w[\w-]*:|\n---)", txt, re.S | re.M)
            out.setdefault(name, (m.group(1) if m else txt[:400]).replace("\n", " ").lower())
    return out
skills = index()
names = set(skills)

# --- learn from the user's words
changed = False
for m in re.finditer(r"\b(always|never|stop|don'?t) (?:use|using) ([a-z0-9][\w:-]+)(?: (?:for|on|when) ([^.\n]{3,80}))?", p):
    verb, sk, ctx = m.groups()
    if sk not in names:
        continue
    if verb == "always" and not ctx:
        if sk not in prefs["always"]: prefs["always"].append(sk); changed = True
        prefs["never"] = [x for x in prefs["never"] if x != sk]
    elif verb in ("never", "stop", "don't", "dont"):
        if sk not in prefs["never"]: prefs["never"].append(sk); changed = True
        prefs["always"] = [x for x in prefs["always"] if x != sk]
for m in re.finditer(r"\buse ([a-z0-9][\w:-]+) (?:for|on|when) ([^.\n]{3,80})", p):
    sk, ctx = m.groups()
    if sk in names:
        words = [w for w in re.findall(r"[a-z]{4,}", ctx) if w not in ("this", "that", "with", "from", "them", "when", "then")]
        if words and not any(l["skill"] == sk and l["words"] == words for l in prefs["learned"]):
            prefs["learned"].append({"skill": sk, "words": words}); changed = True
if changed:
    json.dump(prefs, open(prefs_path, "w"), indent=1)

# --- score descriptions
STOP = set("the and for with that this from your into have will what when make need want give just like some more about them then than also can you are not but all any use using skill skills using file files data".split())
toks = [w for w in re.findall(r"[a-z][a-z0-9]{3,}", p) if w not in STOP]
picks = []
if toks:
    df = {}
    for d in skills.values():
        for w in set(re.findall(r"[a-z][a-z0-9]{3,}", d)):
            df[w] = df.get(w, 0) + 1
    n = max(1, len(skills))
    scored = []
    for name, d in skills.items():
        dw = set(re.findall(r"[a-z][a-z0-9]{3,}", d))
        s = sum(__import__("math").log(1 + n / df[w]) for w in set(toks) if w in dw)
        if name.lower() in p: s += 6
        scored.append((s, name))
    scored.sort(reverse=True)
    picks = [nm for s, nm in scored[:3] if s >= 6.0]
for l in prefs["learned"]:
    if sum(w in p for w in l["words"]) >= max(1, len(l["words"]) // 2) and l["skill"] not in picks:
        picks.append(l["skill"])
for a in prefs["always"]:
    if a not in picks: picks.append(a)
picks = [x for x in picks if x not in prefs["never"]]

# --- skills used so far this session
used = []
log = os.path.join(root, ".claude", "skills-used.log")
try:
    for line in open(log):
        t, s, nm = line.rstrip("\n").split("\t")
        if s == sid and nm not in used:
            used.append(nm)
except Exception:
    pass

msg = []
if picks:
    msg.append("Skill selector (auto, from skill descriptions and the owner's saved preferences): also consider loading "
               + ", ".join(picks) + " if they fit the task. Skip any that do not.")
if prefs["never"]:
    msg.append("Owner said never use: " + ", ".join(prefs["never"]) + ".")
msg.append("If no local skill fits, check the cloud and plugin skills with the ListSkills or SearchSkills tool before improvising. "
           "When you finish a task, end the reply with one line: 'Skills used: a, b, c' (every skill you actually loaded or "
           "followed; say 'none' if none). So far this session the log shows: " + (", ".join(used) or "nothing logged yet") + ".")
print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": " ".join(msg)}}))
