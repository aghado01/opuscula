from pathlib import Path
import re

path = Path(__file__).resolve().parent.parent / "AL2026.md"
text = path.read_text(encoding="utf-8")

replacement = """Remark 3.36. We set $M(\\varepsilon_1) = M(\\varepsilon_1)_1, M(\\varepsilon_1)_2$ and $M(\\pi_1) = M(\\pi_1)_1, M(\\pi_1)_2$, where $M(\\varepsilon_1)_1$ has $\\dim M(a_1)$ columns and $M(\\pi_1)_1$ has $\\dim M(b_1)$ rows. Then the matrix $R(M,I)$ in the first term of (3.42) has the following form:

$$
R(M,I) = \\begin{bmatrix} M(\\varepsilon_1)_1 & M(\\varepsilon_1)_2 & 0 \\\\ M_{b_1,a_1} & 0 & M(\\pi_1)_1 \\\\ 0 & 0 & M(\\pi_1)_2 \\end{bmatrix}.
$$

We denote by $E_r$ the identity matrix of rank $r$. By elementary column transformations within the second block column and elementary row transformations within the first block row, we can transform $M(\\varepsilon_1)_2$ to the normal form $E_{r_1} \\oplus 0$; and by elementary column transformations within the third block column and elementary row transformations within the third block row, we can transform $M(\\pi_1)_2$ to the normal form $E_{r_2} \\oplus 0$. After further row and column operations on $M_1$ and $M_3$, one obtains $\\rank R(M,I) = \\rank M_d + r_1 + r'_1 + r_2 + r'_2$, with $\\rank M(\\varepsilon_1) = r_1 + r'_1$ and $\\rank M(\\pi_1) = r_2 + r'_2$, hence

$$
d_M(V_I) = \\rank M_d.
$$

Example 3.37. In the following diagrams, let $P = G_{4,2}$ be given by the quiver on the left, and $M \\in \\operatorname{mod} A$ be given by the diagram on the right:

![Example 3.37: poset $G_{4,2}$ and module $M$](AL2026/imageFile5.png)

Let $I := [{2,1'},{4,3'}]$ be an interval of $P$. Then $\\dim V_I := [1\\ 1\\ 1\\ 0\\ 0\\ 1\\ 1\\ 1]$, and $a_1 = 2$, $a_2 = 1'$, $a_{12} = 2'$, $b_1 = 4$, $b_2 = 3'$, $b_{12} = 3$, $a'_1 = 4'$, $b'_1 = 1$. Therefore,

$$
\\begin{aligned}
R(M,I) &= \\begin{bmatrix} M_{a_{12},a_1} & -M_{a_{12},a_2} & 0 & 0 \\\\ M_{a'_1,a_1} & 0 & 0 & 0 \\\\ M_{b_1,a_1} & 0 & M_{b_1,b'_1} & M_{b_1,b_{12}} \\\\ 0 & 0 & 0 & -M_{b_2,b_{12}} \\end{bmatrix} \\\\
&\\sim \\begin{bmatrix} M_{2,2} & -M_{2,1'} & 0 & 0 \\\\ M_{4',2} & 0 & 0 & 0 \\\\ 0 & 0 & M_{4,1} & M_{4,3} \\\\ 0 & 0 & 0 & -M_{3',3} \\end{bmatrix}.
\\end{aligned}
$$

Hence $d_M(V_I) = 2$. Noting that $M \\simeq V_I^2 \\oplus V_I \\oplus V_I$, we see that this gives a correct value. Define another $M' \\in \\operatorname{mod} A$ from $M$ by changing the linear maps $M_{4',3'}$ and $M_{4',4'}$ to be $\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}$ and $\\begin{bmatrix} 1 & 0 & 0 \\end{bmatrix}$, respectively. Then

![image 5](AL2026/imageFile5.png)

Hence $d_{M'}(V_I) = 1$, which coincides with the answer obtained from the decomposition $M' \\cong V_I \\oplus V_{[1,4]} \\oplus V_{[{2,1'},4']}$. These decompositions can be easily seen by drawing the structure quivers of $M$, $M'$:

![image 6](AL2026/imageFile6.png)

where $M$ is given by solid arrows, and $M'$ is given by both solid and broken arrows, bases of $M(i)$ are denoted by $i$ or $i_a$ ($a \\in \\{x, y, z\\}$) for all $i \\in P$.

"""

pattern = re.compile(
    r"Remark 3\.36\..*?(?=### 3\.3 Reducing candidates)",
    re.DOTALL,
)
m = pattern.search(text)
if m:
    text = text[: m.start()] + replacement + text[m.end() :]
    print("Replaced Remark 3.36 through Example 3.37")
else:
    print("Pattern not found")

def fix_p_uv(match):
    return """$$
\\begin{aligned}
P'(u)(v) &= P'(u)(v_1) \\oplus \\cdots \\oplus P'(u)(v_n) \\\\
&= P'_{u_1}(v_1) \\oplus \\cdots \\oplus P'_{u_m}(v_1) \\oplus P'_{u_1}(v_2) \\oplus \\cdots \\oplus P'_{u_m}(v_n).
\\end{aligned}
$$"""

text, n = re.subn(
    r"\$\$\n\\begin\{aligned\}\n\$\$\n\n\\begin\{aligned\} P \^ \{ \\prime \} \( u \) \( v \).*?\\end\{aligned\}\n\n\$\$\n\\end\{aligned\}\n\$\$",
    fix_p_uv,
    text,
    count=1,
    flags=re.DOTALL,
)
print("P'(u)(v) fixes:", n)

path.write_text(text, encoding="utf-8")
print("done")
