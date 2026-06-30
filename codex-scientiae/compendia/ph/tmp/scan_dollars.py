#!/usr/bin/env python3
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for p in sorted(root.rglob("*.md")):
    if p.name.startswith(".") or "tmp" in p.parts:
        continue
    t = p.read_text(encoding="utf-8")
    t2 = re.sub(r"(?ms)^```.*?^```", lambda m: " " * len(m.group()), t)
    n = t2.count("$$")
    if n % 2:
        print(f"{p.relative_to(root)}: odd $$ count {n}")
