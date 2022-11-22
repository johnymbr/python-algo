import unittest
from math import sqrt, inf


# Leetcode link: https://leetcode.com/problems/perfect-squares/description/
# TC: O(n * n ^ 1/2)
# SC: O(n)
# We used a class variable to preserve dp array between the tests.
# We start making precompute of perfect_squares, and use this array
# to calculate the least number of perfect square.
def num_squares(n: int) -> int:
    dp = [0]

    # precompute the perfectsquares
    perfect_squares = [pow(i, 2) for i in range(1, int(sqrt(n)) + 1)]

    while len(dp) < n + 1:
        dpI = inf

        for ps in perfect_squares:
            if len(dp) < ps: break
            dpI = min(dpI, 1 + dp[-ps])

        dp.append(dpI)

    return dp[n]


class PerfectSquares(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, num_squares(12))

    def test_02(self):
        self.assertEqual(2, num_squares(13))
