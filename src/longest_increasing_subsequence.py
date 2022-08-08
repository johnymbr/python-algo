import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/longest-increasing-subsequence/
# TC: O(n^2)
# SC: O(n)
# We use DP to solve this problem, start from end to beginning.
# And for each loop, we check what is the longest subsequence.
def length_of_lis(nums: List[int]) -> int:
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)


class LongestIncreasingSubsequence(unittest.TestCase):
    def test_01(self):
        self.assertEqual(4, length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))

    def test_02(self):
        self.assertEqual(4, length_of_lis([0, 1, 0, 3, 2, 3]))

    def test_03(self):
        self.assertEqual(1, length_of_lis([7, 7, 7, 7, 7, 7, 7]))
