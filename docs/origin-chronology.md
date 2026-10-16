# RFT-SIRM: Origin and Development Chronology

**Purpose:** preserve the maintainer-reported order in which the RFT-SIRM project family emerged, while keeping historical order separate from present-day technical dependencies and evidence strength.

[![Rift Network](https://img.shields.io/badge/01-Rift%20Network-7c3aed?style=for-the-badge)](https://github.com/RFT-SIRM/Rift-Network)
[![Rift-L1 Blockchain](https://img.shields.io/badge/02-Blockchain-2563eb?style=for-the-badge)](https://github.com/RFT-SIRM/Rift-L1-Blockchain)
[![UltraCore-RFT](https://img.shields.io/badge/03-UltraCore--RFT-334155?style=for-the-badge)](https://github.com/RFT-SIRM/UltraCore-RFT)

[![Phi-Genesis](https://img.shields.io/badge/05-Phi--Genesis-d97706?style=for-the-badge)](https://github.com/RFT-SIRM/Phi-Genesis)
[![Evgeny-Theorem](https://img.shields.io/badge/06-Evgeny--Theorem-0f766e?style=for-the-badge)](https://github.com/RFT-SIRM/Evgeny-Theorem)
[![Theory of Everything](https://img.shields.io/badge/07-Theory%20of%20Everything-5b4bc4?style=for-the-badge)](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything)

> **Provenance note:** the sequence below records the project maintainer's account of the development order. It is a historical orientation, not a complete commit-by-commit audit. Exact dates are intentionally omitted where they have not been verified against repository history. The dated, commit-linked milestones remain in [Historical Development and Provenance](history.md).

## The development sequence

<box></box>

### 1. Rift Network — the initial network direction

The origin account starts with [Rift Network](https://github.com/RFT-SIRM/Rift-Network), the early network-oriented engineering work. This is the first stage in the maintainer-reported chronology.

### 2. Rift-L1 Blockchain — the blockchain direction

The blockchain work followed as a distinct project: [Rift-L1 Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain). Its code, design, and licensing remain governed by its own repository; its position in the chronology does not make it a component of the mathematical theorem.

### 3. UltraCore-RFT — coordination and research documentation

[UltraCore-RFT](https://github.com/RFT-SIRM/UltraCore-RFT) subsequently became the documentation, research-map, evidence-boundary, and cross-repository coordination hub. It brings the project map and verification status together; it does not replace the source repositories or automatically control their builds.

### 4. Supporting systems — scheduler, memory, and related engineering work

The wider engineering strand includes separate repositories such as:

- [Agave Rift Scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler)
- [ABIv2 memory contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts)
- [Rift Network](https://github.com/RFT-SIRM/Rift-Network) and [Rift-L1 Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain), as distinct protocol/network workstreams
- Additional systems and runtime work documented in their own source repositories

These are separate implementation tracks. Their tests, fuzzing, audits, and deployment records support only the specific claims they actually cover.

### 5. Phi-Genesis — a separate spectral research programme

[Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) studies signed-flux Laplacians, spectral decimation, boundary/corner corrections, inertia computations, and exploratory mass-index patterns. Its Gate A residual and exceptional-set questions remain open in the documented status. It should not be silently folded into the SU(2)-connected operator family of Evgeny-Theorem.

### 6. Evgeny-Theorem — a specific formalized mathematical result

[Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) is the distinct theorem project. Its source repository reports a Lean 4 formalization of a specific fourth-moment trace-defect identity for the definitions and assumptions in that project. That formal result does not by itself prove the SIRM runtime invariants, close Phi-Genesis Gate A, validate hardware, or establish a complete physical theory.

### 7. Evgeny's Theory of Everything — the broader synthesis programme

[Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) came after the theorem in the maintainer-reported sequence and organizes the wider research synthesis: higher-moment recurrence, finite-level certificates, numerical holdouts, dissertation material, and open proof obligations.

**Important:** “Theory of Everything” is the name of a broad research programme, not a claim that a complete physical theory of the Universe has been established. The all-level higher-moment recurrence remains open in the currently documented status.

## Later and exploratory application tracks

The following projects are linked to the wider ecosystem but are not inserted into the core origin sequence without verified dates:

- [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) — pre-experimental quantum-processing architecture.
- [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) — exploratory invariant-driven energy-system model.
- Cosmology-related work is intentionally outside the scope of this chronology update.

Their inclusion in the ecosystem map does not establish a technical dependency on the theorem or the Theory-of-Everything synthesis. Each project retains its own assumptions, evidence requirements, intellectual-property considerations, and licensing terms.

## Two different orders — do not conflate them

| Order | What it answers | Correct use |
|---|---|---|
| **Historical chronology** | What the maintainer reports was developed first, next, and later | Project history, provenance, public narrative |
| **Evidence / reading order** | What a reader should inspect first to assess a mathematical claim | Begin with definitions, exact theorem statement, proof, and reproducible evidence |
| **Technical dependency order** | Which project actually imports, calls, or relies on another | Establish only from code, interfaces, architecture records, and tests |

The evidence-first reading order in the research map is not a claim that mathematics was historically created before the engineering systems. Likewise, chronological precedence alone does not prove a dependency.

## Provenance and maintenance rules

- Use dated commit links when recording a specific historical milestone.
- Do not invent dates to make the chronology look complete.
- Keep the maintainer-reported origin sequence visibly distinct from the verified commit table in [history.md](history.md).
- Preserve failed tests, unresolved questions, and negative results in the historical record.
- Do not imply employment, partnership, sponsorship, endorsement, patent grant, or experimental validation without direct evidence.
- When additional primary repository history is checked, update the sequence with links and dates rather than silently rewriting the narrative.

---

*This page is an orientation record based on the maintainer-reported chronology and linked public repositories. It is not an independent audit of every repository's complete Git history.*
