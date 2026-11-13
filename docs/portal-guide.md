---
title: "Interactive Research Portal Guide"
description: "How to use the UltraCore-RFT interactive research explorer and where each visualized result is verified."
keywords:
  - interactive research explorer
  - theorem explorer
  - mathematical evidence portal
---

# Interactive Research Portal

The [UltraCore-RFT Research Explorer](https://rft-sirm.github.io/UltraCore-RFT/interactive/) is the visual entry point to the research programme. It complements the documentation; it does not replace the primary repositories, Lean proof files, or verification reports.

## Separate pages, separate purposes

The Research Explorer remains a dedicated interactive page. The [Core Development Portfolio](core-development.md) is a separate documentation page for the active engineering and formalization programmes. It is linked from the **Core Development** navigation group and is not appended to the Explorer page.

## What the portal contains

- **Research monographs:** direct routes to the focused SU(2) dissertation and the broader recursive-operator synthesis.
- **Formula explorer:** choose the angle $\theta$ and refinement level $m$ to inspect numerical evaluations of the exact fourth-moment formula, its normalized finite-level value, and the limiting expression.
- **Higher moments:** separate H⁶, H⁸, and H¹⁰ recurrence scopes and their finite-bridge boundaries.
- **Phi-Genesis:** the signed-Laplacian lower bound, least-eigenvalue convergence interval, derivative recursion, and open Gate A questions.
- **SIRM:** a separate invariant-based runtime model and its engineering evidence.
- **Evidence pathway:** a navigable checklist from definitions and proof to reproduction, audit, and application.

## Interpreting the formula explorer

The controls evaluate the closed expression

$$
\Delta_m^{(4)}(\theta)
=-16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right)
$$

and its normalized form. The displayed decimal outputs are an interactive numerical preview of that formula. They are not a replacement for its Lean proof and do not constitute a new numerical experiment or an independent proof.

## Evidence remains source-linked

The portal intentionally does not display invented live CI counters or automatically infer project status. Use the links on each result card to inspect the canonical theorem, Lean formalization, test workflow, research note, or implementation report.

The SU(2) connection operators, the signed $Z_2$-flux graph matrices, and SIRM runtime invariants are distinct strands. A relationship between them requires a separately stated operator map or engineering argument.

---

[Back to Documentation Home](index.md) · [Mathematical Results](results.md) · [Research Map](research-map.md) · [Open the Research Explorer](https://rft-sirm.github.io/UltraCore-RFT/interactive/)
