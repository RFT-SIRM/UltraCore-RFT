# Development Strategy

## Mission

Build a deterministic, mathematically verified economic layer for distributed systems where invariants are hard constraints enforced at every state transition.

## Research Phases

### Phase 1 -- Mathematical Foundation (Complete)

- Define SIRM invariants (I1-I4)
- Prove O(1) distribution correctness
- Build standalone Rust reference implementation
- Verification: 1T+ operations fuzzed, 0 invariant violations

### Phase 2 -- On-Chain Protocol (Complete)

- Port CoreState to Solana/Anchor (`ultra_core_rift`)
- Build SPL token interface (`rift_token`)
- Security audit: 14 findings identified and addressed
- Verification: 2.5B+ fuzz runs, 0 crashes

### Phase 3 -- Runtime Security Research (Active)

- Investigate Agave SVM memory isolation (`agave-abiv2-memory-contexts`)
- Develop conflict-aware scheduler (`agave-rift-scheduler`)
- Report bugs upstream to Solana core
- Results: [CPI permission leakage](https://github.com/anza-xyz/svm/issues/25), dead deferred queue, zero-cost conflict bypass -- all found and fixed

### Phase 4 -- Formal Verification (Planned)

- Model checking for CoreState transitions
- Theorem proving for SIRM invariant preservation
- Integration with existing Solana formal verification frameworks

### Phase 5 -- Network Integration (Planned)

- Integrate scheduler and memory contexts into Agave validator
- Benchmark against mainnet-representative workloads
- Open RFC/PR against `anza-xyz/agave`

## Repository Responsibilities

| Phase | Repository | Status |
|-------|-----------|--------|
| 1 | [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | Complete |
| 2 | [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | RC v1.0 |
| 3a | [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | Active |
| 3b | [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | Active |
| 4 | -- | Planned |
| 5 | -- | Planned |

## Verification Strategy

Every phase must satisfy:

1. Invariant preservation -- all SIRM invariants hold after every operation
2. Fuzz verification -- libFuzzer with stratified mode selection
3. Regression testing -- every bug found gets a dedicated regression test
4. Documentation -- every design decision is documented with rationale

## Upstream Engagement

Security research findings are reported back to the Solana ecosystem:

- [anza-xyz/svm#25](https://github.com/anza-xyz/svm/issues/25) -- CPI permission leakage (reported, awaiting review)
- Future: scheduler RFC against `anza-xyz/agave`

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Upstream RFC rejection | Medium | Medium | Maintain standalone research repositories; continue independent verification |
| Formal verification complexity | High | Low | Phase 4 is exploratory; fuzz verification provides strong interim guarantee |
| Token layer adoption | Medium | High | Core invariants are independent of token layer; economic model is self-contained |

## Timeline

| Milestone | Target | Status |
|-----------|--------|--------|
| SIRM Core complete | Q2 2026 | Done |
| Solana protocol RC | Q3 2026 | Done |
| Agave memory research | Q3 2026 | Active |
| Agave scheduler research | Q3-Q4 2026 | Active |
| Formal verification start | Q4 2026 | Planned |
| Agave integration RFC | Q1 2027 | Planned |

---

See also: [Implementation](implementation.md) for technical details, [Field Trials](field_trials.md) for verification metrics.
