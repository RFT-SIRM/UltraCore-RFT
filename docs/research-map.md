---
title: "Research Map: SU(2) Trace Defect, Phi-Genesis Spectrum, and SIRM"
description: "Evidence map for the machine-checked SU(2) fourth-moment identity, higher-moment recurrence results, the Phi-Genesis signed graph Laplacian lower bound, and its limiting least eigenvalue near 1.3091289."
keywords:
  - mathematical research map
  - SU(2) trace defect
  - Phi-Genesis spectrum
  - signed graph Laplacian
  - A1 Schur root
  - least eigenvalue convergence
---

# Research Map: Mathematical Foundations, Evidence, and Applications

**Evidence-first reading order (not historical chronology):** mathematical theorem and formal evidence → separate Phi-Genesis spectral result → proposed Sierpiński quantum architecture and formal SIRM financial infrastructure → systems methodology → implementations and other applications.

> **Historical origin:** the maintainer-reported sequence is [Rift Network](https://github.com/RFT-SIRM/Rift-Network) → [Rift-L1 Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) → UltraCore-RFT and supporting systems → [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) → [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) → [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything). See the [origin chronology](origin-chronology.md); exact dates are kept separate unless verified from source history.

> **Research monographs:** [Focused theorem dissertation — Spectral Trace Defects of Noncommutative SU(2) Connections on Sierpiński-Gasket Graphs](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [Broader synthesis dissertation — Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md).
>
> The focused document treats the SU(2) fourth-moment theorem and its proof boundaries. The broader monograph records the larger recursive-operator programme and is dated 15 October 2026. See the [monograph guide](monographs.md); neither title is a claim that a complete physical Theory of Everything has been established.

This map is deliberately organized by evidence and research relationships, not by the historical order in which the repositories were created. The title *Evgeny's Theory of Everything* names a broad research programme, not a claim that a complete physical theory of the Universe has been established.

## 1. The programme at a glance

$$
\boxed{\text{Definitions and theorem}}
\longrightarrow
\boxed{\text{Reproducible evidence}}
\longrightarrow
\boxed{\text{Open extensions}}
\longrightarrow
\boxed{\text{Engineering applications}}
$$

The arrows describe an evidence-first reading order, not a theorem asserting that every downstream application follows from the mathematical result.

| Layer | Programme | Status and boundary |
|---|---|---|
| 1. Mathematical anchor | [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Lean 4 proof of the stated fourth-moment identity for the specified SU(2) operators and quantifiers |
| 2. Higher-moment extension | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theory-of-Everything) · [broader synthesis](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | H⁶/H⁸ recurrences for $mge3$ with finite bridges; H¹⁰ recurrence for $mge4$ and affine form for $mge5$; a unified general recurrence remains open |
| 3. Separate spectral model | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Lean proves the stated signed-Laplacian lower bound and least-eigenvalue convergence for the specified signed/signless graph matrices at $Nge6$; Gate A and the quadratic law remain open |
| 4. Quantum-processing architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Proposed 12-transmon mapping and candidate two-dimensional logical subspace; closed-system model only, pre-experimental, no fabricated or measured device |
| 5. Formal financial infrastructure | [SIRM-Financial-Infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) | Lean 4.33.1 abstract financial-state and accounting specification; production runtime, cryptographic identity, custody, reserves, and Rust refinement remain open |
| 6. Exact invariant limit and phenomenological models | [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis) | Exact algebraic limit/remainder for its defined invariant; physical coupling and cosmological response remain phenomenological and observationally unvalidated |
| 7. Systems methodology | [SIRM foundations](foundations.md) | Separate runtime-state invariants and implementation methodology; not proved by the spectral theorem |
| 8. Implementations and exploratory applications | [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain), [Rift-Network](https://github.com/RFT-SIRM/Rift-Network), [seL4 report](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/SEL4_CDT_FUZZING.md), [Invariant Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery) | Implementation-specific tests and exploratory models; evidence does not transfer between repositories |
## Global test and evidence control

UltraCore-RFT is being developed as the central observability layer for cross-repository CI. The [Ecosystem Control Plane](ecosystem-control.md) documents the registered projects, status meanings, run artifacts, and evidence boundaries. Its first phase reads public Actions status; it does not yet dispatch workflows in other repositories.

## Engineering and application tracks

**Featured application index:** [RFT-QPU-Sierpinski, RFT-Invariant-Battery, and RFT-Cosmology-Genesis — scope, status, and evidence boundaries](application-programmes.md). The cosmology project also has a distinct mathematical result: the exact limit and finite-level remainder of its defined normalized invariant, documented in the [theorem dossier](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis/blob/main/EXACT_INVARIANT_REMAINDER_THEOREM.md). This algebraic result does not establish a physical coupling or an observational cosmology claim.


These tracks have their own repositories, validation methods, and limitations; they are not corollaries of the fourth-moment theorem.

- **Solana / Agave:** [Rift-Network](https://github.com/RFT-SIRM/Rift-Network), [Agave Rift Scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler), and [ABIv2 memory contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts).
- **seL4 kernel testing:** [CDT stress-verification report](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/docs/field_trials_sel4.md). Empirical stress testing is not a replacement for formal kernel verification.
- **DeFi model review:** [Aave V4 Hub model review](https://github.com/RFT-SIRM/aave-v4-hub-model-review); this is not an Aave endorsement.
- **Other systems:** [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain), [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski), [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.), and [RFT-Cosmology-Genesis](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis). Exploratory architecture and model studies should not be presented as validated production or physical-device results without separate evidence.
- **Formal contact:** see the [contact and research submission policy](support.md) for attribution, institutional correspondence, and confidential-material handling.

## 2. Mathematical anchor: the fourth-moment identity

For the definitions and assumptions documented by the primary theorem repository,

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16\left(3^{m-1}+1\right)\sin^2\left(\frac{\theta}{2}\right),
\qquad m=1,2,3,\ldots.
$$

With the source's normalization, the exact finite-level formula is

$$
I_m(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right)
-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
$$

Thus

$$
I_\infty(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right),
\qquad
I_\infty\left(\frac{\pi}{2}\right)=-\frac89.
$$

### Algebraic sanity checks

- $3^{m+1}+3=3(3^m+1)$.
- At $m=1,\theta=\pi/2$: $\Delta_1=-16$, dimension $=12$, and $I_1=-4/3$.
- The exact finite-level remainder is $-32\sin^2(\theta/2)/(9(3^m+1))$.

The source repository reports that the fourth-moment statement is formalized in Lean 4 for the concrete operators and the quantifiers in the formal theorem. A checked formal proposition does not by itself settle independent semantic review, peer review, or novelty relative to the literature.

Primary sources: [focused theorem dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md).
## 3. Higher moments: report each theorem at its own scope

The current primary-source status differs by moment:

- **H⁶ and H⁸:** Lean proves the all-angle recurrences for $m\ge3$. Exact symbolic certificates supply the exceptional $m=2\to3$ transitions and combined formulas for $m\ge2$, but the finite bridges are not yet Lean-kernel theorems.
- **H¹⁰:** Lean proves the radius-four transport and the unconditional affine recurrence for $m\ge4$, with the affine formula for $m\ge5$. The level-five correction remains an exact finite trace expression.
- **General extension:** a unified all-level recurrence theorem covering the broader higher-moment family remains open.

A finite certificate proves its stated finite claim, not an infinite family. Numerical holdouts and sparse-matrix-power checks remain finite computational evidence. Do not use the H⁴ proof as if it proved H⁶/H⁸/H¹⁰, and do not flatten the distinct higher-moment proof statuses into one label.

Sources: [focused theorem dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [higher-moment formal status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md) · [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) · [recurrence note](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md) · [modular certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md).

## 4. Phi-Genesis: a separate operator family

[Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) studies signed $Z_2$-flux graph Laplacians, Schur elimination, spectral decimation, boundary/corner corrections, inertia, and exploratory mass-index patterns. This is not the SU(2) operator family in Evgeny's Theorem.

### Proved spectral result

For the signless Laplacian $Q_N$ of the level-$N$ Sierpiński-gasket graph and its diagonal-gauge-conjugate signed matrix, the Lean development proves for every $N=6+n$:

- the canonical A1 root is an eigenvalue and no eigenvalue is smaller;
- the least eigenvalue is the unique A1 root in the fixed bootstrap interval;
- the sequence of least eigenvalues converges to a limit in the exact rational interval

$$
\left[
\frac{1309128920280813421888623088170810187}{10^{36}},
\frac{1309128920280813421888623088170810189}{10^{36}}
\right].
$$

The interval width is $2\times10^{-36}$. In decimal notation, the certified enclosure is

$$
1.309128920280813421888623088170810187
\le\lambda_\infty\le
1.309128920280813421888623088170810189.
$$

The midpoint is approximately $1.309128920280813421888623088170810188$. This is the limiting least-eigenvalue value for the specified graph-matrix sequence, not a known fundamental physical constant.

The result is recorded in [SchurEigenvalue.lean](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean) and transferred to the signed matrix in [SchurSignedTransfer.lean](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean). See also [PR #31](https://github.com/RFT-SIRM/Phi-Genesis/pull/31) and [PR #32](https://github.com/RFT-SIRM/Phi-Genesis/pull/32).

### What remains open

- Gate A: the complete exceptional set and all residual mismatches in the spectral-decimation correspondence.
- The quadratic increment law and existence of its constant; current ratio values are numerical evidence, not a proof.
- A closed form for the limiting eigenvalue and levels $N<6$.
- Identification with an external $\theta=2\pi$ operator beyond the explicitly defined graph matrix.

A fitted mass-index pattern is not an established predictive physical law without a prospective selection mechanism, predeclared predictions, held-out validation, and independent derivation. No equivalence between the SU(2) operators and signed-flux Laplacians is assumed; any bridge needs a precise operator map and proof.

## 5. RFT-QPU-Sierpinski: proposed logical-qubit architecture

The source repository studies a proposed quantum-processing element on a self-similar Sierpiński-gasket graph with non-commuting SU(2) edge transport. Its level-1 mapping contains 6 graph sites, 9 graph edges, 3 selected X/Y/Z links, 12 transmon modes, and 22 effective exchange channels. The candidate logical qubit is a selected two-dimensional low-energy subspace.

The Stage 11B local retune reports a projected process overlap of 0.9999999793763371 after local-Z fitting and average logical-state fidelity including leakage of 0.9999999803654352 for a five-level, 480-step-per-period, three-mode A–coupler–B model. This is a closed-system numerical projection—not measured hardware fidelity and not a full driven simulation of the 12-mode tile.

**Status: pre-experimental.** No chip has been fabricated or measured. The resonant complex-Z implementation, graph-wide nine-tone schedule, seven-level 240/480 convergence, open-system noise analysis, and layout-extracted circuit validation remain open. The source project reports 73 primary and 653 conditional resonance warnings in its current first-order multi-tone screen; simultaneous nine-tone operation is not cleared.

Sources: [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) · [repository status](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/REPOSITORY_STATUS.md) · [validation plan](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/docs/VALIDATION_PLAN.md) · [evidence boundary](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/docs/DISCLOSURE_BOUNDARY.md).

## 6. SIRM Financial Infrastructure: Lean 4 financial-state specification

[SIRM-Financial-Infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) is the dedicated formal specification for SIRM financial-state transitions and accounting. Its combined authorized financial machine represents holder updates and corresponding signed general-ledger postings together in one abstract Lean state transition. Additional modules cover:

- supply/holder reconciliation and balanced per-asset journals;
- finite principal/account control and exact operation grants, including issuer/recipient-aware issuance;
- typed finite account and asset registries, exact base-unit conversion, and route-specific rational migration residuals;
- per-principal nonces, typed transaction receipts, exact retry behaviour, and cached authorization/insufficient-funds denials;
- concurrent escrow records, pooled reserve/vault/GL reconciliation, discrete time-lock expiry, and first-stage per-ID dispute intake/freeze.

The pinned toolchain is Lean 4.33.1. The configured CI topology has one Lean build/theorem-test job and 17 static audits. These are formal-model and source/documentation checks, not a production runtime certification.

The current declarations do not establish real-world account ownership, key custody, cryptographic signature validation, production database persistence or atomicity, complete production transaction encoding, Rust/Lean refinement, reserve backing, external settlement, dispute adjudication, or legal/regulatory compliance. The Rust reference implementation remains planned.

Primary sources: [README](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure#readme) · [formalization status](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/FORMALIZATION_STATUS.md) · [mathematical scope](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/MATHEMATICAL_SCOPE.md) · [testing and verification](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/TESTING.md).


## 7. SIRM runtime model and invariants

SIRM specifies runtime constraints for deterministic state transitions. The compact notation below is mapped to implementation variables immediately afterward.

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

Where $\mathtt{effective\_balance}[i]=\mathtt{base\_balance}[i]+\mathtt{global\_field}$, under the model's integer and scaling conventions.

The $O(1)$ distribution argument concerns a shared scalar update and lazy effective-balance calculation. It does not imply every operation is $O(1)$, nor does the spectral theorem prove the SIRM invariants. Runtime tests, fuzzing, audits, and deployment evidence have implementation-specific scope.

## 8. Evidence vocabulary

| Label | Meaning |
|---|---|
| **Machine-checked** | A stated proposition is accepted by the specified proof assistant and build configuration |
| **Analytically proved** | A written proof establishes the statement from explicit assumptions |
| **Certified finite-level** | A certificate covers the stated finite cases under stated bounds |
| **Numerically reproduced** | Computation matches a prediction on named inputs |
| **Engineering-tested** | Tests, fuzzing, audit, or deployment checks support an implementation-specific claim |
| **Hypothesis / conjecture** | A proposed extension awaiting proof or refutation |
| **Open** | A required derivation, proof, independent replication, or experiment is incomplete |
| **Rejected / not established** | Counterexamples or available evidence do not support the stronger claim |

A passing workflow proves only the assertions it executes. Fuzz counts and test totals are source-reported snapshots unless the page explicitly implements a live data source.

## 9. Historical reading order

1. **Invariant-first engineering:** define runtime state constraints and check them at transitions.
2. **Specific spectral theorem:** state a closed fourth-moment identity for a defined SU(2) operator family; preserve the formal and numerical evidence separately.
3. **Higher-moment extension:** investigate recurrences and finite-level certificates while keeping the all-level problem open.
4. **Separate signed-flux audit:** test spectral-decimation and mass-index claims; preserve failures and unresolved Gate A cases.
5. **Applications:** explore runtimes, protocols, kernel stress testing, quantum architecture, and energy-system models without treating them as proofs of the mathematical programme.

This is a conceptual map, not a substitute for commit-backed chronology. Use [UltraCore history](https://github.com/RFT-SIRM/UltraCore-RFT/commits/main), [theorem history](https://github.com/RFT-SIRM/Evgeny-Theorem/commits/main), [synthesis history](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commits/main), and [Phi-Genesis history](https://github.com/RFT-SIRM/Phi-Genesis/commits/main) for exact dates and changes.

## 10. Release checklist

- [ ] Verify formulas and hypotheses against the primary theorem/specification.
- [ ] Keep the fourth-moment Lean theorem separate from higher-moment conjectures.
- [ ] Confirm each reported metric against its workflow or report and commit.
- [ ] Keep Gate A marked open until its explicit closure criteria are met.
- [ ] Check local links, Markdown math, navigation, and build warnings.
- [ ] Preserve negative results and old workflow records.
- [ ] Do not describe a site as live until its deployment URL and deployment workflow have been verified.
- [ ] Keep the main RFT-SIRM portal intact; link to it instead of replacing it.