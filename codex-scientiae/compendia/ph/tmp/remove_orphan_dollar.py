from pathlib import Path

path = Path(__file__).resolve().parent.parent / "AL2026.md"
lines = path.read_text(encoding="utf-8").splitlines()
stack = []
for i, line in enumerate(lines, 1):
    if line.strip() != "$$":
        continue
    if stack:
        stack.pop()
    else:
        stack.append(i)
if len(stack) == 1:
    # remove orphan opening delimiter
    orphan = stack[0]
    out = []
    for i, line in enumerate(lines, 1):
        if i == orphan and line.strip() == "$$":
            continue
        out.append(line)
    path.write_text("\n".join(out) + ("\n" if lines and not lines[-1].endswith("\n") else ""), encoding="utf-8")
    print(f"Removed orphan $$ at line {orphan}")
else:
    print("Stack state:", stack, "- no single orphan fix applied")
