import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/combination-sum-ii/
# TC: O(2^n)
# SC: O(n)
# we start sorting the candidates array. and use backtrack.
def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    def backtrack(i: int, comb: [int], total: int):
        if total > target:
            return

        if total == target:
            res.append(comb.copy())
            return

        prev = -1
        for j in range(i, len(candidates)):
            if candidates[j] == prev:
                continue
            comb.append(candidates[j])
            backtrack(j + 1, comb, total + candidates[j])
            comb.pop()
            prev = candidates[j]

    res = []
    backtrack(0, [], 0)
    return res


class CombinationSumII(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8))

    def test_02(self):
        self.assertEqual([[1, 2, 2], [5]], combination_sum_ii([2, 5, 2, 1, 2], 5))

    def test_03(self):
        self.assertEqual([[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]], combination_sum_ii([3, 1, 3, 5, 1, 1], 8))
