"""Targeted math repairs for AL2026.md display blocks."""
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")

# Fix Lemma 2.10 proof: remove OCR garbage block (lines ~318-322)
old_proof = (
    "Hence Hom A ( C, M ) \\sim = Ker Hom A ( µ, M ). Now we have\n"
    "$$\n\n"
    "& \\text {Hence Hom}"
)
if old_proof in text:
    start = text.index(old_proof)
    end = text.index("$$\nHence dim Hom A ( C, M )", start)
    replacement = (
        "Hence $\\mathrm{Hom}_A(C,M) \\cong \\mathrm{Ker}\\,\\mathrm{Hom}_A(\\mu,M)$. Now we have\n\n"
        "$$\n"
        "\\begin{aligned}\n"
        "\\mathrm{Ker}\\,\\mathrm{Hom}_A(\\mu,M)\n"
        "&= \\{ f \\in \\mathrm{Hom}_A(X,M) \\mid f\\mu = 0 \\} \\\\\n"
        "&= \\mathrm{Ker}\\,(M(\\mu) \\colon \\bigoplus_{i \\in [m]} M(x_i) \\to \\bigoplus_{j \\in [n]} M(y_j)), \\\\\n"
        "\\dim \\mathrm{Hom}_A(C,M)\n"
        "&= \\sum_{i \\in [m]} \\dim M(x_i) - \\mathrm{rank}\\, M(\\mu).\n"
        "\\end{aligned}\n"
        "$$\n\n"
    )
    text = text[:start] + replacement + text[end:]

# Proposition 3.13 tail: prose captured inside display math
text = text.replace(
    "$$\nfor all \\mathfrak{a}_{c} \\in s c_{1} ( U ) and a \\in s c ( U ) . Here and subsequently, we write the matrices following the lexicographic order \\preceq_{l e x} (see Notation 3.4 (3)) of indices.\nWe here remark that \\varepsilon_{0}^{U} is a projective cover of V_{U} .\n*Proof.* We refer the reader to the proof of (Asashiba et al. 2024, Proposition 5.10), and substitute I_{\\xi} by U . \\square Given an up-set U of P ( U might be non-connected), we consider its decomposition into connected components and apply Proposition 3.13 on each connected component. Following this spirit, we let U \\coloneqq U_{1} \\sqcup \\cdots \\sqcup U_{k} . By Lemma 3.11 and (Munkres 2000, Theorem 25.3), each component is again an open set, thus an up-set of P . Then the following is easy to show.\n**Proposition 3.14.** Let P be a finite poset, and U = U_{1} \\sqcup \\cdots \\sqcup U_{k} an up-set of P with k connected components ( k \\geq 1 ). Set V_{U} \\coloneqq V_{U_{1}} \\oplus \\cdots \\oplus V_{U_{k}} . Then V_{U} has the following (not necessarily minimal) projective presentation:\n$$",
    "for all $\\mathfrak{a}_c \\in \\mathrm{sc}_1(U)$ and $a \\in \\mathrm{sc}(U)$. Here and subsequently, we write the matrices following the lexicographic order $\\preceq_{\\mathrm{lex}}$ (see Notation 3.4 (3)) of indices.\nWe here remark that $\\varepsilon_0^U$ is a projective cover of $V_U$.\n\n*Proof.* We refer the reader to the proof of (Asashiba et al. 2024, Proposition 5.10), and substitute $I_\\xi$ by $U$. $\\square$\n\nGiven an up-set $U$ of $P$ ($U$ might be non-connected), we consider its decomposition into connected components and apply Proposition 3.13 on each connected component. Following this spirit, we let $U \\coloneqq U_1 \\sqcup \\cdots \\sqcup U_k$. By Lemma 3.11 and (Munkres 2000, Theorem 25.3), each component is again an open set, thus an up-set of $P$. Then the following is easy to show.\n\n**Proposition 3.14.** Let $P$ be a finite poset, and $U = U_1 \\sqcup \\cdots \\sqcup U_k$ an up-set of $P$ with $k$ connected components ($k \\geq 1$). Set $V_U \\coloneqq V_{U_1} \\oplus \\cdots \\oplus V_{U_k}$. Then $V_U$ has the following (not necessarily minimal) projective presentation:\n\n$$",
)

text = text.replace(
    "$$\n\\ w h e r e \\, \\varepsilon_{i}^{U} \\colon = \\varepsilon_{i}^{U_{1}} \\oplus \\cdots \\oplus \\varepsilon_{i}^{U_{k}} \\ \\ ( i = 0, 1 ). \\quad \\square\n$$",
    "where $\\varepsilon_i^U \\coloneqq \\varepsilon_i^{U_1} \\oplus \\cdots \\oplus \\varepsilon_i^{U_k}$ ($i=0,1$). $\\square$",
)

