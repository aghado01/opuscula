from pathlib import Path

path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")
lines = text.splitlines()
stack = []
for i, line in enumerate(lines, 1):
    if line.strip() != "$$":
        continue
    if stack:
        opened = stack.pop()
        if i >= 2680:
            print(f"CLOSE {i} pairs with OPEN {opened}")
    else:
        stack.append(i)
        if i >= 2680:
            print(f"OPEN {i}")
print("Remaining unclosed:", stack)
print("Total $$:", sum(1 for l in lines if l.strip() == "$$"))
