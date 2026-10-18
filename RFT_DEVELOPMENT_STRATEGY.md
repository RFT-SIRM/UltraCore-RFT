# RFT-SIRM Research Strategy and Roadmap

**Priority order:** exact mathematics → evidence and open problems → systems methodology → implementations → exploratory applications.

[![Theory of Everything research programme](https://img.shields.io/badge/Theory%20of%20Everything-Research%20programme-5b4bc4?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) [![Fourth-moment theorem](https://img.shields.io/badge/Fourth--moment%20theorem-Lean%204%20formalization-168f83?style=flat-square)](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) [![Phi-Genesis](https://img.shields.io/badge/Phi--Genesis-Gate%20A%20open-d79a31?style=flat-square)](https://github.com/RFT-SIRM/Phi-Genesis)

[![RFT-QPU-Sierpinski](https://img.shields.io/badge/RFT--QPU--Sierpinski-Pre--experimental%20architecture-4f46e5?style=for-the-badge)](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) [![RFT-Invariant-Battery](https://img.shields.io/badge/RFT--Invariant--Battery-Exploratory%20energy%20model-0f766e?style=for-the-badge)](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) [![RFT-Cosmology-Genesis](https://img.shields.io/badge/RFT--Cosmology--Genesis-Phenomenological%20model-7c3aed?style=for-the-badge)](https://github.com/RFT-SIRM/RFT-Cosmology-Genesis) [![Application evidence boundaries](https://img.shields.io/badge/Application%20tracks-Evidence%20bounded-d97706?style=flat-square)](docs/application-programmes.md)

[Detailed application programme index](docs/application-programmes.md).

This roadmap describes research priorities and closure criteria, not completed achievements. “Evgeny's Theory of Everything” is the name of a broad research programme; it does not assert that a complete physical theory of the Universe has been established.

## Historical chronology versus present research priorities

The project history, as reported by the maintainer, begins with Rift Network, continues through Rift-L1 Blockchain and UltraCore-RFT with supporting scheduler/memory systems, and later includes Phi-Genesis, Evgeny-Theorem, and Evgeny's Theory of Everything. The [origin chronology](docs/origin-chronology.md) records that sequence separately from commit-verified milestones.

The priority order below is a current research and evidence-management plan, **not** a claim about which repository was created first.

## 1. Programme structure

The programme has three principal mathematical strands and a downstream engineering strand.

**Defined mathematical objects and assumptions**
→ **Evgeny's Theorem:** fourth-moment identity; Lean 4 formalization reported
→ **Theory-of-Everything synthesis:** higher moments and recursive operators; all-level recurrence OPEN
→ **Phi-Genesis:** signed-flux spectral decimation; Gate A OPEN
→ **SIRM:** invariant-based state transitions
→ **Implementations and experiments:** runtime, protocol, scheduler, kernel stress tests
→ **Exploratory applications:** quantum architecture, energy-system model, and phenomenological cosmology

This is a reading order and research map, not a theorem asserting that each downstream application follows from the mathematics. The fourth-moment theorem does not prove the SIRM invariants, the higher-moment recurrence, the Phi-Genesis decimation mechanism, or a quantum advantage.

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

## 3. Priority II — resolve the higher-moment recurrence

**Primary source:** [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) · [dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md).

The synthesis repository records numerical holdouts and modular/CRT certificates for selected finite-level Fourier coefficients associated with moments $p\in\{6,8,10\}$. The graph/operator construction, denominator control, norm bounds, coefficient bounds, and finite transitions define the certificate's scope.

### Open obligations

1. Derive the exceptional first-transition correction from the recursive graph/operator construction.
2. Prove or refute the candidate all-level recurrence $R_m^{(p)}(\theta)=R_4^{(p)}(\theta)$ for every $m\ge3$ and every stated admissible angle.
3. Test edge cases and alternative graph levels before fixing the theorem statement.
4. Preserve numerical holdouts and certificate inputs as versioned reproducibility artifacts.
5. After a complete written derivation, formalize key lemmas and the theorem in Lean where feasible.

**Current status: open.** The fourth-moment Lean proof does not close this task. Finite certificates and small numerical residuals are evidence for specified cases, not an infinite-level proof.

Closure requires a derivation with explicit indexing and boundary conditions, proof over all required levels and angles, independent counterexample checks, a clean reproducible build, and a public statement that matches the formalization.

## 4. Priority III — close or delimit Phi-Genesis Gate A

**Primary source:** [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) · [commit documenting rigorous decimation verification](https://github.com/RFT-SIRM/Phi-Genesis/commit/c8611cc532b17c1944e2701c10780de99cae4548).

Phi-Genesis studies signed $Z_2$-flux Laplacians, spectral decimation, boundary/corner corrections, inertia calculations, and exploratory mass-index patterns. This is a distinct operator family from the SU(2)-connected theorem.

### Closure criteria

- Characterize the complete exceptional set, including recursively generated cases if that mechanism survives further testing.
- Explain residual mismatches and report matching rates by level and method.
- Retain one-to-one matching constraints and explicit numerical tolerances.
- Test proposed criteria prospectively on levels not used to derive them.
- Keep rejected mass-index fits and look-elsewhere-effect analyses visible.
- Do not describe a selected mass-index pattern as a predictive physical law without a selection mechanism, prospective predictions, held-out validation, and independent derivation.

**Current status: Gate A remains open.** If a complete characterization cannot be proved, publish the exact domain where the criterion works and where it fails rather than claiming general closure.

## 5. Priority IV — maintain SIRM engineering evidence

SIRM (Synthetic Intelligence Reasoning Model; СИРМ — «Синтетическая интеллектуальная модель рассуждений») defines runtime invariants for state transitions. The constraints below use compact symbols to keep the equations readable in GitHub's Markdown renderer:

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