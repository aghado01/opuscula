from pathlib import Path

# WGW2023: truncate corrupted appendix tail and remove orphan $$
p = Path(r"d:\aghado01\codex-scientiae\compendia\ph\WGW2023.md")
lines = p.read_text(encoding="utf-8").splitlines()
marker = "Table 9. Matrix construction of graph G 4 in the top panel of Figure 5."
idx = next(i for i, ln in enumerate(lines) if ln.startswith(marker))
# keep through Table 9 header; drop OCR garbage after
keep = lines[: idx + 1]
keep.append("")
keep.append("*Appendix tables 10–19 omitted here due to OCR corruption in the source extraction.*")
p.write_text("\n".join(keep) + "\n", encoding="utf-8")
print("WGW2023 truncated at line", idx + 1)
