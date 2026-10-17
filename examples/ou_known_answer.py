"""Reproducible OU exact-transition Monte Carlo control (Python standard library).

This is a baseline mathematical check, NOT an SFE superiority demonstration.
Run: python examples/ou_known_answer.py
"""
import math
import random

SEED = 20261016
N = 10000
THETA, MU, SIGMA, X0, T = 0.7, 2.0, 0.5, 5.0, 2.0

def analytic():
    e = math.exp(-THETA * T)
    mean = MU + (X0 - MU) * e
    var = SIGMA**2 * (1 - e**2) / (2 * THETA)
    return mean, var

def simulate(seed=SEED, n=N):
    rng = random.Random(seed)
    mean, var = analytic()
    values = [mean + math.sqrt(var) * rng.gauss(0, 1) for _ in range(n)]
    sample_mean = sum(values) / n
    sample_var = sum((v - sample_mean)**2 for v in values) / (n - 1)
    return sample_mean, sample_var

if __name__ == "__main__":
    m, v = analytic()
    sm, sv = simulate()
    print(f"seed={SEED} n={N}")
    print(f"analytical mean={m:.8f} variance={v:.8f}")
    print(f"sample     mean={sm:.8f} variance={sv:.8f}")
    print(f"mean_error={sm-m:+.8f} variance_error={sv-v:+.8f}")
