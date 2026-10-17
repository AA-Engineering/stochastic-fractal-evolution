# SFE-GEO External Research Collaboration and Validation Roadmap

**Status:** Open call for independent scientific critique; no demonstrated SFE predictive advantage.

## Research question

Can a reproducible, physically constrained stochastic-ensemble framework improve the calibration, diversity, or efficiency of North American plate-evolution scenarios relative to established geodynamic and plate-reconstruction approaches?

## Prior-art anchors

- GPlates: https://www.gplates.org/
- GPlately: https://github.com/GPlates/gplately
- GPlately documentation: https://gplates.github.io/gplately/
- NOAA ETOPO: https://www.ncei.noaa.gov/products/etopo-global-relief-model

The GPlately project already reconstructs geological features and rasters through time and supports comparisons between plate models. SFE must demonstrate a benefit beyond these established capabilities.

## Collaboration opportunities

1. **Plate reconstruction:** independent 30 Ma initial state, plate rotations, topology and withheld observations.
2. **Geodynamics:** physically defensible constitutive and boundary-condition choices.
3. **Uncertainty quantification:** fair baseline ensembles, calibration, coverage and sensitivity.
4. **Numerical methods:** convergence tests, matrix conditioning, and constraint residuals.
5. **Geomorphology:** topographic evolution, erosion and drainage capture.
6. **Visualization:** paired governing equations and maps derived from actual computed state arrays.
7. **Adversarial review:** identify data leakage, incorrect physics, prior art, or overclaiming.

## Benchmark sequence

- Reproduce an exact deterministic or stochastic known-answer case.
- Compare GPlates-derived historical reconstructions with independently withheld observations.
- Construct deterministic and conventional random-field ensemble baselines.
- Introduce SFE transition classes with recorded seeds and ablation controls.
- Evaluate at 30 Ma-to-present before +100 Ma forecasting.
- Publish all outcomes, including null/negative results.

## Required evidence for any reported result

- Source code, dependencies, version and commit.
- Data provenance, units, coordinates and licensing.
- Initial conditions, boundaries and rheology.
- Random generator, seeds, transition distribution.
- Constraint residuals and numerical error.
- Comparison against the same-data, same-budget baseline.
- Maps of the initial seed, modeled topology, reference topology and uncertainty.

## Public communication

Researchers are invited to open a GitHub issue or pull request with a critique, replication, relevant reference, or benchmark implementation. This invitation does not imply endorsement by GPlates, EarthByte, USGS, NOAA, Zenodo, or any outside researcher.

No outreach to third parties has been sent as part of this document. Human researchers should review external communication before sending it.

## Publication status

GitHub is public. Zenodo integration is not verified, and no DOI has been confirmed. The repository has `.zenodo.json` and `CITATION.cff`; Zenodo's documentation says `.zenodo.json` takes precedence when both exist.

Official Zenodo integration steps: https://help.zenodo.org/docs/github/enable-repository/
