import sys
import unittest
from typing import List


def jump(nums: List[int]) -> int:
    n = len(nums)
    max_number = 10**6
    dp = [max_number] * n

    idx = 0
    if idx == n - 1:
        return 0

    def helper(idx) -> int:
        n_aux = len(nums)

        if dp[idx] == max_number:
            if idx == n_aux - 1:
                dp[idx] = 0
            else:
                steps = nums[idx]
                if steps != 0:
                    min_jumps = dp[idx]
                    for j in range(steps):
                        new_idx = idx + j + 1
                        if new_idx < n:
                            idx_aux = helper(new_idx)
                            if idx_aux != -1:
                                min_jumps = min(min_jumps, 1 + idx_aux)

                    dp[idx] = -1 if min_jumps == max_number else min_jumps
                else:
                    dp[idx] = -1

        return dp[idx]

    helper(0)

    return dp[0]


class JumpGameII(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2, jump([2, 3, 1, 1, 4]))

    def test_02(self):
        self.assertEqual(2, jump([2, 3, 0, 1, 4]))

    def test_03(self):
        self.assertEqual(3, jump([2, 2, 0, 1, 4]))

    def test_04(self):
        self.assertEqual(2, jump([1, 2, 3]))

    def test_05(self):
        self.assertEqual(3, jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
