# SFE-GEO-H001 — Historical Hindcasting Protocol (30 Ma to Present)

**Status:** Protocol published; numerical hindcast not yet executed. **No SFE predictive validation is claimed.**

## Research question
Can a physically constrained, seeded stochastic evolution model initialized at approximately 30 Ma recover independently observed aspects of the modern Pacific–North America plate boundary and regional topography without using withheld future observations?

## Established evidence and methods
- GPlates / GPlately can reconstruct plate rotations, plate boundaries, motion paths, and raster features through geological time. https://github.com/GPlates/gplately
- Furlong et al. (2024) document the role of Mendocino triple-junction migration in the transition from convergence to translation. DOI: https://doi.org/10.1029/2023TC007963
- USGS: https://www.usgs.gov/publications/formation-and-evolution-pacific-north-american-san-andreas-plate-boundary-constraints
- NOAA ETOPO global relief is a present-day endpoint reference, not historical initial topography: https://www.ncei.noaa.gov/products/etopo-global-relief-model

## Scientific integrity
1. Identify data used to construct the 30 Ma initial state; separately identify withheld validation data. Plate reconstructions often assimilate later observations, creating potential leakage.
2. Specify plate kinematics, continuum/rheology, surface processes, spatial and temporal discretization, boundary conditions, and conservation checks.
3. Use random seeds **only to explore candidate trajectories**, never to decide whether a physical claim is true.
4. Reject, repair, or explicitly flag physically inadmissible states.
5. Publish failures, uncertainty, and comparisons against deterministic and conventional ensemble baselines.

## Proposed state evolution
```text
X~_(t+dt) = Phi_SFE(X_t, H_t, epsilon_t)
X_(t+dt)  = C_geo(X~_(t+dt))
```
Here C_geo is a documented numerical admissibility operator. It is not itself proof of geophysical validity.

## Evaluation metrics
For comparable plate-boundary regions, use intersection-over-union (IoU) or symmetric-difference area; for topography, RMSE only where independently defensible reference elevations exist. Also report plate-motion errors, conservation residuals, calibration/coverage, invalid trajectories, runtime, and sensitivity.

```text
E_area = area(G_pred symmetric_difference G_ref) / area(G_pred union G_ref)
RMSE_Z = sqrt(mean((Z_pred-Z_ref)^2))
```

## Milestones
- H001-A: verify GPlates historical reconstructions and independently available evidence.
- H001-B: reproduce a known deterministic reference before introducing stochastic forcing.
- H001-C: execute a fixed-seed, preregistered SFE ensemble and competing baselines.
- H001-D: publish paired mathematics and maps: historical seed, evolved result, observed endpoint, and error/uncertainty maps.
- H001-E: assess whether SFE adds value beyond established methods.

## Status of earlier figures
Existing +50 Ma and +100 Ma SFE maps are conceptual illustrations, **not validated simulation outputs**. Any stated run counts, seeds, or likelihoods shown on conceptual artwork must not be interpreted as measured results.

## Public audit
This protocol belongs to the SFE 100-query scientific-integrity audit ledger. No completed 100-query audit is claimed here.
