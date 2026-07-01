# UltraCore RFT

UltraCore RFT is a launch-ready research repository for Reality Fractal Theory (RFT) and the UltraCore Rift architecture. It combines a structured documentation site, architectural narrative, and field-trial readiness guidance for deterministic invariant systems.

This repository is designed for reviewers, engineers, and launch teams. It is aligned with the external Solana implementation repository:

https://github.com/RFT-SIRM/Rift-Network

## What is included

- `ARCHITECT.md` — architecture overview and research mindset
- `RFT_DEVELOPMENT_STRATEGY.md` — development strategy and roadmap
- `RFT_MATHEMATICAL_FOUNDATIONS.md` — mathematical foundations and runtime operators
- `RESEARCH_SUPPORT.md` — collaboration guidance and research positioning

## Objectives

- document the core ideas behind UltraCore Rift and SIRM
- maintain a clear conceptual foundation for field trials
- provide a stable reference for deterministic runtime design
- explain how invariant systems map to execution environments

## Key concepts

- **Reality Fractal Theory (RFT)** — a unified framework for code, mathematics, physics, economics, and distributed systems
- **Stable Invariant Rift Model (SIRM)** — an invariant-preserving runtime model that aims to maintain coherence under extreme concurrency
- **UltraCore Rift** — the applied Solana-oriented architecture for RFT research and validation

## Usage

Read the documents in this repository in the following order:

1. `ARCHITECT.md`
2. `RFT_DEVELOPMENT_STRATEGY.md`
3. `RFT_MATHEMATICAL_FOUNDATIONS.md`

## Field trials

This repository is prepared as a reference design and research artifact. For the actual Solana implementation and runtime engineering work, use:

https://github.com/RFT-SIRM/Rift-Network

## Build and validation

To build the documentation locally:

```bash
python3 -m pip install --user -r requirements.txt
~/.local/bin/mkdocs build --strict
```

## CI

The repository includes a documentation CI workflow at `.github/workflows/docs.yml`. It validates the MkDocs site on `push`, `pull_request`, and manual dispatch.

## Contact

For collaboration and technical review, use GitHub issues or the repository profile. This repository avoids direct donation links and keeps the focus on research, implementation, and launch readiness.

