import re
from pathlib import Path
path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")
new_text, n = re.subn(
    r"\$\$\n\n\\begin\{array\} \{ c c.*?^\$\$\nLet I",
    "$$\n![Example 3.37: poset $G_{4,2}$ and module $M$](AL2026/imageFile5.png)\n$$\n\nLet I",
    text,
    count=1,
    flags=re.MULTILINE | re.DOTALL,
)
if n:
    path.write_text(new_text, encoding="utf-8")
print("replaced", n)
