# Glossary

This glossary defines the canonical terminology used across the RFT-SIRM research and engineering ecosystem. Where a project has a more specific local definition, that definition must not contradict the core names below.

## Core identity

| Term | Canonical definition |
|------|----------------------|
| **SIRM** | **Synthetic Intelligence Reasoning Model** — Russian: **Синтетическая интеллектуальная модель рассуждений**. The name of the invariant-driven reasoning and systems model used in this ecosystem. Do not expand SIRM as “Scalar Invariant Resource Model” or another alternative. |
| **RFT** | **Resonant Field Theory** — Russian: **резонансная теория поля**. This is the canonical expansion of RFT. Do not use “Reality Fractal Theory” as an expansion of RFT. |
| **RFT-SIRM** | The project/ecosystem identifier combining Resonant Field Theory (RFT) and the Synthetic Intelligence Reasoning Model (SIRM). Keep the two names distinct: RFT names the theory; SIRM names the model. |
| **UltraCore-RFT** | The documentation and coordination hub for the research, systems-engineering, and application programmes in this repository. |
| **CoreState** | The central state structure containing `global_field`, `total_base_sum`, `total_supply`, and participant accounts. |
| **global_field** | A shared scalar shift applied to participants' effective balances in the implementation's accounting model. This is a software variable, not by itself a claim about a physical field. |
| **base_balance** | An individual participant's base balance before applying `global_field`. |
| **effective_balance** | `base_balance + global_field`; the participant's effective balance under the model's conventions. |
| **total_base_sum** | Sum of all individual `base_balance` values. |
| **total_supply** | Total economic supply in the system; the implementation specifies its relation to minted and burned amounts. |
| **p** | Participant count: number of active accounts represented in CoreState. |
| **dust_accumulator** | Rounding remainder from division operations; its exact bound and sign convention are defined by the implementation invariant. |
| **edge_cost** | Directed transfer cost or adjustment; the meaning of positive and negative values is implementation-specific and must be stated where used. |
| **NEG_E** | A named negative-entropy adjustment in the implementation. Any numerical scaling is defined by the source code and specification. |
| **redistribute** | An operation that updates `global_field` so a shared adjustment can be reflected in effective balances without eagerly rewriting every participant balance. |
| **check_invariant** | Function that checks the runtime invariants after a state mutation. |
| **Rift Token** | SPL-token interface that reads CoreState without directly writing to it, as specified by the relevant implementation. |
| **rift_multiplier** | Cached conversion factor between SOL and Rift shares in the relevant implementation. |

## Runtime terminology

| Term | Definition |
|------|------------|
| **CPI** | Cross-Program Invocation; Solana mechanism for calling other programs. |
| **PDA** | Program Derived Address; deterministic account address derived from seeds. |
| **libFuzzer** | Coverage-guided fuzz testing engine used for invariant verification. |
| **Memory Contexts** | Per-CPI-frame permission-isolation layer investigated in the Agave SVM research. |
| **Scheduler** | Conflict-aware transaction-ordering component. |
| **hotspot** | Account heat score tracking write contention. |
| **deferred queue** | Queue for transactions blocked by conflicts. |
| **generation** | Monotonic counter representing scheduling passes. |

## Research terminology

| Term | Definition |
|------|------------|
| **RFT** | Resonant Field Theory. Use this exact expansion consistently. |
| **SIRM** | Synthetic Intelligence Reasoning Model (Синтетическая интеллектуальная модель рассуждений). Use this exact expansion consistently. |
| **O(1) distribution** | A constant-time shared-scalar update in the specified balance representation; it does not mean every runtime operation is O(1). |
| **deterministic invariant** | A mathematical or logical constraint that the implementation checks or enforces after a state transition. |
| **upstream contribution** | Bug fix or RFC submitted to an external project (e.g., Anza/Agave). |
| **fuzz harness** | Test framework that generates inputs or state sequences and checks specified invariants. |
| **regression test** | Test designed to prevent a previously fixed bug from recurring. |
| **model field / scalar field** | A variable or mathematical quantity defined by a particular model. Do not imply that a software variable is a physical field without a separate physical definition and evidence. |
| **Reality Fractal Theory** | Not the expansion of RFT in this project. Do not use it as a synonym for Resonant Field Theory. |

---

See also: [Architecture](architecture.md) for system design and [Foundations](foundations.md) for the SIRM model and runtime invariants.
