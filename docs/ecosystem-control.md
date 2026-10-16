# Ecosystem Control Plane

UltraCore-RFT is the coordination and observability hub for the RFT-SIRM research and engineering programme. Phase one collects the latest public GitHub Actions run from each registered repository.

## Live report

Run the [Ecosystem Control Plane workflow](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/ecosystem-control.yml). Every run publishes a Markdown summary and downloadable JSON/Markdown artifacts. The collector runs every six hours and can also be started manually.

## Registered projects

| Project | Scope | Actions |
|---|---|---|
| UltraCore-RFT | Docs, Pages, coordination | [Runs](https://github.com/RFT-SIRM/UltraCore-RFT/actions) |
| Theory of Everything | Dissertation, recurrence audit, reference tests | [Runs](https://github.com/RFT-SIRM/Evgeny-s-Theory-of-Everything/actions) |
| Evgeny Theorem | Lean 4 formalization | [Runs](https://github.com/RFT-SIRM/Evgeny-Theorem/actions) |
| Phi-Genesis | Spectral computation, Gate A | [Runs](https://github.com/RFT-SIRM/Phi-Genesis/actions) |
| Rift Network | Network engineering | [Runs](https://github.com/RFT-SIRM/Rift-Network/actions) |
| Rift-L1 Blockchain | Blockchain engineering | [Runs](https://github.com/RFT-SIRM/Rift-L1-Blockchain/actions) |
| Agave Rift Scheduler | Scheduler CI and fuzz | [Runs](https://github.com/RFT-SIRM/agave-rift-scheduler/actions) |
| Aave V4 Hub model review | Model review and regression | [Runs](https://github.com/RFT-SIRM/aave-v4-hub-model-review/actions) |

## Status meanings

- **PASS** — only the latest reported workflow run succeeded.
- **FAIL** — latest run failed or timed out.
- **RUNNING** — latest run is incomplete.
- **CANCELLED / SKIPPED** — GitHub reported that conclusion.
- **NOT RUN / NOT FOUND / API LIMITED / ERROR** — no pass is implied; open the linked Actions page.

The report includes workflow, branch, commit prefix, timestamp, and source link. A repository-level status is not a universal verdict.

## Phase-one boundary

This is a **read-only monitor**, not yet a remote test dispatcher. Each project's tests continue to execute in its own CI. The collector does not write to upstream repositories or trigger arbitrary workflows. Cross-repository dispatch requires explicit workflow support and least-privilege permissions in participating repositories.

## Evidence boundaries

- Theory of Everything checks validate only the listed source checks; finite tests do not prove an all-level recurrence.
- Evgeny Theorem status is scoped to the Lean workflow and its checked propositions.
- Phi-Genesis numerical checks remain distinct from formal proof; Gate A's unresolved status must remain visible.
- Engineering CI, fuzzing, model review, and deployment evidence are separate classes and are not implied by the mathematical theorem.

The control plane exists to make these distinctions visible, not to flatten them into a misleading green badge.
