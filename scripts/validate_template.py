#!/usr/bin/env python3
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"
FORBIDDEN = [r"\bKEYENCE\b", r"\bGN_UI\b", r"高纳", r"V-Generation"]
TEXT_SUFFIXES = {".md",".txt",".json",".css",".html",".yml",".yaml",".py",".svg"}
REQUIRED = [
 "README.md","manifest.json","SPEC.md","SCREEN_CONTRACT.md","CHECKLIST.md","CHANGELOG.md",
 "BRAND_LAYER.md","USAGE.md","preview/overview.svg","tokens/tokens.json","tokens/tokens.css",
 "components/COMPONENTS.md","layouts/LAYOUTS.md","platforms/DESKTOP.md","platforms/WEB.md",
 "platforms/MOBILE.md","platforms/PPT.md","prompts/UI_GENERATION.md","prompts/NEGATIVE_PROMPT.md",
 "schema/screen-contract.schema.json","scenes/SCENES.md","scenes/scenes.json",
 "examples/demo.html","examples/screen-contract.example.json"
]

def fail(msg):
    print(f"[FAIL] {msg}")
    raise SystemExit(1)

registry=json.loads(REGISTRY.read_text(encoding="utf-8"))
items=registry.get("templates",[])
if len(items) != 15:
    fail(f"expected 15 registered templates, got {len(items)}")
ids=[x["id"] for x in items]
if len(ids)!=len(set(ids)):
    fail("duplicate template id")

for item in items:
    tid=item["id"]
    base=ROOT / item["path"]
    if item.get("brand_neutral") is not True:
        fail(f"{tid}: registry brand_neutral must be true")
    for rel in REQUIRED:
        p=base / rel
        if not p.exists():
            fail(f"{tid}: missing {p.relative_to(ROOT)}")
    manifest=json.loads((base/"manifest.json").read_text(encoding="utf-8"))
    if manifest.get("id") != tid:
        fail(f"{tid}: manifest id mismatch")
    if manifest.get("version") != item.get("version"):
        fail(f"{tid}: version mismatch")
    display=manifest.get("display_name",{})
    if display.get("zh") != item.get("name_zh") or display.get("en") != item.get("name_en"):
        fail(f"{tid}: registry/display_name mismatch")
    if manifest.get("brand_neutral") is not True:
        fail(f"{tid}: manifest brand_neutral must be true")
    tokens=json.loads((base/"tokens/tokens.json").read_text(encoding="utf-8"))
    if tokens.get("meta",{}).get("template") != tid:
        fail(f"{tid}: token template id mismatch")
    if tokens.get("meta",{}).get("brand_neutral") is not True:
        fail(f"{tid}: tokens brand_neutral must be true")
    scenes=json.loads((base/"scenes/scenes.json").read_text(encoding="utf-8"))
    if len(scenes.get("scenes",[])) != 24:
        fail(f"{tid}: expected 24 scenes")
    if not (base/"preview/overview.svg").read_text(encoding="utf-8").lstrip().startswith("<svg"):
        fail(f"{tid}: preview is not svg")

violations=[]
for p in ROOT.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
        continue
    text=p.read_text(encoding="utf-8",errors="ignore")
    for pattern in FORBIDDEN:
        if re.search(pattern,text,flags=re.IGNORECASE):
            if p.name=="validate_template.py":
                continue
            violations.append((str(p.relative_to(ROOT)),pattern))
if violations:
    for file,pattern in violations:
        print(f"[FAIL] forbidden identity {pattern!r} in {file}")
    raise SystemExit(1)

print(f"[PASS] {len(items)} registered templates")
print("[PASS] required structure for every template")
print("[PASS] manifest/token brand-neutral declarations")
print("[PASS] 24-scene coverage for every template")
print("[PASS] preview/example presence")
print("[PASS] forbidden identity scan")
print("UI template family validation passed.")
