#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/"registry.json").read_text(encoding="utf-8")).get("templates",[])
FORBIDDEN=[r"\bKEYENCE\b",r"\bGN_UI\b",r"高纳",r"V-Generation"]
TEXT_SUFFIXES={".md",".txt",".json",".css",".html",".yml",".yaml",".py",".svg"}
REQUIRED=["README.md","manifest.json","SPEC.md","STYLE_DNA.md","SCREEN_CONTRACT.md","CHECKLIST.md","CHANGELOG.md","BRAND_LAYER.md","USAGE.md","preview/overview.svg","tokens/tokens.json","components/COMPONENTS.md","layouts/LAYOUTS.md","platforms/DESKTOP.md","platforms/WEB.md","platforms/MOBILE.md","platforms/PPT.md","prompts/UI_GENERATION.md","prompts/NEGATIVE_PROMPT.md","scenes/SCENES.md","scenes/scenes.json","examples/demo.html"]
def fail(m): print("[FAIL]",m);raise SystemExit(1)
if len(items)!=30: fail(f"expected 30 templates, got {len(items)}")
ids=[x["id"] for x in items]
if len(ids)!=len(set(ids)):fail("duplicate template id")
archetypes=[]
signatures=[]
for item in items:
 base=ROOT/item["path"];tid=item["id"]
 for rel in REQUIRED:
  if not (base/rel).exists():fail(f"{tid}: missing {rel}")
 mf=json.loads((base/"manifest.json").read_text(encoding="utf-8"))
 for key in ("layout_archetype","visual_signature","core_motif"):
  if not mf.get(key):fail(f"{tid}: missing manifest {key}")
 if mf.get("version")!=item.get("version"):fail(f"{tid}: version mismatch")
 if mf.get("layout_archetype")!=item.get("layout_archetype"):fail(f"{tid}: archetype mismatch")
 if mf.get("visual_signature")!=item.get("visual_signature"):fail(f"{tid}: signature mismatch")
 if mf.get("brand_neutral") is not True:fail(f"{tid}: manifest not neutral")
 scenes=json.loads((base/"scenes/scenes.json").read_text(encoding="utf-8"))
 if len(scenes.get("scenes",[]))!=24:fail(f"{tid}: expected 24 scenes")
 archetypes.append(mf["layout_archetype"]);signatures.append(mf["visual_signature"])
if len(set(archetypes))!=30:fail("all 30 templates must have unique layout_archetype")
if len(set(signatures))!=30:fail("all 30 templates must have unique visual_signature")
for p in ROOT.rglob("*"):
 if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:continue
 text=p.read_text(encoding="utf-8",errors="ignore")
 for pattern in FORBIDDEN:
  if re.search(pattern,text,re.I) and p.name!="validate_template.py":fail(f"forbidden identity {pattern!r} in {p.relative_to(ROOT)}")
print("[PASS] 30 templates")
print("[PASS] unique visual signatures and layout archetypes")
print("[PASS] STYLE_DNA present")
print("[PASS] 24 scenes each")
print("[PASS] brand-neutral scan")
