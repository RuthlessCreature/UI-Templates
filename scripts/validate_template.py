#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "industrial" / "industrial-clean-a"

REQUIRED = [
    ROOT / "registry.json",
    TEMPLATE / "README.md",
    TEMPLATE / "manifest.json",
    TEMPLATE / "SPEC.md",
    TEMPLATE / "SCREEN_CONTRACT.md",
    TEMPLATE / "CHECKLIST.md",
    TEMPLATE / "tokens" / "tokens.json",
    TEMPLATE / "components" / "COMPONENTS.md",
    TEMPLATE / "layouts" / "LAYOUTS.md",
    TEMPLATE / "scenes" / "scenes.json",
    TEMPLATE / "prompts" / "UI_GENERATION.md",
]

FORBIDDEN = [
    r"\bKEYENCE\b",
    r"\bGN_UI\b",
    r"高纳",
    r"V-Generation",
]

TEXT_SUFFIXES = {".md", ".txt", ".json", ".css", ".html", ".yml", ".yaml", ".py"}

def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    raise SystemExit(1)

for p in REQUIRED:
    if not p.exists():
        fail(f"required file missing: {p.relative_to(ROOT)}")

registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
ids = [x["id"] for x in registry.get("templates", [])]
if "industrial-clean-a" not in ids:
    fail("industrial-clean-a not registered")

tokens = json.loads((TEMPLATE / "tokens" / "tokens.json").read_text(encoding="utf-8"))
if tokens.get("meta", {}).get("brand_neutral") is not True:
    fail("tokens must declare brand_neutral=true")

manifest = json.loads((TEMPLATE / "manifest.json").read_text(encoding="utf-8"))
if manifest.get("brand_neutral") is not True:
    fail("manifest must declare brand_neutral=true")

scenes = json.loads((TEMPLATE / "scenes" / "scenes.json").read_text(encoding="utf-8"))
if len(scenes.get("scenes", [])) != 24:
    fail("scene library must contain exactly 24 reference scenes")

violations = []
for p in ROOT.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
        continue
    text = p.read_text(encoding="utf-8", errors="ignore")
    for pattern in FORBIDDEN:
        if re.search(pattern, text, flags=re.IGNORECASE):
            # Validator itself contains forbidden patterns by definition.
            if p.name == "validate_template.py":
                continue
            violations.append((str(p.relative_to(ROOT)), pattern))

if violations:
    for file, pattern in violations:
        print(f"[FAIL] forbidden identity pattern {pattern!r} in {file}")
    raise SystemExit(1)

print("[PASS] required structure")
print("[PASS] registry and manifest")
print("[PASS] brand-neutral declarations")
print("[PASS] 24-scene library")
print("[PASS] forbidden identity scan")
print("Industrial Clean A validation passed.")
