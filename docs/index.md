# UltraCore-RFT — Research Home

**Mathematical foundations, formal evidence, recursive spectral research, and invariant-based systems engineering.**

> 🟢 **FEATURED DISSERTATION**
>
> **[Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md)**
>
> The central research synthesis distinguishes the fourth-moment theorem, finite higher-moment certificates, numerical evidence, and open conjectures. It is a research dissertation/monograph—not a claim that a complete physical Theory of Everything has been established.

UltraCore-RFT coordinates the RFT-SIRM ecosystem. Begin with the mathematical result and its exact evidence scope; follow with the broader higher-moment and spectral-decimation programmes; then explore systems engineering and applications.

- [**Dissertation — read the research synthesis**](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md)
- [Evgeny's Theory of Everything — synthesis repository](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything)
- [Evgeny's Theorem — Lean 4 formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization)
- [Phi-Genesis — spectral audit](https://github.com/RFT-SIRM/Phi-Genesis)
- [Interactive research portal](interactive/index.html)
- [AI evidence guide](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/AI_GUIDE.md)

> **Scope:** “Theory of Everything” is the name of a broad research programme, not a claim that a complete physical theory of the Universe has been proved. The Lean-formalized result is a specific fourth-moment identity for defined operators. The all-level higher-moment recurrence and Phi-Genesis Gate A remain open.

## Research map

Use [Research Map](research-map.md) for the research hierarchy, formula, claim-status vocabulary, and open questions. The map distinguishes theorem statements, finite-level certificates, numerical evidence, engineering tests, hypotheses, and applications.

## The mathematical anchor

For the specific operator definitions and assumptions in [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), the fourth-moment trace defect is

$$
\Delta_m(H^4,\theta)
= \operatorname{Tr}(H_C^4)-\operatorname{Tr}(H_{C'}^4)
= -16\bigl(3^{m-1}+1\bigr)\sin^2\!\left(\frac{\theta}{2}\right),
\qquad m\ge 1.
$$

With the documented normalization,

$$
I_m(\theta)
= \frac{\Delta_m(H^4,\theta)}{3^{m+1}+3}
\longrightarrow
-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).
$$

At \(\theta=\pi/2\), the limiting value is \(-8/9\). The primary repository reports a Lean 4 proof for the concrete formalized operators and its stated quantifiers. This does not prove higher moments, physical laws, quantum advantage, or runtime invariants.

## Research strands

| Strand | Primary source | Status |
|---|---|---|
| Fourth-moment theorem | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Lean 4 formalization reported for stated scope |
| Higher-moment recurrence | [Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | Finite-level certificates and numerical holdouts; all-level recurrence open |
| Signed-flux spectral decimation | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Gate A remains open; claims are audited and status-labelled |
| SIRM and deterministic execution | [Foundations](foundations.md) · [Architecture](architecture.md) | Engineering model and implementation-specific evidence |
| Quantum architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Pre-experimental |
| Energy-system modelling | [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery) | Exploratory |

## Documentation

| Document | Purpose |
|---|---|
| [Research Map](research-map.md) | Mathematical hierarchy, evidence classes, open problems |
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