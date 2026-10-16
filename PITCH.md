# UltraCore-RFT — Research Dossier and Programme Thesis

**Mathematical results first. Distinct evidence classes. Engineering applications downstream.**

Primary routes: [README](README.md) · [AI evidence guide](AI_GUIDE.md) · [Research map](docs/research-map.md) · [Main RFT-SIRM portal](https://rft-sirm.github.io/).

## Executive thesis

UltraCore-RFT coordinates a research ecosystem built around exact mathematical constructions, recursive spectral questions, invariant-based computation, and deterministic systems engineering. The programme is strongest when it makes the boundary between a proved statement, a finite computational certificate, an engineering test, and an open hypothesis explicit.

The mathematical anchor is **Evgeny's Theorem**: the source repository reports a Lean 4 formalization of a specific fourth-moment trace-defect identity for a defined noncommuting SU(2) connection on Sierpiński-gasket graphs and a commuting control. A broader synthesis repository, **Evgeny's Theory of Everything**, organizes higher-moment recurrence research, finite-level modular/CRT certificates, numerical holdouts, and open proof obligations. **Phi-Genesis** studies a different signed-flux Laplacian family and audits spectral-decimation and mass-index claims.

The systems strand, SIRM, applies invariant-first design to deterministic state transitions and runtime architecture. Blockchain, scheduler, memory-isolation, seL4 stress-testing, quantum-architecture, and energy-system programmes are applications or adjacent research strands; they do not certify the mathematical claims by association.

**The title “Theory of Everything” is a research-programme name, not a declaration that a complete physical theory of the Universe has been proved.**

## 1. Research anchor: the fourth-moment theorem

### 1.1 Statement and normalization

For the specific operator definitions and assumptions in [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem), the raw fourth-moment trace defect is stated as

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right),
\qquad m\ge1.
$$
The normalized quantity is

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3},
\qquad
\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$
At $\theta=\pi/2$, the limiting value is $-8/9$.

The denominator is the stated Hilbert-space dimension $3^{m+1}+3$. Since $3^{m+1}+3=3(3^m+1)$, the limit follows by dividing numerator and denominator by $3^m$. At $m=1,\theta=\pi/2$, $\Delta_1=-16(1+1)/2=-16$, the dimension is $12$, and $I_1=-4/3$. These elementary checks guard against index and normalization transcription errors.

