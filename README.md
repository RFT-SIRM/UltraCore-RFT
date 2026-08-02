<div align="center">

# UltraCore RFT

**Deterministic Invariant Systems Research Laboratory**

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Research Status](https://img.shields.io/badge/Research-Active-success)](./RESEARCH_SUPPORT.md)

</div>

---

## Overview

UltraCore RFT is the central research documentation and coordination hub for the RFT-SIRM ecosystem. We design, model, and verify **deterministic state invariant systems** — computational architectures where every state transition is governed by mathematically provable constraints.

Our work spans standalone L1 validators, Solana smart contract protocols, and SVM runtime security research. All systems share a single mathematical core: the **Scalar Invariant Resource Model (SIRM)**.

> **Mission:** Build verifiable, invariant-backed distributed systems where correctness is observable, measurable, and reproducible.

---

## Ecosystem

| Repository | Role | Language | Status | Key Results |
|:-----------|:-----|:-------:|:------:|:------------|
| [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Standalone validator core | Rust | Core complete | 1T+ operations fuzzed, 0 invariant violations |
| [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Solana on-chain protocol | Rust / Anchor | RC v1.0 | 2.5B+ fuzz runs, 14 security audit findings addressed |
| [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | SVM memory isolation research | Rust | Active research | [CPI permission leakage](https://github.com/anza-xyz/svm/issues/25) found and reported upstream |
| [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Conflict-aware transaction scheduling | Rust | RFC published | [Bounded retry semantics](https://github.com/anza-xyz/agave/issues/14274) proposed for Agave GreedyScheduler |

---

## SIRM Invariants

All RFT-SIRM systems enforce four hard constraints after every state-mutating operation:

```
I1: total_supply = total_base_sum + global_field * p
I2: total_supply = total_minted - total_burned
I3: dust_accumulator < p  (when p > 0)
I4: effective_balance[i] >= -(total_supply / 10p)
```

Where `effective_balance[i] = base_balance[i] + global_field`.

This model enables **O(1) distribution**: updating `global_field` by a scalar delta changes every participant's effective balance simultaneously, regardless of participant count. No iteration. No per-account writes. Deterministic, verifiable, invariant-backed.

---

## Upstream Contributions

Security research and runtime improvements developed within the RFT-SIRM ecosystem are reported back to the Solana core infrastructure:

| Issue | Component | Description | Status |
|:------|:----------|:------------|:-------|
| [anza-xyz/svm#25](https://github.com/anza-xyz/svm/issues/25) | SVM Runtime | CPI permission leakage: per-frame writable permission rollback failure when multiple `update_account_permissions` calls occur within a single CPI frame. | Reported |
| [anza-xyz/agave#14274](https://github.com/anza-xyz/agave/issues/14274) | Banking Stage | [RFC] Bounded retry semantics and starvation observability for GreedyScheduler: documented scheduling limitation, proposed `max_retry_count` and `dropped_transactions` metric. | RFC Open |

---

## Research Status

| Component | Phase | Verification | Notes |
|:----------|:------|:-------------|:------|
| SIRM Core Invariants | ✅ Complete | Fuzz-verified (1T+ ops) | Mathematical foundation stable |
| Rift L1 Blockchain | ✅ Core complete | Rust + libFuzzer | Standalone validator, consensus-ready architecture |
| Rift Network (Solana) | 🔄 RC v1.0 | Anchor + security audit | On-chain protocol, production candidate |
| Agave Memory Contexts | 🔬 Active research | Bug reported upstream | SVM memory isolation, [svm#25](https://github.com/anza-xyz/svm/issues/25) |
| Agave Scheduler | 📋 RFC published | Invariants verified | [agave#14274](https://github.com/anza-xyz/agave/issues/14274) upstream discussion open |
| Formal Verification | 📅 Planned | Model checking / theorem proving | TLA+ / Coq specifications in development |

**Legend:** ✅ Complete · 🔄 Release Candidate · 🔬 Active Research · 📋 RFC Published · 📅 Planned

---

## Documentation

Full documentation is built with [MkDocs](https://www.mkdocs.org/):

```bash
pip install -r requirements.txt
mkdocs serve
```

| Document | Description |
|:---------|:------------|
| [Architecture](docs/architecture.md) | System architecture and design decisions |
| [Strategy](docs/strategy.md) | Development roadmap and research phases |
| [Foundations](docs/foundations.md) | Mathematical foundations of SIRM |
| [Implementation](docs/implementation.md) | Implementation details and external references |
| [Field Trials](docs/field_trials.md) | Verification results and readiness checklist |
| [Glossary](docs/glossary.md) | Terminology and definitions |
| [Support](docs/support.md) | Research support and collaboration |

---

## Quick Links

- **Protocol Specification:** [`RFT_MATHEMATICAL_FOUNDATIONS.md`](RFT_MATHEMATICAL_FOUNDATIONS.md)
- **Architecture Overview:** [`ARCHITECT.md`](ARCHITECT.md)
- **Development Roadmap:** [`RFT_DEVELOPMENT_STRATEGY.md`](RFT_DEVELOPMENT_STRATEGY.md)
- **Research Support:** [`RESEARCH_SUPPORT.md`](RESEARCH_SUPPORT.md)
- **Citation:** [`CITATION.cff`](CITATION.cff)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.

For security disclosures, see [SECURITY.md](SECURITY.md).

---

## License

Licensed under [Apache License 2.0](LICENSE).

Copyright 2026 Eugeny (RFT-SIRM)
