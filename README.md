# UltraCore-RFT — Mathematical Foundations, Evidence, and Systems

**The RFT-SIRM research and engineering hub:** a coordinated portfolio spanning machine-checked mathematics, recursive spectral research, a proposed Sierpiński/SU(2) quantum-processing architecture, and a Lean-formalized financial-state model. Each workstream has its own definitions, source repository, tests, and evidence boundary. **RFT** means **Resonant Field Theory** (резонансная теория поля); **SIRM** means **Synthetic Intelligence Reasoning Model** (Синтетическая интеллектуальная модель рассуждений).


## Core development portfolio

UltraCore-RFT is the central navigation and evidence hub for four primary, independently scoped development strands. The source repositories remain authoritative for their definitions, proofs, models, tests, and limitations.

| Core strand | Canonical source | Current work | Evidence boundary |
|---|---|---|---|
| **SU(2) mathematical theorem** | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Lean 4 formalization of the stated all-level fourth-moment trace-defect identity for the specified SU(2)-connected Sierpiński-gasket operators. Higher moments H⁶/H⁸/H¹⁰ have separate, narrower proof and certificate statuses. | The theorem covers its encoded operators and quantifiers; it does not prove every higher-moment extension or a physical implementation. |
| **Signed-flux spectral theory** | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Lean proves the stated signed-Laplacian lower bound and, for the signless graph Laplacians and their gauge-conjugate signed matrices at $N\ge6$, least-eigenvalue identification and convergence to a limit in an exact rational interval. | Gate A, the quadratic increment law, levels $N<6$, and the external $\theta=2\pi$ identification remain open. This is a distinct operator family from the SU(2) fourth-moment theorem. |
| **Sierpiński quantum-processing architecture** | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | A proposed level-1 tile has 6 graph sites, 9 edges, 3 selected non-commuting X/Y/Z SU(2) links, 12 transmon modes, and 22 effective exchange channels. A candidate logical qubit is represented by a two-dimensional low-energy subspace; Stage 11B records a re-quantized three-mode gate-model study. | **Pre-experimental.** Stage 11B figures are closed-system model projections, not measured gate fidelities or a full 12-transmon simulation. No chip has been fabricated or measured; the complex-Z link and graph-wide multi-tone plan remain unresolved. |
| **Formal financial infrastructure** | [SIRM-Financial-Infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) | Lean 4 specifies supply and holder state, balanced general-ledger postings, authorization and finite registries, exact asset-unit conversion and migration residuals, nonce/receipt handling, and integrated pooled escrow, time-lock, and first-stage dispute-freeze transitions. | An abstract formal state-transition model, not a deployed financial service. Rust refinement, production persistence and signatures, custody, reserves, settlement, legal and regulatory operation remain separate obligations. |

The four strands are coordinated by this hub, but their results are **not interchangeable**: a proof for one operator family does not establish another family's spectral claims; the QPU model is not hardware validation; and financial-state theorems do not certify a production runtime or network. See the [research map](docs/research-map.md) and [architecture](docs/architecture.md) for the relationships and boundaries.

