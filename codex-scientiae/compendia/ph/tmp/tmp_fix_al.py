from pathlib import Path

p = Path(r"d:\aghado01\codex-scientiae\compendia\ph\AL2026.md")
text = p.read_text(encoding="utf-8")

# Fix Prop 3.12 tail through Prop 3.14 (root pairing break ~line 428)
old = """$$
The equalities (3.13) and (3.14) show that the topological space U with Alexandrov topology is not connected (also by noticing Remark 3.2 (4)). Hence U is not a connected poset by Lemma 3.10, a contradiction. As a consequence, \\operatorname{sc}_1( U ) \\neq \\emptyset .
$$

( 2 ) \\text { This is shown similarly.} \\quad \\Box

$$
With the above preliminaries, we first give a projective presentation of V_U \\in \\operatorname{mod} A , where U is a connected up-set of P .
Proposition 3.13. Let U be a connected up-set of P . Then V_U has the following (not necessarily minimal) projective presentation:
$$

P _ { s c _ { 1 } ( U ) } \\stackrel { \\varepsilon _ { 1 } ^ { U } } { \\longrightarrow } P _ { s c ( U ) } \\stackrel { \\varepsilon _ { 0 } ^ { U } } { \\longrightarrow } V _ { U } \\to 0,

$$
where \\varepsilon_{0}^{U} = [ \\rho_{V_{U}} ( 1_{a} ) ]_{a \\in s c ( U )} , and we set 1_{u} \\coloneqq 1_{k} \\in k = V_{U} ( u ) for all u \\in U , and
$$

\\varepsilon _ { 1 } ^ { U } \\coloneqq [ \\tilde { P } _ { a, a _ { c } } ] _ { ( a, \\mathfrak { a } _ { c } ) \\in s c ( U ) \\times s c _ { 1 } ( U ) } \\\\

with the entries given by

$$
\\tilde { P } _ { a, a _ { c } } \\coloneqq \\begin{cases} P _ { c, a } & ( a = \\underline { a } ), \\\\ - P _ { c, a } & ( a = \\overline { a } ), \\\\ 0 & ( a \\not \\in \\mathfrak { a } ), \\end{cases} \\quad ( 3. 1 6 )
$$"""

new = """The equalities (3.13) and (3.14) show that the topological space $U$ with Alexandrov topology is not connected (also by noticing Remark 3.2 (4)). Hence $U$ is not a connected poset by Lemma 3.10, a contradiction. As a consequence, $\\operatorname{sc}_1(U) \\neq \\emptyset$.

$$
(2) \\text{ This is shown similarly.} \\quad \\Box
$$

With the above preliminaries, we first give a projective presentation of $V_U \\in \\operatorname{mod} A$, where $U$ is a connected up-set of $P$.

**Proposition 3.13.** Let $U$ be a connected up-set of $P$. Then $V_U$ has the following (not necessarily minimal) projective presentation:

$$
P_{\\mathrm{sc}_1(U)} \\stackrel{\\varepsilon_1^U}{\\longrightarrow} P_{\\mathrm{sc}(U)} \\stackrel{\\varepsilon_0^U}{\\longrightarrow} V_U \\to 0,
$$

where $\\varepsilon_0^U = [\\rho_{V_U}(1_a)]_{a \\in \\mathrm{sc}(U)}$, and we set $1_u \\coloneqq 1_k \\in k = V_U(u)$ for all $u \\in U$, and

$$
\\varepsilon_1^U \\coloneqq [\\tilde{P}_{a,a_c}]_{(a,\\mathfrak{a}_c) \\in \\mathrm{sc}(U) \\times \\mathrm{sc}_1(U)}
$$

with the entries given by

$$
\\tilde{P}_{a,a_c} \\coloneqq \\begin{cases} P_{c,a} & (a = \\underline{a}), \\\\ -P_{c,a} & (a = \\overline{a}), \\\\ 0 & (a \\notin \\mathfrak{a}), \\end{cases} \\tag{3.16}
$$"""

if old not in text:
    raise SystemExit("AL2026 block 1 not found")
text = text.replace(old, new, 1)

old2 = """**Proposition 3.14.** Let $P$ be a finite poset, and $U = U_1 \\sqcup \\cdots \\sqcup U_k$ an up-set of $P$ with $k$ connected components ($k \\geq 1$). Set $V_U \\coloneqq V_{U_1} \\oplus \\cdots \\oplus V_{U_k}$. Then $V_U$ has the following (not necessarily minimal) projective presentation:

$$

P _ { s c _ { 1 } ( U ) } \\stackrel { \\varepsilon _ { 1 } ^ { U } } { \\longrightarrow } P _ { s c ( U ) } \\stackrel { \\varepsilon _ { 0 } ^ { U } } { \\longrightarrow } V _ { U } \\to 0,

where $\\varepsilon_i^U \\coloneqq \\varepsilon_i^{U_1} \\oplus \\cdots \\oplus \\varepsilon_i^{U_k}$ ($i=0,1$). $\\square$"""

new2 = """**Proposition 3.14.** Let $P$ be a finite poset, and $U = U_1 \\sqcup \\cdots \\sqcup U_k$ an up-set of $P$ with $k$ connected components ($k \\geq 1$). Set $V_U \\coloneqq V_{U_1} \\oplus \\cdots \\oplus V_{U_k}$. Then $V_U$ has the following (not necessarily minimal) projective presentation:

$$
P_{\\mathrm{sc}_1(U)} \\stackrel{\\varepsilon_1^U}{\\longrightarrow} P_{\\mathrm{sc}(U)} \\stackrel{\\varepsilon_0^U}{\\longrightarrow} V_U \\to 0,
$$

where $\\varepsilon_i^U \\coloneqq \\varepsilon_i^{U_1} \\oplus \\cdots \\oplus \\varepsilon_i^{U_k}$ ($i=0,1$). $\\square$"""

if old2 not in text:
    raise SystemExit("AL2026 block 2 not found")
text = text.replace(old2, new2, 1)

p.write_text(text, encoding="utf-8")
print("AL2026 partial fix done")
