import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/combination-sum-iii/
# TC: O(n^2)
# SC: O(k)
def combination_sum_3(k: int, n: int) -> List[List[int]]:
    res = []

    def backtrack(pos: int, comb: [], total) -> bool:
        if len(comb) > k or total > n:
            return False

        if len(comb) == k and total == n:
            res.append(comb.copy())
            return False

        for i in range(pos, 10):
            comb.append(i)
            can_continue = backtrack(i + 1, comb, total + i)
            comb.pop()
            if not can_continue:
                break

        return True

    backtrack(1, [], 0)
    return res


class CombinationSum3(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[1, 2, 4]], combination_sum_3(3, 7))

    def test_02(self):
        self.assertEqual([[1, 2, 6], [1, 3, 5], [2, 3, 4]], combination_sum_3(3, 9))

    def test_03(self):
        self.assertEqual([], combination_sum_3(4, 1))
