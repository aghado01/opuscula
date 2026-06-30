from pathlib import Path

p = Path(r"d:\aghado01\codex-scientiae\compendia\ph\WGW2023.md")
text = p.read_text(encoding="utf-8")

fig2b = '''**Construction of $L_0$ — Figure 2b.** Since $L_0 = B_1 B_1^{\\mathsf T}$, we construct $B_1 = O_0^{-1} \\tilde{M}_1 O_1$ according to Eq. (24). With edges $e_{12}$, $e_{13}$, and $e_{23}$,

$$
\\tilde{M}_1 = \\begin{array}{c@{\\quad}c@{\\quad}c@{\\quad}c}
& e_{12} & e_{13} & e_{23} \\\\
e_{12} & -1 & -1 & 0 \\\\
e_{13} & 1 & 0 & -1 \\\\
e_{23} & 0 & 1 & 1
\\end{array},
\\quad
O_1 = \\begin{pmatrix} e_{12} & e_{13} & e_{23} \\\\ e_{12} & 1 & 0 & 0 \\\\ e_{13} & 0 & 1 & 0 \\\\ e_{23} & 0 & 0 & 1 \\end{pmatrix}.
$$

Since $e_1$, $e_2$, and $e_3$ are all elementary $0$-paths (vertices), $\\tilde{M}_1 = M_1$. We have

$$
B_1 = O_0^{-1} M_1 O_1 =
\\begin{array}{c@{\\quad}c@{\\quad}c@{\\quad}c}
& e_{12} & e_{13} & e_{23} \\\\
e_1 & -1 & -1 & 0 \\\\
e_2 & 1 & 0 & -1 \\\\
e_3 & 0 & 1 & 1
\\end{array}.
$$

Then $L_0 = B_1 B_1^{\\mathsf T} = \\begin{pmatrix} 2 & -1 & -1 \\\\ -1 & 2 & -1 \\\\ -1 & -1 & 2 \\end{pmatrix}$, which gives $\\operatorname{Spectra}(L_0) = \\{0,3,3\\}$ and thus $\\beta_0 = 1$.

**Construction of $L_1$ — Figure 2b.** We have $L_1 = B_2 B_2^{\\mathsf T} + B_1^{\\mathsf T} B_1$, where $B_1$ has been formed. First, $\\mathcal{A}_2 = \\operatorname{span}\\{e_{123}\\}$ and $\\mathcal{A}_1 = \\operatorname{span}\\{e_{12}, e_{13}, e_{23}\\}$. Note that $\\partial_2(e_{123}) = e_{23} - e_{13} + e_{12}$, where $e_{12}$, $e_{23}$, and $e_{13}$ are all in $\\mathcal{A}_1$. Hence $\\Omega_2 = \\{e_{123}\\}$. We have

$$
\\tilde{M}_2 = \\begin{array}{c} e_{123} \\\\ e_{13} \\\\ e_{23} \\end{array}
\\begin{pmatrix} 1 \\\\ -1 \\\\ 1 \\end{pmatrix},
\\quad
O_2 = \\begin{pmatrix} e_{123} \\\\ e_{123} & 1 \\end{pmatrix}.
$$

The paths $e_{11}$, $e_{21}$, $e_{22}$, $e_{31}$, $e_{32}$, and $e_{33}$ are not elementary $1$-paths in $P$. Hence

$$
B_2 = O_1^{-1} \\tilde{M}_2 O_2 =
\\begin{array}{c} e_{12} \\\\ e_{13} \\\\ e_{23} \\end{array}
\\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix}.
$$

Therefore,

$$
L_1 = B_2 B_2^{\\mathsf T} + B_1^{\\mathsf T} B_1 = \\begin{pmatrix} 3 & 0 & 0 \\\\ 0 & 3 & 0 \\\\ 0 & 0 & 3 \\end{pmatrix},
$$

where $\\operatorname{Spectra}(L_1) = \\{3,3,3\\}$ and thus $\\beta_1 = 0$.

**Construction of $L_2$ — Figure 2b.** According to Eq. (26), we have $L_2 = B_3 B_3^{\\mathsf T} + B_2^{\\mathsf T} B_2$ and $B_3 = O_2^{-1} \\tilde{M}_3 O_3$. Since there is no $3$-path, $M_3$ and $O_3$ are both empty matrices. Hence $L_2 = (3)$, $\\operatorname{Spectra}(L_2) = \\{3\\}$, and thus $\\beta_2 = 0$.
'''

start = text.index("**Construction of $L_0$ — Figure 2b.**")
end = text.index("In the following section, we will omit the detailed construction steps")
text = text[:start] + fig2b + "\n\n" + text[end:]

persist = '''$$
\\beta_n^{t,s} = \\operatorname{nullity}(L_n^{t,s}) = \\text{the number of zero eigenvalues (i.e., harmonic eigenvalues) of } L_n^{t,s}.
$$

**Distance-based filtration.** Specifically, suppose $G(w) = (V,E,w)$ is a weighted digraph, where $V$ is the set of vertices and $E$ is the set of directed edges. Assume $w$ is a weight function $w : E \\to \\mathbb{R}$. For every $\\delta \\in \\mathbb{R}$, a digraph can be described as $G_\\delta = (V, E_\\delta) = (V, \\{e \\in E : w(e) \\leq \\delta\\})$, and a filtration of digraphs can be described as $\\{G_\\delta\\}_{\\delta \\in \\mathbb{R}}$.

Therefore, the persistent $n$-th path Laplacian matrix defined on the filtration is

$$
L_n^{\\delta,\\delta'} = B_{n+1}^{\\delta,\\delta'} P^{-1} (B_{n+1}^{\\delta,\\delta'})^{\\mathsf T} + (B_n^{\\delta})^{\\mathsf T} B_n^{\\delta},
$$

where its corresponding Betti numbers and spectra can be expressed as

$$
\\beta_n^{\\delta,\\delta'} = \\operatorname{nullity}(L_n^{\\delta,\\delta'}) = \\text{the number of zero eigenvalues (i.e., harmonic eigenvalues) of } L_n^{\\delta,\\delta'},
$$

$$
\\operatorname{Spectra}(L_n^{\\delta,\\delta'}) = \\{(\\lambda_1)_n^{\\delta,\\delta'}, (\\lambda_2)_n^{\\delta,\\delta'}, \\ldots, (\\lambda_N)_n^{\\delta,\\delta'}\\}.
$$
'''

old_persist_start = text.index("\\beta _ { n } ^ { t, s } & = \\text {nullity}")
old_persist_end = text.index("Notably, the Fiedler value")
text = text[:old_persist_start] + persist + "\n" + text[old_persist_end:]

p.write_text(text, encoding="utf-8")
print("WGW2023 fixed")
