# Scientific Basis and Evidence Boundaries

**This document separates literal mathematical results from computational modelling language and engineering claims.**

Primary routes: [README](README.md) · [AI evidence guide](AI_GUIDE.md) · [Research map](docs/research-map.md) · [PITCH](PITCH.md).

## 1. Foundational research hierarchy

The research programme is presented in this order:

1. **Literal mathematics:** the source-stated fourth-moment trace-defect identity for a specified SU(2)-connected Sierpiński-gasket operator and commuting control.
2. **Formal and computational evidence:** the Lean 4 proof of the SU(2) fourth-moment identity, the separate Phi-Genesis least-eigenvalue/convergence theorem, direct numerical checks, and separately scoped finite-level certificates.
3. **Open mathematical programmes and extensions:** a unified general higher-moment law and the Phi-Genesis Gate A exceptional-set problem; these remain distinct from the already proved, level-restricted spectral result.
4. **Engineering methodology:** SIRM state invariants, deterministic execution, tests, fuzzing, audit records, and deployment evidence.
5. **Applications and hypotheses:** blockchain systems, quantum-processing architecture, and invariant-driven energy modelling.

These layers are connected through research motivation, not by automatic implication. A result at one layer cannot be used as proof at another without an explicit derivation.

## 2. Literal mathematical result

For the operator definitions and assumptions in [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), the fourth-moment trace defect is stated as

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16\left(3^{m-1}+1\right)\sin^2\left(\frac{\theta}{2}\right),
\quad m\ge1.
$$

With the source's normalization,

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3},
\qquad
\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

At $\theta=\pi/2$, the limit is $-8/9$. The dimension $3^{m+1}+3$ is the stated dimension of the operator Hilbert space, twice the vertex count $n(m)=(3^{m+1}+3)/2$.

**Formal status:** the primary repository reports a Lean 4 formalization for every $m\ge1$ and all angles in the formal statement, for the concrete operators encoded in the project. This establishes the formal proposition in the specified environment. Independent review of the formalization-to-mathematics correspondence, peer review, and external replication are separate questions.

**Not implied:** the full spectrum, all higher moments, a physical law, a quantum speed-up, the SIRM runtime invariants, or a complete physical Theory of Everything.

Sources: [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean code](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md).

## 3. Higher moments and the broader Theory-of-Everything programme

The two research monographs have different scopes: the [focused SU(2) theorem dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) records the theorem and its proof boundaries; the [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) collects the wider recursive-operator programme.

The current higher-moment status in the primary theorem repository is not a single yes/no statement:

- **H⁶ and H⁸:** Lean proves the all-angle recurrences for $m\ge3$. Exact symbolic certificates close the exceptional $m=2\to3$ transition, but those finite bridges are not yet Lean-kernel theorems.
- **H¹⁰:** Lean proves the required radius-four transport, the affine recurrence for $m\ge4$, and the affine formula for $m\ge5$. The level-five correction remains an exact finite trace expression.
- **General extension:** one unified recurrence theorem covering the full higher-moment family remains open.

The broader synthesis dissertation is dated 15 October 2026; it is a dated research record, not the authority for every later status change. Use the primary repositories and their formal declarations for current claims. Finite certificates and numerical checks remain distinct evidence classes.

