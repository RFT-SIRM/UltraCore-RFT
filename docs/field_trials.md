# Field Trials and Verification

> **Scope:** Reproducible verification results, fuzzing methodology, synthetic benchmarks, and readiness assessment for the RFT-SIRM ecosystem.

---

## 1. Verification Philosophy

Every claim in the RFT-SIRM ecosystem is backed by reproducible verification. We measure correctness rather than asserting it.

Our verification pipeline operates at three levels:

| Level | Method | Purpose |
|:------|:-------|:--------|
| **Unit** | `cargo test` — 15+ regression tests per component | Correctness of individual functions |
| **Fuzz** | libFuzzer + cargo-fuzz — 1T+ operations | Invariant preservation under randomized inputs |
| **Synthetic** | Discrete-event simulation — 2,000+ tx scenarios | Behavioral modeling under controlled contention |

---

## 2. Verification Matrix

### 2.1 SIRM Core Invariants

| Method | Metric | Result |
|:-------|:-------|:-------|
| libFuzzer (stratified) | Operations tested | 1,000,000,000,000+ |
| libFuzzer (stratified) | Invariant violations | **0** |
| libFuzzer (stratified) | Crashes | **0** |
| libFuzzer (stratified) | Test duration | 5h 55m per run |
| libFuzzer (stratified) | Throughput (CI) | ~5,750,000 ops/sec |
| libFuzzer (stratified) | Throughput (Apple M4) | >10,000,000 ops/sec |

### 2.2 Rift Network

| Method | Metric | Result |
|:-------|:-------|:-------|
| libFuzzer (cargo-fuzz) | Runs | 2,547,707,477+ |
| libFuzzer (cargo-fuzz) | Crashes | **0** |
| libFuzzer (cargo-fuzz) | Test duration | ~5h 52m daily |
| Security audit | Findings addressed | 14 |

### 2.3 Agave Memory Contexts

| Method | Metric | Result |
|:-------|:-------|:-------|
| libFuzzer | Executions | 4,294,967,296+ |
| libFuzzer | Invariant violations | **0** |
| libFuzzer | Panics | **0** |

### 2.4 Agave Scheduler

| Method | Metric | Result |
|:-------|:-------|:-------|
| libFuzzer | Executions | ~91,000,000 per 5h 55m run |
| libFuzzer | Invariant violations | **0** |
| Unit tests | Regression tests | 15 |
| Synthetic benchmark | Scenarios | 4 (see §4) |
| Synthetic benchmark | Transactions per scenario | 2,000 |

---

## 3. Fuzz Harness Design

### 3.1 Rift L1 Blockchain

Five stratified modes cover distinct protocol paths:

| Mode | Target | Invariant |
|:-----|:-------|:----------|
| 0 | `NEG_E` boundary | Overflow guard on `apply_neg_entropy` |
| 1 | Large `p` | Dust accumulation and redistribution edge cases |
| 2 | Negative field | Debt limit and `DebtOnExit` rejection |
| 3 | `p = 0` | Zero-participant transitions |
| 4 | Near `u128::MAX` | Arithmetic overflow protection |

### 3.2 Rift Network

Stateful fuzzer applies up to 8 randomized state mutations per execution:
- `register_participant`
- `unregister_participant`
- `apply_transfer`
- `redistribute_amount`
- `apply_neg_entropy_tick`

Both SIRM invariants are asserted after every step.

### 3.3 Agave Memory Contexts

Each execution applies up to 8 randomized state mutations and asserts:
- `TOTAL_SUPPLY == TOTAL_MINTED - TOTAL_BURNED`
- `TOTAL_SUPPLY == TOTAL_BASE_SUM + (GLOBAL_FIELD * P)`

Coverage stabilizes at `cov: 53 ft: 166` within the first billion iterations.

### 3.4 Agave Scheduler

Four invariants asserted after every scheduling pass:

| ID | Invariant | Failure Mode |
|:---|:----------|:-------------|
| I1 | `scheduled + deferred + dropped <= scanned` | Unaccounted transaction lifecycle |
| I2 | `summary.generation > 0` | Zero generation deadlock |
| I3 | `scheduler_passes >= 1` | Metrics corruption |
| I4 | Deferred queue drains to zero within bounded passes after input stops | Unbounded starvation |

> **Note:** I1 ensures every transaction is accounted for (scheduled, deferred, or dropped). It does not assert that all transactions are scheduled — bounded retry semantics explicitly allow dropping after `max_retry_count`.

---

## 4. Synthetic Benchmark: Agave Scheduler

### 4.1 Methodology

We constructed a discrete-event simulation that models `GreedyScheduler` behavior under controlled contention patterns. The simulation is **not** a production validator measurement — it is a reference model designed to isolate and observe scheduling behavior under specific workload assumptions.

**Simulation parameters:**
- Priority queue (max-heap by `compute_unit_price`)
- Thread-aware account locks (write/read conflict detection)
- Per-pass execution model: scheduled transactions hold locks for one pass, then release
- Incoming traffic: 50 tx per scheduling pass
- Worker threads: 4
- Drain passes: 200+ after input stops

### 4.2 Scenarios

| Scenario | Description | Conflict Intensity |
|:---------|:------------|:-----------------|
| Sustained Contention | 30% of transactions write to 5 hot accounts | Moderate |
| Burst → Independent | 10 passes of burst contention, then independent transactions | High → None |
| Hot Account Priority Starvation | 70% of transactions write to 1 hot account, random priorities | Extreme |
| Independent | All transactions write to unique accounts | None (baseline) |

