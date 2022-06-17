import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# working with two pointer without using map to store info's.
def two_sum(numbers: List[int], target: int) -> List[int]:
    res = []
    l, r = 0, len(numbers) - 1
    while l < r:
        if target > (numbers[l] + numbers[r]):
            l += 1
        elif target < (numbers[l] + numbers[r]):
            r -= 1
        else:
            res.append(l + 1)
            res.append(r + 1)
            break

    return res


class TwoSumII(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 2], two_sum([2, 7, 11, 15], 9))

    def test_02(self):
        self.assertEqual([1, 3], two_sum([2, 3, 4], 6))

    def test_03(self):
        self.assertEqual([1, 2], two_sum([-1, 0], -1))