> **Research monographs — two distinct scopes**
>
> **Focused theorem dissertation:** [Spectral Trace Defects of Noncommutative SU(2) Connections on Sierpiński-Gasket Graphs](docs/DISSERTATION.md). It covers the specified SU(2) operators, the all-level fourth-moment identity, its normalized limit, and the separately scoped H⁶/H⁸/H¹⁰ results. The formal source remains [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem).
>
> **Broader synthesis dissertation:** [Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md). It surveys the wider recursive-operator programme, finite higher-moment certificates, numerical recurrence work, and the separate signed-flux spectral programme. Its source version is dated 15 October 2026; consult the source repositories for later proof-status changes.
>
> These documents are complementary, not interchangeable. The canonical texts remain in their respective repositories. See the [Research Monographs guide](docs/monographs.md).
>
> [![Read the dissertation](https://img.shields.io/badge/READ%20THE%20DISSERTATION-Research%20synthesis-5b4bc4?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md)

## Research and evidence

These links describe the scientific work and its current evidence status. Badge colours have a consistent meaning: **purple = research programme**, **teal = formalized result**, **amber = open or evidence-limited work**, and **blue = navigation or portal**.

[![Theory of Everything research programme](https://img.shields.io/badge/Research-Theory%20of%20Everything-5b4bc4?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything)
[![Fourth-moment theorem](https://img.shields.io/badge/Formal%20result-Fourth--moment%20theorem-168f83?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization)
[![Phi-Genesis](https://img.shields.io/badge/Phi--Genesis-Convergence%20proved%20-%20Gate%20A%20open-d97706?style=flat-square)](https://github.com/RFT-SIRM/Phi-Genesis)
[![Interactive portal](https://img.shields.io/badge/Portal-Research%20explorer-4777bd?style=flat-square)](https://rft-sirm.github.io/UltraCore-RFT/interactive/)
[![Core development portfolio](https://img.shields.io/badge/Portfolio-Core%20Development-4777bd?style=flat-square)](https://rft-sirm.github.io/UltraCore-RFT/core-development/)

## Other exploratory application programmes

These are additional exploratory or application tracks—not proofs of the mathematical claims or substitutes for the core quantum-architecture and financial-infrastructure workstreams above. They use one badge size and a restrained colour system so they read as one group.

[![RFT-Invariant-Battery](https://img.shields.io/badge/Exploratory%20model-RFT--Invariant--Battery-d97706?style=flat-square)](https://github.com/RFT-SIRM/RFT-Invariant-Battery)
[![RFT-Cosmology-Genesis](https://img.shields.io/badge/Phenomenological%20model-RFT--Cosmology--Genesis-d97706?style=flat-square)](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis)
[![Application evidence boundaries](https://img.shields.io/badge/Application%20tracks-Evidence%20bounded-d97706?style=flat-square)](docs/application-programmes.md)

## Daily spectral computation record

UltraCore-RFT runs the two canonical Phi-Genesis daily computational workloads independently: the level-9 deep suite and the high-precision A1/E spectral-matrix jobs. Each run records the exact upstream Phi-Genesis commit and preserves logs as Actions artifacts.

[Daily computation record](docs/phi-genesis-computations.md) · [Nightly deep workflow](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/phi-genesis-nightly-deep.yml) · [High-precision matrix workflow](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/phi-genesis-high-precision.yml)

## Verification and repository status

These badges report the status of specific workflows only. They do not certify the entire research programme or transfer proof status between repositories.

[![Theory of Everything upstream verification](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/theory-of-everything.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/theory-of-everything.yml)
[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)
[![Pages deployment](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/pages.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/pages.yml)
[![Apache-2.0 license](https://img.shields.io/badge/License-Apache--2.0-blue.svg?style=flat-square)](LICENSE)

## Core engineering and formal-verification strands

[![Rift-L1 Blockchain](https://img.shields.io/badge/Engineering-Rift--L1%20Blockchain-2563eb?style=flat-square)](https://github.com/RFT-SIRM/Rift-L1-Blockchain)
[![Rift Network](https://img.shields.io/badge/Engineering-Rift%20Network-2563eb?style=flat-square)](https://github.com/RFT-SIRM/Rift-Network)
[![Agave Rift Scheduler CI](https://github.com/RFT-SIRM/agave-rift-scheduler/actions/workflows/ci.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/agave-rift-scheduler/actions/workflows/ci.yml)
[![Agave Rift Scheduler Fuzz](https://github.com/RFT-SIRM/agave-rift-scheduler/actions/workflows/fuzz-daily.yml/badge.svg?style=flat-square)](https://github.com/RFT-SIRM/agave-rift-scheduler/actions/workflows/fuzz-daily.yml)
[![Lean 4 formalization tests](https://img.shields.io/github/actions/workflow/status/RFT-SIRM/Evgeny-Theorem/tests.yml?branch=main&label=Lean%204%20tests&style=flat-square)](https://github.com/RFT-SIRM/Evgeny-Theorem/actions/workflows/tests.yml)

These are **separate repositories and separate evidence scopes**. Rift-L1 and Rift Network publish source-available code under their own restrictive terms; the Apache-2.0 badge above applies only to original material in this UltraCore-RFT repository. Scheduler CI/fuzz and Lean 4 test badges link to their source workflows; a badge reflects that workflow, not a universal proof of the wider programme.

## Historical origin sequence

The project family's historical order is distinct from the evidence-first reading order used to assess claims. The maintainer-reported sequence is **Rift Network → Rift-L1 Blockchain → UltraCore-RFT and supporting systems (scheduler, memory, and related engineering) → Phi-Genesis → Evgeny-Theorem → Evgeny's Theory of Everything**. See the [origin chronology](docs/origin-chronology.md) for scope, source links, and the distinction between reported order and commit-verified dates.

This order records development history; it does not claim that every later project depends technically on every earlier one.

**Start with the research, not the applications:** [Focused fourth-moment dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [Broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [Phi-Genesis spectral theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean) · [Research map](docs/research-map.md) · [AI reading guide](AI_GUIDE.md)

UltraCore-RFT is the documentation and coordination hub for the RFT-SIRM ecosystem. Its scientific story begins with mathematical definitions, theorem statements, and their evidence boundaries. Runtime systems, blockchain protocols, and other applications are downstream research programmes—not the foundation used to certify the mathematics.

> **Important scope statement.** The phrase *Evgeny's Theory of Everything* names a broad, ongoing research programme. It does not mean that a complete physical theory of the Universe has been established. The SU(2) fourth-moment identity is formalized in Lean for its stated operators and quantifiers. H⁶ and H⁸ have Lean recurrences from level $m\ge3$ plus exact finite certificates for the exceptional $2\to3$ transition; H¹⁰ has an unconditional Lean recurrence for $m\ge4$ and affine form for $m\ge5$. Phi-Genesis separately proves convergence of the least eigenvalues of its signed/signless graph matrices for $N\ge6$, while Gate A, the quadratic increment law, and the external $\theta=2\pi$ identification remain open.

## Historical record: research and engineering strands

This programme has developed across separate repositories. The following are **documented workstreams**, not claims of institutional endorsement or that every project has the same verification status.

| Workstream | Public record | Scope and evidence boundary |
|---|---|---|
| Mathematical research and dissertations | [Focused fourth-moment dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) | The H⁴ identity is Lean-formalized for all stated levels and angles; H⁶/H⁸/H¹⁰ have distinct, explicitly bounded proof statuses. |
| Spectral computation and formal result | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Lean proves the least eigenvalue and convergence for signed/signless graph matrices at $N\ge6$; Gate A, the quadratic law, and external-model identification remain open. |
| Quantum-processing architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Proposed 12-transmon level-1 mapping and candidate logical subspace; closed-system numerical models only, with physical validation gates open. |
| Formal financial infrastructure | [SIRM-Financial-Infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) | Lean 4 abstract financial-state/accounting model; production identity, persistence, Rust refinement, custody and settlement remain open. |
| Solana / Agave engineering | [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) · [Agave Rift Scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) · [ABIv2 memory contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | On-chain protocol, scheduler and memory-context research; claims are scoped to their code, tests and documented environments. |
| seL4 kernel stress research | [seL4 CDT report](SEL4_CDT_FUZZING.md) · [field-trial report](docs/field_trials_sel4.md) | Reproducible empirical stress-testing report. It does not replace or extend the seL4 project's formal verification claims. |
| DeFi model review | [Aave V4 Hub model review](https://github.com/RFT-SIRM/aave-v4-hub-model-review) | Separate model-based review and invariant-analysis work; not an Aave endorsement. |
| Standalone L1 and exploratory applications | [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain) · [Invariant Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery) | Distinct implementation or exploratory tracks; no implied production or experimentally validated result beyond the linked evidence. |
| Research chronology | [Commit-backed history](docs/history.md) · [Research map](docs/research-map.md) | Selected milestones with direct links; use each repository's commit log for the complete record. |

### External organizations and attribution

Repository activity, public issues, or work in an open-source ecosystem must not be presented as employment, a contract, a partnership, sponsorship, approval, or endorsement by NASA, Anza, Solana, the seL4 project, Aave, or any other institution unless a specific public source establishes that relationship. The current curated project history links to verifiable repository artifacts. A standalone NASA- or MATLAB-specific project is **not listed here as verified** because the available repository and commit evidence reviewed for this update did not identify a matching artifact. If such work exists in a separate public repository or contribution, its exact URL should be added to the chronology rather than inferred from a profile screenshot.

## Formal contact and research submissions

For collaboration proposals, research correspondence, licensing questions, or requests for formal review, use the designated contact route and include a clear subject, the relevant repository/commit, the requested action, and the sender's institutional or organizational affiliation where applicable. A GitHub issue or pull request is appropriate for public, technical, reproducible discussion; confidential, contractual, licensing, or personal information should not be posted publicly.

See [CONTACT.md](CONTACT.md) for the submission and attribution policy. Public contact details should be a dedicated, controlled mailbox that the maintainer intends to monitor; do not assume that a commit-author email is automatically the official legal or business contact.

---

## 1. The mathematical anchor

### Evgeny's Theorem: a closed fourth-moment identity

The primary theorem repository studies a specified SU(2)-valued connection on a Sierpiński-gasket graph and compares a noncommuting configuration $C$ with a commuting control $C'$. For the definitions and assumptions in the source project, the fourth-moment trace defect is stated as

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16\left(3^{m-1}+1\right)\sin^2\left(\frac{\theta}{2}\right),
\qquad m=1,2,3,\ldots.
$$

The normalized quantity is

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3},
\qquad
\lim_{m\to\infty} I_m(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

At the special angle $\theta=\frac{\pi}{2}$, the limit simplifies to:

$$
-\frac{8}{9}
$$

The exact finite-level remainder is

$$
I_m(\theta)-I_\infty(\theta)
=-\frac{32}{9(3^m+1)}\sin^2\left(\frac{\theta}{2}\right).
$$

**What is machine-checked:** the source project reports a Lean 4 formalization for every integer level $m=1,2,3,\ldots$ and every angle covered by its statement, for the concrete operators defined there. The formal proof establishes the formal proposition; readers should still distinguish proof checking from independent review that the formal definitions fully capture the intended mathematical construction.

**What the theorem does not establish:** it does not prove the full spectrum, all higher moments, a physical law, a quantum speed-up, a solution to a Millennium Prize Problem, or the entire broader Theory-of-Everything programme.

Primary sources: [focused theorem dissertation](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/DISSERTATION.md) · [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · [test workflows](https://github.com/RFT-SIRM/Evgeny-Theorem/actions) · [project site](https://rft-sirm.github.io/Evgeny-Theorem/).

### Numerical cross-checks are a different evidence layer

The source repository reports direct numerical comparisons for levels $m=1,\ldots,7$, held-out angle checks, and gauge-transformation checks. These support the implementation and provide reproducibility evidence; the all-level statement rests on the Lean theorem, not on extrapolating a finite table.

| Level $m$ | $\dim(H)=3^{m+1}+3$ | $\Delta_m(H^4,\pi/2)$ | $I_m(\pi/2)$ |
|---:|---:|---:|---:|
| 1 | 12 | −16 | −1.333333 |
| 2 | 30 | −32 | −1.066667 |
| 3 | 84 | −80 | −0.952381 |
| 4 | 246 | −224 | −0.910569 |
| 5 | 732 | −656 | −0.896175 |
| 6 | 2,190 | −1,952 | −0.891324 |
| 7 | 6,564 | −5,840 | −0.889701 |
| Limit | — | — | $-8/9$ |

The raw formula, normalized denominator, and displayed table use the same convention. For example, at $m=1$ and $\theta=\pi/2$, the raw defect is $-16(1+1)/2=-16$; dividing by $12$ gives $-4/3$. As $m$ grows, the ratio tends to $-16/9\sin^2(\theta/2)$.

---

## A separate formal spectral result: Phi-Genesis

This is a second mathematical result in a **different operator family**. It concerns the signless graph Laplacian $Q_N$ on the level-$N$ Sierpiński-gasket graph and its diagonally gauge-conjugate signed matrix. It is not a corollary of the SU(2) fourth-moment theorem above.

For every level $N=6+n$ with $n\ge0$, the Lean development proves that the least eigenvalue exists, is the unique A1 Schur root in the bootstrap interval, and belongs to a convergent sequence. The signed and signless matrices have the same eigenvalues by gauge conjugation.

The limiting least eigenvalue is proved to lie in the exact rational interval

$$
\lambda_\infty\in
\left[
\frac{1309128920280813421888623088170810187}{10^{36}},
\frac{1309128920280813421888623088170810189}{10^{36}}
\right].
$$

The interval has width $2\times10^{-36}$. This is a rigorous enclosure, not a closed form.

**Formal sources:** [least-eigenvalue and convergence theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean) · [signed/signless transfer](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean) · [PR #31: exact next-level identities](https://github.com/RFT-SIRM/Phi-Genesis/pull/31) · [PR #32: signed eigenvalue transfer](https://github.com/RFT-SIRM/Phi-Genesis/pull/32).

**Still open:** a proof of the quadratic increment law and its constant (currently numerical evidence), a closed form for the limit, levels $N<6$, the full Gate A exceptional-set characterization, and identification with an external $\theta=2\pi$ operator beyond the explicitly defined graph matrix. This theorem does not close Gate A or establish a bridge to the SU(2) operators.

---

## 2. The broader research programme

The research programme extends beyond the one formal theorem. Its components must remain connected but not conflated.

<details>
<summary><strong>Strand A — Evgeny's Theory of Everything: higher moments and recursive operators</strong></summary>

Primary repository: [RFT-SIRM/Evgeny-s-Theory-of-Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) · [dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md).

The synthesis programme studies higher-moment trace defects, Fourier coefficients, finite-level recurrence residuals, and the possibility of an all-level law for recursive graph/operator families.

- **H⁶ and H⁸:** Lean proves their all-angle recurrences for $m\ge3$; exact symbolic certificates close the finite $m=2\to3$ transition. These bridges are exact but are not yet Lean-kernel theorems.
- **H¹⁰:** Lean proves the required radius-four transport, the unconditional affine recurrence for $m\ge4$, and the affine formula for $m\ge5$. The level-five correction remains an exact finite trace expression rather than an expanded trigonometric polynomial.
- **Numerical evidence:** held-out angle grids, sparse-matrix-power calculations, and cross-checks are finite reproducibility checks; they do not replace the proof boundaries above.
- **Open extension:** a single general all-level recurrence theorem covering the higher-moment family remains open. Exact certificates and individual moment theorems must be cited at their own stated scope.
- **Research obligation:** derive the exceptional first-transition correction from the recursive construction, prove the recurrence or find a counterexample, and formalize any complete derivation against explicit definitions.

The dissertation itself explicitly distinguishes the fourth-moment theorem from the higher-moment programme. Read [the dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md), [recurrence note](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md), and [modular certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md).

</details>

<details>
<summary><strong>Strand B — Phi-Genesis: signed-flux spectral decimation and mass-formula audit</strong></summary>

Primary repository: [RFT-SIRM/Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) · [live research site](https://rft-sirm.github.io/Phi-Genesis/).

Phi-Genesis studies signed $Z_2$-flux graph Laplacians, spectral decimation with boundary/corner corrections, inertia calculations, and exploratory spectral or mass-index patterns. It is a separate operator family from the SU(2)-connected construction in Evgeny's Theorem.

- Some proposed claims have been rejected or narrowed by the documented audits.
- Numerical results and tests support specific computational statements only within their stated parameters and code paths.
- **Proved in Lean:** for the signless Laplacian $Q_N$ and its gauge-conjugate signed matrix, $N\ge6$, the least eigenvalue is the unique A1 root in the exact 36-digit interval and the sequence of least eigenvalues converges to a point of that interval. See the [formal eigenvalue theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean) and [signed transfer](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean).
- **Still open:** Gate A's full exceptional set, the quadratic increment law and its constant (numerical evidence only), a closed form for the limit, levels $N<6$, and the external $\theta=2\pi$ operator identification.
- A fitted or selected mass-index pattern is not an established predictive physical law without a prospective selection mechanism, predeclared predictions, held-out validation, and an independent derivation.
- No equivalence between the SU(2) operators and signed-flux Laplacians is assumed. Any bridge requires an explicit map, boundary conditions, preserved quantities, exceptional cases, and proof or a clearly labelled conjecture.

Start with [the repository status and methods](https://github.com/RFT-SIRM/Phi-Genesis), then inspect its versioned test workflows and reports. The fact that tests pass does not close Gate A unless the tests actually establish its closure criteria.

</details>

<details>
<summary><strong>Strand C — SIRM and deterministic execution</strong></summary>

SIRM (Synthetic Intelligence Reasoning Model) is the systems-engineering strand: define state invariants and require every state transition to preserve them or fail atomically.

The four stated runtime constraints are shown below using compact mathematical symbols. The mapping table identifies the implementation variables.

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

Here $\mathtt{effective\_balance}[i]=\mathtt{base\_balance}[i]+\mathtt{global\_field}$, under the model's stated integer and scaling conventions. The $O(1)$ distribution claim follows from changing a shared scalar and computing each effective balance on read; it does not mean every runtime operation is $O(1)$, nor does it itself establish security of every implementation.

SIRM is an engineering model and specification. The Lean theorem above is a separate mathematical result; there is no claim that the spectral theorem proves the runtime invariants.

</details>


<details>
<summary><strong>Strand D — RFT-QPU-Sierpinski: proposed logical-qubit architecture</strong></summary>

Primary source: [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) · [repository status](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/REPOSITORY_STATUS.md) · [validation plan](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/docs/VALIDATION_PLAN.md) · [calculated result summary](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/engineering/physical_prototype/results/RESULT_SUMMARY.md).

The architecture maps a level-1 Sierpiński-gasket graph to a proposed transmon system. Each graph site carries a two-component internal degree of freedom; the candidate logical qubit is a selected two-dimensional low-energy subspace. The proposed tile contains 12 transmon modes and 22 effective exchange channels, with three selected non-commuting SU(2) links.

The Stage 11B selected local retune reports a projected process overlap of 0.9999999793763371 after local-Z fitting and an average logical-state fidelity including leakage of 0.9999999803654352 at five retained levels and 480 time steps per pump period. These are **closed-system numerical projections for a three-mode A–coupler–B model**, not measured fidelities and not a driven simulation of the complete 12-mode tile. The seven-level 240/480 propagation remains open, and raw fine-retune JSON/NPZ artifacts are not tracked.

The architecture remains **pre-experimental**. A resonant complex-Z link requires a concrete phase-engineered circuit; the current single real static coupler is insufficient. The graph-wide nine-tone screen reports 73 primary and 653 conditional resonance warnings with zero minimum primary margin. Open-system T1/T2, thermal, flux-line, crosstalk, layout-extraction, fabrication, and measured one-/two-cell validation remain ahead. No chip, measured gate, fault tolerance, or quantum advantage is claimed.

The QPU repository has its own BUSL-1.1 source-licensing terms. The Apache-2.0 licence of this hub does not relicense that repository or its materials.

</details>

<details>
<summary><strong>Strand E — SIRM Financial Infrastructure: formal financial state and accounting</strong></summary>

Primary source: [SIRM-Financial-Infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) · [formalization status](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/FORMALIZATION_STATUS.md) · [mathematical scope](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/MATHEMATICAL_SCOPE.md) · [testing guide](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure/blob/main/docs/TESTING.md).

This is a dedicated Lean 4.33.1 workstream for financial-state transitions and accounting invariants. The combined authorized financial machine updates holder balances and the corresponding signed general-ledger journal in one abstract state transition. Its wider model includes:

- supply/holder reconciliation, balanced journals, and matching holder/GL postings;
- exact principal/account control, operation-scoped grants, typed account and asset registries, and issuer/recipient-aware issuance;
- exact decimal-to-base-unit conversion, rational cross-network migration, and route/account-partitioned residual carry-forward;
- per-principal nonces, typed request receipts, exact retry behaviour, and cached authorization/insufficient-funds denials;
- concurrent escrow IDs, pooled reserve/vault/GL reconciliation, discrete deadlines and expiry refunds, and a first-stage per-ID dispute intake/freeze.

The pinned workflow is configured as one Lean build/theorem-test job plus 17 independent static audits. That is a description of the CI topology; a specific passing result must always be tied to its exact commit and workflow run.

The model is not a production financial service. The repository explicitly leaves real identity and key custody, cryptographic signatures and thresholds, persistent transaction storage, production database atomicity, full canonical request encoding, Lean-to-Rust refinement, reserve backing, redemption, external settlement, adjudication, and legal/regulatory operation outside the current proofs. The Rust reference implementation is planned, not complete.

This financial specification is related to the RFT-SIRM ecosystem but is not derived from the Sierpiński spectral theorems. See its own [README](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure#readme) and evidence documents for exact assumptions.

</details>

---

## 3. From mathematics to applications

The project hierarchy is intentional: theorem and evidence first, related research programmes second, implementation and application systems third.

| Research/application layer | Primary source | Current scope and boundary |
|---|---|---|
| **Formal fourth-moment theorem** | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Specific SU(2)/Sierpiński-gasket identity; Lean 4 formalization reported for all stated levels |
| **Higher-moment research** | [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | Finite-level certificates and numerical holdouts; all-level recurrence open |
| **Signed-flux spectral research** | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Spectral decimation and mass-formula audit; Gate A open |
| **Quantum-processing architecture** | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Core engineering architecture with a candidate two-dimensional logical subspace; numerical only and pre-experimental, with no fabricated device or measured gate |
| **Formal financial infrastructure** | [SIRM Financial Infrastructure](https://github.com/RFT-SIRM/SIRM-Financial-Infrastructure) | Lean 4 financial-state and accounting model with integrated holder/GL transitions, authorization, registries, migration, receipts, and escrow/dispute invariants; no production runtime or external-settlement claim |
| **Energy-system model** | [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery) | Exploratory computational scenarios with explicit assumptions |
| **Standalone execution runtime** | [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Implementation-specific runtime, invariant checks, and fuzzing reports |
| **On-chain protocol** | [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) · [Devnet client](https://rift-network.vercel.app) | Solana Devnet research deployment; not a claim of mainnet readiness |
| **SVM memory-context research** | [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | Proof-of-concept investigation; findings are specific to its studied code path |
| **Conflict-aware scheduling** | [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Scheduler research and upstream discussion |
| **DeFi ledger model** | [aave-v4-hub-model-review](https://github.com/RFT-SIRM/aave-v4-hub-model-review) | Invariant model review, complementary to rather than replacing formal verification |
| **Kernel stress testing** | [seL4 test report](SEL4_CDT_FUZZING.md) | Complementary stress testing of a specific seL4 subsystem; not a replacement for seL4's formal proof |

Metrics such as fuzz-run counts, test totals, audit findings, and runtime durations are source-reported snapshots, not live counters in this README. Consult each source repository and its dated workflow/report before quoting a figure externally.

---

## 4. Historical development and provenance

The programme should be read as a portfolio of increasingly explicit evidence obligations—not as a story in which every hypothesis has become a theorem. The QPU architecture and SIRM Financial Infrastructure are tracked as core engineering strands with separate source repositories and release gates.

1. **Invariant-first engineering.** SIRM began as a way to specify and enforce state constraints across deterministic runtime transitions. The runtime repositories retain their own implementation histories and test records.
2. **A precise spectral identity.** Evgeny's Theorem isolates a concrete SU(2)-connected Sierpiński-gasket operator and a commuting control, then states a closed form for the fourth-moment trace defect. The theorem repository contains the formalization and numerical verification records.
3. **Extension beyond the fourth moment.** The Theory-of-Everything synthesis repository collects higher-moment computations and finite-level certificates. It explicitly leaves the all-level recurrence open.
4. **A separate spectral-decimation audit.** Phi-Genesis examines signed-flux Laplacians and mass-index claims. Rejections and open residuals are retained as results of the audit, not erased to make the narrative look complete.
5. **Core engineering and applications.** The Sierpiński QPU architecture and SIRM Financial Infrastructure have dedicated evidence records alongside deterministic runtime, blockchain, and energy-system work. Their models and proofs remain separate from the mathematical theorem repositories; none retroactively proves another strand.

For chronology, cite the actual source history rather than inferring dates from this summary: [UltraCore commit history](https://github.com/RFT-SIRM/UltraCore-RFT/commits/main) · [Evgeny-Theorem history](https://github.com/RFT-SIRM/Evgeny-Theorem/commits/main) · [Theory-of-Everything history](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commits/main) · [Phi-Genesis history](https://github.com/RFT-SIRM/Phi-Genesis/commits/main).

---

## 5. Evidence vocabulary

| Label | Meaning in this repository |
|---|---|
| **Machine-checked** | A stated proposition is accepted by the specified proof assistant/build configuration. Review that formal definitions match the intended mathematics. |
| **Analytically proved** | A written proof establishes the stated claim from explicit assumptions; cite the proof. |
| **Numerically reproduced** | Computation matches a stated prediction on named inputs. Finite checks alone do not prove a universal claim. |
| **Engineering-tested** | Tests, fuzzing, audit work, or deployment checks support an implementation-specific statement. |
| **Certified finite-level** | A certificate establishes the stated finite coefficient or case under its explicit bounds and assumptions; it does not automatically quantify over all levels. |
| **Hypothesis / conjecture** | A precise proposed extension awaiting proof, refutation, or decisive validation. |
| **Open** | The required proof, derivation, independent replication, or experiment remains incomplete. |
| **Rejected / not established** | Available counterexamples or evidence do not support the stronger claim. Keep the reason and scope visible. |

A passing workflow supports only the assertions it runs. A proof in one repository does not transfer automatically to a related repository, operator family, physical interpretation, or application.

---

## 6. Navigation

- **[Research map and evidence boundaries](docs/research-map.md)** — relationships, statuses, and closure criteria.
- **[AI guide](AI_GUIDE.md)** — instructions for language models and automated research assistants; read before summarizing claims.
- **[Scientific basis](SCIENTIFIC_BASIS.md)** — modelling vocabulary versus literal mathematics.
- **[Pitch and research dossier](PITCH.md)** — audience-facing narrative, methodology, and claims register.
- **[Platform strategy](docs/platform.md)** and [architecture](docs/architecture.md) — runtime architecture and engineering decisions.
- **[SIRM foundations](docs/foundations.md)** — model definitions and invariants.
- **[Verification evidence](docs/field_trials.md)** and [seL4 report](SEL4_CDT_FUZZING.md) — implementation-specific validation.
- **[Main RFT-SIRM portal](https://rft-sirm.github.io/)** — organization-wide entry point. It remains separate and is not replaced by this repository.

## License

Original material in this repository is distributed under [Apache-2.0](LICENSE), subject to the license and NOTICE files. Linked repositories are separate works with their own histories, content, and licensing terms.

_Copyright 2026 Evgeniy Zaprudnov (RFT-SIRM)._

## Cross-repository verification: Theory of Everything

The **Theory of Everything — upstream verification** workflow checks the current `main` revision of [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) from this repository. It validates the dissertation and required research files, runs the documentation/provenance audit, and executes the recurrence arithmetic audit and its regression tests.

- [Workflow runs and logs](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/theory-of-everything.yml)
- Triggered manually with **Run workflow**, on relevant changes to this integration, and on a daily schedule.
- The job log records the exact upstream Git revision it checked, so a green result can be traced to a specific source snapshot.
- A passing run means only that these listed checks passed. It does **not** establish the still-open all-level higher-moment recurrence or replace the pinned Lean and specialized numerical workflows in the source repository.
