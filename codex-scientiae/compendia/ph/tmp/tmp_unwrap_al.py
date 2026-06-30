import re
from pathlib import Path

PROSE = re.compile(
    r"^(Here|Proof|Proposition|Notation|Theorem|Remark|Summarizing|It remains|"
    r"The pushout|The canonical|Note that in|Therefore,|Hence by|where the entry|"
    r"for all |that is induced|3 We changed|of the domain|with the entries|"
    r"Here µ|Here,|of \\tau|b \\in|Here we claim|This proves|Without loss|"
    r"By \( Gabriel|By assumption|Indeed,|Since P_1|We are now|Summarizing Theorems|"
    r"Here we collect|with the entries given|where we applied|Finally,|"
    r"Also |More precisely|Thus |Now if |where \\pi :=|where \\varepsilon_E|"
    r"The pushout extends|and \\pi_1|Choose also|Choose any|The ranks of|"
    r"Indeed, recalling|We remark that|Or more directly|It is similar|"
    r"Summary of the|In this section|Additionally,|This example|One can get|"
    r"Moreover, it|Notably,|Throughout|Assume that|Remember that|"
    r"Concerning|However,|In the above|We here remark|We first|We next|"
    r"To apply|Given an|Following this|The following|If \$|Then \$|"
    r"Hence \$|and \$|with \$|where \$|respectively\.|set \\|"
    r"Fig\.|Example|Lemma|Corollary|Case |Prof\.|Declarations|"
    r"Path homology|Topological Laplacians|Construction of|Table |"
    r"Appendix\.|Side View|Top View|Figure |"
    r"where \\varepsilon|where \\psi|where \\pi|where \\nu|where \\iota|"
    r"where \\lambda|where \\eta|where \\mu|where \\zeta|where \\tilde|"
    r"where \\hat|where \\delta|where \\rho|where \\dim|where \\rank|"
    r"where \\text|where \\mathrm|where \\operatorname|where \\Hom|where \\mod|"
    r"where \\cong|where \\sim|where \\oplus|where \\coloneqq|where \\tag|"
    r"where \\Box|where \\square|where \\Leftarrow|where \\Rightarrow|"
    r"where \\longrightarrow|where \\xrightarrow|where \\stackrel|"
    r"where \\begin|where \\end|where \\left|where \\right|"
    r"where \\cdot|where \\times|where \\cap|where \\cup|where \\setminus|"
    r"where \\subset|where \\in|where \\notin|where \\emptyset|"
    r"where \\infty|where \\partial|where \\sum|where \\prod|where \\int|"
    r"where \\lim|where \\sup|where \\inf|where \\max|where \\min|"
    r"where \\det|where \\ker|where \\Im|where \\sqrt|where \\frac|"
    r"where \\over|where \\under|where \\overline|where \\underline|"
    r"where \\widehat|where \\widetilde|where \\hat|where \\tilde|"
    r"where \\bar|where \\vec|where \\math|where \\textbf|where \\textit|"
    r"where \\textrm|where \\emph|where \\mathbf|where \\mathit|where \\mathbb|"
    r"where \\mathcal|where \\mathscr|where \\mathfrak|where \\mathsf|"
    r"where \\mathtt|where \\boldsymbol|where \\bm|"
    r"where \\| |where \\, |where \\; |where \\quad|where \\qquad|"
    r"where \\cite|where \\ref|where \\label|where \\eqref|where \\pageref|"
    r"where \\footnote|where \\url|where \\href|where \\includegraphics|"
    r"where \\input|where \\include|where \\usepackage|where \\documentclass|"
    r"where \\begin\{document\}|where \\end\{document\}|where \\maketitle|"
    r"where \\author|where \\date|where \\thanks|where \\abstract|"
    r"where \\keywords|where \\affiliation|where \\email|where \\orcid|"
    r"where \\institute|where \\department|where \\address|where \\city|"
    r"where \\country|where \\postcode|where \\phone|where \\fax|where \\homepage)",
    re.I,
)
MATH = re.compile(
    r"\\[a-zA-Z]+|[_^]\s*\{|\\begin|P_\s*\{|\\coloneqq|\\oplus|"
    r"\\longrightarrow|\\xrightarrow|\\\\|&=|\\begin\{aligned\}|\\begin\{cases\}"
)


def is_math(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    first = t.split("\n", 1)[0].strip()
    if PROSE.match(first):
        return False
    if re.match(r"^[A-Za-z].{30,}", first) and not MATH.search(first[:80]):
        return False
    if not MATH.search(t):
        return False
    masked = re.sub(r"\\[a-zA-Z]+", " ", t)
    masked = re.sub(r"\$[^$]+\$", " ", masked)
    return len(re.findall(r"[A-Za-z]{4,}", masked)) <= 3


def repair(text: str) -> str:
    lines = text.split("\n")
    out, i, in_fence = [], 0, False
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            i += 1
            continue
        if in_fence or ln.strip() != "$$":
            out.append(ln)
            i += 1
            continue
        j = i + 1
        while j < len(lines) and lines[j].strip() != "$$":
            j += 1
        if j >= len(lines):
            out.append(ln)
            i += 1
            continue
        inner = "\n".join(lines[i + 1 : j]).strip()
        if not inner or not is_math(inner):
            out.extend(lines[i + 1 : j])
        else:
            if "&" in inner and "\\begin{" not in inner:
                inner = "\\begin{aligned}\n" + inner + "\n\\end{aligned}"
            out.append("$$")
            out.extend(inner.split("\n"))
            out.append("$$")
        i = j + 1
    return "\n".join(out)


p = Path(r"d:\aghado01\codex-scientiae\compendia\ph\AL2026.md")
p.write_text(repair(p.read_text(encoding="utf-8")), encoding="utf-8")
print("done")
