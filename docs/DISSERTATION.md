# Spectral Trace Defects of Noncommutative SU(2) Connections on Sierpiński-Gasket Graphs

## Research dissertation

**Author:** Evgeny Zaprudnov  
**Research group:** RFT-SIRM  
**Version:** 1.0 — UltraCore edition  
**Date:** 9 November 2026  
**Primary formal project:** [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem)  
**Source dissertation:** [upstream research manuscript](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md)

---

## Abstract

This dissertation studies trace defects of recursively defined graph operators on finite Sierpiński-gasket approximations. Each vertex carries a two-component complex state, while selected graph edges carry SU(2)-valued connection matrices. Two connection configurations are compared on the same graph: a non-commuting configuration whose flux-edge axes cycle through $x,y,z$, and a commuting control whose flux edges all use the fixed $z$-axis.

The principal result is an exact fourth-moment identity. For every refinement level $m\ge1$ and every real angle $\theta$,

$$
\Delta_m^{(4)}(\theta)
=\mathrm{Tr}\!\left(H_C(m,\theta)^4\right)
-\mathrm{Tr}\!\left(H_{C'}(m,\theta)^4\right)
=-16\left(3^{m-1}+1\right)
\sin^2\!\left(\frac{\theta}{2}\right).
$$

The concrete statement is machine-checked in Lean 4 as `traceDefect_closed` in the primary project. Its proof is based on recursive gluing and two coupled orientation recurrences. The proof has no unproved placeholder; the formalization records its dependencies on the standard Lean axioms `propext`, `Classical.choice`, and `Quot.sound`.

After normalization by the matrix dimension, the fourth-moment defect has an exact limit

$$
I_\infty(\theta)
=\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right).
$$

This is a theorem about one normalized trace observable. It is not a formula for the full spectrum, individual eigenvalues, the spectral gap, or computational complexity.

The dissertation also records distinct higher-moment results. H⁶ and H⁸ have Lean-proved all-angle recurrences for $m\ge3$, combined with exact symbolic certificates for the exceptional transition $m=2\to3$. Those finite bridges are exact but are not yet Lean-kernel theorems. H¹⁰ has an unconditional Lean-proved affine recurrence for $m\ge4$ and affine form for $m\ge5$, because the required radius-four transport is itself proved in Lean. The level-five correction remains an exact finite trace expression rather than an expanded trigonometric polynomial.

The central methodological point is that a Lean theorem, a finite exact symbolic certificate, and a floating-point regression are different kinds of evidence. Every claim in this dissertation is restricted to the graph, orientation convention, and operators defined by the primary project.

**Keywords:** Sierpiński-gasket graphs; trace defect; spectral moments; SU(2) connection; non-commuting holonomy; recursive gluing; exact symbolic computation; Lean 4.

---

## 1. Scope and status

The principal theorem is universal over the stated refinement levels and angles: it holds for every integer $m\ge1$ and every $\theta\in\mathbb R$. The universal statement is not inferred from the finite numerical tables; it is proved for the concrete matrices in the formalization.

The current proof hierarchy is:

| Moment | Established result | Evidence boundary |
|---|---|---|
| H⁴ | Exact all-level, all-angle closed form for $m\ge1$. | Unconditional Lean-kernel theorem. |
| H⁶ | All-angle recurrence for $m\ge3$; combined formula for $m\ge2$. | Lean recurrence plus exact Gaussian-integer polynomial certificate for $2\to3$. The finite bridge is not yet in the Lean kernel. |
| H⁸ | All-angle recurrence for $m\ge3$; combined formula for $m\ge2$. | Lean recurrence plus exact sparse-polynomial certificate for $2\to3$. The finite bridge is not yet in the Lean kernel. |
| H¹⁰ | Unconditional affine recurrence for $m\ge4$ and affine form for $m\ge5$. | Lean-kernel theorems; radius-four transport is proved. The level-five correction remains an exact finite trace expression. |

The H⁶ and H⁸ transition certificates are exact and reproducible, but their finite $2\to3$ bridges are not yet formalized inside the Lean kernel. This is different from H¹⁰: its transport hypothesis has itself been discharged in Lean. Simplifying the H¹⁰ correction coefficient would improve its presentation, but is not a missing hypothesis in the stated recurrence.

This work does not claim a formula for all eigenvalues, the spectral gap, a computational-complexity classification, or a physical law.

## 2. Graph and connection operators

### 2.1 Recursive graph and Hilbert space

Let $SG(m)$ be the finite Sierpiński-gasket approximation graph at refinement level $m$. It is formed recursively by assembling three copies of the preceding level and identifying their corner vertices. The combinatorial counts are

$$
|V_m|=\frac{3^{m+1}+3}{2},
\qquad
|E_m|=3^{m+1},
\qquad
|F_m|=3^m.
$$

Each vertex carries two complex state components, so the Hilbert space and its dimension are

$$
\mathcal H_m
=\mathbb C^{|V_m|}\otimes\mathbb C^2,
\qquad
N_m=\dim\mathcal H_m=3^{m+1}+3.
$$

### 2.2 SU(2) edge data

Let $\sigma_x,\sigma_y,\sigma_z$ denote the Pauli matrices. A flux edge with rotation axis $a\in\{x,y,z\}$ carries the matrix

$$
U_a(\theta)
=\cos\!\left(\frac{\theta}{2}\right)I_2
-i\sin\!\left(\frac{\theta}{2}\right)\sigma_a.
$$

The reverse orientation carries the adjoint:

$$
U(b,a)=U(a,b)^*.
$$

Exactly one designated edge of each elementary triangle carries this rotation; the other edges carry the identity.

Configuration $C$ assigns the axes $x,y,z$ cyclically by triangle index modulo three. Configuration $C'$ keeps the graph and flux-edge locations fixed but assigns the $z$-axis to every triangle. Its edge rotations commute and split into two decoupled U(1)-magnetic Sierpiński-gasket operators with fluxes $+\theta/2$ and $-\theta/2$.

The operator is of graph-Laplacian form

$$
H=D-A,
$$

where $D$ is the degree matrix tensored with $I_2$, and $A$ is the connection adjacency matrix. At $\theta=0$, both configurations reduce to two copies of the ordinary Sierpiński-gasket Laplacian.

### 2.3 Orientation is part of the definition

The theorem uses the vertex-index orientation convention of the primary project: Lean uses `vIdx`, and the Python implementation orders edge endpoints by vertex indices. This convention must be retained when reproducing the theorem.

The upstream orientation audit reports that a different, geometrically uniform direction convention gives, for the tested levels $m=1,\ldots,4$,

$$
-32\cdot3^{m-1}\sin^2\!\left(\frac{\theta}{2}\right).
$$

That alternative is a finite-level comparison, not the all-level theorem stated here. Graph indexing, face order, flux-edge choice, and edge orientation must not be silently changed.

## 3. Trace-defect notation

For an even moment $p$, define

$$
\Delta_m^{(p)}(\theta)
=\mathrm{Tr}\!\left(H_C(m,\theta)^p\right)
-\mathrm{Tr}\!\left(H_{C'}(m,\theta)^p\right).
$$

For the higher-moment Lean statements, $D_m^{(p)}(\theta)$ denotes the corresponding numbering-orientation quantity defined by the primary declarations `defectO6`, `defectO8`, and `defectO10`.

For the polynomial formulae below, use

$$
\phi=\frac{\theta}{2},
\qquad
c=\cos\phi,
\qquad
s=\sin\phi,
\qquad
c^2+s^2=1.
$$

## 4. Main theorem: fourth spectral moment

### Theorem 4.1 — exact fourth-moment trace defect

For every integer $m\ge1$ and every real $\theta$,

$$
\boxed{
\Delta_m^{(4)}(\theta)
=-16\left(3^{m-1}+1\right)
\sin^2\!\left(\frac{\theta}{2}\right)
}.
$$

The concrete Lean declaration is `traceDefect_closed` in `formalization/EvgenyTheorem/TildeEntries.lean` of the primary project.

The identity implies

$$
\Delta_m^{(4)}(\theta)\le0,
$$

and the defect vanishes exactly when $\theta\in2\pi\mathbb Z$.

### 4.1 Normalization, exact finite-level formula, and limit

Normalize by the matrix dimension:

$$
I_m(\theta)
=\frac{\Delta_m^{(4)}(\theta)}{3^{m+1}+3}
=-16\frac{3^{m-1}+1}{3^{m+1}+3}
\sin^2\!\left(\frac{\theta}{2}\right).
$$

The scalar factor satisfies

$$
\frac{3^{m-1}+1}{3^{m+1}+3}
=\frac{1}{9}\frac{3^m+3}{3^m+1}.
$$

Therefore the exact finite-level expression is

$$
I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right)
-\frac{32}{9(3^m+1)}
\sin^2\!\left(\frac{\theta}{2}\right).
$$

Consequently,

$$
\boxed{
I_\infty(\theta)
=\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\!\left(\frac{\theta}{2}\right)
}.
$$

The exact finite-level remainder is

$$
\boxed{
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}
\sin^2\!\left(\frac{\theta}{2}\right)
}.
$$

In particular,

$$
I_\infty\!\left(\frac{\pi}{2}\right)=-\frac89.
$$

For $\theta\notin2\pi\mathbb Z$, the ratio of successive absolute remainders is

$$
\frac{|I_{m+1}(\theta)-I_\infty(\theta)|}
{|I_m(\theta)-I_\infty(\theta)|}
=\frac{3^m+1}{3^{m+1}+1}
\longrightarrow\frac13.
$$

For $\theta\in2\pi\mathbb Z$, both remainders vanish identically, and this ratio is undefined. This is a limit of the normalized fourth-moment trace defect; it is not a statement about eigenvalue convergence or the spectral gap.

## 5. Lean proof architecture

The general-level proof uses the recursive gluing structure and two orientation states. Let $D_m$ be the numbering-orientation defect and $\widetilde D_m$ the defect with the designated corner orientation flipped. Put $s=\sin(\theta/2)$. The initial values are

$$
D_1=-32s^2,
\qquad
\widetilde D_1=0.
$$

The coupled recurrences are

$$
\begin{aligned}
D_{m+1}&=2D_m+\widetilde D_m,\\
\widetilde D_{m+1}&=D_m+2\widetilde D_m,
\end{aligned}
\qquad m\ge1.
$$

Set

$$
S_m=D_m+\widetilde D_m,
\qquad
E_m=D_m-\widetilde D_m.
$$

Then

$$
S_{m+1}=3S_m,
\qquad
E_{m+1}=E_m,
\qquad
S_1=E_1=-32s^2.
$$

Thus

$$
S_m=-32\cdot3^{m-1}s^2,
\qquad
E_m=-32s^2.
$$

Recovering $D_m=(S_m+E_m)/2$ gives

$$
D_m=-16\left(3^{m-1}+1\right)s^2,
$$

which is the asserted theorem.

The formal proof uses recursive gluing, block-matrix trace identities, corner data, and orientation transport. The primary Lean development is organized across modules including `GlueAlg`, `GlueBridge`, `GlueSG`, `GlueK`, `GlueCorner`, `FinalOrient`, `FinalTilde`, `FinalArith`, and `TildeEntries`.

The machine-checked result should be cited through the declaration `traceDefect_closed` and its coupled-recursion proof route. The upstream formalization records the dependencies on the standard Lean axioms `propext`, `Classical.choice`, and `Quot.sound`. The earlier hand-oriented manuscript `docs/PROOF.md` is not the machine-checked proof.

## 6. Higher-moment results

### 6.1 Sixth moment

For the numbering-orientation quantity $D_m^{(6)}(\theta)$, Lean proves

$$
D_{m+1}^{(6)}(\theta)
=3D_m^{(6)}(\theta)+C_6(\theta),
\qquad m\ge3.
$$

The exact finite certificate gives

$$
D_2^{(6)}(\theta)
=-14592s^2+1344cs^2-384s^3,
$$

and

$$
C_6(\theta)=4512s^2+192cs^2+768s^3.
$$

Combining the Lean recurrence with the finite transition gives, for every $m\ge2$,

$$
\boxed{
D_m^{(6)}(\theta)
=3^{m-2}D_2^{(6)}(\theta)
+\frac{3^{m-2}-1}{2}C_6(\theta)
}.
$$

Equivalently,

$$
\boxed{
\begin{aligned}
D_m^{(6)}(\theta)
={}&-(12336\cdot3^{m-2}+2256)s^2\\
&+(1440\cdot3^{m-2}-96)cs^2
-384s^3.
\end{aligned}
}
$$

At $\theta=\pi$, the recurrence coefficient is $C_6(\pi)=5280$.

**Proof boundary.** The recurrence for $m\ge3$ is proved in Lean. The exceptional $m=2\to3$ transition is certified by exact Gaussian-integer polynomial arithmetic in `computational/p6_level3_orientation_certificate.py` and tested in `tests/test_higher_moments.py`. This finite bridge is exact symbolic evidence, but it is not yet a Lean-kernel theorem.

On $SG(1)$, the exact length-six walk classification gives 66 walks in each one-triangle class, 168 in each two-triangle class, and 486 walks visiting all three elementary triangles. The first two groups contribute zero; the all-three-triangle group contributes nonzero. This is a finite-level path-class result, not an all-level path-class theorem.

### 6.2 Eighth moment

For $D_m^{(8)}(\theta)$, Lean proves

$$
D_{m+1}^{(8)}(\theta)
=3D_m^{(8)}(\theta)+C_8(\theta),
\qquad m\ge3.
$$

The exact certificate gives

$$
\begin{aligned}
D_2^{(8)}(\theta)
={}&-1335552s^2+244352cs^2-40064s^3\\
&+64cs^3+1920s^4,
\end{aligned}
$$

and

$$
\begin{aligned}
C_8(\theta)
={}&193600s^2+75776cs^2+83712s^3\\
&-512cs^3+192s^4.
\end{aligned}
$$

For every $m\ge2$,

$$
\boxed{
D_m^{(8)}(\theta)
=3^{m-2}D_2^{(8)}(\theta)
+\frac{3^{m-2}-1}{2}C_8(\theta)
}.
$$

At $\theta=\pi$, $C_8(\pi)=277504$.

**Proof boundary.** The recurrence is Lean-formalized for $m\ge3$. The exceptional $m=2\to3$ identity is computed coefficient-by-coefficient over Gaussian integers in `computational/p8_base_certificate.py`. It is exact and reproducible, but not yet a Lean-kernel theorem.

### 6.3 Tenth moment

The tenth-moment development contains an ordered $p=10$ trace expansion, exact word-stratum reductions, gluing assembly, orientation recurrences, and transport of the required corner rows through degree nine.

The proposition `H10TransportAll` is proved by `H10TransportAll_proved` for both the face-axis and fixed-$z$ configurations at every $m\ge4$. Lean therefore proves unconditionally

$$
\boxed{
D_{m+1}^{(10)}(\theta)
=3D_m^{(10)}(\theta)+C_{10}^{(5)}(\theta),
\qquad m\ge4
}.
$$

The corresponding affine form is

$$
\boxed{
D_m^{(10)}(\theta)
=3^{m-5}\left(
D_5^{(10)}(\theta)+\frac{C_{10}^{(5)}(\theta)}{2}
\right)
-\frac{C_{10}^{(5)}(\theta)}{2},
\qquad m\ge5
}.
$$

The exact correction $C_{10}^{(5)}(\theta)$ is the finite trace expression named `defectO10_num_residual_constant`. It has not yet been expanded as a trigonometric polynomial. This is a presentation task, not a remaining hypothesis in the recurrence theorem.

## 7. Numerical and exact-computation records

At $\theta=\pi/2$, direct fourth-moment matrix calculations give:

| $m$ | $\dim\mathcal H_m$ | $I_m(\pi/2)$ |
|---:|---:|---:|
| 1 | 12 | $-1.333333$ |
| 2 | 30 | $-1.066667$ |
| 3 | 84 | $-0.952381$ |
| 4 | 246 | $-0.910569$ |
| 5 | 732 | $-0.896175$ |
| 6 | 2190 | $-0.891324$ |
| 7 | 6564 | $-0.889701$ |

The held-out H⁴ matrix-power comparisons recorded upstream have maximum listed absolute discrepancy $2.54\times10^{-11}$. The higher-moment regression table at $\theta=\pi/2$ covers $m=1,\ldots,4$. These finite tables are numerical checks, not the universal proof.

The Python tests also check selected vertex-wise gauge transformations. At level three, the recorded maximum spectral discrepancy is $7.99\times10^{-15}$; the fourth-moment difference is zero at displayed precision. These checks are not assumptions in the Lean theorem.

## 8. Reproducibility and proof artifacts

The source-of-truth formal and computational artifacts remain in [RFT-SIRM/Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem):

| Artifact | Role |
|---|---|
| `src/graph/sg_graph.py` | Recursive graph construction and combinatorial counts. |
| `src/operators/operators.py` | Python graph operators and SU(2) connection. |
| `formalization/EvgenyTheorem/Operator.lean` | Concrete Lean operators and trace-defect definition. |
| `formalization/EvgenyTheorem/TildeEntries.lean` | Theorem `traceDefect_closed`. |
| `formalization/EvgenyTheorem/FinalTilde.lean` | Coupled H⁴ recurrences and H⁶ results. |
| `formalization/EvgenyTheorem/FinalClosed10.lean` | Unconditional H¹⁰ transport and affine theorem. |
| `computational/p6_level3_orientation_certificate.py` | Exact H⁶ transition certificate. |
| `computational/p8_base_certificate.py` | Exact H⁸ transition certificate. |
| `docs/HIGHER_MOMENTS.md` | Higher-moment formulae and proof boundaries. |
| `docs/ORIENTATION_NOTE.md` | Orientation convention audit. |
| `VERIFICATION.md` | Numerical and held-out checks. |

From a clean checkout of the primary project, the documented checks are:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r reproducibility/requirements.txt
pytest tests/ -m "not slow" -v
pytest tests/ -m slow -v
lake build
```

The Python suite checks numerical regressions and exact finite certificates. The Lean build checks formal proofs. A successful run certifies only the assertions actually executed by that run. The primary project's `lakefile.toml` and `lean-toolchain` pin the Mathlib revision and Lean toolchain.

## 9. Limitations and non-claims

1. **No full-spectrum formula.** The fourth-moment trace identity does not determine all eigenvalues or the complete spectral distribution.
2. **No spectral-gap theorem.** No conclusion about the smallest positive eigenvalue follows from this identity alone.
3. **No complexity-theory result.** The closed form evaluates the scalar trace defect without constructing the full matrix. This is not a complexity-class separation, lower bound, or bit-complexity theorem.
4. **No silent change of orientation.** A different edge orientation defines a different operator family.
5. **No automatic extension to higher moments.** Each higher moment requires its own recurrence and boundary argument.
6. **No conflation of evidence.** Lean theorems, exact external certificates, and floating-point regressions are distinct.
7. **No cross-project identification.** This work does not identify the SU(2) operators with signed $Z_2$-flux or spectral-decimation models.
8. **No physical-law claim.** All statements concern the graph operators defined in the primary project.

The six-criterion protocol in the primary repository is a project-defined diagnostic for the normalized H⁴ invariant. It is not an external peer-review verdict and does not replace the theorem or its proof.

## 10. Conclusion

For the specified Sierpiński-gasket graph and vertex-index-oriented SU(2) connection, the fourth-moment trace defect has the exact all-level, all-angle formula

$$
\Delta_m^{(4)}(\theta)
=-16\left(3^{m-1}+1\right)
\sin^2\!\left(\frac{\theta}{2}\right).
$$

The result is machine-checked in Lean 4. Its normalized form has an exact limit and a fully explicit finite-level remainder. The H⁶ and H⁸ developments combine Lean recurrences with exact finite transition certificates; the H¹⁰ recurrence and affine form are unconditional Lean theorems.

This document consolidates the proved fourth-moment theorem and the current higher-moment advances. It does not claim that every related spectral question is closed. The full spectrum, spectral gap, Lean formalization of the H⁶/H⁸ finite bridges, and explicit trigonometric simplification of the H¹⁰ correction remain outside the principal H⁴ theorem.

## References and primary research artifacts

1. [Evgeny-Theorem repository](https://github.com/RFT-SIRM/Evgeny-Theorem) — source, formalization, certificates, tests, and research records.
2. [THEOREM.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) — statement of the fourth-moment identity.
3. [Lean formalization guide](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) — theorem declaration, proof architecture, axioms, and build instructions.
4. [Higher-moment results](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md) — detailed H⁶, H⁸, and H¹⁰ formulae.
5. [Orientation note](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/ORIENTATION_NOTE.md) — edge-orientation convention.
6. [Verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) — finite numerical and held-out checks.

---

*This is a research dissertation/monograph about the mathematics maintained in RFT-SIRM/Evgeny-Theorem. It is not a claim of an academic degree and is separate from the broader “Theory of Everything” synthesis dissertation.*
