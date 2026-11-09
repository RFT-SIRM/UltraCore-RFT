---
title: "Phi-Genesis Daily Computational Verification"
description: "Daily high-cost spectral matrix computations, Schur interval certificates, and deep statistical audits reproduced by UltraCore-RFT from the canonical Phi-Genesis source."
keywords:
  - Phi-Genesis
  - daily spectral computation
  - dense level-nine eigensolve
  - high-precision A1 E sectors
  - Schur interval inertia certificate
  - reproducible CI
---

# Phi-Genesis Daily Computational Verification

UltraCore-RFT mirrors the computational verification workload of [Phi-Genesis](https://github.com/RFT-SIRM/Phi-Genesis) as a first-class part of this research hub. The runs use the **canonical Python source from Phi-Genesis `main`**; the algorithms and tests are not forked or copied into this repository.

Each run records both the UltraCore-RFT commit and the exact Phi-Genesis commit it checked out. Logs and provenance files are retained as downloadable GitHub Actions artifacts.

## Daily schedules

<div class="grid cards" markdown>

-   **Nightly deep verification**

    ---

    **00:00 UTC every day**

    The marked deep-test suite, including the level-9 dense spectral calculation and statistical / decimation audits.

    [Open workflow](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/phi-genesis-nightly-deep.yml) · [View all runs](https://github.com/RFT-SIRM/UltraCore-RFT/actions?query=workflow%3A%22Phi-Genesis+Nightly+Deep+Verification%22)

-   **High-precision spectral matrix**

    ---

    **03:00 UTC every day**

    A1 level 9, A1 level 10, E level 9, plus independent Schur interval / derivative certificates.

    [Open workflow](https://github.com/RFT-SIRM/UltraCore-RFT/actions/workflows/phi-genesis-high-precision.yml) · [View all runs](https://github.com/RFT-SIRM/UltraCore-RFT/actions?query=workflow%3A%22Phi-Genesis+High-Precision+Spectral+Matrix%22)

</div>

The schedules match the corresponding daily source workflows in Phi-Genesis. They are separate GitHub Actions runs: a pass in one repository does not automatically certify the other repository's workflow or prove a mathematical statement beyond the assertions actually executed.

## 1. Nightly deep suite

The source workflow is `nightly-deep-tests.yml`; UltraCore-RFT checks out Phi-Genesis and runs:

```bash
pytest -v -s -m nightly
```

The suite currently selects eight deep tests from the source test collection. The checks include:

- Construction of the level-9 Sierpiński-gasket graph: **29,526 vertices and 59,049 edges**.
- An attempted full dense eigendecomposition of the level-9 graph Laplacian.
- A Gate E statistical null sweep over 20 million random index quadruples for each configured search bound.
- Gate A matched-pair and machine-precision residual diagnostics.
- Spectral-window summaries at levels 8 and 9.

A successful historical run on 9 November 2026 completed in 47 minutes 26 seconds. The level-9 dense eigensolve itself completed in 1,282 seconds on that run. The test records the outcome; it does not assert that every runner will have the same memory/time characteristics.

[Historical source run — 9 November 2026](https://github.com/RFT-SIRM/Phi-Genesis/actions/runs/42563349435) · [Canonical source test](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/test_nightly_deep.py).

## 2. High-precision spectral matrix

The matrix workflow runs three independent jobs in parallel using:

```text
Python 3.12
mixed-precision working precision: 360 decimal digits
sparse linear solve target:        210 decimal digits
inverse iterations:                250
progress output:                   every 20 iterations
```

| Sector | Graph level | Full graph dimension | Symmetry-sector dimension |
|---|---:|---:|---:|
| A1 | 9 | 29,526 | 4,926 |
| A1 | 10 | 88,575 | 14,768 |
| E | 9 | 29,526 | 9,842 |

These calculations resolve extremely close low spectral modes that ordinary float64 single-vector iteration can collapse. The A1 and E jobs are different symmetry sectors of the same specified graph-matrix family. The output is a high-precision numerical calculation with residual diagnostics; it is not, by itself, an interval proof or an infinite-level convergence theorem.

A verified historical high-precision run completed in about 124 minutes overall. The E-sector level-9 calculation was the dominant job, with a reported computational elapsed time of about 7,394 seconds. The [source Actions run](https://github.com/RFT-SIRM/Phi-Genesis/actions/runs/42172777291) retains the original logs and artifacts.

**Canonical code:** [symmetry_sector_bottom.py](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/symmetry_sector_bottom.py) · [source workflow](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/.github/workflows/spectral-gap-high-precision.yml).

## 3. Schur interval certificates

The high-precision workflow also runs two outward-rounded interval computations directly from the Phi-Genesis source.

### Finite-level Schur / inertia certificate

```bash
python computational/spectral_gap_theta_2pi/schur_inertia_certificate.py --max-level 12 --dps 2450 --radius-digits 2390
```

This checks the A1 ground-state root and E doublet through finite levels 1–12, including root brackets, derivative signs, and positive midpoint pivots. Its scope is a finite-level computer-assisted interval/inertia certificate, not a Lean-kernel theorem and not an infinite-level limit proof.

### Schur derivative-transition certificate

```bash
python computational/spectral_gap_theta_2pi/schur_derivative_certificate.py --max-level 14 --start-level 5 --dps 10000 --radius-digits 9400
```

This certifies the specified finite transitions 5 through 13 using interval arithmetic at 10,000 decimal digits. It provides estimates relevant to the proposed quadratic increment law; it does **not** prove that law for all levels or establish a global limiting coefficient.

**Canonical code:** [Schur inertia certificate](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/schur_inertia_certificate.py) · [Schur derivative certificate](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/schur_derivative_certificate.py) · [Schur proof map](https://github.com/RFT-SIRM/Phi-Genesis/blob/main/computational/spectral_gap_theta_2pi/PROOF_MAP.md).

## Provenance and evidence boundary

Every UltraCore-RFT run:

1. Checks out the current `main` of Phi-Genesis into a dedicated `phi-genesis/` directory.
2. Records the exact source commit SHA and the UltraCore-RFT workflow commit SHA.
3. Runs the original source commands without modifying the source repository.
4. Uploads text logs and the provenance record as workflow artifacts, retained for 30 days.

A workflow pass means that the selected command completed successfully for the checked-out revisions and runner environment. It does not upgrade numerical evidence into a Lean theorem, close Gate A, prove the quadratic increment law, or identify the graph matrix with an external physical operator.

The formal results and open questions remain in the [Phi-Genesis research record](https://github.com/RFT-SIRM/Phi-Genesis) and the [UltraCore mathematical results register](results.md).

---

**Evidence first. Preserve the source, the configuration, the commit, and the full run log.**
