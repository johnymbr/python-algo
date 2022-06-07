import unittest
from typing import List


# LeetCode Link: https://leetcode.com/problems/running-sum-of-1d-array/
# run through the list nums, and for each position,
# sum current position with the anterior position.
def running_sum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]

    return nums


class RunningSum1dArray(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 3, 6, 10], running_sum([1, 2, 3, 4]))

    def test_02(self):
        self.assertEqual([1, 2, 3, 4, 5], running_sum([1, 1, 1, 1, 1]))

    def test_03(self):
        self.assertEqual([3, 4, 6, 16, 17], running_sum([3, 1, 2, 10, 1]))
