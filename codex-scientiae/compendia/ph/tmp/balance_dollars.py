from pathlib import Path
lines = Path(__file__).resolve().parent.parent / "AL2026.md"
lines = lines.read_text(encoding="utf-8").splitlines()
stack = []
for i, line in enumerate(lines, 1):
    if line.strip() != "$$":
        continue
    if stack:
        o = stack.pop()
        # print(f"{i}: close {o}")
    else:
        stack.append(i)
        print(f"{i}: OPEN (unmatched)")
print("Final unclosed opens:", stack)
# find line where net opens first become permanently odd
bal = 0
max_bal = 0
for i, line in enumerate(lines, 1):
    if line.strip() == "$$":
        if bal == 0:
            bal = 1
        else:
            bal = 0
        if bal == 1:
            print(f"Enter block at {i}")
        else:
            print(f"Exit block at {i}")
