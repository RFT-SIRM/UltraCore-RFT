# Development Strategy

> **Scope:** Strategic roadmap, research phases, and ecosystem positioning for the RFT-SIRM deterministic invariant systems laboratory.

---

## 1. Mission

Build a deterministic, mathematically verified economic layer for distributed systems where invariants are hard constraints enforced at every state transition.

**Core principle:** Correctness is not assumed — it is measured, fuzzed, and documented. Every state transition must satisfy the SIRM invariant suite (I1–I4) or be explicitly rejected.

## 2. Strategic priority: mathematics and evidence first

This is a reading order and research map, not a theorem asserting that each downstream application follows from the mathematics. The fourth-moment theorem does **not** prove the SIRM invariants, the higher-moment recurrence, the Phi-Genesis decimation mechanism, or a quantum advantage.

### Priority I — protect and independently audit the formal theorem

**Primary source:** [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md).

For the specific operator definitions and assumptions in the source repository, the fourth-moment trace defect is stated as

$$
\Delta_m(H^4,\theta)
= \operatorname{Tr}(H_C^4)-\operatorname{Tr}(H_{C'}^4)
= -16(3^{m-1}+1)\sin^2\left(\frac{\theta}{2}\right),
\qquad m\ge 1.
$$

With the documented normalization,

$$
I_m(\theta)
= \frac{\Delta_m(H^4,\theta)}{3^{m+1}+3}
\longrightarrow
-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right),
\qquad
I_m\left(\frac{\pi}{2}\right)\longrightarrow-\frac{8}{9}.
$$

#### Closure and maintenance tasks

- Keep the theorem statement, operator definitions, and normalization synchronized with the primary repository; treat that repository as authoritative.
- Re-run the Lean build from the documented formalization directory after any theorem or dependency change, and report the exact command and result.
- Independently check the finite-level trace identity against the stated formula, including the boundary cases and the angle convention.
- Keep the fourth-moment result separate from the higher-moment recurrence: do not describe the all-level recurrence as proved unless its proof is present and verified.
- Track numerical or spectral-decimation observations as separate evidence; they do not replace the formal theorem's assumptions or proof.

### Priority II — establish the higher-moment programme

Maintain finite-level certificates and numerical cross-checks as evidence, while marking the all-level recurrence as open until a complete proof is available.

### Priority III — audit the spectral-decimation programme independently

Use [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) to track spectral-decimation checks, boundary/corner corrections, and unresolved Gate A criteria. Report residual mismatches rather than describing the mechanism as fully closed.

### Priority IV — specify and verify SIRM as an engineering model

SIRM uses four stated runtime constraints. Short symbols are used below to keep the equations robust across GitHub Markdown renderers; the table maps each symbol to the implementation variable.

$$
\begin{aligned}
I_1:\quad & S = B + Gp,\\
I_2:\quad & S = M - D,\\
I_3:\quad & d < p \quad (p>0),\\
I_4:\quad & E_i \ge -\frac{S}{10p}.
\end{aligned}
$$

The effective-balance relation is

$$
E_i = b_i + G.
$$

| Symbol | Implementation variable |
|---|---|
| $S$ | `total_supply` |
| $B$ | `total_base_sum` |
| $G$ | `global_field` |
| $M$ | `total_minted` |
| $D$ | `total_burned` |
| $d$ | `dust_accumulator` |
| $E_i$ | `effective_balance[i]` |
| $b_i$ | `base_balance[i]` |

These constraints are an engineering specification; they are not consequences of the fourth-moment theorem.

### Priority V — evaluate applications against their own evidence

Assess Rift-L1, Rift-Network, scheduler, memory-context, and exploratory application tracks using their own tests, audits, benchmarks, and deployment criteria. Do not infer production readiness or quantum advantage from the mathematical results above.
---

## 3. The RFT Methodology

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

## 4. Research Phases

### Phase 0 — Mathematical Foundation (Complete)

**Goal:** Define the Synthetic Intelligence Reasoning Model (Синтетическая искусственная модель рассуждений) and prove its correctness properties.

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

## 5. Velocity & Execution Pace

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

## 6. Repository Alignment

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

## 7. Verification Strategy

Every phase must satisfy four verification gates before advancing:

| Gate | Method | Acceptance Criteria |
|:-----|:-------|:------------------|
| **Invariant Preservation** | Unit tests + property-based tests | All SIRM invariants hold after every operation; zero violations |
| **Fuzz Verification** | libFuzzer with stratified mode selection | Coverage saturation (`cov` / `ft` stable); zero crashes over 5h+ runs |
| **Regression Testing** | Dedicated test per bug class | Every historical bug has a regression test that fails if reintroduced |
| **Documentation** | Design docs + RFCs + audit trails | Every design decision has rationale; every upstream finding has permalink |

---

## 8. Upstream Engagement

Security research and architectural findings are reported back to the Solana core infrastructure. We do not hoard findings — we publish them to improve the ecosystem.

| Issue | Component | Type | Description | Status |
|:------|:----------|:-----|:------------|:-------|
| [anza-xyz/svm#25](https://github.com/anza-xyz/svm/issues/25) | SVM Runtime | Security | CPI permission leakage: per-frame writable permission rollback failure when multiple `update_account_permissions` calls occur within a single CPI frame. | Reported, awaiting review |
| [anza-xyz/agave#14274](https://github.com/anza-xyz/agave/issues/14274) | Banking Stage | RFC | Bounded retry semantics and starvation observability for GreedyScheduler: documented scheduling limitation, proposed `max_retry_count` and `dropped_transactions` metric. | RFC open, discussion active |

**Engagement principle:** We open RFCs and bug reports, provide reference implementations, and await upstream feedback. We do not fork core infrastructure without community consensus.

---

## 9. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|:------|:-----------|:-------|:-----------|
| Upstream RFC rejection or stall | Medium | Medium | Maintain standalone research repositories; publish benchmark results independently; continue independent verification |
| Formal verification complexity exceeds timeline | Medium | Low | Phase 3 is accelerated but scoped; fuzz verification provides strong interim guarantee; milestones are modular |
| Token layer adoption slower than expected | Medium | High | Core invariants are independent of token layer; economic model is self-contained and portable across runtimes |

> **Note on bandwidth:** Previous risk assessments flagged "solo-researcher bandwidth" as high-risk. Execution data (see §4) shows this risk is mitigated by modular architecture and deterministic invariants. Velocity has consistently exceeded projections.

---

## 10. Timeline (Accelerated)

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

## 11. Funding Strategy

RFT-SIRM operates on a **milestone-based, accelerated funding model**. Each research phase is scoped, costed, and delivered independently — with timelines compressed to match execution velocity.

| Phase | Typical Scope | Timeline | Funding Source |
|:------|:--------------|:---------|:---------------|
| 0–1 | Core protocol, security research | 4–5 months | Microgrants, hackathon prizes, ecosystem grants |
| 2 | Upstream research, RFCs, benchmarks | 2–3 months | Ecosystem grants (Solana Foundation, Anza), research fellowships |
| 3 | Formal verification, theorem proving | 3–4 months | Academic grants, foundation research programs |
| 4 | Production integration, mainnet readiness | 3–4 months | Infrastructure grants, protocol revenue, strategic partnerships |

**Principle:** No phase begins without scoped deliverables and defined acceptance criteria. We do not seek open-ended funding. We prefer **shorter timelines with higher intensity** over extended research periods.

---

## 12. Cross-References

- [Implementation](implementation.md) — Technical architecture and build instructions
- [Field Trials](field_trials.md) — Verification metrics, fuzzing results, benchmark data
- [Architecture](architecture.md) — System design decisions and component diagrams
- [Foundations](foundations.md) — Mathematical foundations of SIRM
