# Research Map: Mathematical Foundations, Evidence, and Applications

**Reading order:** dissertation and mathematical theorem → formal evidence → higher-moment research → separate spectral-decimation programme → systems methodology → implementations and applications.

> 🟢 **Featured dissertation:** [Recursive Graph Operators, Spectral Trace Defects, and Higher-Moment Recurrence](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md). This research monograph separates formal results, finite certificates, numerical evidence, and open questions; it does not claim a completed physical Theory of Everything.

This map is deliberately hierarchical. The title *Evgeny's Theory of Everything* names a broad research programme, not a claim that a complete physical theory of the Universe has been established.

## 1. The programme at a glance

$$
\boxed{\text{Definitions and theorem}}
\longrightarrow
\boxed{\text{Reproducible evidence}}
\longrightarrow
\boxed{\text{Open extensions}}
\longrightarrow
\boxed{\text{Engineering applications}}
$$

The arrows describe an evidence-first reading order, not a theorem asserting that every downstream application follows from the mathematical result.

| Layer | Programme | Status and boundary |
|---|---|---|
| 1. Mathematical anchor | [Evgeny's Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | Source repository reports a Lean 4 proof of a specific fourth-moment identity for concrete SU(2) operators |
| 2. Recursive extension | [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) | Finite-level certificates and numerical holdouts for higher moments; all-level recurrence remains open |
| 3. Separate spectral model | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Signed-flux Laplacians, decimation audit, boundary/corner corrections; Gate A remains open |
| 4. Systems methodology | [SIRM foundations](foundations.md) | Runtime state invariants and deterministic transition model; not proved by the spectral theorem |
| 5. Implementations | [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain), [Rift-Network](https://github.com/RFT-SIRM/Rift-Network), [seL4 report](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/SEL4_CDT_FUZZING.md) | Implementation-specific tests, fuzzing, audit, and deployment evidence |
| 6. Exploratory applications | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski), [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery) | Pre-experimental or exploratory; no speed-up or physical-device claim is implied |

## Global test and evidence control

UltraCore-RFT is being developed as the central observability layer for cross-repository CI. The [Ecosystem Control Plane](ecosystem-control.md) documents the registered projects, status meanings, run artifacts, and evidence boundaries. Its first phase reads public Actions status; it does not yet dispatch workflows in other repositories.

## Engineering and application tracks

These tracks have their own repositories, validation methods, and limitations; they are not corollaries of the fourth-moment theorem.

- **Solana / Agave:** [Rift-Network](https://github.com/RFT-SIRM/Rift-Network), [Agave Rift Scheduler](https://github.com/RFT-SIRM/agave-rift-scheduler), and [ABIv2 memory contexts](https://github.com/RFT-SIRM/agave-abiv2-memory-contexts).
- **seL4 kernel testing:** [CDT stress-verification report](https://github.com/RFT-SIRM/UltraCore-RFT/blob/main/docs/field_trials_sel4.md). Empirical stress testing is not a replacement for formal kernel verification.
- **DeFi model review:** [Aave V4 Hub model review](https://github.com/RFT-SIRM/aave-v4-hub-model-review); this is not an Aave endorsement.
- **Other systems:** [Rift-L1](https://github.com/RFT-SIRM/Rift-L1-Blockchain), [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski), and [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.). Exploratory architecture and model studies should not be presented as validated production or physical-device results without separate evidence.
- **Formal contact:** see the [contact and research submission policy](support.md) for attribution, institutional correspondence, and confidential-material handling.

## 2. Mathematical anchor: the fourth-moment identity

For the definitions and assumptions documented by the primary theorem repository,

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16\left(3^{m-1}+1\right)\sin^2\left(\frac{\theta}{2}\right),
\qquad m=1,2,3,\ldots.
$$

With the source's normalization,

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3},
\qquad
\lim_{m\to\infty}I_m(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

At the special angle \(\theta=\frac{\pi}{2}\), the limiting value is:

$
-\frac{8}{9}
$

### Algebraic sanity checks

- \(3^{m+1}+3=3(3^m+1)\).
- At \(m=1,\theta=\pi/2\): \(\Delta_1=-16\), dimension \(=12\), and \(I_1=-4/3\).
- The limit follows by dividing numerator and denominator by \(3^m\).

The source repository reports that the fourth-moment statement is formalized in Lean 4 for the concrete operators and the quantifiers in the formal theorem. A checked formal proposition does not by itself settle independent semantic review, peer review, or novelty relative to the literature.

Primary sources: [theorem statement](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md).

## 3. Higher moments: what is and is not closed

The [Theory-of-Everything synthesis repository](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) studies \(H^6,H^8,H^{10}\), Fourier coefficients, residuals, and a candidate recurrence.

**Supported within the documented finite scope:** selected transition coefficients have modular/CRT certificates under explicit construction, denominator, norm, and coefficient-bound arguments; numerical holdouts and sparse-matrix-power checks are also reported.

**Still open:** proving the all-level recurrence \(R_m^{(p)}(\theta)=R_4^{(p)}(\theta)\) for all \(m\ge3\), all stated admissible angles, and \(p\in\{6,8,10\}\). The exceptional first-transition correction also needs a derivation from the recursive graph/operator structure.

A finite certificate proves its stated finite claim, not an infinite family. Small numerical residuals are evidence, not a universal proof. Read the [dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md), [recurrence note](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md), and [modular certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md).

## 4. Phi-Genesis: a separate operator family

[Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) studies signed \(Z_2\)-flux Laplacians, spectral decimation, boundary/corner corrections, inertia computations, and exploratory mass-index patterns.

- Gate A remains open while the full exceptional set and residual mismatches are not explained.
- Tests support only the assertions and inputs actually covered.
- A selected mass-index pattern is not an established predictive physical law without a mechanism, predeclared predictions, held-out validation, and independent derivation.
- No equivalence with the SU(2)-connected operators is assumed. A bridge needs an explicit operator map, boundary conditions, preserved quantities, exceptions, and a proof or clearly labelled conjecture.

Keep failed checks and rejected claims in the historical record. They are evidence about the research path, not cosmetic blemishes.

## 5. SIRM: engineering model and invariants

SIRM specifies runtime constraints for deterministic state transitions:

$$
\begin{aligned}
I_1:\;&\text{total\_supply}=\text{total\_base\_sum}+\text{global\_field}\cdot p,\\
I_2:\;&\text{total\_supply}=\text{total\_minted}-\text{total\_burned},\\
I_3:\;&\text{dust\_accumulator}<p\quad(p>0),\\
I_4:\;&\text{effective\_balance}[i]\ge-\frac{\text{total\_supply}}{10p}.
\end{aligned}
$$

Where \(\text{effective\_balance}[i]=\text{base\_balance}[i]+\text{global\_field}\), under the model's integer and scaling conventions.

The \(O(1)\) distribution argument concerns a shared scalar update and lazy effective-balance calculation. It does not imply every operation is \(O(1)\), nor does the spectral theorem prove the SIRM invariants. Runtime tests, fuzzing, audits, and deployment evidence have implementation-specific scope.

## 6. Evidence vocabulary

| Label | Meaning |
|---|---|
| **Machine-checked** | A stated proposition is accepted by the specified proof assistant and build configuration |
| **Analytically proved** | A written proof establishes the statement from explicit assumptions |
| **Certified finite-level** | A certificate covers the stated finite cases under stated bounds |
| **Numerically reproduced** | Computation matches a prediction on named inputs |
| **Engineering-tested** | Tests, fuzzing, audit, or deployment checks support an implementation-specific claim |
| **Hypothesis / conjecture** | A proposed extension awaiting proof or refutation |
| **Open** | A required derivation, proof, independent replication, or experiment is incomplete |
| **Rejected / not established** | Counterexamples or available evidence do not support the stronger claim |

A passing workflow proves only the assertions it executes. Fuzz counts and test totals are source-reported snapshots unless the page explicitly implements a live data source.

## 7. Historical reading order

1. **Invariant-first engineering:** define runtime state constraints and check them at transitions.
2. **Specific spectral theorem:** state a closed fourth-moment identity for a defined SU(2) operator family; preserve the formal and numerical evidence separately.
3. **Higher-moment extension:** investigate recurrences and finite-level certificates while keeping the all-level problem open.
4. **Separate signed-flux audit:** test spectral-decimation and mass-index claims; preserve failures and unresolved Gate A cases.
5. **Applications:** explore runtimes, protocols, kernel stress testing, quantum architecture, and energy-system models without treating them as proofs of the mathematical programme.

This is a conceptual map, not a substitute for commit-backed chronology. Use [UltraCore history](https://github.com/RFT-SIRM/UltraCore-RFT/commits/main), [theorem history](https://github.com/RFT-SIRM/Evgeny-Theorem/commits/main), [synthesis history](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/commits/main), and [Phi-Genesis history](https://github.com/RFT-SIRM/Phi-Genesis/commits/main) for exact dates and changes.

## 8. Release checklist

- [ ] Verify formulas and hypotheses against the primary theorem/specification.
- [ ] Keep the fourth-moment Lean theorem separate from higher-moment conjectures.
- [ ] Confirm each reported metric against its workflow or report and commit.
- [ ] Keep Gate A marked open until its explicit closure criteria are met.
- [ ] Check local links, Markdown math, navigation, and build warnings.
- [ ] Preserve negative results and old workflow records.
- [ ] Do not describe a site as live until its deployment URL and deployment workflow have been verified.
- [ ] Keep the main RFT-SIRM portal intact; link to it instead of replacing it.