Primary records: [THEOREM.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [VERIFICATION.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · [test workflows](https://github.com/RFT-SIRM/Evgeny-Theorem/actions).

### 1.2 Evidence and limits

| Claim | Evidence class | Scope / caveat |
|---|---|---|
| Closed form matches the source construction's direct computations at levels 1–7 | Numerically reproduced, source-reported | Finite levels and sampled parameters; not the universal proof |
| Gauge-transformation checks preserve the reported fourth-moment quantity within numerical tolerance | Numerical test, source-reported | Tolerance and test construction are documented upstream |
| Identity holds for all stated $m\ge1$ and angles | Machine-checked, source-reported | Lean statement covers the concrete formalized operators and its assumptions |
| Formal definitions match the intended mathematical construction | Requires independent review | Proof checking does not replace semantic review |
| Peer review and external replication | Not yet established in the current dossier | Do not imply either has occurred |
| Other moments $p=6,8,10$ obey an all-level recurrence | Open research | Not covered by the fourth-moment proof |
| Quantum advantage, new physical law, or complete theory of the Universe | Not claimed | No evidence in this result establishes these |

### 1.3 Why the result is useful without overclaiming

The closed form supplies a known-answer reference for one specific spectral quantity across graph refinement levels. That can be useful for checking implementations of the stated operator construction, investigating gauge-invariant quantities, and designing future trace-estimation experiments.

The formula can be evaluated in constant arithmetic work for any stated level, while direct matrix computation grows with operator dimension. This complexity comparison applies to **the one closed-form trace defect only**—not to the full spectrum, circuit implementation, spectral gap, or another moment.

Possible uses in quantum simulation and trace estimation remain hypotheses until a circuit or algorithm, resource estimate, error analysis, and reproducible experiment are published. No speed-up is claimed.

## 2. Evgeny's Theory of Everything: the higher-moment programme

Primary source: [RFT-SIRM/Evgeny-s-Theory-of-Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) · [dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md).

The synthesis repository studies recursive operator families and higher trace moments $H^6,H^8,H^{10}$, Fourier coefficient structure, transition residuals, and a candidate recurrence.

### Evidence already documented

- Finite-level modular/CRT certificates for specified Fourier coefficients and transitions, for $p\in\{6,8,10\}$, under explicit denominator, norm, prime, and coefficient-bound arguments.
- Predeclared finite-angle holdouts and a sparse-matrix-power route that does not use eigenspectrum evaluation.
- Versioned numerical outputs and reports that allow the stated calculations to be reproduced.

### What remains open

The all-level recurrence $R_m^{(p)}(\theta)=R_4^{(p)}(\theta)$ for all $m\ge3$ and all stated admissible angles has not been proved. The exceptional first-transition correction still requires an explanation derived from the recursive graph/operator construction. Finite certificates and small numerical residuals do not prove these universal claims.

Closure criteria should include a complete derivation, explicit indexing and boundary conditions, proof for all required levels and angles, counterexample search, reproducible regression tests, and formalization where feasible. Until then, the correct status is **active research / open theorem**.

Evidence routes: [recurrence note](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md) · [sparse level-7 report](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_SPARSE_LEVEL7.md) · [coefficient candidates](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md) · [modular certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md).

## 3. Phi-Genesis: spectral decimation and mass-formula audit

Primary source: [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) · [live site](https://rft-sirm.github.io/Phi-Genesis/).

Phi-Genesis examines signed $Z_2$-flux Laplacians, spectral decimation, boundary/corner corrections, inertia computation, and exploratory mass-index patterns. It is a distinct mathematical model from the SU(2)-connected operator family in Evgeny's Theorem.

The current status must preserve both positive and negative findings:

- Computations and tests support only the statements within their declared inputs, algorithms, and checks.
- Claims contradicted by the audit should remain marked rejected or narrowed, with evidence links.
- **Gate A remains open:** residual mismatches and the full exceptional set are not completely explained.
- The proposed mass-index pattern is not an established predictive physical law without a selection mechanism, prospective predictions, held-out validation, and independent derivation.
- A connection to the SU(2) model is not assumed. Any bridge must define an operator map, boundary conditions, preserved quantities, exceptional cases, and a proof or a falsifiable conjecture.

A high-quality scientific narrative includes failed hypotheses and unresolved residuals. It does not erase them to produce an artificially complete story.

## 4. SIRM: invariant-first systems engineering

SIRM (Stable Invariant Rift Model) specifies runtime state constraints and the expectation that every mutating transition preserve them or fail atomically. The current model summary states:

$$
\begin{aligned}
I_1:\;&\mathtt{total\_supply}=\mathtt{total\_base\_sum}+\mathtt{global\_field}\cdot p,\\
I_2:\;&\mathtt{total\_supply}=\mathtt{total\_minted}-\mathtt{total\_burned},\\
I_3:\;&\mathtt{dust\_accumulator}<p\quad(p>0),\\
I_4:\;&\mathtt{effective\_balance}[i]\ge-\frac{\mathtt{total\_supply}}{10p}.
\end{aligned}
$$
With $\mathtt{effective\_balance}[i]=\mathtt{base\_balance}[i]+\mathtt{global\_field}$, and the integer/scaling conventions of the implementation.

An $O(1)$ global distribution can follow from updating a shared scalar and deriving each participant's effective balance on read. That does not imply that every operation in the system is constant-time, nor that a design statement proves every implementation correct. Tests, fuzzing, audits, and deployment checks are engineering evidence with bounded scope.

The fourth-moment theorem is mathematically separate. No derivation currently makes it a proof of SIRM's four runtime invariants.

## 5. Research-to-application map

| Programme | Primary source | Current status / boundary |
|---|---|---|
| Fourth-moment theorem | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Specific theorem; Lean 4 formalization reported for stated scope |
| Higher moments | [Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | Finite-level certificates and numerical holdouts; all-level recurrence open |
| Signed-flux spectral research | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Audit programme; Gate A open |
| Quantum architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Pre-experimental; no speed-up or hardware advantage established |
| Energy-system model | [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) | Exploratory scenarios and explicit modelling assumptions |
| Standalone runtime | [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Implementation-specific engineering and fuzzing records |
| Solana protocol | [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Devnet research deployment; no mainnet-readiness implication |
| SVM memory isolation | [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | Specific proof-of-concept investigation |
| Scheduler | [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Engineering research and upstream discussion |
| DeFi ledger model | [aave-v4-hub-model-review](https://github.com/RFT-SIRM/aave-v4-hub-model-review) | Invariant model review; complementary to formal verification |
| seL4 stress testing | [UltraCore report](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/SEL4_CDT_FUZZING.md) | Specific subsystem stress testing; not a replacement for seL4 formal proof |

Counts such as fuzz operations, test totals, audit findings, and durations are source-reported snapshots. Quote them only with their report/workflow and context; do not present them as live counters or as comparable measures of mathematical certainty.

## 6. Historical interpretation

The documented programme has several distinguishable stages:

1. **Invariant-first execution design:** SIRM expresses runtime correctness as constraints checked at state transitions.
2. **A concrete spectral theorem:** Evgeny's Theorem states an exact fourth-moment trace defect for a specified operator family and includes a Lean formalization record.
3. **Higher-moment extension:** the Theory-of-Everything repository collects numerical and finite-certificate evidence while retaining the unresolved all-level recurrence.
4. **A separate decimation audit:** Phi-Genesis investigates signed-flux Laplacians and keeps rejected claims and open residuals visible.
5. **Systems and application research:** UltraCore links these programmes to runtimes, protocols, kernel stress tests, quantum architecture, and energy-system modelling without treating applications as proof of the mathematics.

This is a conceptual chronology, not a substitute for commit-level provenance. For exact dates, changes, and status at a point in time, use [UltraCore commit history](https://github.com/RFT-SIRM/UltraCore-RFT/commits/main), [theorem history](https://github.com/RFT-SIRM/Evgeny-Theorem/commits/main), [synthesis history](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commits/main), and [Phi-Genesis history](https://github.com/RFT-SIRM/Phi-Genesis/commits/main).

## 7. Evidence and collaboration protocol

A research claim is ready for promotion only when its record identifies:

- precise statement, symbols, quantifiers, domain, assumptions, and boundary conditions;
- proof, certificate, algorithm, or test that actually supports it;
- source commit, toolchain, dependencies, commands, parameters, tolerances, and raw outputs where relevant;
- counterexamples, failed runs, known exceptions, and what remains untested;
- an evidence label that matches the method, not the ambition of the programme.

| Label | Required meaning |
|---|---|
| Machine-checked | Formal proposition accepted by a specified proof assistant/build |
| Analytically proved | Written derivation with explicit assumptions |
| Certified finite-level | Certificate for stated finite cases under stated bounds |
| Numerically reproduced | Computation agrees on stated inputs |
| Engineering-tested | Implementation-specific test, fuzz, audit, or deployment evidence |
| Hypothesis / open | Proposed or unresolved; not to be marketed as established |

A workflow passing means only that its assertions passed. Independent review, peer review, external replication, and application-level validation are separate milestones.

## 8. Reader routes

- [README](README.md) — public research overview and formula checks.
- [AI_GUIDE.md](AI_GUIDE.md) — required guardrails for AI summaries.
- [Scientific basis](SCIENTIFIC_BASIS.md) — mathematical results versus modelling vocabulary.
- [Research map](docs/research-map.md) — evidence hierarchy and open problems.
- [Historical development](docs/history.md) — selected commit-backed milestones.
- [Architecture](docs/architecture.md) and [platform strategy](docs/platform.md) — systems design.
- [Verification evidence](docs/field_trials.md) — engineering results and limitations.
- [Main RFT-SIRM portal](https://rft-sirm.github.io/) — preserved organization-wide interactive entry point.

## License and provenance

This repository's original material is distributed under [Apache-2.0](LICENSE), subject to LICENSE and NOTICE. Linked repositories are independent works with their own source histories and licensing. This dossier is research communication, not legal advice, peer review, or a substitute for the primary sources.