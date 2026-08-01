# Field Trials and Verification

## Verification Philosophy

Every claim in the RFT-SIRM ecosystem is backed by reproducible verification. We measure correctness rather than asserting it.

## Verification Matrix

| Component | Method | Metric | Result |
|-----------|--------|--------|--------|
| SIRM Core Invariants | libFuzzer (stratified) | Operations tested | 1,000,000,000,000+ |
| SIRM Core Invariants | libFuzzer (stratified) | Invariant violations | 0 |
| SIRM Core Invariants | libFuzzer (stratified) | Crashes | 0 |
| SIRM Core Invariants | libFuzzer (stratified) | Test duration | 5h 55m |
| SIRM Core Invariants | libFuzzer (stratified) | Throughput (CI) | ~5,750,000 ops/sec |
| SIRM Core Invariants | libFuzzer (stratified) | Throughput (Apple M4) | >10,000,000 ops/sec |
| Rift Network | libFuzzer (cargo-fuzz) | Runs | 2,547,707,477+ |
| Rift Network | libFuzzer (cargo-fuzz) | Crashes | 0 |
| Rift Network | libFuzzer (cargo-fuzz) | Test duration | ~5h 52m daily |
| Rift Network | Security audit | Findings addressed | 14 |
| Agave Memory Contexts | libFuzzer | Executions | 4,294,967,296+ |
| Agave Memory Contexts | libFuzzer | Invariant violations | 0 |
| Agave Memory Contexts | libFuzzer | Panics | 0 |
| Agave Scheduler | libFuzzer | Executions | ~91,000,000 per 5h 55m run |
| Agave Scheduler | libFuzzer | Invariant violations | 0 |
| Agave Scheduler | Unit tests | Regression tests | 15 |

## Fuzz Harness Design

### Rift L1 Blockchain

Five stratified modes cover distinct protocol paths:

| Mode | Target | Invariant |
|------|--------|-----------|
| 0 | NEG_E boundary | Overflow guard on `apply_neg_entropy` |
| 1 | Large `p` | Dust accumulation and redistribution edge cases |
| 2 | Negative field | Debt limit and `DebtOnExit` rejection |
| 3 | `p = 0` | Zero-participant transitions |
| 4 | Near `u128::MAX` | Arithmetic overflow protection |

### Rift Network

Stateful fuzzer applies up to 8 randomized state mutations per execution:
- `register_participant`
- `unregister_participant`
- `apply_transfer`
- `redistribute_amount`
- `apply_neg_entropy_tick`

Both SIRM invariants are asserted after every step.

### Agave Memory Contexts

Each execution applies up to 8 randomized state mutations and asserts:
- `TOTAL_SUPPLY == TOTAL_MINTED - TOTAL_BURNED`
- `TOTAL_SUPPLY == TOTAL_BASE_SUM + (GLOBAL_FIELD * P)`

Coverage stabilizes at `cov: 53 ft: 166` within the first billion iterations.

### Agave Scheduler

Four invariants asserted after every scheduling pass:

| ID | Invariant | Failure Mode |
|----|-----------|--------------|
| I1 | `scheduled + deferred + dropped <= scanned` | Silent transaction loss |
| I2 | `summary.generation > 0` | Zero generation deadlock |
| I3 | `scheduler_passes >= 1` | Metrics corruption |
| I4 | Deferred queue drains to zero within bounded passes | Permanent starvation |

## Coverage Stabilization

Coverage typically stabilizes within the first 100,000 executions (`cov: ~420 ft: ~2600` for the scheduler). Subsequent runs refine the corpus but rarely discover new coverage, indicating the harness has exhausted the reachable state space for inputs within the size limits.

## Limitations

Fuzzing explores the input space stochastically. A 5h 55m run increases confidence that no invariant violation exists for inputs of the tested size and shape. It does not constitute a formal proof. Formal verification (model checking or theorem proving) is planned for Phase 4.

## Readiness Checklist

- [x] SIRM invariants defined and documented
- [x] O(1) distribution proven correct
- [x] Standalone Rust implementation complete
- [x] Solana/Anchor protocol (RC v1.0)
- [x] Security audit completed (14 findings addressed)
- [x] Fuzz verification: 1T+ ops, 0 violations
- [x] Fuzz verification: 2.5B+ runs, 0 crashes
- [x] Agave memory contexts: CPI permission leakage found and fixed
- [x] Agave scheduler: dead deferred queue and zero-cost bypass found and fixed
- [x] External references and upstream contributions documented
- [ ] Formal verification (Phase 4)
- [ ] Agave integration RFC (Phase 5)
- [ ] Mainnet deployment

---

See also: [Implementation](implementation.md) for build instructions, [Strategy](strategy.md) for research phases.
