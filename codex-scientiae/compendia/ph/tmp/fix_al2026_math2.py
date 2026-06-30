"""Second pass AL2026 math repairs."""
import re
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")

# Remove orphan $$ wrapping prose after Lemma 2.10 proof
text = text.replace(
    "$$\nHence dim Hom A ( C, M ) = i \\in [ m ] dim M ( x i ) - rank M ( µ ).\nRemark 2.11.",
    "Hence $\\dim \\mathrm{Hom}_A(C,M) = \\sum_{i \\in [m]} \\dim M(x_i) - \\mathrm{rank}\\, M(\\mu)$.\n\nRemark 2.11.",
)

# Replace corrupted G_{5,2} Hasse quiver array
pattern = r"\$\$\n\n\\begin\{array\} \{ c c.*?^\$\$"
replacement = (
    "The Hasse quiver of $G_{5,2}$ is the standard grid poset on $[5] \\times [2]$ "
    "(see e.g. Fig. 1 for the grid convention).\n\n$$G_{5,2} := [5] \\times [2]$$"
)
text, n = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE | re.DOTALL)
print(f"G_5,2 array replacements: {n}")

# Proposition 3.24 pushout diagram block -> CD diagram
text = text.replace(
    "$$\n\n\\eta ^ { \\prime } \\coloneqq \\begin{bmatrix} P _ { b _ { 1 }, a _ { 1 } } & 0 & P _ { s c ( I ) } = P _ { a _ { 1 } } \\oplus \\cdots \\oplus P _ { a _ { n } } \\\\ 0 & 0 & \\widehat { \\ } c \\end{bmatrix} & \\underset { \\eta } { \\searrow } \\begin{bmatrix} V _ { I } \\\\ \\varepsilon _ { 0 } = \\left [ \\rho _ { 1 a _ { 1 } } ^ { V _ { I } }, \\dots, \\rho _ { 1 a _ { n } } ^ { V _ { I } } \\right ] \\,. \\\\ \\end{bmatrix} \\\\ P _ { s k ( I ) } \\underset { \\eta } { \\leq } & \\underset { \\eta } { \\longrightarrow } V _ { I }\n\n$$",
    "$$\n\\begin{CD}\nP_{\\mathrm{sc}(I)} @>{\\eta'}>> V_I \\\\\n@VV{\\eta}V @VV{\\varepsilon_0}V \\\\\nP_{\\mathrm{sk}(I)} @>>{\\eta}> V_I\n\\end{CD}\n$$",
)

# Theorem 3.25 proof aligned
text = text.replace(
    "$$\n\nd _ { M } ( V _ { I } ) & = \\dim H o m _ { A } ( V _ { I }, M ) - \\dim H o m _ { A } ( E, M ) \\\\ & + \\dim H o m _ { A } ( \\tau ^ { - 1 } V _ { I }, M ) \\\\ & = \\dim H o m _ { A } ( V _ { I }, M ) - \\dim H o m _ { A } ( E \\oplus P _ { 2 }, M ) \\\\ & + \\dim H o m _ { A } ( \\tau ^ { - 1 } V _ { I } \\oplus P _ { 2 }, M ),\n\n$$",
    "$$\n\\begin{aligned}\nd_M(V_I) &= \\dim \\mathrm{Hom}_A(V_I,M) - \\dim \\mathrm{Hom}_A(E,M) + \\dim \\mathrm{Hom}_A(\\tau^{-1}V_I,M) \\\\\n&= \\dim \\mathrm{Hom}_A(V_I,M) - \\dim \\mathrm{Hom}_A(E \\oplus P_2,M) + \\dim \\mathrm{Hom}_A(\\tau^{-1}V_I \\oplus P_2,M),\n\\end{aligned}\n$$",
)

# Remove corrupted commutative diagram block (lines ~800) - replace with prose
pattern2 = r"\$\$\n\n\\text \{bottom row exact:\}.*?^\$\$\nwhere we set \\mu_E"
if re.search(pattern2, text, re.MULTILINE | re.DOTALL):
    repl = "The pushout extends to a commutative diagram with exact bottom row (see the proof of Proposition 3.24), where we set $\\mu_E$"
    text = re.sub(pattern2, lambda _m: repl, text, count=1, flags=re.MULTILINE | re.DOTALL)
    print("Removed corrupted diagram block")

# rank C(alpha) - use regular brackets
text = text.replace(
    "\\mathrm{rank}\\, C(\\alpha) = \\dim C(y) - \\dim P(u)(y) + \\mathrm{rank}\\,\\bigl[P(\\beta)(y),\\, P(u)(\\alpha)\\bigr].",
    "\\mathrm{rank}\\, C(\\alpha) = \\dim C(y) - \\dim P(u)(y) + \\mathrm{rank}\\,[P(\\beta)(y),\\, P(u)(\\alpha)].",
)

# Appendix A double-complex diagram
text = text.replace(
    "$$\nX_{i - 1, j - 1} \\underbrace{X_{i - 1, j}}_{d_{i - 1, j - 1}} \\left | \\downarrow d_{i - 1, j}^{V} \\right | \\\\ X_{i, j - 1} \\underbrace{\\frac{d_{i, j - 1}^{H}}{X_{i, j}} \\rightarrow X_{i, j}}_{\\downarrow d_{i, j}^{V}} \\rightarrow X_{i, j + 1} \\cdot \\\\ X_{i + 1, j} \\underbrace{X_{i + 1, j + 1}}_{X_{i + 1, j}}\n$$",
    "$$\n\\begin{array}{ccccc}\n& X_{i-1,j-1} & \\xrightarrow{d_{i-1,j-1}^{H}} & X_{i-1,j} & \\xrightarrow{} \\cdots \\\\\n& \\downarrow^{d_{i-1,j-1}^{V}} & & \\downarrow^{d_{i-1,j}^{V}} & \\\\\n& X_{i,j-1} & \\xrightarrow{d_{i,j-1}^{H}} & X_{i,j} & \\xrightarrow{d_{i,j}^{H}} X_{i,j+1}\n\\end{array}\n$$",
)

path.write_text(text, encoding="utf-8")
print("Second pass complete.")
