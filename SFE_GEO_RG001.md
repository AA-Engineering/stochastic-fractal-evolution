# SFE-GEO-RG001 — Rio Grande–Pecos Capture via Tijeras Canyon

**Status:** Conceptual scenario and falsifiable research protocol; no DEM-derived simulation has yet been executed.

## Hypothesis

Could westward drainage integration through Tijeras Canyon, combined with divide erosion across the Estancia Basin and eastern uplands, allow part or all of the upper Pecos drainage to be captured by the Rio Grande in a future geological epoch?

**Crucial geographic fact:** The Estancia Basin is internally drained and lies between the Rio Grande and Pecos basins. Tijeras Arroyo drains west to the Rio Grande. A complete capture therefore requires a connected route across multiple divides; opening Tijeras Canyon alone is insufficient.

## Established evidence

- USGS Tijeras Arroyo station and Rio Grande drainage: https://waterdata.usgs.gov/monitoring-location/USGS-08330600/
- USGS classification of Estancia as a closed basin: https://water.usgs.gov/GIS/huc_name.html
- Morgan (1942), Pecos basin drainage divides including Pedernal and Glorieta: https://doi.org/10.1029/TR023i001p00027
- USGS Rio Grande basin integration history: https://www.usgs.gov/publications/geomorphic-evolution-san-luis-basin-and-rio-grande-southern-colorado-and-northern-new

## SFE formulation

Use a physically calibrated landscape evolution model:

```text
dz/dt = U - K A^m |grad(z)|^n + D laplacian(z)
K_i(x,y) = K0(x,y) exp(alpha * S_geo(x,y) * eta_i(x,y))
```

where `eta_i` is a normalized Mandelbrot-derived spatial perturbation with recorded seed and parameters. Physical parameters and units must be calibrated before interpreting results.

**Do not use fractal image pixels as terrain elevation.** The fractal modulates uncertain material/process parameters only.

## Planned validation

1. Acquire USGS 3DEP DEM, mapped drainage and fault/geologic units for Albuquerque–Tijeras–Estancia–Pedernal/Glorieta–Pecos.
2. Derive actual flow routing, drainage divides and candidate lowest passes.
3. Determine minimum divide incision and base-level gradients along each candidate route.
4. Run deterministic, Gaussian-field, correlated-field, and Mandelbrot-seeded ensembles with matched statistics and computational budgets.
5. Apply physical constraints, reroute drainage after each valid step, and track the emergence of connected westward paths.
6. Report capture frequencies as **model-conditioned frequencies**, not calibrated real-world probabilities.
7. Compare alternative corridors north and south of Tijeras; do not assume Tijeras is optimal.

## Capture criterion

A trajectory counts as capture only when a continuous downstream drainage path from a defined Pecos source region reaches the Rio Grande through the target corridor, without internal sinks or uphill routing under the selected flow model.

```text
P_model(capture) = N_capture / N_valid
```

No probability or capture time is currently estimated.

## Visual interpretation

The associated conceptual figure shows present drainage and a hypothetical two-divide capture route through Estancia and Tijeras. It is **not a georeferenced DEM product**, numerical SFE run, or prediction. Locations, elevation profile and geometry must be replaced by computed and verified GIS outputs.

## Scientific controls

- Fixed climate for v0.1, with explicit erosion assumptions.
- No unconstrained tectonic deformation.
- Record seeds, model code, spatial resolution, uncertainty, rejected states, and validation evidence.
- Preserve the original fractal seed and show governing equations alongside every future map.
- Publish negative results if the corridor is not viable.

## Preliminary assessment

The scenario is testable, but no evidence yet establishes that the Rio Grande will capture the Pecos through Tijeras. The major obstacle is achieving a continuous physically plausible path through multiple present drainage divides.
