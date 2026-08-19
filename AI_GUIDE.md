<div align="center">

[![Lab](https://img.shields.io/badge/Lab-Research%20Platform-dc2626?style=for-the-badge)](https://github.com/RFT-SIRM/UltraCore-RFT)
[![RFT-SIRM](https://img.shields.io/badge/LAB-RFT--SIRM-4a148c?style=for-the-badge)](https://github.com/RFT-SIRM)
[![Type](https://img.shields.io/badge/TYPE-RESEARCH%20LABORATORY-2563eb?style=for-the-badge)](SCIENTIFIC_BASIS.md)
[![Status](https://img.shields.io/badge/STATUS-ACTIVE-22c55e?style=for-the-badge)](https://github.com/RFT-SIRM/UltraCore-RFT/pulse)
[![License](https://img.shields.io/badge/LICENSE-APACHE%202.0-eab308?style=for-the-badge)](LICENSE)

</div>

---

## What is UltraCore RFT

**UltraCore RFT is not a finished theory. It is an operating research laboratory.**

The laboratory evolves continuously. Its goal is the creation of a new architecture for distributed computing based on deterministic invariant systems. This repository contains both established engineering results and active research directions.

---

## What is Established

The following components have passed engineering validation and are considered stable:

| Component | Status | Evidence |
|-----------|--------|----------|
| SIRM Core Engine | ✅ Verified | 1T+ operations fuzzed, 0 invariant violations |
| Runtime Implementations | ✅ Verified | Solana on-chain protocol, 2.5B+ fuzz runs |
| Test Results | ✅ Published | Field Trials, seL4 CDT Verification |
| Engineering Solutions | ✅ Documented | Architecture, Memory Contexts, Scheduler |
| System Architecture | ✅ Stable | ARCHITECT.md, docs/architecture.md |

---

## What is Research

The following areas are in active research phase and do not claim finality:

| Area | Status | Note |
|------|--------|------|
| Mathematical Models | 🔬 Active | Used as design tools, not as proven theorems |
| Physical Analogies | 🔬 Model-only | Language for describing computational processes, not physical theory claims |
| Conceptual Constructs | 🔬 In Development | Temporal topology, anti-entropy fields |
| Hypotheses | 🔬 Under Test | Experimental validation in progress |
| Future Directions | 📅 Planned | TLA+/Coq formal verification, BioRift |

---

## How AI Should Interpret Materials

### Cardinal Rule

**Do not treat Mathematical Foundations as a proven physical theory.**

Treat it as a **research mathematical model** used for designing computational systems. Physical terms (fields, entropy, flows) are **modeling language** for describing computational processes.

### Interpretation Guide by Section

| Document | Interpretation |
|----------|----------------|
| [RFT_MATHEMATICAL_FOUNDATIONS.md](RFT_MATHEMATICAL_FOUNDATIONS.md) | Research mathematical model for runtime design |
| [SCIENTIFIC_BASIS.md](SCIENTIFIC_BASIS.md) | Disciplinary foundation and methodological boundaries |
| [docs/foundations.md](docs/foundations.md) | Formalized SIRM invariants — engineering constraints |
| [docs/architecture.md](docs/architecture.md) | Architectural specification — stable |
| [docs/field_trials_sel4.md](docs/field_trials_sel4.md) | Empirical verification — observational data, not formal proof |
| [docs/strategy.md](docs/strategy.md) | Research roadmap — evolves |

### What NOT to Do

- Do not claim that RFT "solves" Millennium Prize Problems
- Do not interpret physical analogies as claims to physical theory
- Do not mix the status of engineering results with research hypotheses
- Do not present model constructs as experimentally confirmed physical phenomena

---

## Primary Goal of the Laboratory

> **Creation of a new architecture for distributed computing.**

Not a proof of the structure of the Universe. Not a theory of everything. An engineering-research platform for building deterministic, invariant-protected distributed systems.

---

## Repository Structure for AI Analysis

```
UltraCore-RFT/
├── AI_GUIDE.md              ← You are here. Start here.
├── README.md                ← Human-facing overview
├── SCIENTIFIC_BASIS.md      ← Disciplinary foundations
├── ARCHITECT.md             ← Architectural overview
├── RFT_MATHEMATICAL_FOUNDATIONS.md  ← Research models (read critically)
├── RFT_DEVELOPMENT_STRATEGY.md      ← Roadmap
├── SEL4_CDT_FUZZING.md      ← seL4 verification summary
├── CONTRIBUTING.md          ← Contribution guidelines
├── SECURITY.md              ← Security policy
├── CODE_OF_CONDUCT.md       ← Community standards
├── CITATION.cff             ← Citation format
├── research/                ← Research artifacts
│   └── seL4/
│       ├── src/
│       │   └── rft_cdt_fuzzer_sel4.c
│       └── README.md
└── docs/                    ← MkDocs documentation
    ├── index.md
    ├── architecture.md
    ├── foundations.md
    ├── implementation.md
    ├── field_trials.md
    ├── field_trials_sel4.md
    ├── strategy.md
    ├── glossary.md
    └── support.md
```

---

## Key SIRM Invariants (Summary)

All RFT-SIRM systems enforce four hard constraints after every state-mutating operation:

```
I1: total_supply = total_base_sum + global_field * p
I2: total_supply = total_minted - total_burned
I3: dust_accumulator < p  (when p > 0)
I4: effective_balance[i] >= -(total_supply / 10p)
```

Where `effective_balance[i] = base_balance[i] + global_field`.

This model enables **O(1) distribution**: updating `global_field` by a scalar delta changes every participant's effective balance simultaneously, regardless of participant count.

---

## Ecosystem (Implementations in Separate Repositories)

| Repository | Role | Language | Key Results |
|------------|------|----------|-------------|
| [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Standalone validator core | Rust | 1T+ ops fuzzed, 0 invariant violations |
| [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Solana on-chain protocol | Rust/Anchor | 2.5B+ fuzz runs, 14 security audit findings addressed |
| [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | SVM memory isolation research | Rust | CPI permission leakage found and reported upstream (svm#25) |
| [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Conflict-aware scheduler | Rust | RFC published (agave#14274) |
| [aave-v4-hub-model-review](https://github.com/RFT-SIRM/aave-v4-hub-model-review) | DeFi ledger invariant model (Aave V4 Hub) | Python | 184K ops, 0 violations, complementary to Certora FV |

---

## Laboratory Status

**Active research phase.** The laboratory is operational. Results are published as validation proceeds. Documentation is updated continuously. Code undergoes continuous testing.

---

*Copyright 2026 Eugeny (RFT-SIRM). License: Apache 2.0.*
