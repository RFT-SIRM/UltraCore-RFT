# RFT-SIRM Research Strategy and Roadmap

**Priority order:** exact mathematics → evidence and open problems → systems methodology → implementations → exploratory applications.

[![Theory of Everything research programme](https://img.shields.io/badge/Theory%20of%20Everything-Research%20programme-5b4bc4?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) [![Fourth-moment theorem](https://img.shields.io/badge/Fourth--moment%20theorem-Lean%204%20formalization-168f83?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) [![Phi-Genesis](https://img.shields.io/badge/Phi--Genesis-Gate%20A%20open-d79a31?style=flat-square)](https://github.com/RFT-SIRM/Phi-Genesis)

[![RFT-QPU-Sierpinski](https://img.shields.io/badge/RFT--QPU--Sierpinski-Pre--experimental%20architecture-4f46e5?style=flat-square)](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) [![RFT-Invariant-Battery](https://img.shields.io/badge/RFT--Invariant--Battery-Exploratory%20energy%20model-0f766e?style=flat-square)](https://github.com/RFT-SIRM/RFT-Invariant-Battery) [![RFT-Cosmology-Genesis](https://img.shields.io/badge/RFT--Cosmology--Genesis-Phenomenological%20model-7c3aed?style=flat-square)](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis) [![Application evidence boundaries](https://img.shields.io/badge/Application%20tracks-Evidence%20bounded-d97706?style=flat-square)](docs/application-programmes.md)

[Detailed application programme index](docs/application-programmes.md).

This roadmap describes research priorities and closure criteria, not completed achievements. “Evgeny's Theory of Everything” is the name of a broad research programme; it does not assert that a complete physical theory of the Universe has been established.

## Historical chronology versus present research priorities

## Current evidence and priority snapshot — 9 November 2026

This dated register updates the mathematical status without erasing the earlier planning history below. The primary theorem repositories remain authoritative for exact definitions, theorem declarations, and proof artifacts.

| Workstream | Established result | Remaining boundary / next priority |
|---|---|---|
| SU(2) fourth moment | Exact all-level, all-angle H⁴ trace-defect identity in Lean for the defined operator and commuting control; exact normalized limit and finite-level remainder. | Independent semantic review, literature comparison, and external replication remain separate tasks. |
| H⁶ / H⁸ | Lean recurrences for \(m\ge3\); exact symbolic certificates for the exceptional \(m=2\to3\) transitions. | Formalize the finite transition bridges in Lean; do not yet describe those bridges as Lean-kernel proofs. |
| H¹⁰ | Lean-proved radius-four transport and unconditional affine recurrence for \(m\ge4\); affine form for \(m\ge5\). | The level-five correction is an exact finite trace expression; simplifying it is a presentation task. |
| Phi-Genesis lower bound | Every real eigenvalue with a nonzero real eigenvector of the defined signed Laplacian is at least (1), at every refinement level. | Preserve the precise matrix and eigenvector hypotheses in every summary. |
| Phi-Genesis least eigenvalue | For \(N\ge6\), least eigenvalues of the signless graph matrices and their gauge-conjugate signed matrices converge to \(\lambda_\infty\). | Exact rational enclosure of width \(2\times10^{-36}\), centred near (1.309128920280813421888623088170810188). |
| SIRM and applications | Separate runtime-invariant, protocol, scheduler, memory-isolation, stress-testing, and exploratory application workstreams. | Each retains its own validation criteria; no mathematical result transfers to an application by association. |

The Phi-Genesis value \(1.309128920280813421888623088170810188\ldots\) is a **limiting least-eigenvalue value for a specified graph-matrix sequence**, not a known closed-form constant and not a claim about a universal constant of nature.

### Current research priorities

1. Review the formal SU(2) operator definitions independently and compare the theorem with the relevant literature.
2. Formalize the exact H⁶/H⁸ \(m=2\to3\) finite bridges in Lean while preserving the existing reproducible certificates.
3. Simplify the H¹⁰ level-five correction coefficient without changing the proved recurrence.
4. Investigate a unified higher-moment recurrence as a separate theorem.
5. Extend the Phi-Genesis least-eigenvalue result beyond its proved \(N\ge6\) range; investigate Gate A's exceptional set and residuals independently.
6. Prove or refute the numerical quadratic increment law; seek a closed form for \(\lambda_\infty\) as a separate problem.
7. Establish any external \(\theta=2\pi\) operator identification by an explicit operator map and proof, not by numerical resemblance.

**Status rule:** the least-eigenvalue convergence theorem is complete within its stated matrix and level range; Gate A and the listed extensions remain open. Do not hide a completed result behind a broader open problem, and do not present a broader open problem as completed because a related theorem is proved.



The project history, as reported by the maintainer, begins with Rift Network, continues through Rift-L1 Blockchain and UltraCore-RFT with supporting scheduler/memory systems, and later includes Phi-Genesis, Evgeny-Theorem, and Evgeny's Theory of Everything. The [origin chronology](docs/origin-chronology.md) records that sequence separately from commit-verified milestones.

The priority order below is a current research and evidence-management plan, **not** a claim about which repository was created first.

## 1. Programme structure

The programme has three principal mathematical strands and a downstream engineering strand.

**Defined mathematical objects and assumptions**
→ **Evgeny's Theorem:** exact H⁴ SU(2) trace-defect identity; machine-checked in Lean 4
→ **Higher-moment programme:** H⁶/H⁸ recurrences and H¹⁰ affine recurrence with distinct finite/formal proof boundaries; a unified general recurrence remains open
→ **Phi-Genesis:** signed-Laplacian lower bound \(\lambda\ge1\) at every level; least-eigenvalue convergence for \(N\ge6\); exact Schur parameter-derivative recursion in the bootstrap window. Gate A and the quadratic increment law remain open.
→ **RFT-Cosmology-Genesis:** separate exact invariant limit/remainder and a phenomenological cosmology model; physical interpretation remains open
→ **SIRM:** invariant-based state transitions and engineering constraints
→ **Implementations and experiments:** runtime, protocol, scheduler, kernel stress tests
→ **Exploratory applications:** quantum architecture, energy-system model, and phenomenological cosmology

This is a reading order and research map, not a theorem asserting that each downstream application follows from the mathematics. The H⁴ trace-defect theorem does not prove the SIRM invariants, a unified higher-moment recurrence, the Phi-Genesis Gate A mechanism, or a quantum advantage. The Phi-Genesis lower bound and least-eigenvalue convergence theorem are separate completed spectral results within their stated matrix and level ranges. The exact invariant limit/remainder in RFT-Cosmology-Genesis is a separate algebraic result; its phenomenological cosmology model is not observationally validated.

## 2. Priority I — protect and independently audit the formal theorem

**Primary source:** [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md).

For the specific operator definitions and assumptions in the source repository, the fourth-moment trace defect is stated as

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge1.
$$

With the documented normalization,

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3}
\longrightarrow-\frac{16}{9}\sin^2(\theta/2),
\qquad I_m(\pi/2)\longrightarrow-\frac89.
$$

### Closure and maintenance tasks

- Keep the theorem statement, Lean declaration, definitions, assumptions, toolchain, and reproducibility commands synchronized.
- Check that the proof covers the exact quantifiers and concrete formalized operators claimed in public summaries.
- Invite independent review of the formal definitions and their correspondence to the intended mathematical construction.
- Publish a precise literature comparison and replication status; do not imply peer review until it occurs.
- Keep numerical residuals and finite-level tests separate from the universal formal statement.

The theorem is a fourth-moment result for specified operators, not a proof of every claim in the wider programme.

## 3. Priority II — complete finite higher-moment bridges and investigate the general recurrence

**Primary sources:** [Evgeny-Theorem higher-moment status](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/docs/HIGHER_MOMENTS.md) · [focused theorem dissertation](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/docs/DISSERTATION.md) · [broader synthesis dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md).

The proof status is moment-specific:

- **H⁶:** Lean proves the all-angle recurrence for \(m\ge3\); the exact \(m=2\to3\) transition is supplied by a Gaussian-integer polynomial certificate.
- **H⁸:** Lean proves the all-angle recurrence for \(m\ge3\); the exact \(m=2\to3\) transition is supplied by a sparse-polynomial certificate.
- **H¹⁰:** Lean proves the radius-four transport and unconditional affine recurrence for \(m\ge4\), with the affine formula for \(m\ge5\). Its level-five correction remains a finite exact trace expression.

The H⁶/H⁸ transition certificates are exact but are not yet Lean-kernel theorems. This is the next formalization target; it is inaccurate to describe every higher-moment result as either wholly open or wholly proved.

### Current open obligations

1. Move the exact H⁶ and H⁸ \(m=2\to3\) bridges into the Lean kernel.
2. Simplify the H¹⁰ correction expression while preserving the current unconditional theorem.
3. Prove or refute a unified recurrence for the wider family of higher moments, with explicit indexing, angles, and boundary assumptions.
4. Keep modular/CRT certificates, numerical holdouts, and Lean theorems labelled by their actual scope.

**Current status:** moment-specific results exist; a unified general higher-moment recurrence remains open.

## 4. Priority III — extend the proved Phi-Genesis spectral result and audit Gate A separately

**Primary sources:** [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) · [spectral-gap dossier](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/README.md) · [Schur eigenvalue theorem](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurEigenvalue.lean) · [signed transfer](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/PhiGenesis/SpectralGap/SchurSignedTransfer.lean).

### Completed spectral theorems

1. **Uniform lower bound:** every real eigenvalue with a nonzero real eigenvector of the explicitly defined signed Laplacian satisfies \(\lambda\ge1\), at every refinement level. See \`sgSignedLaplacianMatrix_eigenvalue_ge_one\`.
2. **Least-eigenvalue identification:** for the signless Laplacians \(Q_{6+n}\), the canonical A1 Schur root in the fixed bootstrap interval is the least eigenvalue. The same result transfers to the gauge-conjugate signed matrices.
3. **Convergence:** both least-eigenvalue sequences converge to \(\lambda_\infty\), with
$$
\frac{1309128920280813421888623088170810187}{10^{36}}
\le\lambda_\infty\le
\frac{1309128920280813421888623088170810189}{10^{36}}.
$$
   Its decimal location is approximately \(1.309128920280813421888623088170810188\), with interval width \(2\times10^{-36}\).

The number \(1.3091289\ldots\) is a limiting least-eigenvalue value for the specified graph matrices. It is not currently known in closed form and is not claimed to be a fundamental physical constant.

### Remaining Gate A and extension criteria

- Characterize the complete exceptional set in the broader spectral-decimation correspondence.
- Explain residual mismatches and retain matching rates by level and method.
- Prove or refute the observed quadratic increment law and determine whether its numerical coefficient has a rigorous limit.
- Extend the least-eigenvalue convergence theorem to levels \(N<6\).
- Prove any external \(\theta=2\pi\) operator identification using an explicit operator map, boundary conditions, and a proof.
- Keep mass-index hypotheses separate from proved graph-spectral statements.

**Current status:** the lower-bound and least-eigenvalue convergence theorems are proved within their stated matrix and level ranges. Gate A remains open; it is not closed by the least-eigenvalue theorem.

## 5. Priority IV — maintain SIRM engineering evidence

SIRM (Synthetic Intelligence Reasoning Model) defines runtime invariants for state transitions. The constraints below use compact symbols to keep the equations readable in GitHub's Markdown renderer:

- \(S\): total supply
- \(B\): total base sum
- \(G\): global field
- \(M\): total minted
- \(R\): total burned
- \(D\): dust accumulator
- \(b_i\): effective balance of account \(i\)
- \(q_i\): base balance of account \(i\)

$$
I_{1}: S = B + Gp
$$

$$
I_{2}: S = M - R
$$

$$
I_{3}: 0 \le D < p,\qquad p > 0
$$

$$
I_{4}: b_i \ge -\frac{S}{10p}
$$

The effective balance is defined by \(b_i = q_i + G\), subject to the implementation's integer and scaling conventions.

The global-scalar representation can make the distribution update $O(1)$; that statement does not imply every operation is constant-time. Engineering validation should remain tied to the code and tested configuration.

| Workstream | Evidence discipline |
|---|---|
| [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Runtime tests, fuzz configuration, invariant assertions, versioned outputs |
| [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Devnet evidence, audit findings, test coverage, explicit network status |
| [Agave memory contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | Distinguish proof-of-concept findings from upstream architecture and current releases |
| [Agave scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Reproducible benchmark scenarios, source revision, workload assumptions, upstream discussion |
| [seL4 CDT stress test](SEL4_CDT_FUZZING.md) | Complementary stress testing, not a replacement for seL4's formal proof |
| [Aave V4 Hub model review](https://github.com/RFT-SIRM/aave-v4-hub-model-review) | Model review, not protocol-wide formal verification |

Every public metric should point to a report or dated workflow. Passing tests demonstrate the assertions executed, not every possible execution.

## 6. Priority V — applications remain explicitly exploratory

- **[RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski):** pre-experimental architecture. Do not claim hardware advantage, circuit efficiency, or quantum speed-up without resource estimates and experiments. See the [application programme index](docs/application-programmes.md) for validation and disclosure boundaries.
- **[RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.):** exploratory computational scenarios. Model outputs are not independent experimental validation of a battery technology.
- Other physical, biological, and temporal-topology directions remain hypotheses or planned research unless a specific model, experiment, and evidence record is linked.

## 7. Evidence labels and promotion rules

| Label | Promotion criterion |
|---|---|
| **Machine-checked** | Exact formal statement builds with a pinned toolchain; assumptions and definitions are linked |
| **Analytically proved** | Complete written proof with quantifiers, assumptions, boundary conditions, and exceptional cases |
| **Certified finite-level** | Certificate and bounds establish the stated finite cases only |
| **Numerically reproduced** | Inputs, parameters, code revision, tolerance, outputs, and limitations are recorded |
| **Engineering-tested** | Tests, fuzzing, audits, or deployments support a specified implementation claim |
| **Hypothesis / open** | A clear proposed claim with a falsifiable closure plan |
| **Rejected / not established** | Counterexample or evidence record explains why the stronger claim is unsupported |

A claim moves to a stronger category only when its evidence changes. A new badge, successful workflow, or rewritten pitch cannot upgrade the underlying result.

## 8. Historical and release discipline

The history is part of the evidence. Preserve failed workflows, corrections, rejected hypotheses, and earlier status reports. Later results should add context rather than rewrite what was known at the time.

- [Commit-backed historical chronology](docs/history.md)
- [Research map](docs/research-map.md)
- [AI reading guide](AI_GUIDE.md)
- [Scientific basis](SCIENTIFIC_BASIS.md)
- [Main RFT-SIRM portal](https://rft-sirm.github.io/) — remains the organization-wide entry point

Before a release, verify formulas against primary sources; run the documented tests; build MkDocs strictly; check internal and external links; confirm the interactive page output; verify status labels; and report any remaining failure explicitly.

---

_Copyright 2026 Eugeny (RFT-SIRM). License: Apache-2.0 for original repository content, subject to LICENSE and NOTICE._