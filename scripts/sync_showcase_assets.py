#!/usr/bin/env python3
import io, json, pathlib, urllib.request
from PIL import Image, ImageOps

ROOT=pathlib.Path(__file__).resolve().parents[1]
parts=[ROOT/"scripts"/f"showcase-assets-part{i}.json" for i in (1,2,3)]
assets=[]
for p in parts:
    assets.extend(json.loads(p.read_text(encoding="utf-8"))["assets"])
assert len(assets)==30, f"expected 30 assets, got {len(assets)}"

for i,a in enumerate(assets,1):
    req=urllib.request.Request(a["source_url"],headers={"User-Agent":"UI-Templates-showcase-sync/1.0"})
    with urllib.request.urlopen(req,timeout=120) as r:
        data=r.read()
    img=Image.open(io.BytesIO(data)).convert("RGB")
    # Normalize to portfolio-poster 4:5 without distorting the artwork.
    img=ImageOps.fit(img,(1440,1800),method=Image.Resampling.LANCZOS,centering=(0.5,0.5))
    out=ROOT/a["destination"]
    out.parent.mkdir(parents=True,exist_ok=True)
    img.save(out,"JPEG",quality=92,optimize=True,progressive=True)
    print(f"[{i:02d}/30] {a['id']} -> {out.relative_to(ROOT)}")
