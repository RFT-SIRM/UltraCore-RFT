# seL4 Complementary Verification

> **RFT-SIRM Deterministic Empirical Verification of the seL4 Capability Derivation Tree**
>
> Document ID: RFT-EXP-SELC4-2026-001

<p align="center">
  <img src="https://img.shields.io/badge/seL4-CDT%20Stress%20Test-indigo?style=for-the-badge">
  <img src="https://img.shields.io/badge/Operations-%3E1B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Crashes-0-success?style=for-the-badge">
</p>

---

## Contents

```
research/seL4/
├── src/
│   └── rft_cdt_fuzzer_sel4.c      # Fuzzer implementation (single-file drop-in)
└── README.md                       # This file
```

---

## Quick Start

### Prerequisites

- Docker with QEMU support
- Git
- CMake / Ninja build system

### Step-by-Step Reproduction

```bash
# 1. Clone the seL4 testbed
git clone https://github.com/seL4/sel4test.git
cd sel4test

# 2. Place the fuzzer source
cp research/seL4/src/rft_cdt_fuzzer_sel4.c    projects/sel4test/apps/sel4test-tests/src/tests/

# 3. Build
cd build-aarch64
ninja

# 4. Run smoke test (200 ops, ~1 minute)
SEL4TEST_FILTER='RFT_CDT_0001' ./simulate

# 5. Run 20-minute test (2M ops)
SEL4TEST_FILTER='RFT_CDT_20MIN' ./simulate

# 6. Run full marathon (~100 hours, 1B+ ops)
SEL4TEST_FILTER='RFT_CDT_MARATHON' ./simulate
```

---

## What This Tests

The fuzzer exercises the seL4 Capability Derivation Tree (CDT) through pseudo-random, syntactically valid capability operations under deterministic seed control.

| Operation Family | seL4 Primitive |
|-----------------|----------------|
| Retype | `seL4_Untyped_Retype` |
| Copy | `seL4_CNode_Copy` |
| Delete | `seL4_CNode_Delete` |
| Mint | `seL4_CNode_Mint` |
| Revoke | `seL4_CNode_Revoke` |
| Move | `seL4_CNode_Move` |
| Mutate | `seL4_CNode_Mutate` |
| Rotate | `seL4_CNode_Rotate` |
| CancelBadgedSends | `seL4_Endpoint_CancelBadgedSends` |

Object types: Endpoint, Notification, TCB.

---

## Results Summary

| Metric | Value |
|--------|-------|
| Total operations | > 1.0 × 10⁹ |
| Kernel crashes | 0 |
| Kernel panics | 0 |
| Capability leaks post-drain | 0 |
| seL4 test suite post-marathon | 123 / 123 passed |

---

## Full Report

See [`docs/field_trials_sel4.md`](../../docs/field_trials_sel4.md) for the complete experimental report with methodology, limitations, and reproducibility checklist.

---

## License

Apache-2.0 — Copyright 2026 Eugeny (RFT-SIRM)
