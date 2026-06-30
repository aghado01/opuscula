import re
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")

# Example 3.37: replace corrupted array + broken aligned block with figure reference
pattern = r"\$\$\n\n\\begin\{array\} \{ c c.*?^\$\$\nLet I"
repl = "$$\n![Example 3.37: poset $G_{4,2}$ and module $M$](AL2026/imageFile5.png)\n$$\n\nLet I"
text, n = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE | re.DOTALL)
print("Example 3.37 replacements:", n)

# Fix broken R(M,I) example block - wrap in aligned or replace with summary
pattern2 = r"\$\$\n\n1, a _ \{ 1 2 \}.*?^\$\$\nHence d M"
repl2 = (
    "$$\n"
    "\\begin{aligned}\n"
    "R(M,I) &\\sim \\begin{bmatrix}\n"
    "M_{a_{12},a_1} & -M_{a_{12},a_2} & 0 & 0 \\\\\n"
    "M_{a_1',a_1} & 0 & 0 & 0 \\\\\n"
    "M_{b_1,a_1} & 0 & M_{b_1,b_1} & M_{b_1,b_{12}} \\\\\n"
    "0 & 0 & 0 & -M_{b_2,b_{12}}\n"
    "\\end{bmatrix}\n"
    "\\end{aligned}\n"
    "$$\n\nHence d M"
)
text, n2 = re.subn(pattern2, repl2, text, count=1, flags=re.MULTILINE | re.DOTALL)
print("R(M,I) block replacements:", n2)

# Proposition A.2 salamander sequence - wrap in aligned
text = text.replace(
    "$$\nC_{\\Box} \\stackrel{a}{\\rightarrow} A^{\\|} \\stackrel{b}{\\rightarrow} A_{\\Box} \\stackrel{c}{\\rightarrow} \\Box B \\stackrel{d}{\\rightarrow} B^{\\|} \\stackrel{e}{\\rightarrow} \\Box D \\\\ ( r e s p. \\, C_{\\Box} \\stackrel{a}{\\rightarrow} = A \\stackrel{b}{\\rightarrow} A_{\\Box} \\stackrel{c}{\\rightarrow} \\Box B \\stackrel{d}{\\rightarrow} = B \\stackrel{e}{\\rightarrow} \\Box D ),\n$$",
    "$$\n\\begin{aligned}\n& C_{\\Box} \\xrightarrow{a} A^{\\|} \\xrightarrow{b} A_{\\Box} \\xrightarrow{c} \\Box B \\xrightarrow{d} B^{\\|} \\xrightarrow{e} \\Box D \\\\\n& \\text{(resp.\\ } C_{\\Box} \\xrightarrow{a} =\\!A \\xrightarrow{b} A_{\\Box} \\xrightarrow{c} \\Box B \\xrightarrow{d} =\\!B \\xrightarrow{e} \\Box D \\text{)},\n\\end{aligned}\n$$",
)

# Remove prose-in-$$ at Remark 3.36 area
text = text.replace(
    "$$\nWe denote by E r the identity matrix",
    "We denote by $E_r$ the identity matrix",
)
text = text.replace(
    "$$\nwhere the last equivalence is obtained by transforming M a,M b,M c",
    "where the last equivalence is obtained by transforming $M_a,M_b,M_c$",
)

path.write_text(text, encoding="utf-8")
print("Third pass complete.")
