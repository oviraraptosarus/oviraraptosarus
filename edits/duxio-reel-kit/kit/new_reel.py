#!/usr/bin/env python3
"""Start a reel from a style template.

  py -3.12 kit/new_reel.py                      list styles and templates
  py -3.12 kit/new_reel.py <template> <id> [--style style-1]

Copies styles/<style>/templates/<template>.json to kit/specs/<id>.json with the id set, then prints the slots to rewrite.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); KIT = os.path.dirname(HERE)


def main():
    a = sys.argv[1:]
    style = a[a.index("--style") + 1] if "--style" in a else "style-1"
    a = [x for i, x in enumerate(a) if x != "--style" and (i == 0 or a[i - 1] != "--style")]
    tdir = os.path.join(KIT, "styles", style, "templates")
    if not os.path.isdir(tdir): sys.exit(f"no such style: {style} (see styles/README.md)")
    names = sorted(f[:-5] for f in os.listdir(tdir) if f.endswith(".json"))
    if len(a) < 2:
        print(f"{style} templates:")
        for n in names: print(f"  {n}: {json.load(open(os.path.join(tdir, n + '.json'), encoding='utf-8')).get('_template', '')}")
        print("\nusage: py -3.12 kit/new_reel.py <template> <id> [--style style-1]"); return
    tpl, rid = a[0], a[1]
    if tpl not in names: sys.exit(f"unknown template {tpl!r}; choose from: {', '.join(names)}")
    if not rid.replace("-", "").replace("_", "").isalnum(): sys.exit("id: letters, digits, - and _ only")
    out = os.path.join(HERE, "specs", rid + ".json")
    if os.path.exists(out): sys.exit(f"{out} already exists")
    spec = json.load(open(os.path.join(tdir, tpl + ".json"), encoding="utf-8"))
    spec["id"] = rid; spec["_style"] = style; spec["_from_template"] = tpl
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(spec, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"created {out}\nrewrite these slots:")
    for s in spec.get("_slots", []): print("  -", s)
    print(f"\nthen: py -3.12 kit/make.py kit/specs/{rid}.json   (or kit/batch.py with several specs)")


if __name__ == "__main__":
    main()
