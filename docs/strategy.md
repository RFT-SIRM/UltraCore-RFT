# Development Strategy

> **Scope:** Strategic roadmap, research phases, and ecosystem positioning for the RFT-SIRM deterministic invariant systems laboratory.

---

## 1. Mission

Build a deterministic, mathematically verified economic layer for distributed systems where invariants are hard constraints enforced at every state transition.

**Core principle:** Correctness is not assumed — it is measured, fuzzed, and documented. Every state transition must satisfy the SIRM invariant suite (I1–I4) or be explicitly rejected.

---

## 2. The RFT Methodology

RFT-SIRM operates as a **multi-stage research pipeline**. Each stage feeds into the next, but stages are independent enough to be evaluated, funded, and deployed separately.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Stage 0       │ --> │   Stage 1       │ --> │   Stage 2       │
│  Mathematical   │     │  Reference      │     │  Protocol       │
│  Foundation     │     │  Implementation │     │  Deployment     │
│  (SIRM)         │     │  (Rust/Anchor)  │     │  (Solana L1)    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                       │                       │
         v                       v                       v
   Invariant spec          Fuzz verification       Security audit
   Formal model            CI/CD integration     Mainnet readiness
```

**Key insight:** Stages are decoupled. SIRM can be instantiated in any runtime — Solana, standalone L1, or future environments — without changing the invariant specification.

---

## 3. Research Phases

### Phase 0 — Mathematical Foundation (Complete)

**Goal:** Define the Scalar Invariant Resource Model and prove its correctness properties.

| Deliverable | Status |
|:------------|:-------|
| SIRM invariants I1–I4 defined and documented | ✅ Complete |
| O(1) distribution correctness proven | ✅ Complete |
| Formal specification draft | ✅ Complete |
| Reference Rust implementation (Rift L1 Blockchain) | ✅ Complete |
| Fuzz verification: 1T+ operations, 0 violations | ✅ Complete |

**Repository:** [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain)

### Phase 1 — On-Chain Protocol (Complete)

**Goal:** Port CoreState to Solana runtime via Anchor, maintaining all invariants on-chain.

| Deliverable | Status |
|:------------|:-------|
| `ultra_core_rift` program (CoreState logic) | ✅ Complete |
| `rift_token` program (SPL-compatible token interface) | ✅ Complete |
| Security audit: 14 findings identified and addressed | ✅ Complete |
| Fuzz verification: 2.5B+ runs, 0 crashes | ✅ Complete |
| Release Candidate v1.0 | ✅ Complete |

**Repository:** [Rift-Network](https://github.com/RFT-SIRM/Rift-Network)

### Phase 2 — Runtime Security Research (Active)

**Goal:** Identify and address security gaps in Solana core infrastructure. Feed findings upstream.

#### 2a — SVM Memory Isolation

| Deliverable | Status |
|:------------|:-------|
| CPI permission leakage analysis | ✅ Complete |
| Bug reported upstream: [anza-xyz/svm#25](https://github.com/anza-xyz/svm/issues/25) | ✅ Complete |
| Awaiting upstream review / integration | ⏳ Pending |

**Repository:** [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts)

#### 2b — Transaction Scheduler Observability

| Deliverable | Status |
|:------------|:-------|
| Bounded retry semantics research | ✅ Complete |
| Reference implementation (Rift Scheduler) | ✅ Complete |
| Fuzz verification: 91M+ executions, 0 invariant violations | ✅ Complete |
| RFC published: [anza-xyz/agave#14274](https://github.com/anza-xyz/agave/issues/14274) | ✅ Complete |
| Draft PR against `anza-xyz/agave` (pending RFC feedback) | 🔜 Q3 2026 |
| Side-by-side benchmark via `scheduler-bindings` | 🔜 Q3 2026 |

**Repository:** [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler)

> **Note:** The RFC documents an observed scheduling limitation (unbounded deferred retry without observability), not a security vulnerability. The proposal is a minimal, opt-in addition: `max_retry_count` and `dropped_transactions` metric.

### Phase 3 — Formal Verification (Accelerated)

**Goal:** Machine-checked proofs for critical SIRM invariants.

| Deliverable | Status | Target |
|:------------|:-------|:-------|
| TLA+ specification for CoreState transitions | 📋 Planned | Q3 2026 |
| Coq proof of O(1) distribution correctness | 📋 Planned | Q4 2026 |
| Integration with existing Solana formal verification frameworks | 📋 Planned | Q4 2026 |

> **Acceleration:** Phase 3 is being brought forward from Q4 2026 to Q3 2026. Mathematical foundations are mature; formal tooling is the remaining bottleneck, not model complexity.

### Phase 4 — Ecosystem Integration (Accelerated)

**Goal:** Transition from research to production-ready infrastructure.

| Deliverable | Status | Target |
|:------------|:-------|:-------|
| Agave scheduler: Draft PR merged or rejected with feedback | 📋 Planned | Q3 2026 |
| Agave memory: Upstream fix integrated or documented | 📋 Planned | Q3 2026 |
| Rift Network: Mainnet deployment readiness assessment | 📋 Planned | Q4 2026 |
| Rift L1: Consensus-layer benchmarking under realistic load | 📋 Planned | Q4 2026 |

> **Acceleration:** Integration milestones are being compressed into Q3–Q4 2026. Research velocity has exceeded initial projections; upstream engagement is active.

---

## 4. Velocity & Execution Pace

RFT-SIRM operates at **research velocity significantly above baseline** for solo infrastructure research:

| Phase | Planned Duration | Actual Duration | Acceleration |
|:------|:---------------|:----------------|:-------------|
| Phase 0 — Mathematical Foundation | 6 months | 4 months | **1.5×** |
| Phase 1 — On-Chain Protocol | 6 months | 5 months | **1.2×** |
| Phase 2a — Memory Security Research | 4 months | 3 months | **1.3×** |
| Phase 2b — Scheduler Research | 4 months | 2.5 months | **1.6×** |

**Why this pace is sustainable:**
- **Modular architecture:** Each component is self-contained; parallel workstreams do not block each other.
- **Deterministic invariants:** I1–I4 provide unambiguous acceptance criteria; no scope creep.
- **CI-driven verification:** Every commit is fuzz-tested; regressions are caught immediately.
- **Upstream-first approach:** Findings are reported early, not hoarded; feedback loops are short.

**Implication for funding:** Milestones can be delivered earlier than standard grant timelines assume. We prefer **aggressive, scoped sprints** over extended, open-ended research periods.

---

## 5. Repository Alignment

| Phase | Repository | Status | Primary Output |
|:------|:-----------|:-------|:---------------|
| 0 | [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain) | ✅ Complete | Standalone validator core, invariant spec |
| 1 | [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | ✅ RC v1.0 | Solana on-chain protocol |
| 2a | [agave-abiv2-memory-contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts) | 🔬 Active | Security research, upstream bug report |
| 2b | [agave-rift-scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler) | 📋 RFC Published | Reference implementation, RFC discussion |
| 3 | — | 📅 Planned | Formal specifications |
| 4 | — | 📅 Planned | Production integration |

**Legend:** ✅ Complete · 🔄 Release Candidate · 🔬 Active Research · 📋 RFC Published · 📅 Planned

---

## 6. Verification Strategy

Every phase must satisfy four verification gates before advancing:

| Gate | Method | Acceptance Criteria |
|:-----|:-------|:------------------|
| **Invariant Preservation** | Unit tests + property-based tests | All SIRM invariants hold after every operation; zero violations |
| **Fuzz Verification** | libFuzzer with stratified mode selection | Coverage saturation (`cov` / `ft` stable); zero crashes over 5h+ runs |
| **Regression Testing** | Dedicated test per bug class | Every historical bug has a regression test that fails if reintroduced |
| **Documentation** | Design docs + RFCs + audit trails | Every design decision has rationale; every upstream finding has permalink |

---

## 7. Upstream Engagement

Security research and architectural findings are reported back to the Solana core infrastructure. We do not hoard findings — we publish them to improve the ecosystem.

| Issue | Component | Type | Description | Status |
|:------|:----------|:-----|:------------|:-------|
| [anza-xyz/svm#25](https://github.com/anza-xyz/svm/issues/25) | SVM Runtime | Security | CPI permission leakage: per-frame writable permission rollback failure when multiple `update_account_permissions` calls occur within a single CPI frame. | Reported, awaiting review |
| [anza-xyz/agave#14274](https://github.com/anza-xyz/agave/issues/14274) | Banking Stage | RFC | Bounded retry semantics and starvation observability for GreedyScheduler: documented scheduling limitation, proposed `max_retry_count` and `dropped_transactions` metric. | RFC open, discussion active |

**Engagement principle:** We open RFCs and bug reports, provide reference implementations, and await upstream feedback. We do not fork core infrastructure without community consensus.

---

## 8. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|:------|:-----------|:-------|:-----------|
| Upstream RFC rejection or stall | Medium | Medium | Maintain standalone research repositories; publish benchmark results independently; continue independent verification |
| Formal verification complexity exceeds timeline | Medium | Low | Phase 3 is accelerated but scoped; fuzz verification provides strong interim guarantee; milestones are modular |
| Token layer adoption slower than expected | Medium | High | Core invariants are independent of token layer; economic model is self-contained and portable across runtimes |

> **Note on bandwidth:** Previous risk assessments flagged "solo-researcher bandwidth" as high-risk. Execution data (see §4) shows this risk is mitigated by modular architecture and deterministic invariants. Velocity has consistently exceeded projections.

---

## 9. Timeline (Accelerated)

| Milestone | Original Target | Accelerated Target | Status |
|:----------|:----------------|:-------------------|:-------|
| SIRM Core complete | Q2 2026 | Q2 2026 | ✅ Done |
| Solana protocol RC v1.0 | Q3 2026 | Q3 2026 | ✅ Done |
| Agave memory research: upstream report filed | Q3 2026 | Q3 2026 | ✅ Done |
| Agave scheduler RFC published | Q4 2026 | Q3 2026 | ✅ Done |
| Agave scheduler: Draft PR or benchmark | Q4 2026 | **Q3 2026** | 🔜 In progress |
| Formal verification: TLA+ spec started | Q4 2026 | **Q3 2026** | 📋 Planned |
| Agave integration: upstream feedback loop closed | Q1 2027 | **Q4 2026** | 📋 Planned |
| Rift Network: mainnet readiness assessment | Q1 2027 | **Q4 2026** | 📋 Planned |

---

## 10. Funding Strategy

RFT-SIRM operates on a **milestone-based, accelerated funding model**. Each research phase is scoped, costed, and delivered independently — with timelines compressed to match execution velocity.

| Phase | Typical Scope | Timeline | Funding Source |
|:------|:--------------|:---------|:---------------|
| 0–1 | Core protocol, security research | 4–5 months | Microgrants, hackathon prizes, ecosystem grants |
| 2 | Upstream research, RFCs, benchmarks | 2–3 months | Ecosystem grants (Solana Foundation, Anza), research fellowships |
| 3 | Formal verification, theorem proving | 3–4 months | Academic grants, foundation research programs |
| 4 | Production integration, mainnet readiness | 3–4 months | Infrastructure grants, protocol revenue, strategic partnerships |

**Principle:** No phase begins without scoped deliverables and defined acceptance criteria. We do not seek open-ended funding. We prefer **shorter timelines with higher intensity** over extended research periods.

---

## 11. Cross-References

- [Implementation](implementation.md) — Technical architecture and build instructions
- [Field Trials](field_trials.md) — Verification metrics, fuzzing results, benchmark data
- [Architecture](architecture.md) — System design decisions and component diagrams
- [Foundations](foundations.md) — Mathematical foundations of SIRM
