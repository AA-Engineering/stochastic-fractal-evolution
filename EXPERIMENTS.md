# SFE Experiments

## Experiment 0 — Fractal visual laboratory

Purpose: make transition classes directly observable to humans.

Each evolution displays the current fractal seed alongside the evolved state. Random seeds and parameters are retained so every frame can be reproduced.

Primary measurements:

- evolutionary distance;
- continuity/discontinuity;
- structural persistence;
- bifurcation frequency;
- restart frequency.

## Experiment 1 — Geophysical microdomain

### Objective

Test constrained SFE on a deliberately small drainage/topography system before increasing model complexity.

### Candidate domain

Tijeras-Estancia-Pecos region, New Mexico.

### v0.1 state variables

- elevation/topography;
- prescribed uplift/subsidence;
- fault-controlled susceptibility;
- deterministic erosion;
- deposition;
- drainage direction/network;
- stochastic multiscale perturbation.

Climate variability, vegetation, groundwater, sea-level variation, volcanism, and other secondary stochastic subsystems are reserved for later versions.

### Conceptual update

```text
Z*_(t+1) = C[
    Z_t
    + U_t
    - S_t
    - E(Z_t)
    + D_t
    + epsilon_t S_geo
]
```

Drainage is then recomputed from the constrained terrain, conceptually following gravitational descent:

```text
q_(t+1) proportional to -grad Z*_(t+1)
```

### Ensemble experiment

Run many independently seeded trajectories while retaining all seeds. Measure:

- drainage reorganization;
- divide migration;
- stream capture;
- uplift/subsidence persistence;
- invalid/rejected states;
- attractor density.

For a capture event:

```text
P_model(capture) = N_capture / N_valid
```

This is an empirical frequency **within the model**, not automatically a real-world probability.

### Initial outputs

1. initial terrain;
2. ensemble-mean final terrain;
3. drainage/capture frequency map;
4. geological-attractor density map.

### Baselines

Compare against deterministic evolution, conventional Monte Carlo perturbation, and at least one established spatial stochastic/random-field approach.
