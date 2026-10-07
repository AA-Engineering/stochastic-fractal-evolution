# SFE Benchmark Program

## Purpose

Determine whether SFE provides measurable value beyond established methods.

## Baseline families

At minimum, experiments should compare:

1. deterministic evolution;
2. independent-noise Monte Carlo;
3. correlated/random-field Monte Carlo;
4. an established stochastic dynamical model appropriate to the domain;
5. SFE with identical initial conditions where feasible.

## Ablation tests

Run SFE while removing one component at a time:

- no fractal/multiscale correlation;
- fixed rather than state-dependent transition weights;
- no evolutionary memory;
- no major-jump class;
- no genesis/restart class;
- simplified constraint operator;
- no attractor aggregation.

This identifies which components actually matter.

## Metrics

Domain-independent candidate metrics:

- valid-state fraction;
- trajectory diversity;
- evolutionary distance distribution;
- rare-state discovery rate;
- attractor stability across seeds;
- sensitivity to parameters;
- computational cost;
- reproducibility.

Domain-specific experiments must add externally meaningful validation metrics.

## Experimental integrity

Predefine primary outcomes when possible. Retain unsuccessful runs. Report rejected states. Do not tune SFE on a test set and then claim the same test as independent validation.

## Replication tiers

**Tier 0:** exact seed reproduction.

**Tier 1:** independent implementation using the same specification.

**Tier 2:** independent data/domain replication.

**Tier 3:** prospective or experimentally observed validation.

Claims should state the highest tier actually achieved.
