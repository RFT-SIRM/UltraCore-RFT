# UltraCore RFT

UltraCore RFT is a launch-ready research repository for Reality Fractal Theory (RFT) and the UltraCore Rift architecture. It combines a structured documentation site, architectural narrative, and field-trial readiness guidance for deterministic invariant systems.

Since July 2026, the research has expanded beyond theoretical architecture into an actively developed Layer-1 blockchain runtime based on the UltraCore-RFT engine and the Stable Invariant Rift Model (SIRM).

This repository is designed for reviewers, engineers, and launch teams.

## Implementation Repositories

**Rift Network** (Solana-oriented implementation)

https://github.com/RFT-SIRM/Rift-Network

**Rift L1 Blockchain** (standalone UltraCore-RFT blockchain runtime)

https://github.com/RFT-SIRM/Rift-L1-Blockchain

---

## What is included

* ARCHITECT.md — architecture overview and research mindset
* RFT_DEVELOPMENT_STRATEGY.md — development strategy and roadmap
* RFT_MATHEMATICAL_FOUNDATIONS.md — mathematical foundations and runtime operators
* RESEARCH_SUPPORT.md — collaboration guidance and research positioning

---

## Objectives

* document the core ideas behind UltraCore Rift and SIRM
* maintain a clear conceptual foundation for field trials
* provide a stable reference for deterministic runtime design
* explain how invariant systems map to execution environments
* support both research and production-oriented blockchain development

---

## Key concepts

**Reality Fractal Theory (RFT)**

A unified framework for code, mathematics, physics, economics, and distributed systems.

**Stable Invariant Rift Model (SIRM)**

An invariant-preserving runtime model designed to maintain mathematical consistency under extreme concurrency.

**UltraCore Rift**

The deterministic execution architecture built around SIRM.

**Rift Network**

Solana-oriented implementation and ecosystem research.

**Rift L1 Blockchain**

A standalone Layer-1 blockchain implementation of the UltraCore-RFT runtime featuring deterministic execution, mathematical invariant validation, and integrated stress-fuzz testing.

---

## Usage

Read the documents in this repository in the following order:

1. ARCHITECT.md
2. RFT_DEVELOPMENT_STRATEGY.md
3. RFT_MATHEMATICAL_FOUNDATIONS.md

---

## Field Validation

UltraCore-RFT is currently validated through continuous runtime verification and deterministic stress testing.

Current development includes:

* deterministic invariant validation
* integrated stress fuzzing
* operation replay using deterministic seeds
* runtime state fingerprinting
* invariant checking after every operation
* ongoing Layer-1 blockchain development

Reference implementations:

**Rift Network**

https://github.com/RFT-SIRM/Rift-Network

**Rift L1 Blockchain**

https://github.com/RFT-SIRM/Rift-L1-Blockchain

---

## Build and validation

To build the documentation locally:

```bash
python3 -m pip install --user -r requirements.txt
~/.local/bin/mkdocs build --strict
```

---

## CI

The repository includes a documentation CI workflow at `.github/workflows/docs.yml`.

It validates the MkDocs documentation on push, pull request, and manual workflow execution.

---

## Contact

For collaboration and technical review, use GitHub Issues or the repository profile.

This repository focuses on research, engineering, implementation, and long-term development of deterministic distributed systems.