Sources: [Evgeny-Theorem dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [higher-moment status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md) · [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) · [recurrence note](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md) · [modular certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md).

## 4. Phi-Genesis: signed-flux spectral research

[Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) investigates signed $Z_2$-flux graph Laplacians, Schur elimination, spectral decimation, boundary/corner corrections, inertia calculations, and exploratory mass-index patterns. It is a separate operator family from the SU(2) construction.

**Proved in Lean:** for the signless Laplacian $Q_N$ and its diagonal-gauge-conjugate signed matrix, at levels $N\ge6$, the least eigenvalue is the unique A1 root in the bootstrap interval and the least-eigenvalue sequence converges. The limit belongs to the exact rational interval

$$
\left[
\frac{1309128920280813421888623088170810187}{10^{36}},
\frac{1309128920280813421888623088170810189}{10^{36}}
\right],
$$

of width $2\times10^{-36}$. See [SchurEigenvalue.lean](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean), [SchurSignedTransfer.lean](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean), [PR #31](https://github.com/RFT-SIRM/Phi-Genesis/pull/31), and [PR #32](https://github.com/RFT-SIRM/Phi-Genesis/pull/32).

**Still open:** Gate A's complete exceptional set, the quadratic increment law and its constant, a closed form for the limit, levels $N<6$, and identification with an external $\theta=2\pi$ operator beyond the defined graph matrix. This result does not close Gate A.

- Passing tests support only the assertions and parameter range that they actually test.
- A fitted mass-index pattern is not an established predictive physical law without a mechanism, predeclared predictions, held-out validation, and independent derivation.
- No equivalence with the SU(2)-connected operators is assumed. A bridge needs an explicit operator map, boundary conditions, preserved quantities, exceptional cases, and a proof or a clearly labelled conjecture.

Rejected claims and failed experiments are part of the scientific record and should remain linked.

## 5. SIRM: mathematical model for software systems

SIRM (Synthetic Intelligence Reasoning Model; СИРМ — «Синтетическая интеллектуальная модель рассуждений») uses four stated runtime constraints, expressed in compact notation and mapped to implementation variables below.

$$
\begin{aligned}
I_1:\quad & S = B + Gp,\\
I_2:\quad & S = M - D,\\
I_3:\quad & d < p \quad (p>0),\\
I_4:\quad & E_i \ge -\frac{S}{10p}.
\end{aligned}
$$

The effective-balance relation is

$$
E_i = b_i + G.
$$

| Symbol | Implementation variable |
|---|---|
| $S$ | `total_supply` |
| $B$ | `total_base_sum` |
| $G$ | `global_field` |
| $M$ | `total_minted` |
| $D$ | `total_burned` |
| $d$ | `dust_accumulator` |
| $E_i$ | `effective_balance[i]` |
| $b_i$ | `base_balance[i]` |

Where $\mathtt{effective\_balance}[i]=\mathtt{base\_balance}[i]+\mathtt{global\_field}$, under the implementation's integer and scaling conventions.

An $O(1)$ distribution model can update a shared scalar and derive effective balances on read. That observation concerns this representation; it does not assert every operation is $O(1)$, nor does it prove the correctness of every implementation. Runtime tests, fuzzing, audits, and deployment checks are engineering evidence bounded by the code and assertions examined.

The SIRM constraints are not consequences of the spectral theorem. The theorem and runtime model are separate results.

## 6. Physical vocabulary in software documentation

Terms such as *field*, *flow*, *entropy*, *energy*, *pressure*, and *topology* may be used as modelling vocabulary in runtime documents. Their computational meaning must be defined locally—for example, a shared scalar variable, a memory-access pattern, a measure of state variability, an operation cost, queue load, or a dependency graph.

Such language does not imply a literal physical field, experimentally established physical phenomenon, or a new law of nature. Do not translate an analogy into a physics claim without a separate mathematical model, measurable predictions, and experimental evidence.

Likewise, references to P vs NP, the Riemann Hypothesis, Navier–Stokes, Yang–Mills, Hodge, BSD, or the Poincaré conjecture as design inspiration are not claims to solve those problems.

## 7. Evidence classes

| Class | Meaning |
|---|---|
| **Machine-checked** | A stated proposition is accepted by a specified proof assistant/build configuration |
| **Analytically proved** | A written proof follows from explicit assumptions |
| **Certified finite-level** | A certificate proves a finite set of stated cases under stated bounds |
| **Numerically reproduced** | Computation matches a prediction for stated inputs |
| **Engineering-tested** | Tests, fuzzing, audit, or deployment checks support an implementation-specific statement |
| **Hypothesis / open** | A proposed or unresolved extension |
| **Rejected / not established** | Evidence or counterexamples do not support the stronger statement |

No label is interchangeable with another. A passing CI run proves only the assertions executed by that workflow. A formal proof's strength is determined by its statement and definitions, not by the ambition of the project title.

## 8. Release and interpretation rules

- Link every theorem to its primary statement and formalization.
- Keep the fourth-moment theorem separate from higher-moment conjectures.
- Keep SU(2)-connected and signed-flux operator families distinct unless a bridge is proved.
- Attribute metrics to dated reports or workflows; do not present snapshots as live counters.
- Preserve negative results, exceptional cases, failed checks, and open questions.
- Do not imply peer review, independent replication, physical validation, or application-level advantage without evidence.
- Keep the main [RFT-SIRM portal](https://rft-sirm.github.io/) intact; UltraCore documentation is one connected entry point, not a replacement for the organization-wide portal.

This document defines interpretation boundaries. It does not replace the primary theorem, implementation specifications, source histories, or test artifacts.