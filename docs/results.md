---
title: "Mathematical Results and Evidence Register"
description: "A structured register of the SU(2) fourth-moment theorem, higher-moment results, Phi-Genesis signed graph spectra, and independent SIRM invariants."
keywords:
  - mathematical results
  - SU(2) fourth-moment theorem
  - higher spectral moments
  - Phi-Genesis least eigenvalue
  - signed graph Laplacian
  - SIRM invariants
---

# Mathematical Results and Evidence Register

This page is the compact technical reference for the mathematical results presented by UltraCore-RFT. Each result is attached to its own operator family, quantifiers, proof artifacts, and limitations. The SU(2) connection operators, the signed $Z_2$-flux graph matrices, and the SIRM runtime model are **separate mathematical or engineering objects**.

<div class="uc-stat-grid" markdown>
<div class="uc-stat" markdown>
<strong>H⁴</strong>
<span>All-level SU(2) trace-defect identity, $m\ge1$</span>
</div>
<div class="uc-stat" markdown>
<strong>H⁶ / H⁸ / H¹⁰</strong>
<span>Lean recurrences with distinct starting levels and finite-bridge boundaries</span>
</div>
<div class="uc-stat" markdown>
<strong>$\lambda_\infty$</strong>
<span>Phi-Genesis least-eigenvalue limit, levels $N\ge6$</span>
</div>
</div>

## 1. SU(2) connection operators: the fourth moment

For the specific non-commuting SU(2) connection $C$ and commuting control $C'$ defined in the primary project, the fourth-moment trace defect is

$$
\boxed{
\Delta_m^{(4)}(\theta)
=\mathrm{Tr}\!\left(H_C(m,\theta)^4\right)
-\mathrm{Tr}\!\left(H_{C'}(m,\theta)^4\right)
=-16\left(3^{m-1}+1\right)
\sin^2\!\left(\frac{\theta}{2}\right)
}
$$

for every integer $m\ge1$ and every real $\theta$. The concrete theorem is machine-checked in Lean 4 in [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), under the definitions and assumptions recorded there.

### Normalization and finite-size correction

The Hilbert-space dimension is $N_m=3^{m+1}+3$. Define

$$
I_m(\theta)
=\frac{\Delta_m^{(4)}(\theta)}{3^{m+1}+3}.
$$

The exact finite-level expression separates into its limit and a finite-size remainder:

$$
\boxed{
I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right)
-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right)
}
$$

Consequently,

$$
I_\infty(\theta)
=\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right),
$$

and the exact remainder is

$$
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}\sin^2\!\left(\frac{\theta}{2}\right).
$$

At $\theta=\pi/2$, the limit is exactly $-8/9$. The finite-level error decays with the explicit factor $(3^m+1)^{-1}$; no numerical fitting is needed for this identity.

!!! info "Scope of the theorem"
    This result concerns the specified SU(2)-connected graph operators and their commuting control. It does not, by itself, prove the higher-moment recurrences, the Phi-Genesis spectral statements, a physical law, or an engineering invariant.