# Formula (1.5)
old_15 = (
    "$$\n\n"
    "d _ { M } ( V _ { I } ) = & \\, \\frac { P ^ { \\prime } ( g _ { 1 } ) ( x ) }"
)
if old_15 in text:
    start = text.index(old_15)
    end = text.index("$$\nHere, all block matrices in (1.5)", start)
    replacement = (
        "$$\n"
        "\\begin{aligned}\n"
        "d_M(V_I) &= \\mathrm{rank}\\, M\\!\\left(\\begin{bmatrix} P'(g_1)(x) & P'(\\mathrm{sc}_1(I) \\oplus \\mathrm{sc}(\\Uparrow I))(\\alpha) & 0 \\\\ P'(g_3)(x) & 0 & P'(\\mathrm{sk}(I))(\\alpha) \\\\ P'(g_2)(x) & 0 & 0 \\end{bmatrix}\\right) \\\\\n"
        "&\\quad - \\mathrm{rank}\\, M\\!\\left(\\begin{bmatrix} P'(g_1)(x) & P'(\\mathrm{sc}_1(I) \\oplus \\mathrm{sc}(\\Uparrow I))(\\alpha) & 0 \\\\ 0 & 0 & P'(\\mathrm{sk}(I))(\\alpha) \\\\ 0 & P'(g_2)(x) & 0 \\end{bmatrix}\\right). \\tag{1.5}\n"
        "\\end{aligned}\n"
        "$$\n\n"
    )
    text = text[:start] + replacement + text[end:]

# sc_1^circ / sk_1^circ
text = text.replace(
    "$$\n\n& s c _ { 1 } ^ { \\circ } ( I ) = \\{ a _ { i, i + 1 } \\colon = a _ { i } \\vee a _ { i + 1 } \\, | \\, i = 1, \\dots, k - 1 \\}, \\text { and } \\\\ & s k _ { 1 } ^ { \\circ } ( I ) = \\{ b _ { i, i + 1 } \\colon = b _ { i } \\wedge b _ { i + 1 } \\, | \\, i = 1 \\dots, l - 1 \\}.\n\n$$",
    "$$\n\\begin{aligned}\n\\mathrm{sc}_1^{\\circ}(I) &= \\{a_{i,i+1} \\coloneqq a_i \\vee a_{i+1} \\mid i = 1,\\dots,k-1\\}, \\\\\n\\mathrm{sk}_1^{\\circ}(I) &= \\{b_{i,i+1} \\coloneqq b_i \\wedge b_{i+1} \\mid i = 1,\\dots,l-1\\}.\n\\end{aligned}\n$$",
)

# crt_zp
text = text.replace(
    "$$\n\n\\ c r t _ { z p } ( M ) & \\coloneqq \\{ I \\in I \\ | \\ M _ { b, a } \\neq 0 \\text { for all } ( a, b ) \\in \\text {sc} ( I ) \\times \\text {sk} ( I ) \\text { with } a \\leq b \\} \\\\ & = \\{ I \\in I \\ | \\ ( \\text {sc} ( I ) \\times \\text {sk} ( I ) ) \\cap z p ( M ) = \\emptyset \\}.\n\n$$",
    "$$\n\\begin{aligned}\n\\mathrm{crt}_{zp}(M) &\\coloneqq \\{ I \\in \\mathcal{I} \\mid M_{b,a} \\neq 0 \\text{ for all } (a,b) \\in \\mathrm{sc}(I) \\times \\mathrm{sk}(I) \\text{ with } a \\leq b \\} \\\\\n&= \\{ I \\in \\mathcal{I} \\mid (\\mathrm{sc}(I) \\times \\mathrm{sk}(I)) \\cap zp(M) = \\emptyset \\}.\n\\end{aligned}\n$$",
)

# Theorem 5.1 cases (line ~1592)
text = text.replace(
    "V_{\\uparrow a} ( a_{j i} p_{j, x_{i}} ) = \\begin{cases} a_{j i} & \\text{if} a \\leq x_{i}, y_{j}, \\\\ 0 & \\text{otherwise}, \\end{cases} \\quad \\text{and} \\quad V_{\\uparrow a} ( a_{j i} p_{j, x_{i}} ) = \\begin{cases} a_{j i} & \\text{if} a < x_{i}, y_{j}, \\\\ 0 & \\text{otherwise}. \\end{cases} \\quad \\Box",
    "V_{\\uparrow a}(a_{ji} p_{j,x_i}) = \\begin{cases} a_{ji} & \\text{if } a \\leq x_i, y_j, \\\\ 0 & \\text{otherwise,} \\end{cases} \\quad \\text{and} \\quad V_{\\{a\\}}(a_{ji} p_{j,x_i}) = \\begin{cases} a_{ji} & \\text{if } a < x_i, y_j, \\\\ 0 & \\text{otherwise.} \\end{cases} \\qquad \\Box",
)

# Corrupted E_1/E_2 diagram (~1596) - replace with short prose + existing figure ref
old_e = "E_{1} \\colon \\begin{array}{c c c c c c c c} & & & [ \\frac{1}{0} ]"
if old_e in text:
    start = text.index("$$\nE_{1} \\colon \\begin{array}")
    end = text.index("$$\n\nDefine an $M", start)
    replacement = (
        "See the representation diagrams in the figure below (Example 3.37).\n\n$$E_1 \\oplus E_2$$\n\n"
    )
    text = text[:start] + replacement + text[end + 3:]

path.write_text(text, encoding="utf-8")
print("Repairs written.")
