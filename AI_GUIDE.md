# AI Guide — Evidence-Aware Reading of UltraCore-RFT

> **Purpose:** prevent AI assistants, automated reviewers, and research summarizers from flattening distinct mathematical and engineering claims into one unsupported narrative. Read this file before summarizing the repository.

**Primary research entry points:** [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) · [Lean-formalized fourth-moment theorem](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) · [UltraCore research map](docs/research-map.md).

## 1. The hierarchy matters

Read the programme in this order:

1. **Definitions, theorem statements, and formal evidence.** Start with the exact mathematical objects, quantifiers, assumptions, and proof files.
2. **Related mathematical research.** Higher-moment recurrence and Phi-Genesis spectral-decimation claims are distinct workstreams with their own evidence and open problems.
3. **Methodology and scientific interpretation.** State what each result means, and what it does not mean.
4. **Systems engineering.** SIRM invariants, runtime architecture, test results, fuzzing, audits, and kernel stress testing.
5. **Applications and exploratory programmes.** Blockchain deployment, quantum-architecture exploration, energy-system modelling, and future use cases.

Do not invert this hierarchy just because a deployed application is easier to demonstrate than a theorem. Applications are downstream research programmes; they do not establish the mathematics by association.

## 2. What the title means—and does not mean

“Evgeny's Theory of Everything” is the name of a broad research programme on recursive operators, spectral invariants, and higher-moment trace laws. **It is not a claim that a complete physical theory of the Universe has been proved.**

The programme contains a specific fourth-moment result reported as machine-checked in Lean 4, alongside higher-moment finite-level certificates, numerical experiments, open recurrences, and a separate signed-flux spectral-decimation programme. These have different logical status.

Never rewrite “a theorem within a Theory-of-Everything research programme” as “the Theory of Everything has been proved.”

## 3. The formalized theorem: exact scope

