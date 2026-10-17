"""Run: python -m unittest discover -s tests -v"""
import math
import unittest
from examples.ou_known_answer import analytic, simulate

class TestOU(unittest.TestCase):
    def test_exact_moments(self):
        mean, var = analytic()
        self.assertAlmostEqual(mean, 2 + 3*math.exp(-1.4), places=12)
        self.assertAlmostEqual(var, .25*(1-math.exp(-2.8))/1.4, places=12)

    def test_seed_reproducibility(self):
        self.assertEqual(simulate(123, 200), simulate(123, 200))

    def test_statistical_tolerance(self):
        mean, var = analytic()
        sm, sv = simulate(20261016, 10000)
        self.assertLess(abs(sm-mean), 5*math.sqrt(var/10000))
        self.assertLess(abs(sv-var), 0.05)

if __name__ == "__main__":
    unittest.main()
