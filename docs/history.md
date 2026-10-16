# Historical Development and Provenance

This page records a **selected, commit-backed chronology** across the research repositories. It is not a complete log of every experiment, nor does it reinterpret old results in light of later work. For exhaustive history, use each repository's Git log and versioned evidence files.

## 1. Selected dated milestones

| Date (UTC) | Repository | Recorded milestone | What the record does—and does not—establish |
|---|---|---|---|
| 2026-09-06 | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis/commit/32623dcec1e773074053219b8d5ba6a3bb55266e) | Carpet-model audit records look-elsewhere effects and rejects treating four mass-index matches as evidence of a selection rule | A negative result and a methodological warning; not a mass-law discovery |
| 2026-09-07 | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis/commit/c8611cc532b17c1944e2701c10780de99cae4548) | Gate A decimation check uses one-to-one eigenvalue matching and records sub-100% matching at low levels after simple exclusions | The polynomial relation matches where matches are found; the full exceptional set remains open |
| 2026-09-14 | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/ca2d6ecfcf19c875937b98047a5b7a565b7c80c2) | Lean formalization scaffold added | Formalization infrastructure was introduced; a scaffold alone is not the completed theorem |
| 2026-10-03 | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/39d7b772bdd4241ed4eef062e78f1a1e224eb5cd) | Lean work on the fourth-power trace expansion | Records an intermediate proof-development step |
| 2026-10-11 | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem/commit/180a96c692c0a13466140a5a3ef625b2aba469fa) | Commit message records the operator-level bridge and closed form for all \(m\ge1\) | Primary provenance for the formalized fourth-moment claim; read the theorem and proof files for exact scope |
| 2026-10-15 | [Theory-of-Everything synthesis](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commit/0ae3307a31f1dad88f59befbc1af9312ad6a85a9) | Higher-moment recurrence base-transition audit and arithmetic CI added | Strengthens the finite-level audit; does not close the all-level recurrence |
| 2026-10-15 | [Theory-of-Everything synthesis](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commit/159a95c54b0923218640a1563a220a7c4ef3c95e) | Reproducible level-5 higher-moment holdout added | Adds a finite holdout, not an infinite-level proof |
| 2026-10-15 | [Theory-of-Everything synthesis](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commit/c04785a8d3baa88e4ff2e6fd36b78583a4f52cde) | Higher-moment Fourier coefficient candidates reconstructed | Candidate coefficients and certificates have the scope specified in the accompanying report |
| 2026-10-16 | [UltraCore-RFT](https://github.com/RFT-SIRM/UltraCore-RFT/commit/c1aaecaae6af68dd352d2b358c6d7ae44bdac070) | Research hierarchy and evidence boundaries documented; README badge clutter reduced | A documentation/navigation milestone, not a new mathematical proof |

## 2. How to read this chronology

### The fourth-moment result

The formalization history is evidence of the development path, but the current source theorem, formal declarations, toolchain, and build are the authoritative objects for checking the result. A commit message summarizes intent; it is not itself the proof.

### Higher moments

The sequence of coefficient reconstruction, holdout tests, and arithmetic checks documents the move from observed recurrence patterns to stronger finite-level evidence. The synthesis repository explicitly leaves the all-level recurrence open. Later passing checks must not be described as closing a theorem they do not prove.

### Phi-Genesis

The Gate A and look-elsewhere-effect commits show why negative results and residual mismatches belong in the published record. The decimation relation is not “fully solved” while the exceptional set remains uncharacterized. Mass-index matches do not by themselves identify a predictive physical law.

### Engineering and applications

Runtime, protocol, scheduler, memory-isolation, and kernel-stress milestones should be reconstructed from their own commit histories, tests, audit records, and deployments. They are not used as proxies for the status of the mathematical theorem.

## 3. Provenance rules

- Preserve old failed workflows and reports; do not replace them with later success without retaining the earlier record.
- Tie every numeric claim to a repository, commit or dated workflow, input scope, and method.
- Treat the primary theorem source as authoritative for the formal statement; use this repository as a synthesis and navigation layer.
- Distinguish commit timestamps from publication, review, or independent-replication dates.
- Do not infer peer review, external validation, or novelty from a merge or a passing CI job.

## 4. Full histories

- [UltraCore-RFT commits](https://github.com/RFT-SIRM/UltraCore-RFT/commits/main)
- [Evgeny-Theorem commits](https://github.com/RFT-SIRM/Evgeny-Theorem/commits/main)
- [Theory-of-Everything commits](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commits/main)
- [Phi-Genesis commits](https://github.com/RFT-SIRM/Phi-Genesis/commits/main)
- [RFT-SIRM organization portal source history](https://github.com/RFT-SIRM/RFT-SIRM.github.io/commits/main)

## 3. Cross-project engineering strands

The mathematical research is one part of a wider public repository history. These implementation tracks are documented separately so their evidence is not conflated with the theorem:

- **Solana / Agave:** [Rift-Network](https://github.com/RFT-SIRM/Rift-Network), [Agave Rift Scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler), and [ABIv2 memory contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts).
- **seL4:** [UltraCore seL4 CDT stress-verification report](field_trials_sel4.md) and [fuzzing notes](../SEL4_CDT_FUZZING.md). These describe empirical testing and do not supersede the seL4 project's formal verification.
- **DeFi model review:** [Aave V4 Hub model review](https://github.com/RFT-SIRM/aave-v4-hub-model-review), a separate model-analysis track and not an Aave endorsement.
- **Standalone and exploratory systems:** [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain), [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski), and [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.). Each project has its own scope and evidence requirements.

### Attribution standard

This chronology records public artifacts and does not infer employment, contracts, partnerships, sponsorship, or endorsement from open-source activity or a repository name. NASA- or MATLAB-specific work should be added as a dated milestone only when its direct public artifact (repository, commit, paper, or documented contribution) has been identified and checked. A profile activity screenshot is useful as a lead, but is not sufficient to establish the exact project, technical contribution, or institutional relationship.
