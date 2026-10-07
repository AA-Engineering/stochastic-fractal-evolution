# Reproducibility Standard

Every SFE experiment should archive enough information to reproduce an individual trajectory and the ensemble.

Minimum record:

- software/version/commit;
- initial state and source data;
- pseudorandom number generator;
- random seed(s);
- transition classes and probabilities;
- stochastic-field generator and parameters;
- constraint operator;
- timestep and number of steps;
- spatial/temporal resolution;
- parameter values and units;
- rejection/projection behavior;
- output metrics;
- hardware/software dependencies when relevant.

## Seed ledger

Each run should receive a stable run identifier and preserve its seed. Published figures should identify the run(s) or ensemble that generated them.

## Human-evaluable visual state

For visual SFE experiments, every evolution should retain/display the initial or inherited fractal seed together with the resulting state so a human reviewer can evaluate the relationship between seed and evolution.

## Ensemble reporting

Report total attempted runs, valid runs, rejected runs, convergence criteria, and uncertainty intervals. Do not present ensemble frequency as empirical real-world probability without external calibration.
