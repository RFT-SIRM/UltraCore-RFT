# UltraCore RFT

Research laboratory for deterministic execution topology, invariant systems, and high-concurrency runtime architecture based on **Reality Fractal Theory (RFT)**.

---

## What is this?

UltraCore RFT is the central research hub for a family of experimentally verified distributed system components. All implementations share a common foundation: **mathematical invariants enforced at runtime, verified through continuous fuzzing**.

Since July 2026, the research has expanded from theoretical architecture into three actively developed and fuzz-tested implementations.

---

## Implementation Repositories

### [Rift L1 Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain)

Standalone Layer-1 blockchain runtime built on the UltraCore-RFT engine and SIRM.

| Metric | Result |
|--------|--------|
| Operations fuzz-tested | 256,150,000+ |
| SIRM invariant violations | 0 |
| Crashes | 0 |
| Test duration | 5+ hours |
| Avg ops/sec | 8,530,712 |

**Key properties:** deterministic execution, mathematical invariant validation after every operation, integrated stress-fuzz testing, Apache 2.0.

---

### [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts)

Research module for per-CPI-frame writable permission isolation in Agave SVM ABIv2.

**Bug found and fixed:** The original implementation called `snapshot.entries.clear()` before re-snapshotting on every `update_account_permissions()` call within the same CPI frame. On `pop()`, only the last-touched account was restored. All earlier accounts retained their modified writable permission permanently — a silent permission leak across CPI frames.

| Metric | Result |
|--------|--------|
| Fuzz executions | 4,294,967,296+ |
| Execution speed | ~421,000 exec/s |
| Invariant violations | 0 |
| Duration | 5h 55m |

---

### [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler)

Research implementation of a conflict-aware transaction scheduler for Agave SVM.

**Bugs found and fixed:**

**Bug 1 — Dead deferred queue:** Transactions were pushed into the deferred queue but nothing ever read them back. Every conflicting transaction was silently lost forever.

**Bug 2 — Zero-cost bypass:** A `tx.cost > 0` guard allowed zero-cost transactions to bypass conflict detection entirely, scheduling immediately on contested accounts.

**Bug 3 — Fuzzer invariant gap:** `max_retry_count=15` created backoff chains up to 2303 generations, exceeding the 512-pass drain limit. Found and fixed during fuzzing.

| Metric | Result |
|--------|--------|
| Fuzz executions (daily) | ~91,000,000 per run |
| Execution speed | ~4,300 exec/s (CI) / ~8,500 exec/s (M1) |
| Invariant violations | 0 |
| Unit tests | 15 passed |
| Daily fuzz duration | 5h 55m |

---

### [Rift-Network](https://github.com/RFT-SIRM/Rift-Network)

Solana-oriented implementation and ecosystem research. Security audit completed: 14 findings documented and addressed.

---

## Core Concepts

**Reality Fractal Theory (RFT)**  
A unified framework applied across code, mathematics, economics, and distributed systems. The central idea: invariants are not checked after the fact — they are structural properties of the runtime itself.

**Stable Invariant Rift Model (SIRM)**  
An invariant-preserving runtime model maintaining mathematical consistency under concurrent execution. Every operation either preserves all invariants or is rejected atomically.

Core SIRM invariants (applied in Rift L1):
**UltraCore Rift**  
The deterministic execution architecture built around SIRM. Identical inputs produce identical outputs. State is always consistent. No silent failures.

---

## Verification Approach

All implementations share the same verification methodology:

| Layer | Tool | Coverage |
|-------|------|----------|
| Unit tests | cargo test | Regression, edge cases |
| Property tests | Manual random seeds | 100+ seeds per property |
| Fuzz testing | libFuzzer via cargo-fuzz | Invariants under random inputs |
| Long-run fuzz | GitHub Actions schedule | 5h 55m daily per repository |
| Differential tests | Buggy vs fixed impl | Confirms bug is reproducible |

**Why long-duration fuzzing matters:** At ~4,000–8,000 exec/s, a 5h 55m run produces 90–170 million executions asserting all invariants. This does not prove correctness formally, but it provides strong experimental evidence that no invariant violation exists within the reachable input space.

---

## Repository Documents

Read in this order:

1. [ARCHITECT.md](ARCHITECT.md) — architecture overview and research mindset
2. [RFT_DEVELOPMENT_STRATEGY.md](RFT_DEVELOPMENT_STRATEGY.md) — development strategy and roadmap
3. [RFT_MATHEMATICAL_FOUNDATIONS.md](RFT_MATHEMATICAL_FOUNDATIONS.md) — mathematical foundations and runtime operators
4. [RESEARCH_SUPPORT.md](RESEARCH_SUPPORT.md) — collaboration guidance

---

## Roadmap

**Phase 1 — Research implementations (current)**  
Three fuzz-verified components. Bugs found, fixed, and regression-tested.

**Phase 2 — Agave integration**  
Integrate memory-contexts fix and scheduler into `anza-xyz/agave`.  
Replace research mocks with real `TransactionContext` and `AccountId`.

**Phase 3 — Validator benchmarks**  
Measure against production Agave on mainnet-representative workloads.  
Produce Criterion before/after numbers.

**Phase 4 — RFC / PR**  
Draft PR against `anza-xyz/agave` with fuzz corpus, benchmarks, and invariant documentation as evidence.

---

## Build Documentation Locally

```bash
python3 -m pip install --user -r requirements.txt
~/.local/bin/mkdocs build --strict
```

---

## License

Apache-2.0

This repository focuses on research, engineering, and long-term development of deterministic distributed systems.

© 2026 Eugeny (RFT-SIRM)
