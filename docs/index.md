---
title: "UltraCore-RFT research hub"
description: "Research hub for the SU(2) fourth-moment trace-defect theorem, higher spectral moments, the Phi-Genesis graph-Laplacian lower bound and limiting eigenvalue near 1.3091289, and SIRM engineering research."
keywords:
  - SU(2) fourth-moment trace-defect theorem
  - Sierpiński-gasket graph spectrum
  - Phi-Genesis least eigenvalue
  - spectral limit 1.309128920280813421888623088170810188
  - higher spectral moments H6 H8 H10
  - SIRM runtime invariants
---

# UltraCore-RFT — Research Home

**Mathematical foundations, formal evidence, recursive spectral research, and invariant-based systems engineering.**

> **TWO RESEARCH DISSERTATIONS — DIFFERENT SCOPES**
>
> **Focused theorem:** [Spectral Trace Defects of Noncommutative SU(2) Connections on Sierpiński-Gasket Graphs](DISSERTATION.md) — the SU(2) operator construction, the all-level H⁴ identity, its normalized limit, and the separately scoped H⁶/H⁸/H¹⁰ results. Its machine-checked source is [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).
>
> **Broader synthesis:** [Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) — the wider recursive-operator programme, finite higher-moment certificates, numerical checks, and open questions. The source version is dated 15 October 2026; consult the individual repositories for later updates.
>
> See the [Research Monographs guide](monographs.md). The two documents complement one another and should not be treated as one theorem.

UltraCore-RFT coordinates the RFT-SIRM ecosystem. Begin with the mathematical result and its exact evidence scope; follow with the broader higher-moment and spectral-decimation programmes; then explore systems engineering and applications.

- [**Dissertation — read the research synthesis**](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md)
- [Evgeny's Theory of Everything — synthesis repository](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything)
- [Evgeny's Theorem — Lean 4 formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization)
- [Phi-Genesis — spectral audit](https://github.com/RFT-SIRM/Phi-Genesis)
- [Interactive research portal](interactive/index.html)
- [AI evidence guide](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/AI_GUIDE.md)

> **Scope:** “Theory of Everything” is the name of a broad research programme, not a claim that a complete physical theory of the Universe has been proved. The SU(2) H⁴ identity is Lean-formalized for its stated operators. H⁶/H⁸ have Lean recurrences from $m\ge3$ plus exact finite bridges; H¹⁰ has a Lean recurrence from $m\ge4$ and affine form from $m\ge5$. Phi-Genesis separately proves least-eigenvalue convergence for its signed/signless graph matrices at $N\ge6$; Gate A and the quadratic increment law remain open.

## Research map

Use [Research Map](research-map.md) for the research hierarchy, formula, claim-status vocabulary, and open questions. The map distinguishes theorem statements, finite-level certificates, numerical evidence, engineering tests, hypotheses, and applications.

## The mathematical anchor

For the specific operator definitions and assumptions in [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), the fourth-moment trace defect is

$$
\Delta_m(H^4,\theta)
= \mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
= -16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right),
\qquad m\geq 1.
$$

With the documented normalization, the intensive invariant is

$$
I_m(\theta)
= \frac{\Delta_m(H^4,\theta)}{3^{m+1}+3}
\longrightarrow -\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

At `theta = pi/2`, the limiting value is `-8/9`. The primary repository reports a Lean 4 proof for the concrete formalized operators and its stated quantifiers. The focused theorem dissertation is [available here](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md). This does not prove physical laws, quantum advantage, or runtime invariants.

## A separate formal spectral result: Phi-Genesis

For the signless Laplacian $Q_N$ of the level-$N$ Sierpiński-gasket graph and its gauge-conjugate signed matrix, Lean proves for $N\ge6$ that the least eigenvalue is the unique A1 Schur root in the bootstrap interval and that the sequence of least eigenvalues converges. The limit lies in the exact rational interval

$$
\left[
\frac{1309128920280813421888623088170810187}{10^{36}},
\frac{1309128920280813421888623088170810189}{10^{36}}
\right].
$$

The interval width is $2\times10^{-36}$; no closed form is claimed. The [eigenvalue theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean), [signed transfer theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean), [PR #31](https://github.com/RFT-SIRM/Phi-Genesis/pull/31), and [PR #32](https://github.com/RFT-SIRM/Phi-Genesis/pull/32) contain the formal record.

This is a separate signed-flux graph problem, not a bridge to the SU(2) operators. Gate A, the quadratic increment law, levels $N<6$, and the external $\theta=2\pi$ identification remain open.

## Research strands

| Strand | Primary source | Status |
|---|---|---|
| Fourth-moment theorem | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Lean 4 formalization reported for stated scope |
| Higher-moment results | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) · [Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | H⁶/H⁸ recurrences for $m\ge3$ plus finite bridges; H¹⁰ recurrence for $m\ge4$ and affine form for $m\ge5$; a unified general recurrence remains open |
| Signed-flux spectral research | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Least-eigenvalue identification and convergence proved in Lean for $N\ge6$; Gate A and further extensions remain open |
| SIRM and deterministic execution | [Foundations](foundations.md) · [Architecture](architecture.md) | Engineering model and implementation-specific evidence |
| Quantum architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Pre-experimental |
| Energy-system modelling | [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery) | Exploratory |

## Documentation

| Document | Purpose |
|---|---|
| [Research Map](research-map.md) | Mathematical hierarchy, evidence classes, open problems |
| [Research Monographs](monographs.md) | Two separate dissertations and their source-of-truth repositories |
| [Platform](platform.md) | Execution architecture and strategic identity |
| [Architecture](architecture.md) | Components, interfaces, design decisions |
| [Foundations](foundations.md) | SIRM model and invariant definitions |
| [Implementation](implementation.md) | Engineering implementation details |
| [Field Trials](field_trials.md) | Runtime test evidence and limitations |
| [seL4 CDT Verification](field_trials_sel4.md) | Complementary stress-testing of a specific subsystem |
| [Strategy](strategy.md) | Engineering roadmap |
| [Glossary](glossary.md) | Terminology |
| [Support](support.md) | Research collaboration and support |
| [AI Guide](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/AI_GUIDE.md) | Guardrails for automated summaries |

## Ecosystem

The organization-wide [RFT-SIRM portal](https://rft-sirm.github.io/) remains intact and continues to serve as the shared entry point. UltraCore-RFT provides its own research-focused navigation and does not replace the main portal.

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)

_Copyright 2026 Evgeniy Zaprudnov (RFT-SIRM). License: Apache 2.0._