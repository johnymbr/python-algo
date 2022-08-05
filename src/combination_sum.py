import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/combination-sum/
# TC O(2^target * k) : k is the average length of the input
# SC O(k * n) : n is the number of combination in the output
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []

    def comb_sum(csum: int, comb: List[int], candidates_aux: List[int]):
        for idx, value in enumerate(candidates_aux):
            if csum + value < target:
                comb.append(value)
                comb_sum(csum + value, comb, candidates_aux[idx:])
                comb.pop()
            elif csum + value == target:
                comb.append(value)
                res.append(comb.copy())
                comb.pop()
                break
            else:
                break

    comb_sum(0, [], candidates)

    return res


class CombinationSum(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[2, 2, 3], [7]], combination_sum([2, 3, 6, 7], 7))

    def test_02(self):
        self.assertEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], combination_sum([2, 3, 5], 8))

    def test_03(self):
        self.assertEqual([], combination_sum([2], 1))
