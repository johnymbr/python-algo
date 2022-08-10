import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/binary-trees-with-factors/
# TC: O(n^2)
# SC: O(n)
# To solve this problem I use dynamic programming.
def num_factor_binary_trees(arr: List[int]) -> int:
    mod = 10 ** 9 + 7
    arr.sort()
    dp = [1] * len(arr)

    index = {x: i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        for j in range(i):
            if x % arr[j] == 0:
                right = x / arr[j]
                if right in index:
                    dp[i] += dp[j] * dp[index[right]]
                    dp[i] %= mod

    return sum(dp) % mod


class BinaryTreesWithFactors(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, num_factor_binary_trees([2, 4]))

    def test_02(self):
        self.assertEqual(7, num_factor_binary_trees([2, 4, 5, 10]))
