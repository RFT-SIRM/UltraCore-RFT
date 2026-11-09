# Research Monographs

UltraCore-RFT links two complementary research dissertations maintained in their primary repositories. They address related graph-operator themes, but they do not make the same theorem claims.

## 1. Focused mathematical dissertation

**[Spectral Trace Defects of Noncommutative SU(2) Connections on Sierpiński-Gasket Graphs](DISSERTATION.md)**

**Primary project:** [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)  
**Date:** 9 November 2026 (UltraCore edition)  
**Scope:** the specified non-commuting SU(2)-connected operator on Sierpiński-gasket graphs and its commuting control.

The central result is the exact fourth-moment trace-defect identity

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right),
\qquad m\ge1,\ \theta\in\mathbb R.
$$

After normalization by the Hilbert-space dimension $3^{m+1}+3$,

$$
I_\infty(\theta)
=\lim_{m\to\infty}
\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3}
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

The focused UltraCore dissertation is a theorem-centred edition prepared from the primary source records. The machine-checked Lean declarations, computational scripts, and detailed source history remain in [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem). It also documents the distinct proof status of H⁶, H⁸, and H¹⁰. The H⁴ statement is the primary all-level theorem; higher moments must be cited at their own levels and with their own proof boundaries.

**Primary verification sources:** [THEOREM.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [VERIFICATION.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · [higher-moment status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md).

## 2. Broader synthesis dissertation

**[Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md)**

**Primary project:** [RFT-SIRM/Evgeny-s-Theory-of-Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything)  
**Date in source document:** 15 October 2026  
**Scope:** a broader research synthesis covering recursive graph operators, trace-defect moments, finite Fourier-coefficient certificates, numerical recurrence checks, and a separate signed $Z_2$-flux spectral-decimation programme.

This document is a dated research snapshot. Its discussion of proof status predates some later formal results in the primary repositories. For current status, consult [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) and [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis), rather than treating the older synthesis text as a live status dashboard.

## 3. Keep the mathematical strands distinct

- The SU(2) fourth-moment theorem is a statement about its specified connection operators and commuting control.
- The higher-moment programme has separate H⁶/H⁸/H¹⁰ results and finite-certificate boundaries.
- Phi-Genesis proves a separate least-eigenvalue/convergence theorem for signed and signless graph Laplacians at levels $N\ge6$. Its Gate A exceptional-set problem and external $\theta=2\pi$ identification remain open.
- No equivalence between the SU(2) operators and the signed $Z_2$-flux operators is claimed.

The focused theorem dissertation is maintained in this repository as the UltraCore edition; its formal proof artifacts remain canonical in [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem). The broader synthesis dissertation remains canonical in its own repository. This page is the navigation guide between the two distinct documents.

---

[Research Map](research-map.md) · [Scientific Basis](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/SCIENTIFIC_BASIS.md) · [UltraCore README](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/README.md)
