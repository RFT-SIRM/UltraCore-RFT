# Research Map and Evidence Boundaries

**Purpose:** provide one historically cautious map of the RFT-SIRM research ecosystem without changing the execution architecture or treating distinct research claims as interchangeable.

## The seven-step transition plan

These steps describe the documentation and evidence transition. They do not imply that every scientific conjecture is proved.

1. **Preserve the existing architecture.** UltraCore remains the coordination hub for deterministic execution, SIRM runtime invariants, implementation repositories, and verification practice. This documentation pass does not redesign the runtime.
2. **Separate the claim classes.** Mark each statement as a formal theorem, reproduced numerical result, engineering result reported by its source repository, research hypothesis, or open problem.
3. **Anchor the mathematical theorem to its exact scope.** Evgeny's Theorem concerns a specified noncommutative SU(2)-connection operator on Sierpiński-gasket graphs and its commuting control, for the fourth-moment trace defect. It is not a general proof of all RFT claims.
4. **Keep higher moments distinct.** The finite-level Fourier coefficients for selected higher-moment residuals have their own modular/CRT certificate. The all-level recurrence remains open and must not be presented as a consequence of the fourth-moment theorem.
5. **Separate the sibling research strands.** Phi-Genesis, RFT-QPU-Sierpinski, and RFT-Invariant-Battery have different goals and evidence standards. Links between them express research context, not automatic mathematical implication.
6. **Make navigation and visual hierarchy consistent.** Keep a restrained set of top-level links; place detailed badges, tables, methods, and historical notes inside the relevant sections or documents.
7. **Run a source-and-build audit before release.** Check relative links, repository names, formula delimiters, workflow evidence, and MkDocs navigation. Record failures instead of silently weakening claims or validation thresholds.

## Research strands

| Strand | Primary source | What is supported | Boundary |
| --- | --- | --- | --- |
| Deterministic execution and SIRM | [UltraCore-RFT](https://github.com/RFT-SIRM/UltraCore-RFT), [Rift-L1-Blockchain](https://github.com/RFT-SIRM/Rift-L1-Blockchain), [Rift-Network](https://github.com/RFT-SIRM/Rift-Network) | Runtime invariants, implementation-specific tests, fuzzing, and deployment evidence reported by each project | Runtime evidence does not prove a separate spectral identity |
| Fourth-moment spectral theorem | [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) | For the specified operators and assumptions, the fourth-moment trace defect is stated as the closed form below; the repository reports a Lean 4 formalization for all graph levels (m\ge1) | This is a specific operator identity, not a universal physical theory or a proof about all moments |
| Higher-moment Fourier analysis | [Coefficient candidates](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_COEFFICIENT_CANDIDATES.md), [modular certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md) | Exact finite-level coefficients for the stated residuals, subject to the certificate's construction and bounds | The proposed all-level recurrence remains an open conjecture |
| Spectral mass-formula audit | [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) | Computational claims are tested, rejected, or labelled open in that project's evidence record | A spectral fit or invariant does not become a physical mass law without independent derivation and validation |
| Quantum-processing architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | A pre-experimental architecture exploring Sierpiński connectivity and SU(2) transport | No quantum speed-up, hardware advantage, or circuit-cost result is implied |
| Invariant-driven energy model | [RFT-Invariant-Battery](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) | Exploratory deterministic scenarios with stated assumptions and auditable outputs | Model outputs are not independent experimental validation of a battery technology |
| Kernel stress-verification | [seL4 report](../SEL4_CDT_FUZZING.md), [field-trial report](field_trials_sel4.md) | Complementary stress-testing of a specific seL4 subsystem | Fuzzing does not replace or extend the kernel's formal proof |

## Mathematical anchor: fourth-moment trace defect

For the operator definitions and assumptions documented by the source project, the fourth-moment identity is

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16\left(3^{m-1}+1\right)\sin^2\left(\frac{\theta}{2}\right),
\qquad m\ge1.
$$

With the normalization used in the theorem documentation,

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3},
\qquad
\lim_{m\to\infty} I_m(\theta)
=-\frac{16}{9}\sin^2\left(\frac{\theta}{2}\right).
$$

In particular, at $\theta=\pi/2$, the limiting value is \(-8/9\). The normalized value is a spectral anchor used by related exploratory work; it does not by itself establish a quantum-computing advantage or a physical law.

## Claim-status vocabulary

Use these labels consistently in this repository and its linked research summaries:

- **Formal theorem:** a precisely stated result established by a checked proof in the stated formal system and scope.
- **Numerically reproduced:** computation agrees with a stated prediction on specified inputs; this is not, by itself, a proof for all inputs.
- **Engineering-tested:** tests, fuzzing, or deployment checks support an implementation-specific claim.
- **Hypothesis:** a plausible interpretation or proposed extension awaiting decisive validation.
- **Open:** a required derivation, proof, independent replication, or experiment has not yet been completed.
- **Not claimed:** an explicit boundary preventing readers from inferring a stronger result than the evidence supports.

## Release checklist

Before changing the public overview or publishing a new research status:

- [ ] Confirm the theorem and its assumptions against the primary theorem repository.
- [ ] Confirm every numerical metric against a dated run, report, or reproducible artifact.
- [ ] Keep fourth-moment theorem claims separate from higher-moment conjectures.
- [ ] Check all local links against the actual repository tree.
- [ ] Check GitHub Markdown math in both inline and display form; use display blocks only for equations that benefit from a separate line.
- [ ] Build the MkDocs site and inspect warnings before merging.
- [ ] Preserve the commit history and record unresolved issues rather than rewriting historical status.
