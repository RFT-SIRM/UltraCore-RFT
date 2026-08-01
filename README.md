# UltraCore RFT Laboratory

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Rift-Network](https://img.shields.io/badge/implementation-Rift--Network-brightgreen)](https://github.com/RFT-SIRM/Rift-Network)

**Independent research laboratory focused on deterministic distributed systems,
invariant-preserving runtime architecture, and blockchain execution environments.**

Scientific foundation: **Reality Fractal Theory (RFT)** and the **Stable Invariant Rift Model (SIRM)**.

---

## Research Dossier

**[→ docs/UltraCore_RFT_Dossier.pdf](docs/UltraCore_RFT_Dossier.pdf)**

The primary document for investors, protocol engineers, and strategic partners.
Covers all five research programs, SIRM mathematical model, verification results,
Agave SVM findings, and the current funding opportunity.

---

## Research Programs

Five interconnected programs — one laboratory architecture.

| Program | Layer | Status | Validation |
|---------|-------|--------|-----------|
| [UltraCore-RFT](https://github.com/RFT-SIRM/UltraCore-RFT) | Architecture / Theory | Active | This repository |
| [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Solana Protocol | Audited | 14 findings addressed |
| [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | SVM Security | Active | 4.29B+ exec · RFC submitted |
| [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | SVM Scheduling | Active | 91M exec/run · 3 bugs fixed |

All active programs run continuous libFuzzer verification — **5 hours 55 minutes daily**.

---

## Scientific Foundation

**Reality Fractal Theory (RFT)** — a unified framework connecting mathematics,
deterministic computation, distributed execution, and protocol architecture.
The central principle: correctness is a structural constraint enforced at every
state transition, not a property verified after the fact.

**Stable Invariant Rift Model (SIRM)** — the execution model derived from RFT.
Every operation either preserves all defined mathematical invariants or is
rejected atomically. No intermediate state exists.

---

## Key Engineering Findings

**CPI permission leakage** (`agave-abiv2-memory-contexts`)
The original Agave implementation destroyed rollback entries on multiple permission
updates within a single CPI frame. On pop(), accounts retained modified writable
permissions permanently. Fixed and RFC submitted to anza-xyz/svm.

**Dead deferred queue** (`agave-rift-scheduler`)
Conflicting transactions were pushed into the deferred queue but never retried.
Every deferred transaction was silently lost forever. Fixed.

**Zero-cost conflict bypass** (`agave-rift-scheduler`)
Transactions with cost=0 bypassed conflict detection entirely. Fixed.

---

## Verification Summary

| Component | Executions | Violations | Daily fuzz |
|-----------|-----------|------------|-----------|
| agave-abiv2-memory-contexts | 4,294,967,296+ | 0 | 5h 55m |
| agave-rift-scheduler | ~91M per run | 0 | 5h 55m |
| Rift-Network | 2.5B+ | 0 | Continuous |

---

## External References

| Artifact | Link | Status |
|----------|------|--------|
| Solana Protocol Implementation | [RFT-SIRM/Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Active |
| Security Audit | [Rift-Network#security](https://github.com/RFT-SIRM/Rift-Network#security) | 14 findings addressed |
| Fuzz Verification | [Rift-Network Actions](https://github.com/RFT-SIRM/Rift-Network/actions) | 2.5B+ runs, 0 violations |
| Agave SVM RFC | [anza-xyz/agave](https://github.com/anza-xyz/agave) | RFC draft available upon request |

## Version Alignment

| UltraCore-RFT | Rift-Network | Status |
|---------------|--------------|--------|
| main | v1.0 RC | Synchronized |

---

## Repository Documents

1. [ARCHITECT.md](ARCHITECT.md) — architecture overview and research principles
2. [RFT_DEVELOPMENT_STRATEGY.md](RFT_DEVELOPMENT_STRATEGY.md) — development strategy and roadmap
3. [RFT_MATHEMATICAL_FOUNDATIONS.md](RFT_MATHEMATICAL_FOUNDATIONS.md) — mathematical foundations
4. [RESEARCH_SUPPORT.md](RESEARCH_SUPPORT.md) — collaboration guidance
5. [docs/UltraCore_RFT_Dossier.pdf](docs/UltraCore_RFT_Dossier.pdf) — full research dossier

---

## Roadmap

**Phase 1 — Foundation** ✅ Complete
All programs implemented and fuzz-verified. Security audit on Rift-Network complete.
RFC submitted to anza-xyz/svm.

**Phase 2 — Agave Integration** ⏳ In progress
Integrate fixes into anza-xyz/agave. Draft PR with fuzz corpus and invariant docs.

**Phase 3 — Validator Benchmarks** 🔮 Planned
Testnet deployment. Criterion benchmarks against production Agave.

**Phase 4 — Production & Ecosystem** 🔮 Planned
Rift-Network mainnet launch.

---

## License

Apache-2.0 — © 2026 Eugeny (RFT-SIRM) · [github.com/RFT-SIRM](https://github.com/RFT-SIRM)
