# Implementation Reference

This repository is a documentation and research reference. The actual Solana implementation is located in the external repository.

## External production reference

https://github.com/RFT-SIRM/Rift-Network

## What it contains

The external repository contains:

- Anchor workspace configuration
- `ultra_core_rift` core program
- `rift_token` token interface program
- shared `rift-common` crate
- protocol specification and tests

## This repository

This repository provides:

- concept documentation
- architectural diagrams
- development strategy
- mathematical foundations

## Build and validation

Documentation is validated through MkDocs build and CI.

```bash
pip install -r requirements.txt
mkdocs build --strict
```