### 4.3 Results

#### Scenario: Hot Account Priority Starvation

| Metric | GreedyScheduler (reference model) |
|:-------|:----------------------------------|
| Total transactions | 2,000 |
| Scheduled | 835 (41.8%) |
| Deferred (still in queue after 200+ drain passes) | 1,165 (58.3%) |
| Explicitly dropped | 0 (0%) — no mechanism exists |
| Mean scheduling latency | 28.9 passes |
| P99 scheduling latency | 210 passes |
| Max queue depth observed | 1,382 |

**Interpretation:** In this synthetic model, lower-priority transactions to the hot account are deferred indefinitely while higher-priority traffic continues to be scheduled. There is no metric that would allow an operator to observe this accumulation. The transactions are **not lost** — they remain in the queue — but their scheduling latency is unbounded.

#### Scenario: Burst → Independent

| Metric | GreedyScheduler (reference model) |
|:-------|:----------------------------------|
| Scheduled | 2,000 (100%) — with high latency tail |
| Mean latency | 11.4 passes |
| P99 latency | 92 passes |
| Queue drain time after burst ends | ~100 passes |

**Interpretation:** After a burst of contention ends, the scheduler must sequentially drain a large deferred backlog before new independent transactions experience low latency.

#### Scenario: Independent (baseline)

| Metric | GreedyScheduler (reference model) |
|:-------|:----------------------------------|
| Scheduled | 2,000 (100%) |
| Mean latency | ~0 passes |
| P99 latency | 1 pass |

**Interpretation:** With zero conflicts, the scheduler performs optimally. No regression observed.

### 4.4 Rift Scheduler Reference Model Comparison

Under identical synthetic workloads, the Rift Scheduler (bounded retry semantics) demonstrates:

| Metric | GreedyScheduler | Rift Scheduler (research) |
|:-------|:----------------|:--------------------------|
| Deferred queue drain | Unbounded | Bounded by `max_retry_count` |
| Starvation observability | None | `dropped_transactions` metric |
| Recovery after burst | ~100 passes | ~40 passes |
| Mean latency (hot priority) | 28.9 passes | 1.0 pass |

> **Important:** These are reference model results comparing two scheduling semantics under identical synthetic assumptions. They do not constitute a claim that Rift Scheduler is superior in all production scenarios.

---

## 5. Coverage Stabilization

Coverage typically stabilizes within the first 100,000 executions (`cov: ~420 ft: ~2600` for the scheduler). Subsequent runs refine the corpus but rarely discover new coverage, indicating the harness has exhausted the reachable state space for inputs within the size limits.

---

## 6. Limitations

### 6.1 Fuzzing

Fuzzing explores the input space stochastically. A 5h 55m run increases confidence that no invariant violation exists for inputs of the tested size and shape. It does not constitute a formal proof. Formal verification (model checking or theorem proving) is planned for Phase 4.

### 6.2 Synthetic Benchmark

The scheduler benchmark is a **discrete-event simulation**, not a measurement from a production validator or mainnet traffic. Results are valid under the stated assumptions (50 tx/pass, 4 threads, random priorities, specific contention ratios). Real-world validator behavior may differ due to:
- Network latency and jitter
- Variable transaction arrival patterns
- CU budget constraints not modeled in the simulation
- Hardware differences (NUMA, cache hierarchy)

### 6.3 General

No verification method can exhaustively prove absence of bugs. Our approach is defense in depth: unit tests catch obvious errors, fuzzing catches edge cases, synthetic benchmarks model specific scenarios, and formal verification (planned) will provide machine-checked proofs for critical invariants.

---

## 7. Readiness Checklist

### Core Ecosystem

- [x] SIRM invariants defined and documented
- [x] O(1) distribution proven correct
- [x] Standalone Rust implementation complete (Rift L1 Blockchain)
- [x] Solana/Anchor protocol (RC v1.0)
- [x] Security audit completed (14 findings addressed)
- [x] Fuzz verification: 1T+ ops, 0 violations
- [x] Fuzz verification: 2.5B+ runs, 0 crashes

### Agave Research

- [x] Agave memory contexts: CPI permission leakage found and reported ([svm#25](https://github.com/anza-xyz/svm/issues/25))
- [x] Agave scheduler: bounded retry semantics and starvation observability researched
- [x] Agave scheduler: RFC published ([agave#14274](https://github.com/anza-xyz/agave/issues/14274))
- [x] Agave scheduler: synthetic benchmark completed (4 scenarios, 2,000 tx each)
- [x] Agave scheduler: reference implementation fuzz-verified (91M+ exec, 0 violations)
- [ ] Agave scheduler: side-by-side benchmark via `scheduler-bindings` (planned)
- [ ] Agave scheduler: upstream RFC acceptance or feedback integration (awaiting)

### Future Phases

- [ ] Formal verification (TLA+ / Coq)
- [ ] Mainnet deployment readiness assessment
- [ ] Production validator integration

---

## 8. Cross-References

- [Implementation](implementation.md) — Build instructions and component architecture
- [Strategy](strategy.md) — Research phases and development roadmap
- [Architecture](architecture.md) — System design decisions
- [Foundations](foundations.md) — Mathematical foundations of SIRM