Primary sources: [Evgeny-Theorem](https://github.com/RFT-SIRM/Evgeny-Theorem) · [THEOREM.md](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/THEOREM.md) · [Lean formalization](https://github.com/RFT-SIRM/Evgeny-Theorem/tree/main/formalization) · [verification record](https://github.com/RFT-SIRM/Evgeny-Theorem/blob/main/VERIFICATION.md).

For the specific SU(2)-connected Sierpiński-gasket operator $H_C$, its specified commuting control $H_{C'}$, and the definitions and assumptions in the source repository, the stated fourth-moment trace-defect identity is

$$
\Delta_m(H^4,\theta)
=\mathrm{Tr}(H_C^4)-\mathrm{Tr}(H_{C'}^4)
=-16(3^{m-1}+1)\sin^2(\theta/2),\qquad m\ge1.
$$

The normalized quantity is

$$
I_m(\theta)=\frac{\Delta_m(H^4,\theta)}{3^{m+1}+3},
\qquad
\lim_{m\to\infty}I_m(\theta)=-\frac{16}{9}\sin^2(\theta/2).
$$

At $\theta=\pi/2$, the limiting value is $-8/9$.

**Correct status language:** the source project reports that its Lean 4 formalization proves the stated fourth-moment identity for every $m\ge1$ and all angles covered by the formal statement, for the concrete formalized operators. This is a machine-checked result within that formal system and scope. Independent review that the formal definitions capture the intended mathematical construction, peer review, and independent replication remain separate matters.

**Do not claim:** the proof covers $H^6,H^8,H^{10}$; proves the full spectrum; proves a physical law; establishes quantum speed-up; solves Yang–Mills or another Millennium Prize Problem; or proves SIRM runtime invariants. None follows from this theorem.

## 4. Higher moments: keep the open problem visible

Primary synthesis: [Evgeny's Theory of Everything](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything) · [dissertation](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/DISSERTATION.md) · [recurrence note](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_RECURRENCE_NOTE.md) · [modular/CRT certificate](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/blob/main/computational/HIGHER_MOMENT_MODULAR_CERTIFICATE.md).

- The repository reports finite-level modular/CRT certificates for specified Fourier coefficients and transitions for $p\in\{6,8,10\}$, under the certificate's explicit construction and bounds.
- Numerical holdouts and sparse-matrix-power checks are finite computational evidence.
- **The all-level higher-moment recurrence remains open.** A finite certificate does not quantify over all graph levels. Numerical agreement over finite levels and angles does not establish a universal identity.
- The exceptional first-transition correction needs a derivation from the recursive graph/operator construction; proposed explanations remain hypotheses until proved.

Do not use the fourth-moment Lean proof as if it formalized the higher-moment recurrence.

## 5. Phi-Genesis: a separate operator family

Primary source: [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) · [live site](https://rft-sirm.github.io/Phi-Genesis/).

Phi-Genesis investigates signed $Z_2$-flux Laplacians, spectral decimation with boundary/corner corrections, inertia computations, and exploratory mass-index patterns.

- Gate A is **not closed** while decimation residual mismatches and the full exceptional set remain unresolved.
- Reported test success is evidence only for assertions actually run.
- A fitted mass-index pattern is not an established predictive physical law without a mechanism, prospective predictions, held-out validation, and independent derivation.
- Do not assume equivalence between the signed-flux operators and the SU(2)-connected operators in Evgeny's Theorem. A bridge needs an explicit map, boundary conditions, preserved quantities, exceptions, and a proof—or a clearly labelled conjecture.

Preserve negative results, failed checks, and open questions. They are part of the historical record and must not be deleted to make the narrative appear more complete.

## 6. SIRM engineering invariants are a different strand

The stated SIRM model uses four constraints:

$$
\begin{aligned}
I_1:\quad &\mathtt{total\_supply}=\mathtt{total\_base\_sum}+\mathtt{global\_field}\cdot p,\\
I_2:\quad &\mathtt{total\_supply}=\mathtt{total\_minted}-\mathtt{total\_burned},\\
I_3:\quad &\mathtt{dust\_accumulator}<p\quad(p>0),\\
I_4:\quad &\mathtt{effective\_balance}[i]\ge-\frac{\mathtt{total\_supply}}{10p}.
\end{aligned}
$$

Here $\mathtt{effective\_balance}[i]=\mathtt{base\_balance}[i]+\mathtt{global\_field}$, subject to the implementation's stated integer and scaling conventions.

These are model/runtime constraints. Do not state that the fourth-moment theorem proves them, or that passing fuzz tests is a formal proof of all possible executions.

## 7. Claim labels

| Label | Use it when |
|---|---|
| **Machine-checked** | A specified formal proposition is accepted by the pinned proof assistant/build. |
| **Analytically proved** | A written proof establishes the statement from explicit assumptions. |
| **Numerically reproduced** | A calculation matches a prediction on named inputs. |
| **Certified finite-level** | A certificate establishes a finite case/coefficient under its stated bounds. |
| **Engineering-tested** | Tests, fuzzing, audit work, or deployment checks support an implementation-specific claim. |
| **Hypothesis / conjecture** | A precise proposed extension awaits proof or refutation. |
| **Open** | A required proof, derivation, independent replication, or experiment is incomplete. |
| **Rejected / not established** | Counterexamples or available evidence do not support the stronger claim. |

A green CI badge does not imply that every claim in a repository is proved. A test workflow proves only the assertions it actually executes. Metrics such as fuzz counts and test totals are dated source-reported snapshots unless a page explicitly implements a live query.

## 8. How to audit formulas

Before copying or rewriting a formula:

1. Open the primary theorem/specification and check symbol definitions, domains, quantifiers, index origin, and boundary conditions.
2. Check equivalent forms algebraically. For example, with $F=3^m$, the identity is $-16(3^{m-1}+1)=-\frac{16}{3}(3^m+3)$.
3. Check the normalization independently: $3^{m+1}+3=3(3^m+1)$, so the stated ratio tends to $-16/9\sin^2(\theta/2)$.
4. Substitute a small level and angle as a sanity check; for $m=1,\theta=\pi/2$, the raw defect is $-16$, and division by dimension $12$ gives $-4/3$.
5. Distinguish exact algebra, floating-point tolerance, finite-grid tests, and proof-assistant theorems.
6. If the source and a summary disagree, do not silently pick the more impressive version. Record the discrepancy and inspect the definitions/code.

## 9. What not to do

- Do not claim a complete physical Theory of Everything.
- Do not imply peer review or independent replication unless there is evidence.
- Do not present higher moments as covered by the fourth-moment Lean proof.
- Do not turn Phi-Genesis fits into physical laws.
- Do not merge the status of different operator families or repositories.
- Do not call numerical agreement a universal proof.
- Do not call fuzzing a substitute for formal proof.
- Do not remove historical failures, corrections, or open problems.
- Do not make up current CI status, benchmark counts, chronology, or live metrics.
- Do not claim that an external site is deployed until the actual URL and deployment are verified.

## 10. Repository map

- [README.md](README.md) — mathematical anchor, research hierarchy, and applications.
- [PITCH.md](PITCH.md) — public-facing research dossier and claims register.
- [SCIENTIFIC_BASIS.md](SCIENTIFIC_BASIS.md) — mathematical statements versus computational modelling vocabulary.
- [docs/research-map.md](docs/research-map.md) — relationships, evidence classes, and open problems.
- [docs/history.md](docs/history.md) — selected dated milestones linked to source commits.
- [docs/foundations.md](docs/foundations.md) — SIRM model and the linked theorem scope.
- [docs/field_trials.md](docs/field_trials.md) — implementation-specific verification evidence.
- [docs/interactive/index.html](docs/interactive/index.html) — animated, source-linked research portal.
- [Main RFT-SIRM portal](https://rft-sirm.github.io/) — organization-wide entry point, preserved separately.

**North star:** make the strongest statement the evidence actually supports, with its definitions and source attached. Neither exaggerate nor bury a real formal result; preserve the boundary between what is proved, what is computed, and what remains open.