import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/shuffle-the-array/description/
# TC: O(n)
# SC: O(n)
# We use an additional space with length n.
def shuffle(nums: List[int], n: int) -> List[int]:
    res = [0] * (2 * n)
    for i in range(n):
        res[2 * i] = nums[i]
        res[2 * i + 1] = nums[i + n]

    return res


class ShuffleTheArray(unittest.TestCase):
    def test_01(self):
        self.assertEqual([2, 3, 5, 4, 1, 7], shuffle([2, 5, 1, 3, 4, 7], 3))

    def test_02(self):
        self.assertEqual([1, 4, 2, 3, 3, 2, 4, 1], shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))

    def test_03(self):
        self.assertEqual([1, 2, 1, 2], shuffle([1, 1, 2, 2], 2))
