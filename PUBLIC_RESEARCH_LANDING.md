# Stochastic Fractal Evolution — Public Research Entry Point

**Status:** Open experimental research proposal; **not** a validated new scientific field.

**Canonical source:** https://github.com/AA-Engineering/stochastic-fractal-evolution

## What is SFE?

SFE proposes recursively evolving constrained state ensembles with multiscale/fractal-correlated initial fields, seeded transition regimes, and memory.

```text
K_t ~ P(K | X_t, H_t, E_t)
X~_(t+1) = Phi_K(X_t, H_t, E_t, epsilon_t)
X_(t+1) = C_domain(X~_(t+1))
```

## What is available?

- [Mathematical specification](SPECIFICATION.md)
- [Scientific limitations and prior art](PRIOR_ART_AND_NOVELTY.md)
- [Benchmarks and falsification](BENCHMARKS.md)
- [Historical North American plate validation protocol](SFE_GEO_H001.md)
- [Known-answer OU numerical control](examples/ou_known_answer.py)
- [Research reproducibility standard](REPRODUCIBILITY.md)

## Plate tectonics: current research focus

The proposed North American Plate experiment will hindcast from 30 Ma to the present before attempting +100 Ma forward ensembles. Plate-boundary history, initial states, geodynamic constraints, and withheld validation observations must be documented to avoid information leakage.

The earlier future-plate artwork is **conceptual only**; it is not the result of an executed geodynamic ensemble.

## What can independent researchers test?

1. Can the numerical engine reproduce analytical state-space moments and deterministic dynamics?
2. Can a geophysical implementation reconstruct known plate-boundary changes without leakage?
3. Does SFE improve calibration, physical validity, or rare-event coverage over existing methods at comparable computational cost?
4. Are the reported results stable across random seeds, parameter changes, and independent implementations?

## How to cite

See [CITATION.cff](CITATION.cff). A DOI has **not yet been issued**. Do not cite a DOI until an archive actually confirms it.

## Authorship and AI disclosure

Initial concepts and documentation were developed through human-directed conversations with ChatGPT. Independent verification is required; generated content is not evidence of scientific validity.
