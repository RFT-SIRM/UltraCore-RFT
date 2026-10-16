# UltraCore-RFT

**Deterministic Invariant Systems Research Laboratory**

UltraCore-RFT is the architecture and coordination hub for the RFT-SIRM ecosystem: deterministic execution systems, invariant-based verification, and connected mathematical research. The repository distinguishes proved results, tested engineering claims, and open research questions.

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

**Primary routes:** [Platform](docs/platform.md) · [Architecture](docs/architecture.md) · [Mathematical foundations](docs/foundations.md) · [Verification evidence](docs/field_trials.md) · [Scientific boundaries](SCIENTIFIC_BASIS.md)

---

## 🎯 Start Here

| Route | Resource | Purpose |
| --- | --- | --- |
| **Overview** | This README | Scope, program map, and evidence boundaries |
| **Platform strategy** | [docs/platform.md](docs/platform.md) | How the execution architecture and its implementations fit together |
| **Systems engineering** | [ARCHITECT.md](ARCHITECT.md) · [docs/architecture.md](docs/architecture.md) | Components, interfaces, and design decisions |
| **SIRM model** | [docs/foundations.md](docs/foundations.md) | The four runtime invariants and their intended scope |
| **Mathematical result** | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) · [formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) | The specified SU(2) Sierpiński-gasket fourth-moment identity, formalized in Lean 4 |
| **Spectral research** | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Separate spectral-computation program; claims are classified as supported, rejected, or open |
| **Quantum architecture** | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Pre-experimental SU(2)/Sierpiński quantum-processing architecture |
| **Energy-system model** | [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) | Exploratory invariant-driven battery scenarios with explicit assumptions |
| **Live protocol demo** | [Rift Network Devnet](https://rift-network.vercel.app) | Interactive client for the Solana Devnet deployment |
| **Research dossier** | [PITCH.md](PITCH.md) · [SCIENTIFIC_BASIS.md](SCIENTIFIC_BASIS.md) | Evidence, roadmap, and limits of interpretation |

> **One-sentence summary:** UltraCore RFT is a research laboratory building a deterministic execution platform for distributed systems, where mathematical invariants are hard constraints enforced after every state transition.

---

## ✨ At a Glance

```mermaid
flowchart TB
    subgraph MATH["Mathematical Core"]
        I1["I1: Supply Conservation"]
        I2["I2: Mint/Burn Accounting"]
        I3["I3: Dust Bound"]
        I4["I4: Debt Limit"]
    end
    subgraph RUNTIME["Runtime Layer"]
        MEM["Memory Contexts<br/>CPI Isolation"]
        SCHED["Conflict-Aware<br/>Scheduler"]
    end
    subgraph VERIFY["Verification"]
        FUZZ["4.29B+ Fuzz<br/>Executions"]
        SEL4["seL4 CDT<br/>1B+ Ops"]
        AUDIT["14 Findings<br/>Addressed"]
    end
    MATH --> RUNTIME
    MATH --> VERIFY
    RUNTIME --> VERIFY
```

| Metric | Value |
| --- | --- |
| **Fuzz Executions** | 4.29B+ |
| **Invariant Violations** | 0 |
| **Security Findings Fixed** | 14 |
| **Upstream RFCs** | 2 |
| **seL4 Kernel Crashes** | 0 |
| **Daily CI Fuzzing** | 5h 55m |

* * *

## 🌐 What Is UltraCore RFT?

UltraCore RFT is best understood as an **execution architecture** — a deterministic execution substrate — rather than as a single blockchain or mathematical theory.

### The Platform Stack

```mermaid
flowchart TB
    subgraph SF["Scientific Foundations"]
        MATH["Mathematics · Graph Theory · Category Theory<br/>Information Theory · Dynamical Systems · Invariant Theory"]
    end
    subgraph CONCEPT["Conceptual Framework"]
        RFT["Reality Fractal Theory"]
    end
    subgraph MODEL["Execution Model"]
        SIRM["Stable Invariant Rift Model<br/>I1–I4 Hard Constraints"]
    end
    subgraph RUNTIME["Runtime Engine"]
        UC["UltraCore Runtime<br/>Deterministic State Machine · O(1) Distribution"]
    end
    subgraph ARCH["Execution Architecture"]
        MEM["Memory Contexts · CPI Isolation"]
        SCHED["Conflict-Aware Scheduler"]
        ROLL["Permission Rollback · Atomic Operations"]
    end
    subgraph BLOCK["Blockchain Layer"]
        L1["Rift-L1 Blockchain<br/>Standalone Validator Core"]
        NET["Rift Network<br/>Solana On-Chain Protocol"]
    end
    subgraph FUTURE["Future Targets"]
        HA["High-Assurance Infrastructure"]
        CRIT["Critical Computing Environments"]
        KERNEL["Additional Verified Kernels"]
    end
    SF --> CONCEPT
    CONCEPT --> MODEL
    MODEL --> RUNTIME
    RUNTIME --> ARCH
    ARCH --> BLOCK
    BLOCK --> FUTURE
    ARCH -.->|"kernel-agnostic"| FUTURE
```

**Key insight:** The blockchain is one implementation. The runtime is another. The verification methodology is another. Together they form one coherent architecture — layered, verifiable, and kernel-agnostic.

See [docs/platform.md](docs/platform.md) for the full strategic identity document.

* * *

## ⚖️ What Is SIRM?

**SIRM** = Stable Invariant Rift Model. It is the mathematical core of every RFT-SIRM system.

All systems enforce four hard constraints after every state-mutating operation:

```
I1: total_supply = total_base_sum + global_field * p
I2: total_supply = total_minted - total_burned
I3: dust_accumulator < p  (when p > 0)
I4: effective_balance[i] >= -(total_supply / 10p)
```

Where `effective_balance[i] = base_balance[i] + global_field`.

This model enables **O(1) distribution**: updating `global_field` by a scalar delta changes every participant's effective balance simultaneously, regardless of participant count. No iteration. No per-account writes.

See [docs/foundations.md](docs/foundations.md) for the mathematical derivation.

* * *

## 🔬 Research Programs

| Repository | Role | Status | Key Evidence |
| --- | --- | --- | --- |
| [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Standalone L1 runtime | Active | 1T+ ops, 0 invariant violations |
| [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Solana on-chain protocol | Audited | 14 findings addressed, 2.5B+ fuzz runs · [Live Demo (Devnet)](https://rift-network.vercel.app) |
| [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | SVM memory isolation (PoC) | Research Complete | 4.29B+ exec, PoC-only bug found & documented — upstream uses `abi_v2_prepare_for_instruction` architecture |
| [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Conflict-aware scheduling | Active | 91M exec/run, [agave#14274](https://github.com/anza-xyz/agave/issues/14274) |
| [aave-v4-hub-model-review](https://github.com/RFT-SIRM/aave-v4-hub-model-review) | DeFi ledger invariant model (Aave V4 Hub) | Complete | 184K ops, 0 violations, complementary to Certora FV |
| [research/seL4](https://github.com/RFT-SIRM/UltraCore-RFT/tree/main/research/seL4) | Kernel verification | Complete | 1B+ ops deterministic fuzzing |
| [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Fractal spectral physics — mass-formula audit | Active | 14/14 tests passing · 2 claims formally rejected (η-invariant, ad hoc topology fit) · 2 open problems documented, not hidden · [live site](https://rft-sirm.github.io/Phi-Genesis/) |
| [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Noncommutative spectral geometry — SU(2) gauge theory on fractals | Active | 55/55 tests passing · closed-form H⁴ identity verified to 1e-13, held-out cross-check, gauge invariance to 8e-15 · Lean 4 proof for every `m ≥ 1` · [live site](https://rft-sirm.github.io/Evgeny-Theorem/) |
| [Higher-moment research](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | Higher-moment Fourier coefficients and recurrence audit | Active research | Selected finite-level coefficients have a modular/CRT certificate; the all-level recurrence remains open |
| [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | Gauge-covariant fractal SU(2) quantum-processing architecture | Research architecture / pre-experimental | Sierpiński connectivity, SU(2) transport, candidate logical-qubit model, normalized spectral anchor −8/9 |
| [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) | Invariant-driven battery-system architecture | Exploratory computational research | Deterministic reference model, reproducible 10,000-km scenarios, explicit assumptions and auditable CSV outputs |


* * *

## 🔷 Evgeny's Theorem

**Evidence and status:** [Lean 4 formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [Verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · [Test workflow](https://github.com/RFT-SIRM/Evgeny-Theorem/actions) · [Project site](https://rft-sirm.github.io/Evgeny-Theorem/)

> **An exact, closed-form, gauge-invariant fingerprint of non-commutativity for an SU(2) gauge field on a fractal — one number at every refinement level, reproducible in seconds.**

**The object.** The Sierpiński-gasket graph `SG(m)` with Hilbert space `C^n ⊗ C²` and an SU(2)-valued connection whose rotation axis cycles x / y / z from triangle to triangle, so that the holonomies of neighbouring triangles genuinely do not commute. It is compared against the commuting control `C′` (fixed axis: exactly two decoupled U(1) copies) at the same angle `θ`.

**The result.** The raw fourth-moment trace defect is given exactly by

$$
\Delta_m(H^4,\theta)=\mathrm{Tr}\left(H_C^4\right)-\mathrm{Tr}\left(H_{C'}^4\right)=-16\left(3^{m-1}+1\right)\sin^2\left(\frac{\theta}{2}\right)
$$

**The invariant.** Normalizing by `dim(H) = 3^(m+1) + 3` gives the intensive quantity

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3}
\qquad\Longrightarrow\qquad
\lim_{m\to\infty} I_m(\theta)=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right),
\qquad
\lim_{m\to\infty} I_m\left(\frac{\pi}{2}\right)=-\frac{8}{9}
$$

Equivalently, with `F = 3^m` triangular faces, the defect is linear in the face count:

$$
\Delta_m=-\frac{16}{3}\left(3^{m}+3\right)\sin^2\left(\frac{\theta}{2}\right)
$$

### Convergence at θ = π/2

| m | dim(H) | Δ_m(H⁴, π/2) | I_m(π/2) | distance to −8/9 |
| --- | --- | --- | --- | --- |
| 1 | 12 | -16 | -1.333333 | 0.444444 |
| 2 | 30 | -32 | -1.066667 | 0.177778 |
| 3 | 84 | -80 | -0.952381 | 0.063492 |
| 4 | 246 | -224 | -0.910569 | 0.021680 |
| 5 | 732 | -656 | -0.896175 | 0.007286 |
| 6 | 2,190 | -1,952 | -0.891324 | 0.002435 |
| 7 | 6,564 | -5,840 | -0.889701 | 0.000813 |

### Why it stands out

| | Property | Evidence |
| --- | --- | --- |
| 🎯 | **Exact** | One closed form gives `Δ_m` for any `m` and `θ` in O(1). At level 20 the operator has more than 10¹⁰ dimensions; the closed form costs a few arithmetic operations. *(Applies to this single quantity only, not to the full spectrum.)* |
| 🔒 | **Gauge-invariant** | Under a Haar-random SU(2) gauge transformation the spectrum changes by at most 8 × 10⁻¹⁵ and `M₄` is identical |
| 🧪 | **Held-out tested** | Five `(m, θ)` pairs chosen *after* the formula was fixed agree to 10⁻¹¹–10⁻¹⁴; a 20-point θ-grid agrees to below 10⁻⁹ |
| 📐 | **A non-Abelian witness** | The defect is exactly zero for moments `p = 1, 2, 3` and first appears at `p = 4`; it vanishes in the commuting limit |
| ♻️ | **Reproducible** | 55 fast checks run in seconds; level 7 (dim 6,564) agrees with the closed form to 9 × 10⁻¹³ absolute, 1.6 × 10⁻¹⁶ relative |

### Verification status

| Statement | Status |
| --- | --- |
| Closed form equals direct computation for every tested `(m, θ)`, `m = 1…7` | ✅ Established (reproducible) |
| Gauge invariance of the fourth moment | ✅ Established |
| The closed form holds for **all** `m ≥ 1` and `θ` | ✅ Machine-checked in Lean 4 (no `sorry`; standard axioms only) |
| Lean 4 formalization | ✅ Complete for the stated scope: concrete SU(2) connection operators on `SG(m)`, fourth moment, every `m ≥ 1`, every `θ` — [`formalization/README.md`](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/formalization/README.md) |
| Peer review / independent replication | 📅 Not yet |

### Where it could matter — hypotheses, not results

- **Quantum simulation:** a known-answer benchmark for simulators of non-Abelian gauge dynamics. The state space is a site register plus one spin-½: level 7 fits in 13 qubits by dimension count. Circuit cost is not yet studied.
- **Trace estimation:** an exact test vector for spectral-moment estimators, quantum or randomized classical.
- **Further identities:** the same framework may yield exact results for other moments, fractals and gauge groups.

**Not claimed:** any speed-up for quantum algorithms, any statement about physical gauge theories, or any result on Millennium Prize Problems. Details, validation program and boundaries: [PITCH.md](PITCH.md#2-evgenys-theorem).

### Reproduce it yourself

```bash
git clone https://github.com/RFT-SIRM/Evgeny-Theorem.git && cd Evgeny-Theorem
python3 -m venv .venv && source .venv/bin/activate
pip install -r reproducibility/requirements.txt
pytest tests/ -m "not slow" -v     # 55 checks, seconds
pytest tests/ -m slow -v           # level 7, a few minutes
```

Full statement: [THEOREM.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · Numerical record: [VERIFICATION.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md) · Mathematical framework: [docs/foundations.md](docs/foundations.md)

* * *

## ⚛️ RFT-QPU-Sierpinski

**Repository:** [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) · **Architecture:** [SU(2) gauge-covariant design](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/docs/ARCHITECTURE.md) · **Status:** [Pre-experimental](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/REPOSITORY_STATUS.md)

> **A research architecture connecting the Sierpiński fractal, SU(2) transport, and candidate quantum-processing primitives.**

The QPU program extends the noncommutative SU(2) structure developed in **Evgeny's Theorem** toward a gauge-covariant fractal quantum-processing architecture.

**Current research anchors:**

- Sierpiński-gasket connectivity
- SU(2) gauge transport
- Candidate logical-qubit model
- Normalized spectral anchor `−8/9`
- Explicit pre-experimental status and reproducible computational structure

[**Open RFT-QPU-Sierpinski →**](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)

## 🔋 RFT-Invariant-Battery

**Repository:** [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) · **Model specification:** [MODEL_SPEC.md](https://github.com/RFT-SIRM/RFT-Invariant-Battery./blob/main/MODEL_SPEC.md) · **Status:** [Exploratory research](https://github.com/RFT-SIRM/RFT-Invariant-Battery./blob/main/RESEARCH_STATUS.md)

> **An exploratory systems program applying invariant-driven modelling to battery and energy-system scenarios.**

The Battery program provides a deterministic reference model with reproducible long-range scenarios, explicit assumptions, and auditable CSV outputs.

**Current research anchors:**

- Deterministic reference model
- Reproducible 10,000-km scenarios
- Explicit modelling assumptions
- Auditable numerical outputs

[**Open RFT-Invariant-Battery →**](https://github.com/RFT-SIRM/RFT-Invariant-Battery.)

## ✅ Verification

Every claim is backed by reproducible verification. We measure correctness rather than asserting it.

| Layer | Method | Evidence |
|-------|--------|----------|
| L1 — Static | Clippy, Miri, cargo-audit | Every push |
| L2 — Engineering | Unit + integration + differential tests | 15+ tests per component |
| L3 — Fuzzing | libFuzzer deterministic fuzzing | 4.29B+ exec, 0 invariant violations |
| L3b — Kernel | seL4 CDT complementary verification | 1B+ ops, 0 kernel crashes |
| L3c — DeFi Model | Python deterministic state-machine fuzz | 184K ops, 0 INV violations |
| L4 — Formal | TLA+ / Coq | Planned |

See [docs/field_trials.md](docs/field_trials.md) for the full verification report.

* * *

## 🧪 seL4 Complementary Verification

Independent engineering validation of the formally verified seL4 microkernel:

- **Subsystem:** Capability Derivation Tree (CDT)
- **Operations:** > 1.0 × 10⁹
- **Kernel crashes:** 0
- **Post-marathon test suite:** 123 / 123 passed

> **Important:** This was infrastructure research, not a claim of production deployment. See [SEL4_CDT_FUZZING.md](SEL4_CDT_FUZZING.md) and [docs/field_trials_sel4.md](docs/field_trials_sel4.md).

* * *

## 📚 Documentation

Full documentation is built with MkDocs Material:

```bash
pip install -r requirements.txt
mkdocs serve
```

| Document | Description | Audience |
| --- | --- | --- |
| [docs/platform.md](docs/platform.md) | Strategic identity: what UltraCore is and why it matters | Everyone |
| [docs/research-map.md](docs/research-map.md) | Research relationships, evidence classes, and seven-step documentation plan | Researchers and maintainers |
| [docs/architecture.md](docs/architecture.md) | Detailed architecture with Mermaid diagrams | Engineers |
| [docs/foundations.md](docs/foundations.md) | Formalized SIRM invariants | Researchers |
| [docs/field_trials.md](docs/field_trials.md) | Verification results & readiness checklist | Validators |
| [docs/field_trials_sel4.md](docs/field_trials_sel4.md) | seL4 CDT stress-verification report | OS Researchers |
| [docs/strategy.md](docs/strategy.md) | Full development strategy | All |
| [docs/implementation.md](docs/implementation.md) | Build instructions and component architecture | Developers |
| [docs/glossary.md](docs/glossary.md) | Terminology and definitions | All |
| [docs/support.md](docs/support.md) | Research support and collaboration | All |

* * *

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). For security disclosures, see [SECURITY.md](SECURITY.md).

* * *

## 📋 License

**License:** [Apache-2.0](LICENSE)

_Copyright 2026 Eugeny (RFT-SIRM). Licensed under [Apache 2.0](LICENSE)._
