# RFT-SIRM Application Programmes: QPU/Sierpiński and Invariant Battery

**Purpose:** a source-linked, evidence-bounded index of two distinct RFT-SIRM application research tracks. This page records their place in the wider programme; it does not merge their implementations into UltraCore-RFT or certify their technical, commercial, or legal status.

[![RFT-QPU-Sierpinski](https://img.shields.io/badge/RFT--QPU--Sierpinski-Pre--experimental%20architecture-4f46e5?style=for-the-badge)](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)

[![RFT-Invariant-Battery](https://img.shields.io/badge/RFT--Invariant--Battery-Exploratory%20energy%20model-0f766e?style=for-the-badge)](https://github.com/RFT-SIRM/RFT-Invariant-Battery.)

[![Evidence boundary](https://img.shields.io/badge/Evidence-Model%20and%20research%20status-d97706?style=for-the-badge)](#evidence-and-claim-boundaries)

> **Reading rule:** the badges are navigation and status labels only. They are not certification marks, experimental results, patent-status indicators, or endorsements.

## 1. Where these programmes sit

UltraCore-RFT is the documentation and coordination hub. The two programmes below are downstream application research tracks with their own repositories, assumptions, code, tests, and licensing terms. They are **not corollaries of the fourth-moment theorem**, and no mathematical or engineering result should be transferred between them without an explicit derivation and evidence.

| Track | Primary source | Current description | What is not established by the repository description |
|---|---|---|---|
| Quantum-processing architecture | [RFT-QPU-Sierpinski](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski) | A proposed graph-based architecture using self-similar Sierpiński-gasket connectivity, SU(2)-valued edge transport, and a candidate two-dimensional logical subspace. The repository includes a minimal research simulator and a patent-oriented technical disclosure for counsel review. | A fabricated or experimentally validated device; fault tolerance; measured gate fidelity; universal noise protection; demonstrated quantum advantage or speed-up; patent grant or established patentability. |
| Energy-system model | [RFT-Invariant-Battery.](https://github.com/RFT-SIRM/RFT-Invariant-Battery.) | An invariant-driven state-transition model and reproducible vehicle/energy scenarios, with assumptions and CSV outputs described by the source repository. | A physically demonstrated 10,000-km battery; new cell chemistry; validated battery-management controller; safety certification; independently demonstrated energy savings; patent grant or established patentability. |

## 2. RFT-QPU-Sierpinski

The source repository proposes connecting self-similar graph geometry with non-Abelian SU(2) transport and projected logical controls. Its documentation describes a **pre-experimental architecture**, not a completed quantum processor.

The repository reports a minimal numerical core and lists a validation programme that includes logical-subspace isolation, leakage separation, projected-control independence, calibration sensitivity, disorder, thermal effects, readout, crosstalk, and scaling. These are validation obligations, not results that should be presumed complete.

- **Primary source:** [repository README](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski)
- **Technical disclosure:** [PATENT_SPEC.md](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/PATENT_SPEC.md)
- **Source-repository terms:** [LICENSE.md](https://github.com/RFT-SIRM/RFT-QPU-Sierpinski/blob/main/LICENSE.md)

The patent-oriented document is a technical disclosure for qualified counsel to review. It is not a legal opinion, a patent application receipt, a granted patent, or a conclusion that any claim meets novelty, inventive-step/non-obviousness, enablement, ownership, or other legal requirements.

## 3. RFT-Invariant-Battery

The source repository studies an invariant-gated state-transition pattern:

`measure → state → invariant gate → allowed transition → execute → verify`

It reports a 10,000-km vehicle/energy-system scenario under a deliberately high **1,500 Wh/kg pack-level energy-density research sweep**. The README reports 2.761 MWh for a baseline scenario, 3.205 MWh for an adverse scenario, and 2.716 MWh for a bounded-controller hypothesis. These are **model outputs under stated assumptions**, not measured pack performance or experimental proof of the controller's benefit.

- **Primary source:** [RFT-Invariant-Battery. repository](https://github.com/RFT-SIRM/RFT-Invariant-Battery.)
- **Source-repository terms:** [LICENSE.md](https://github.com/RFT-SIRM/RFT-Invariant-Battery./blob/main/LICENSE.md)

The project itself states that it has not established a physical 10,000-km battery, new cell chemistry, validated BMS controller, safety certification, or experimental benefit from invariant-driven control. This status must remain explicit in public descriptions.

## 4. Evidence and claim boundaries

Use these labels consistently across the programme:

- **Formal theorem:** a proposition proved in a specified formal system for its exact definitions and assumptions.
- **Numerically reproduced:** a computational result tied to named code, inputs, parameters, tolerances, and outputs.
- **Engineering-tested:** a claim supported by tests or experiments for a specified implementation and configuration.
- **Research architecture:** a proposed design whose key physical or operational requirements remain to be validated.
- **Modelled scenario:** an output of a model under declared assumptions; not a physical measurement.
- **Patent-oriented disclosure:** technical material organized for counsel review; not a statement of patent grant, patentability, priority, or freedom to operate.

A successful test suite, an attractive banner, a numerical fit, or a patent-oriented document cannot by itself promote a claim to a stronger evidence category. Report unresolved validation items rather than silently treating them as complete.

## 5. Attribution, licensing, and public-disclosure discipline

The two source repositories currently publish their own `LICENSE.md` files describing **Business 1.0 proprietary / all-rights-reserved terms**. Those terms are separate from the Apache-2.0 license for original UltraCore-RFT content.

Accordingly, this hub provides source links and short factual descriptions; it does not copy source code, figures, tables, or substantial passages from those repositories. The UltraCore-RFT license must not be read as relicensing upstream project materials. Permission to reuse third-party material must be checked against the relevant source license and, where necessary, obtained in writing from the rights holder.

Public GitHub publication is not a substitute for an IP strategy. Before making further disclosures or relying on a patent position, obtain qualified advice on ownership and inventorship, prior art, filing dates and jurisdictions, claim scope, enablement, licensing, confidentiality, and any applicable disclosure deadlines. This page is a documentation record, **not legal advice** and not a determination that any invention is patentable or protected.

No employment, partnership, institutional sponsorship, endorsement, regulatory approval, or commercial readiness is implied by inclusion in this index.

## 6. Maintenance checklist

- [ ] Keep each description synchronized with its primary repository and current evidence.
- [ ] Preserve the exact repository URL for the battery project, including the final period in its repository name.
- [ ] Keep model assumptions and experimental status beside any quoted numerical result.
- [ ] Do not imply that the fourth-moment theorem validates either application.
- [ ] Do not copy upstream proprietary implementation materials into UltraCore-RFT without confirming permission.
- [ ] Update these labels only when the underlying evidence changes.

---

*This index summarizes public repository documentation as a research-navigation aid. It is not an independent technical audit, legal opinion, patentability assessment, or investment recommendation.*
