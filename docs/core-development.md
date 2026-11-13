---
title: "Core Development Portfolio"
description: "Sierpiński-first research and engineering across quantum architecture, formal financial models, mathematical theorems, and spectral graph research."
keywords:
  - RFT-SIRM core development
  - Sierpiński quantum-processing architecture
  - Lean formal financial infrastructure
  - SU(2) trace-defect theorem
  - Phi-Genesis spectral research
---

# Core Development Portfolio

<p class="uc-lead">Sierpiński-first research and engineering, connected by shared mathematical interests but kept in separate repositories with independent definitions, validation plans, and evidence boundaries.</p>

This is a **separate page** from the [interactive Research Explorer](https://rft-sirm.github.io/UltraCore-RFT/interactive/). The Explorer remains focused on mathematical results and interactive inspection; this page is the portfolio view of the active engineering and formalization programmes.

## Flagship architecture

<div class="grid cards" markdown>

-   :material-chip:{ .lg .middle } **RFT-QPU-Sierpinski**

    ---

    A proposed logical-qubit architecture built on a self-similar Sierpiński-gasket graph with non-commuting SU(2) edge transport. The level-1 design record specifies 6 graph sites, 9 edges, 3 selected X/Y/Z links, 12 transmon modes, and 22 non-zero effective exchange channels. A two-dimensional low-energy subspace is the candidate logical qubit.

    [Repository](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) · [Status](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/REPOSITORY_STATUS.md) · [Validation plan](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/docs/VALIDATION_PLAN.md)

</div>

!!! warning "QPU evidence boundary"
    The current Stage 11B gate study is a re-quantized **three-mode A–coupler–B model**, not a driven simulation of the complete 12-mode tile. Reported overlap and fidelity values are closed-system model outputs, not measured gate fidelities. The raw JSON/NPZ artifacts for the local retune are not yet tracked; a reproducing runner and archived artifacts are required before that retune is a fully reproducible public release. No chip has been fabricated or measured.

## Mathematical and formal foundations

<div class="grid cards" markdown>

-   :material-bank:{ .lg .middle } **SIRM Financial Infrastructure**

    ---

    A Lean 4 financial-state and accounting specification covering supply/holder reconciliation, paired holder and general-ledger transitions, authorization, typed registries, exact migration arithmetic, replay receipts, and integrated pooled escrow safeguards.

    The current dispute layer formalizes authorized intake and a per-record safety freeze. It does **not** formalize adjudication, evidence authenticity, appeals, or final beneficiary/refund settlement. The model is not a deployed financial service.

    [Repository](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) · [Formalization status](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/FORMALIZATION_STATUS.md) · [Mathematical scope](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/MATHEMATICAL_SCOPE.md)

-   :material-function-variant:{ .lg .middle } **Evgeny's Theorem**

    ---

    The specified non-commuting SU(2) operators on Sierpiński-gasket graphs have an all-angle fourth-moment trace-defect identity, Lean-checked for every refinement level \(m\ge1\).

    Higher moments have narrower boundaries: H⁶ and H⁸ recurrences are Lean-formalized for \(m\ge3\), while their finite \(m=2\to3\) bridges are exact certificates but not yet Lean-kernel theorems. H¹⁰ has a Lean recurrence for \(m\ge4\) and affine form for \(m\ge5\); its level-five correction remains an exact trace expression.

    [Repository](https://github.com/RFT-SIRM/Evgeny-Theorem) · [Verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · [Higher-moment status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md)

-   :material-chart-line:{ .lg .middle } **Phi-Genesis**

    ---

    Spectral research on signed-flux graph Laplacians, Schur analysis, and the specified Sierpiński graph-matrix sequences. The repository records a formally verified least-eigenvalue identification and convergence result for its stated sequence at \(N\ge6\), with an exact rational enclosure.

    Gate A and the quadratic increment law remain open. Other finite-level searches, estimates, and numerical studies retain their own narrower evidence classifications; they are not automatically Lean theorems.

    [Repository](https://github.com/RFT-SIRM/Phi-Genesis) · [Verified results and evidence boundaries](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/docs/verified-results.md) · [Open problems](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/docs/open-problems.md)

</div>

## Shared engineering standard

The four programmes are coordinated under RFT-SIRM, but their results are **not interchangeable**. A theorem for one operator family does not establish a result for another; a circuit model does not establish hardware performance; and a Lean financial-state model does not establish production custody, reserves, settlement, legal status, or runtime correctness.

Each source repository remains authoritative for the exact statement, formal proof, finite certificate, numerical experiment, validation gate, and remaining limitations.

## Continue

[Interactive Research Explorer](https://rft-sirm.github.io/UltraCore-RFT/interactive/) · [Research Map](research-map.md) · [Mathematical Results](results.md) · [Documentation Home](index.md)
