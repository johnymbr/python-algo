import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/combination-sum-iv/
# TC: O(n*t)
# SC: O(t)
# In this problem it was used a dynamic programming approach.
def combination_sum_4(nums: List[int], target: int) -> int:
    cache = {0: 1}

    for total in range(1, target + 1):
        cache[total] = 0
        for n in nums:
            cache[total] += cache.get(total - n, 0)

    return cache[target]


class CombinationSum4(unittest.TestCase):
    def test_01(self):
        self.assertEqual(7, combination_sum_4([1, 2, 3], 4))

    def test_02(self):
        self.assertEqual(0, combination_sum_4([9], 3))

    def test_03(self):
        self.assertEqual(39882198, combination_sum_4([4, 2, 1], 32))
