#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/"registry.json").read_text(encoding="utf-8")).get("templates",[])
FORBIDDEN=[r"\bKEYENCE\b",r"\bGN_UI\b",r"高纳",r"V-Generation"]
TEXT_SUFFIXES={".md",".txt",".json",".css",".html",".yml",".yaml",".py",".svg"}
REQUIRED=["README.md","manifest.json","SPEC.md","STYLE_DNA.md","SCREEN_CONTRACT.md","CHECKLIST.md","CHANGELOG.md","BRAND_LAYER.md","USAGE.md","preview/overview.svg","tokens/tokens.json","components/COMPONENTS.md","layouts/LAYOUTS.md","platforms/DESKTOP.md","platforms/WEB.md","platforms/MOBILE.md","platforms/PPT.md","prompts/UI_GENERATION.md","prompts/NEGATIVE_PROMPT.md","scenes/SCENES.md","scenes/scenes.json","examples/demo.html","SHOWCASE.md","pages/pages.json"]
def fail(m): print("[FAIL]",m);raise SystemExit(1)
if len(items)!=30: fail(f"expected 30 templates, got {len(items)}")
ids=[x["id"] for x in items]
if len(ids)!=len(set(ids)):fail("duplicate template id")
archetypes=[];signatures=[];total_pages=0
for item in items:
 base=ROOT/item["path"];tid=item["id"]
 if item.get("showcase_level")!="gold":fail(f"{tid}: all templates must be gold")
 if item.get("preview_mode")!="all-pages-live":fail(f"{tid}: preview must be all-pages-live")
 if item.get("page_count",0)<12:fail(f"{tid}: registry page_count < 12")
 for rel in REQUIRED:
  if not (base/rel).exists():fail(f"{tid}: missing {rel}")
 mf=json.loads((base/"manifest.json").read_text(encoding="utf-8"))
 for key in ("layout_archetype","visual_signature","core_motif"):
  if not mf.get(key):fail(f"{tid}: missing manifest {key}")
 if mf.get("version")!=item.get("version"):fail(f"{tid}: version mismatch")
 if mf.get("layout_archetype")!=item.get("layout_archetype"):fail(f"{tid}: archetype mismatch")
 if mf.get("visual_signature")!=item.get("visual_signature"):fail(f"{tid}: signature mismatch")
 if mf.get("brand_neutral") is not True:fail(f"{tid}: manifest not neutral")
 if mf.get("showcase_level")!="gold":fail(f"{tid}: manifest not gold")
 pages=json.loads((base/"pages/pages.json").read_text(encoding="utf-8"))
 if pages.get("version")!=item.get("version"):fail(f"{tid}: page manifest version mismatch")
 if len(pages.get("pages",[]))<12:fail(f"{tid}: requires >=12 pages")
 mobile=sum(1 for p in pages["pages"] if p.get("device")=="mobile")
 if mobile<2:fail(f"{tid}: requires >=2 mobile pages")
 for p in pages["pages"]:
  fp=base/p["path"]
  if not fp.exists():fail(f"{tid}: missing page {p['path']}")
  text=fp.read_text(encoding="utf-8",errors="ignore")
  if "<title>" not in text or len(text)<1200:fail(f"{tid}: page too thin {p['path']}")
 total_pages+=len(pages["pages"])
 scenes=json.loads((base/"scenes/scenes.json").read_text(encoding="utf-8"))
 if len(scenes.get("scenes",[]))!=24:fail(f"{tid}: expected 24 scenes")
 archetypes.append(mf["layout_archetype"]);signatures.append(mf["visual_signature"])
if total_pages<360:fail(f"expected >=360 pages, got {total_pages}")
if len(set(archetypes))!=30:fail("all 30 templates must have unique layout_archetype")
if len(set(signatures))!=30:fail("all 30 templates must have unique visual_signature")
for p in ROOT.rglob("*"):
 if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:continue
 text=p.read_text(encoding="utf-8",errors="ignore")
 for pattern in FORBIDDEN:
  if re.search(pattern,text,re.I) and p.name!="validate_template.py":fail(f"forbidden identity {pattern!r} in {p.relative_to(ROOT)}")
print("[PASS] 30 / 30 Gold templates")
print(f"[PASS] {total_pages} real showcase pages")
print("[PASS] all previews are live all-pages systems")
print("[PASS] unique visual signatures and layout archetypes")
print("[PASS] brand-neutral scan")
