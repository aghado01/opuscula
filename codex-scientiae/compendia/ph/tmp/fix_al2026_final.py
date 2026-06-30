from pathlib import Path
import re

path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")

# Fix Remark 5.8 P'(u)(v) block
old1 = """$$
\\begin{aligned}
$$

\\begin{aligned} P ^ { \\prime } ( u ) ( v ) = P ^ { \\prime } ( u ) ( v _ { 1 } ) \\oplus \\cdots \\oplus P ^ { \\prime } ( u ) ( v _ { n } ) = P ^ { \\prime } _ { u _ { 1 } } ( v _ { 1 } ) \\oplus \\cdots \\oplus P ^ { \\prime } _ { u _ { m } } ( v _ { 1 } ) \\oplus P ^ { \\prime } _ { u _ { 1 } } ( v _ { 2 } ) \\oplus \\cdots \\oplus \\\\ P ^ { \\prime } _ { u _ { m } } ( v _ { 2 } ) \\oplus \\cdots \\oplus P ^ { \\prime } _ { u _ { 1 } } ( v _ { n } ) \\oplus \\cdots \\oplus P ^ { \\prime } _ { u _ { m } } ( v _ { n } ).
\\end{aligned}


$$
\\end{aligned}
$$"""

new1 = """$$
\\begin{aligned}
P'(u)(v) &= P'(u)(v_1) \\oplus \\cdots \\oplus P'(u)(v_n) \\\\
&= P'_{u_1}(v_1) \\oplus \\cdots \\oplus P'_{u_m}(v_1) \\oplus P'_{u_1}(v_2) \\oplus \\cdots \\oplus P'_{u_m}(v_n).
\\end{aligned}
$$"""

if old1 in text:
    text = text.replace(old1, new1, 1)
    print("fixed P'(u)(v) block")
else:
    print("P'(u)(v) pattern not found")

# Fix Proposition 3.14 prose-in-math
old2 = """$$

P _ { s c _ { 1 } ( U ) } \\stackrel { \\varepsilon _ { 1 } ^ { U } } { \\longrightarrow } P _ { s c ( U ) } \\stackrel { \\varepsilon _ { 0 } ^ { U } } { \\longrightarrow } V _ { U } \\to 0,

where $\\varepsilon_i^U \\coloneqq \\varepsilon_i^{U_1} \\oplus \\cdots \\oplus \\varepsilon_i^{U_k}$ ($i=0,1$). $\\square$"""

new2 = """$$
P_{\\mathrm{sc}_1(U)} \\stackrel{\\varepsilon_1^U}{\\longrightarrow} P_{\\mathrm{sc}(U)} \\stackrel{\\varepsilon_0^U}{\\longrightarrow} V_U \\to 0,
$$

where $\\varepsilon_i^U \\coloneqq \\varepsilon_i^{U_1} \\oplus \\cdots \\oplus \\varepsilon_i^{U_k}$ ($i=0,1$). $\\square$"""

if old2 in text:
    text = text.replace(old2, new2, 1)
    print("fixed Prop 3.14")
else:
    print("Prop 3.14 pattern not found")

# Fix Example 3.37 R(M,I) block - extract prose, wrap in aligned
old3 = re.compile(
    r"\$\$\n\n1, a _ \{ 1 2 \} & = 2.*?^\$\$\nHence d",
    re.MULTILINE | re.DOTALL,
)
new3 = """Let $a_1 = 2$, $a_2 = 1'$, $a_{12} = 2'$, $b_1 = 4$, $b_2 = 3'$, $b_{12} = 3$, $a'_1 = 4'$, $b'_1 = 1$. Therefore,

$$
\\begin{aligned}
R(M,I) &= \\begin{bmatrix} M_{a_{12},a_1} & -M_{a_{12},a_2} & 0 & 0 \\\\ M_{a'_1,a_1} & 0 & 0 & 0 \\\\ M_{b_1,a_1} & 0 & M_{b_1,b'_1} & M_{b_1,b_{12}} \\\\ 0 & 0 & 0 & -M_{b_2,b_{12}} \\end{bmatrix} \\\\
&\\sim \\begin{bmatrix} M_{2,2} & -M_{2,1'} & 0 & 0 \\\\ M_{4',2} & 0 & 0 & 0 \\\\ 0 & 0 & M_{4,1} & M_{4,3} \\\\ 0 & 0 & 0 & -M_{3',3} \\end{bmatrix}.
\\end{aligned}
$$

Hence $d_M(V_I) = 2$. Noting that $M \\simeq V_I^2 \\oplus V_I \\oplus V_I$, we see that this gives a correct value. Define another $M' \\in \\operatorname{mod} A$ from $M$ by changing the linear maps $M_{4',3'}$ and $M_{4',4'}$ to be $\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}$ and $\\begin{bmatrix} 1 & 0 & 0 \\end{bmatrix}$, respectively. Then

Hence d"""

m3 = old3.search(text)
if m3:
    text = text[: m3.start()] + new3 + text[m3.end() :]
    print("fixed Example 3.37 R(M,I)")
else:
    print("Example 3.37 R(M,I) pattern not found")

# Fix Remark 3.36 section - extract prose from $$ wrappers
replacements = [
    (
        "$$\nRemark 3.36. We set M ( \\varepsilon 1 )",
        "Remark 3.36. We set $M(\\varepsilon_1) = M(\\varepsilon_1)_1, M(\\varepsilon_1)_2$ and $M(\\pi_1) = M(\\pi_1)_1, M(\\pi_1)_2$, where $M(\\varepsilon_1)_1$ has $\\dim M(a_1)$ columns and $M(\\pi_1)_1$ has $\\dim M(b_1)$ rows. Then the matrix $R(M,I)$ in the first term of (3.42) has the following form:\n\n$$",
    ),
    (
        "$$\nWe denote by E r the identity matrix",
        "We denote by $E_r$ the identity matrix",
    ),
    (
        "$$\nIn the same way, we can transform M 1 and M 3",
        "In the same way, we can transform $M_1$ and $M_3$ to the normal forms:\n\n$$",
    ),
    (
        "$$\nbecause rank R ( M,I ) = rank M d",
        "because $\\operatorname{rank} R(M,I) = \\operatorname{rank} M_d + r_1 + r'_1 + r_2 + r'_2$, $\\operatorname{rank} M(\\varepsilon_1) = r_1 + r'_1$, and $\\operatorname{rank} M(\\pi_1) = r_2 + r'_2$.\n\n",
    ),
    (
        "$$\nLet I : = [{2, 1 '},{4, 3 '} ]",
        "Let $I := [{2,1'},{4,3'}]$ be an interval of $P$. Then $\\dim V_I := [1\\ 1\\ 1\\ 0\\ 0\\ 1\\ 1\\ 1]$, and ",
    ),
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new, 1)
        print("fixed:", old[:40])

path.write_text(text, encoding="utf-8")
print("done")
