---
title: "UltraCore-RFT Research Hub"
description: "RFT-SIRM hub for the SU(2) fourth-moment theorem, Phi-Genesis spectral results, the Sierpiński quantum-processing architecture, and Lean-formalized financial infrastructure."
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

-   :material-layers:{ .lg .middle } **Core Development Portfolio**

    ---

    A separate page for the proposed Sierpiński QPU architecture, Lean financial-state model, SU(2) theorem, and Phi-Genesis spectral work, with the current validation boundaries made explicit.

    [Open Core Development](core-development.md)

-   :material-book-open-variant:{ .lg .middle } **Focused SU(2) dissertation**

    ---

    The exact fourth-moment trace-defect theorem, normalized limit, graph-operator definitions, Lean proof architecture, and separate H⁶/H⁸/H¹⁰ results.

    [Read the dissertation](DISSERTATION.md)

-   :material-graph:{ .lg .middle } **Phi-Genesis spectral results**

    ---

    Signed-flux graph Laplacians, Schur analysis, the proved least-eigenvalue result for $N\ge6$, and the exact limiting enclosure. Gate A and the quadratic increment law remain open.

    [Open Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis)

-   :material-chip:{ .lg .middle } **RFT-QPU-Sierpinski**

    ---

    A proposed Sierpiński/SU(2) quantum-processing architecture with a candidate two-dimensional logical subspace and a 12-transmon level-1 mapping. Pre-experimental; no fabricated or measured device is claimed.

    [Explore the QPU project](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)

-   :material-bank:{ .lg .middle } **SIRM Financial Infrastructure**

    ---

    A Lean 4 financial-state and accounting specification covering holder/GL transitions, authorization, registries, migration, replay receipts, and escrow invariants. Production deployment remains out of scope.

    [Open the financial specification](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure)

-   :material-bookshelf:{ .lg .middle } **Research monographs**

    ---

    A guide to the focused theorem dissertation and the broader recursive-operator synthesis. The two documents have different scopes.

    [Compare both monographs](monographs.md)

-   :material-chart-timeline-variant:{ .lg .middle } **Mathematical results**

    ---

    A compact register of exact formulas, recurrence thresholds, the Phi-Genesis spectral enclosure, and SIRM invariants.

    [Open the results register](results.md)

-   :material-server-network:{ .lg .middle } **Daily spectral computations**

    ---

    Reproducible nightly deep tests and high-precision A1/E spectral-matrix calculations, run from the canonical Phi-Genesis source with archived logs and commit provenance.

    [View daily computation record](phi-genesis-computations.md)

-   :material-graph:{ .lg .middle } **Interactive research explorer**

    ---

    Navigate the research map, vary the parameters in the H⁴ formula, and inspect the evidence boundary attached to each strand.

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


## Core engineering programmes

### RFT-QPU-Sierpinski — proposed logical-qubit architecture

The level-1 design maps a Sierpiński-gasket graph with 6 sites and 9 edges to 12 transmon modes and 22 effective exchange channels. Three selected non-commuting X/Y/Z SU(2) links define the graph transport, and the candidate logical qubit is a two-dimensional low-energy subspace.

The Stage 11B local retune reports a projected process overlap of 0.9999999793763371 after local-Z fitting and an average logical-state fidelity including leakage of 0.9999999803654352 at five retained levels and 480 steps per pump period. These are closed-system projections of a three-mode A–coupler–B model, **not measured gate fidelities and not a full 12-transmon-tile simulation**. The resonant complex-Z link, graph-wide multi-tone plan, open-system noise modelling, and hardware validation remain open.

Sources: [QPU project](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) · [repository status](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/REPOSITORY_STATUS.md) · [validation plan](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/docs/VALIDATION_PLAN.md).

### SIRM Financial Infrastructure — Lean 4 financial-state model

The financial repository develops a normative abstract state-transition and accounting specification. It combines holder-balance changes with matching signed general-ledger postings in one Lean state transition, and layers authorization, finite authority/control registries, typed assets/accounts, exact base-unit and migration arithmetic, per-principal nonce/receipt rules, cached authorization/insufficient-funds denials, and integrated pooled escrow, time-lock, and first-stage dispute-freeze invariants.

Its current CI design consists of one Lean build/theorem-test job and 17 independent static audits. This describes the workflow structure, not a blanket claim that every revision has passed. The repository uses Lean 4.33.1. The model does not yet prove production database persistence/atomicity, cryptographic signing, custody, reserve backing, external settlement, or Lean-to-Rust refinement; the Rust reference implementation remains planned.

Sources: [financial infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) · [formalization status](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/FORMALIZATION_STATUS.md) · [mathematical scope](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/MATHEMATICAL_SCOPE.md) · [testing guide](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/TESTING.md).

!!! note "Independent evidence boundaries"
    These engineering programmes are part of the same RFT-SIRM portfolio, but they are not consequences of the same theorem. The SU(2) trace-defect result does not certify a physical QPU; the Phi-Genesis signed-flux spectrum is a separate operator family; and Lean financial proofs apply only to the abstract model and assumptions stated in the financial repository.

## Research strands at a glance

| Strand | Primary source | Current evidence boundary |
|---|---|---|
| SU(2) fourth moment | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Lean 4 theorem for the specified operators, $m\ge1$ |
| Higher moments | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | H⁶/H⁸ recurrences for $m\ge3$ with exact finite bridges; H¹⁰ recurrence for $m\ge4$ and affine form for $m\ge5$ |
| Signed-flux spectral research | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Uniform lower bound and least-eigenvalue convergence proved in their stated scopes; Gate A remains open |
| SIRM Financial Infrastructure | [Lean specification](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) | Lean 4 model of holder/supply reconciliation, balanced holder/GL transitions, authorization, typed registries, migration, replay/receipt handling, and integrated escrow safety; production runtime and Rust refinement remain open |
| SIRM runtime model | [Foundations](foundations.md) · [Architecture](architecture.md) | Separate deterministic-runtime invariant model and implementation-specific validation |
| Quantum-processing architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Pre-experimental Sierpiński/SU(2) architecture; candidate logical subspace and 12-transmon mapping are numerical/design artifacts, not fabricated or measured hardware |
| Energy and cosmology models | [Application Programmes](application-programmes.md) | Exploratory / phenomenological; separate assumptions and validation |

!!! note "Two dissertations, two scopes"
    The [focused SU(2) dissertation](DISSERTATION.md) is a theorem-centred treatment of one operator family. The [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) surveys a wider recursive-operator programme and is dated 15 October 2026. They complement one another; neither is a claim that a complete physical Theory of Everything has been established.

## Continue through the research hub

[Research Map](research-map.md) · [Research Monographs](monographs.md) · [Mathematical Results](results.md) · [Architecture](architecture.md) · [Foundations](foundations.md) · [Application Programmes](application-programmes.md) · [AI Evidence Guide](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/AI_GUIDE.md)

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)

_Copyright 2026 Evgeniy Zaprudnov (RFT-SIRM). License: Apache 2.0._
