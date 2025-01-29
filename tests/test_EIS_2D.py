import unittest
import numpy as np
from scripts import EIS_2D

class TestEqualIntervalSearch(unittest.TestCase):

    def setUp(self):
        self.function = lambda x: (10 * x[0]**2) + (4 * x[1]**2) + (3 * x[0] * x[1]) + (2 * x[0]) + (2 * x[1]) + 1
        self.initialX = [1, 1]
        self.searchDirection = [-1/np.sqrt(2), -1/np.sqrt(2)]
        self.bracket = [0, 5]
        self.numIntervals = 10

    def test_isDescentDirection(self):
        self.assertTrue(EIS_2D.isDescentDirection(self.function, self.searchDirection, self.initialX))

    def test_equalIntervalSearch(self):
        stepSize, bracketReduction, functionEvaluations = EIS_2D.equalIntervalSearch(self.function, self.initialX, self.searchDirection, self.bracket, self.numIntervals, printBracket=False)
        self.assertAlmostEqual(stepSize, 1.5805916297198204, places=8)

    def test_compare_with_scipy(self):
        stepSize, _, _ = EIS_2D.equalIntervalSearch(self.function, self.initialX, self.searchDirection, self.bracket, self.numIntervals, printBracket=False)
        x1, x2 = self.initialX[0] + (stepSize * self.searchDirection[0]), self.initialX[1] + (stepSize * self.searchDirection[1])
        x_opt = EIS_2D.verifyMinima(self.function, self.initialX, self.searchDirection)
        self.assertAlmostEqual(x1, x_opt[0], places=6)
        self.assertAlmostEqual(x2, x_opt[1], places=6)

if __name__ == "__main__":
    unittest.main()
