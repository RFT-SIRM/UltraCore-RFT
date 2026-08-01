# UltraCore RFT

> Deterministic Invariant Systems Research Laboratory

[![Docs CI](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml/badge.svg)](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/docs.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

---

UltraCore RFT is the central research documentation hub for the RFT-SIRM ecosystem. It specifies the mathematical foundations, architecture, and verification methodology for deterministic state invariant systems.

The ecosystem spans standalone Rust validators, Solana smart contracts, and Agave SVM runtime security research. All systems share a single mathematical core: the Scalar Invariant Resource Model (SIRM).

## Ecosystem

| Repository | Role | Language | Key Results |
|------------|------|----------|-------------|
| [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Standalone validator core | Rust | 1T+ operations fuzzed, 0 invariant violations |
| [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Solana on-chain protocol | Rust/Anchor | 2.5B+ fuzz runs, 14 audit findings addressed |
| [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | SVM memory isolation research | Rust | [CPI permission leakage](https://github.com/anza-xyz/svm/issues/25) found and reported |
| [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Conflict-aware transaction scheduler | Rust | Dead deferred queue and zero-cost conflict bypass found and fixed |

## SIRM Invariants

All RFT-SIRM systems enforce four hard constraints after every state-mutating operation:

```
I1: total_supply = total_base_sum + global_field * p
I2: total_supply = total_minted - total_burned
I3: dust_accumulator < p  (when p > 0)
I4: effective_balance[i] >= -(total_supply / 10p)
```

Where `effective_balance[i] = base_balance[i] + global_field`.

This model enables O(1) distribution: updating `global_field` by a scalar delta changes every participant's effective balance simultaneously, regardless of participant count.

## Upstream Contributions

Security research and runtime fixes developed within the RFT-SIRM ecosystem are reported back to the Solana core infrastructure:

- **[anza-xyz/svm#25](https://github.com/anza-xyz/svm/issues/25)** — CPI permission leakage: per-frame writable permission rollback failure when multiple `update_account_permissions` calls occur within a single CPI frame.

## Research Status

| Component | Status | Verification |
|-----------|--------|--------------|
| SIRM Core Invariants | Complete | Fuzz-verified (1T+ ops) |
| Rift L1 Blockchain | Core complete | Rust + libFuzzer |
| Rift Network (Solana) | RC v1.0 | Anchor + security audit |
| Agave Memory Contexts | Active research | Bug reported upstream |
| Agave Scheduler | Active research | Invariants verified |
| Formal Verification | Planned | Model checking / theorem proving |

## Documentation

Full documentation is built with [MkDocs](https://www.mkdocs.org/):

```bash
pip install -r requirements.txt
mkdocs serve
```

| Document | Description |
|----------|-------------|
| [Architecture](docs/architecture.md) | System architecture and design decisions |
| [Strategy](docs/strategy.md) | Development roadmap and research phases |
| [Foundations](docs/foundations.md) | Mathematical foundations of RFT |
| [Implementation](docs/implementation.md) | Implementation details and external references |
| [Field Trials](docs/field_trials.md) | Verification results and readiness checklist |
| [Glossary](docs/glossary.md) | Terminology and definitions |
| [Support](docs/support.md) | Research support and collaboration |

## Quick Links

- **Protocol Specification:** [`RFT_MATHEMATICAL_FOUNDATIONS.md`](RFT_MATHEMATICAL_FOUNDATIONS.md)
- **Architecture Overview:** [`ARCHITECT.md`](ARCHITECT.md)
- **Development Roadmap:** [`RFT_DEVELOPMENT_STRATEGY.md`](RFT_DEVELOPMENT_STRATEGY.md)
- **Research Support:** [`RESEARCH_SUPPORT.md`](RESEARCH_SUPPORT.md)
- **Citation:** [`CITATION.cff`](CITATION.cff)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.

For security disclosures, see [SECURITY.md](SECURITY.md).

## License

Licensed under [Apache License 2.0](LICENSE).

Copyright 2026 Eugeny (RFT-SIRM)
