import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# TC: O(nums1 * nums2)
# SC: O(nums1 * nums2)
# To solve this problem, we use DP. We build a memo,
# and for each nums[i] and nums[j] we calculate memo, using i+1 and j+1 position and plus 1.
def find_length(nums1: List[int], nums2: List[int]) -> int:
    memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

    for i in range(len(nums1) - 1, -1, -1):
        for j in range(len(nums2) - 1, -1, -1):
            if nums1[i] == nums2[j]:
                memo[i][j] = memo[i + 1][j + 1] + 1

    ans = 0
    for row in memo:
        for col in row:
            ans = max(col, ans)

    return ans


class MaximumLengthOfRepeatedSubarray(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))

    def test_02(self):
        self.assertEqual(5, find_length([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
