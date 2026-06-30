from pathlib import Path

lines = Path(__file__).resolve().parent.parent / "AL2026.md"
lines = lines.read_text(encoding="utf-8").splitlines()
stack = []
issues = []
for i, line in enumerate(lines, 1):
    if line.strip() != "$$":
        continue
    if stack:
        o = stack.pop()
        if i > 2600:
            print(f"{i}: CLOSE (opened {o})")
    else:
        stack.append(i)
        if i > 2600:
            print(f"{i}: OPEN")
print("Final stack (unclosed opens):", stack)
# find first index where cumulative balance != 0 at end
bal = 0
first_imbalance = None
for i, line in enumerate(lines, 1):
    if line.strip() == "$$":
        bal = 1 - bal  # toggle: odd = inside block
        if bal not in (0, 1):
            pass
# simpler: count
opens = sum(1 for l in lines if l.strip() == "$$")
print("Total $$ lines:", opens, "even?" , opens % 2 == 0)
