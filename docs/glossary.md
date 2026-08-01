# Glossary

## Core Terminology

| Term | Definition |
|------|------------|
| SIRM | Scalar Invariant Resource Model -- the mathematical framework governing all RFT-SIRM systems |
| CoreState | The central state structure containing `global_field`, `total_base_sum`, `total_supply`, and participant accounts |
| global_field | A uniform scalar shift applied to all participants' effective balances |
| base_balance | Individual deviation from the `global_field`; unique per participant |
| effective_balance | `base_balance + global_field`; the actual economic balance of a participant |
| total_base_sum | Sum of all individual `base_balance` values |
| total_supply | Total economic supply in the system; must equal `total_minted - total_burned` |
| p | Participant count; number of active accounts in CoreState |
| dust_accumulator | Rounding remainder from division operations; bounded by `p` (I3) |
| edge_cost | Directed transfer tax or subsidy; positive = burn, negative = mint |
| NEG_E | Negative entropy deflationary tick using Euler's number (`-e * 10^18`) |
| redistribute | O(1) operation that updates `global_field` to distribute rewards to all participants |
| check_invariant | Function that verifies I1-I4 after every state mutation |
| Rift Token | SPL token interface that reads CoreState but never writes to it |
| rift_multiplier | Cached conversion factor between SOL and Rift shares |

## Runtime Terminology

| Term | Definition |
|------|------------|
| CPI | Cross-Program Invocation; Solana mechanism for calling other programs |
| PDA | Program Derived Address; deterministic account address derived from seeds |
| libFuzzer | Coverage-guided fuzz testing engine used for invariant verification |
| Memory Contexts | Per-CPI-frame permission isolation layer in Agave SVM |
| Scheduler | Conflict-aware transaction ordering component |
| hotspot | Account heat score tracking write contention |
| deferred queue | Queue for transactions blocked by conflicts |
| generation | Monotonic counter representing scheduling passes |

## Research Terminology

| Term | Definition |
|------|------------|
| RFT | Reality Fractal Theory -- the overarching research framework |
| O(1) distribution | Constant-time reward distribution via scalar field update |
| deterministic invariant | Hard mathematical constraint enforced after every operation |
| upstream contribution | Bug fix or RFC submitted to external project (e.g., anza-xyz) |
| fuzz harness | Test framework that generates random inputs and checks invariants |
| regression test | Test that prevents a previously fixed bug from reoccurring |

---

See also: [Architecture](architecture.md) for system design, [Foundations](foundations.md) for mathematical derivations.