**Primary evidence:** [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · [focused dissertation](DISSERTATION.md).

## 2. Higher moments: three distinct proof boundaries

The higher moments are not one undifferentiated theorem. Each has its own recurrence, starting level, and exceptional finite transition.

<div class="grid cards" markdown>
-   **Sixth moment — H⁶**

    ---

    Lean proves the all-angle recurrence

    $$
    D_{m+1}^{(6)}(\theta)=3D_m^{(6)}(\theta)+C_6(\theta),\quad m\ge3.
    $$

    The $m=2\to3$ transition is covered by an exact symbolic certificate, not yet by a Lean-kernel theorem.

-   **Eighth moment — H⁸**

    ---

    Lean proves

    $$
    D_{m+1}^{(8)}(\theta)=3D_m^{(8)}(\theta)+C_8(\theta),\quad m\ge3.
    $$

    Its exceptional $m=2\to3$ transition also has an exact finite certificate; keep that boundary explicit.

-   **Tenth moment — H¹⁰**

    ---

    Lean proves the radius-four transport and unconditional affine recurrence for $m\ge4:

    $$
    D_{m+1}^{(10)}(\theta)=3D_m^{(10)}(\theta)+C_{10}^{(5)}(\theta).
    $$

    The affine closed form applies for $m\ge5$; the level-five correction remains an exact finite trace expression.
</div>

A unified all-level recurrence covering the broader higher-moment family remains open. Finite certificates prove their stated finite claims; numerical holdouts are not substitutes for universal proofs.

**Primary evidence:** [higher-moment status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md) · [formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md).

## 3. Phi-Genesis: a separate signed $Z_2$-flux graph problem

Phi-Genesis studies signed and signless graph Laplacians, Schur elimination, spectral decimation, and boundary-corner corrections. It is **not** the SU(2) connection-operator family above; no operator equivalence is claimed.

### Uniform signed-Laplacian lower bound

For every refinement level, every real eigenvalue $\lambda$ of the explicitly defined signed Laplacian with a nonzero real eigenvector satisfies

$$
\boxed{\lambda\ge1.}
$$

The matrix definition and eigenvector hypotheses are part of the statement. This is a uniform lower bound, not the least-eigenvalue limit theorem below.

### Least-eigenvalue identification and convergence

For the level-$N$ signless Laplacians $Q_N$ and their gauge-conjugate signed matrices, the canonical A1 Schur root is identified as the least eigenvalue for $N\ge6$. Both least-eigenvalue sequences converge to $\lambda_\infty$ in the exact interval

$$
\boxed{
\frac{1309128920280813421888623088170810187}{10^{36}}
\le\lambda_\infty\le
\frac{1309128920280813421888623088170810189}{10^{36}}
}
$$

The interval width is exactly $2\cdot10^{-36}$ and its half-width is $10^{-36}$. Its midpoint is approximately

$$
1.309128920280813421888623088170810188.
$$

This number is the limiting least eigenvalue of the specified graph-matrix sequence. It is not known in closed form and is not claimed to be a universal physical constant.

### Parameter derivatives and the open quadratic law

The Lean development also proves parameter differentiability of both finite-level Schur boundary coordinates throughout the closed bootstrap interval. This is an analytic ingredient for further estimates, not the quadratic increment theorem.

!!! warning "Still open in Phi-Genesis"
    The complete Gate A exceptional-set characterization, the quadratic increment law $\delta_{m+1}\sim c\delta_m^2$ and existence of $c$, levels $N<6$, a closed form for $\lambda_\infty$, and identification with an external $\theta=2\pi$ operator remain open. The derivative recursion does not close these problems.

**Primary evidence:** [least-eigenvalue theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean) · [signed transfer](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean) · [uniform lower bound](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SignedLaplacianMatrix.lean) · [Schur derivative trajectory](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurDerivTrajectory.lean) · [proof map](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/PROOF_MAP.md).

## 4. SIRM: an independent runtime-invariant model

SIRM expresses constraints on runtime state transitions. The notation below is the compact mathematical model; implementation-specific variable mappings and integer/scaling conventions are documented in [Foundations](foundations.md).

$$
\begin{aligned}
I_1:\quad & S=B+Gp,\\
I_2:\quad & S=M-D,\\
I_3:\quad & d<p\quad(p>0),\\
I_4:\quad & E_i\ge-\frac{S}{10p}.
\end{aligned}
$$

The effective balance is

$$
E_i=b_i+G.
$$

| Symbol | Meaning |
|---|---|
| $S$ | Total supply |
| $B$ | Sum of base balances |
| $G$ | Global field / shared scalar |
| $p$ | Participant count |
| $M,D$ | Total minted and total burned |
| $d$ | Dust accumulator |
| $E_i,b_i$ | Effective and base balance of participant $i$ |

These are runtime-model invariants. They are not corollaries of the SU(2) trace identity or the Phi-Genesis graph spectrum; they require implementation-specific tests, fuzzing, audit, and deployment evidence.

## 5. Evidence vocabulary

| Label | What it means | What it does not mean |
|---|---|---|
| **Lean-proved** | The stated proposition is accepted by the configured Lean kernel/build | Independent semantic review is unnecessary |
| **Exact finite certificate** | A finite symbolic identity is reproduced for its stated inputs | An all-level theorem is proved |
| **Numerical evidence** | A computation supports a stated finite observation or conjecture | A proof or universal error bound exists |
| **Engineering-tested** | Specific code paths/configurations passed recorded tests | All executions or all implementations are correct |
| **Open** | A proof obligation remains unresolved | Related completed theorems should be hidden or downgraded |

---

**Next:** [Focused SU(2) dissertation](DISSERTATION.md) · [Research Monographs](monographs.md) · [Research Map](research-map.md) · [Interactive Portal](https://rft-sirm.github.io/UltraCore-RFT/interactive/).
