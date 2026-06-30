Now I can see exactly what's going on. Both papers have **full, real content** — the issue is purely indexing:

**PNV20XX** (Persistent Nerves Revisited) — sections: Introduction, Background, Results (+ Theorem 1, the ε-good-cover nerve bound). 
**HBM-44-4637** (fMRI brain networks) — full structure: Abstract, Introduction, Related Work, Methods (+ 6 subsections), Results, Discussion, Conclusion.

But in both: (a) the per-paper `## Contents` is **misplaced at the end** (PNV20XX line 49 after Results; HBM line 505 after Conclusion) instead of below the title per STANDARDS §6, and (b) the **top-level `_CONTENTS.md` lists only their `References`** — none of the sections above. So the two most-recently-promoted papers are effectively invisible in the telescoping index.

## Review summary

**Good shape, as you said:** the header corruption is gone from the main papers, and the zigzag line is all promoted and clean —
- **Z5**: `2103.07353` (graph-zigzag) ✅ in, clean, I've read the algorithm
- **Z3-relevant**: `2105.03629` (involuted-homology reps) ✅ in
- zigzag family: CDSM2009, 2204.11080 (FastZigzag), DLST2026 (Conley-Morse), DS2026 (quasi-zigzag), FH2024, GVPB2025 — all present

**Two real gaps (the just-promoted pair):** PNV20XX and HBM-44-4637 are under-indexed — misplaced `## Contents` + top-level entry showing only References. That's a §6 repair (move/populate each paper's Contents, fix the two top-level entries).

**Minor cosmetic** (you may already consider these acceptable): QW2024's chapter *sections* are still flattened to `##` (should be `###` under each `## CHAPTER N`); a few `_CONTENTS` sub-entries are indented one space short (AL2026 3.1.1, FH2024 2.2.1, KGW2026); 2412.02591's `Abstract` is indented.

