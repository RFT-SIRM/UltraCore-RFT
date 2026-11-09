---
title: "UltraCore-RFT Research Hub"
description: "Research hub for the SU(2) fourth-moment theorem, higher spectral moments, the Phi-Genesis signed graph-Laplacian results, and invariant-based systems engineering."
keywords:
  - SU(2) fourth-moment trace-defect theorem
  - Sierpiński-gasket graph spectrum
  - Phi-Genesis least eigenvalue
  - higher spectral moments H6 H8 H10
  - SIRM runtime invariants
---

# UltraCore-RFT Research Hub

<p class="uc-lead">Mathematical foundations, formal evidence, recursive spectral research, and invariant-based systems engineering — presented as distinct workstreams with explicit proof boundaries.</p>

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **Focused SU(2) dissertation**

    ---

    The exact fourth-moment trace-defect theorem, normalized limit, graph-operator definitions, Lean proof architecture, and separate H⁶/H⁸/H¹⁰ results.

    [Read the dissertation](DISSERTATION.md)

-   :material-bookshelf:{ .lg .middle } **Research monographs**

    ---

    A guide to the focused theorem dissertation and the broader recursive-operator synthesis. The two documents have different scopes.

    [Compare both monographs](monographs.md)

-   :material-chart-timeline-variant:{ .lg .middle } **Mathematical results**

    ---

    A compact register of exact formulas, recurrence thresholds, the Phi-Genesis spectral enclosure, and SIRM invariants.

    [Open the results register](results.md)

-   :material-graph:{ .lg .middle } **Interactive research explorer**

    ---

    Navigate the research map, vary the parameters in the H⁴ formula, and inspect the evidence boundary attached to each strand.

    [Open the interactive portal](https://rft-sirm.github.io/UltraCore-RFT/interactive/)

</div>

## The central SU(2) result

For the specific non-commuting SU(2) connection $C$ and commuting control $C'$ defined in [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), the fourth-moment trace defect is

$$
\boxed{
\Delta_m^{(4)}(\theta)
=\mathrm{Tr}\!\left(H_C(m,\theta)^4\right)
-\mathrm{Tr}\!\left(H_{C'}(m,\theta)^4\right)
=-16\left(3^{m-1}+1\right)\sin^2\!\left(\frac{\theta}{2}\right),
\quad m\ge1.
}
$$

After normalization by the Hilbert-space dimension $3^{m+1}+3$, the exact finite-level expression and its limit are

$$
I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right)
-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right),
\qquad
I_\infty(\theta)=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).
$$

At $\theta=\pi/2$, the limiting value is exactly $-8/9$. The primary repository contains the Lean 4 declaration, its dependencies, and the verification record. The focused theorem is not a proof of the other research strands.

## A separate formal spectral result: Phi-Genesis

For the explicitly defined signed Laplacian, every real eigenvalue with a nonzero real eigenvector satisfies $\lambda\ge1$ at every refinement level. Separately, for the signless graph Laplacians $Q_N$ and their gauge-conjugate signed matrices, Lean identifies the least eigenvalue for $N\ge6$ and proves convergence to a limit in the exact interval

$$
\boxed{
\frac{1309128920280813421888623088170810187}{10^{36}}
\le\lambda_\infty\le
\frac{1309128920280813421888623088170810189}{10^{36}}.
}
$$

The interval width is exactly $2\times10^{-36}$. The midpoint is approximately $1.309128920280813421888623088170810188$. This is the limiting least eigenvalue for the specified graph-matrix sequence, not a known closed-form or universal physical constant. Gate A, the quadratic increment law, levels $N<6$, and external $\theta=2\pi$ identification remain open. See the [Mathematical Results register](results.md) and [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis).

## Research strands at a glance

| Strand | Primary source | Current evidence boundary |
|---|---|---|
| SU(2) fourth moment | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Lean 4 theorem for the specified operators, $m\ge1$ |
| Higher moments | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | H⁶/H⁸ recurrences for $m\ge3$ with exact finite bridges; H¹⁰ recurrence for $m\ge4$ and affine form for $m\ge5$ |
| Signed-flux spectral research | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Uniform lower bound and least-eigenvalue convergence proved in their stated scopes; Gate A remains open |
| SIRM runtime model | [Foundations](foundations.md) · [Architecture](architecture.md) | Independent invariant model and implementation-specific validation |
| Quantum architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Pre-experimental |
| Energy and cosmology models | [Application Programmes](application-programmes.md) | Exploratory / phenomenological; separate assumptions and validation |

!!! note "Two dissertations, two scopes"
    The [focused SU(2) dissertation](DISSERTATION.md) is a theorem-centred treatment of one operator family. The [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) surveys a wider recursive-operator programme and is dated 15 October 2026. They complement one another; neither is a claim that a complete physical Theory of Everything has been established.

## Continue through the research hub

[Research Map](research-map.md) · [Research Monographs](monographs.md) · [Mathematical Results](results.md) · [Architecture](architecture.md) · [Foundations](foundations.md) · [Application Programmes](application-programmes.md) · [AI Evidence Guide](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/AI_GUIDE.md)

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)

_Copyright 2026 Evgeniy Zaprudnov (RFT-SIRM). License: Apache 2.0._
