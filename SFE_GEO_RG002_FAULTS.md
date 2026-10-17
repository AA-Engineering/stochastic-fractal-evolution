# SFE-GEO-RG002 — Fault-Controlled Westward Drainage Hypotheses

**Status: literature-grounded conceptual scenarios, NOT an executed DEM/tectonic SFE simulation.**

## Question

Could inherited fault and fracture structures favor westward drainage integration from the Pecos basin, across Estancia, through Tijeras Canyon, and into the Rio Grande?

## Evidence and limits

1. Tijeras–Cañoncito fault system (~100 km) links the Española and Albuquerque rift regions. Paleoseismic observations near Golden document two fault strands and a deflection of a west-flowing arroyo; this is local structural influence, **not** proof of Pecos capture. https://nmgs.nmt.edu/publications/guidebooks/details.cfml?ID=18318
2. Tijeras fault mapping describes NE-striking steep faulting, complex fractures, and differential Sandia–Manzanita block rotation. https://nmgs.nmt.edu/meeting/abstracts/view.cfm?aid=1834
3. Sandia and Hubbell Spring fault systems include down-to-west normal faulting along the Albuquerque Basin margin. https://www.sandia.gov/app/uploads/sites/165/2022/09/2021_ASER_NM.pdf
4. The Sandia Mountains are an east-tilted fault block; the Tijeras rift belt has graben/horst structural components. https://geoinfo.nmt.edu/publications/monographs/memoirs/29/home.cfm
5. The Pecos western drainage divide extends through Gallinas/Pedernal/Glorieta uplands. This barrier must be explicitly resolved; no throughgoing low corridor is established. https://www.usgs.gov/publications/solution-phenomena-pecos-basin-new-mexico
6. Mapping of faults in Albuquerque Basin: https://geoinfo.nmt.edu/publications/maps/geologic/gm/78/

## Competing SFE scenarios (unranked; no assigned probabilities)

- **A. Fault-guided headward erosion:** west-draining tributaries exploit fractured rock near Tijeras, with capture only if the eastern divide is also breached.
- **B. Differential uplift/subsidence:** plausible spatially varying deformation shifts divides, possibly toward or away from the Rio Grande.
- **C. Structural inheritance without capture:** fault-controlled Tijeras drainage persists but the Estancia closed basin and Pecos divide remain barriers.
- **D. Alternative corridor:** a different pass north/south of Tijeras captures drainage first.
- **E. Internal Estancia integration only:** Estancia develops an outlet toward Tijeras without capturing the Pecos.

## Physics and mathematical formulation

Use measured DEM Z0 and mapped geology/fault geometry. A schematic landscape evolution equation is:

```text
dZ/dt = U(x,y,t) - K(x,y) A(x,y)^m |grad Z|^n + D laplacian(Z)
K_i(x,y) = K0(x,y) exp(alpha S_fault(x,y) eta_i(x,y))
```

- U: uplift/subsidence inferred from a calibrated tectonic model.
- S_fault: susceptibility based on **mapped fault damage zones, lithology, and uncertainty**, not merely distance to a line.
- eta_i: recorded Mandelbrot-derived field, used as a hypothesis about spatial parameter heterogeneity.
- Fault weakness does not itself set river flow direction; drainage must be recomputed from modeled terrain, with physically consistent base levels.
- Erosion, deposition, tectonic strain, and mass balance require unit-consistent calibration.

For each realization require a continuous downstream Pecos-to-Rio Grande path through the stated corridor. Report `N_capture/N_valid` only after executing and validating the ensemble. **No capture probability, timescale, or westward forcing rate has been calculated.**

## Tests that distinguish hypotheses

1. Acquire USGS 3DEP DEM and New Mexico Bureau of Geology fault GIS layers, with CRS, resolution, and provenance.
2. Compute actual lowest divide saddles and minimum required incision along Tijeras, northern, and southern alternatives.
3. Use structural cross-sections and geophysics to assess faults, damage zones, and signs of differential vertical motion.
4. Run matched deterministic, Gaussian-correlated, and Mandelbrot-seeded SFE scenarios, including a no-fault-susceptibility ablation.
5. Check river profile monotonicity, sediment mass balance, basin outlet formation, timestep convergence, and seed reproducibility.
6. Compare with independent geological evidence of past drainage reorganizations.

## Falsification

Reject the Tijeras capture hypothesis under a tested parameter envelope if no admissible trajectories can breach the necessary divides, or if another corridor consistently dominates. Failure to simulate capture is conditional on model assumptions, not a proof that capture is impossible in all futures.

## Visual requirements

Every numerical output must show governing equations, initial fractal seed, actual terrain data, hypothetical evolved topography, fault overlays, and uncertainty. Earlier illustrated scenarios remain **conceptual art**, not numerical results.
