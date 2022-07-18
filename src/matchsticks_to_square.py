import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/matchsticks-to-square/
# TC: O(4^n)
# SC: O(n)
# This solution uses backtrack to try all possibilities.
# A bit trick is looking if a sides[j] is equal zero, this means that match fails when adding to sides[j]
# and it will fail with another j's too.
def make_square(matchsticks: List[int]) -> bool:
    length = sum(matchsticks) // 4
    sides = [0] * 4

    if sum(matchsticks) / 4 != length:
        return False

    matchsticks.sort(reverse=True)

    def dfs(index: int):
        if index == len(matchsticks):
            return True

        for j in range(4):
            if sides[j] + matchsticks[index] <= length:
                sides[j] += matchsticks[index]
                if dfs(index + 1):
                    return True
                sides[j] -= matchsticks[index]

                if sides[j] == 0:
                    break
        return False

    return dfs(0)


class MatchSticksToSquare(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, make_square([1, 1, 2, 2, 2]))

    def test_02(self):
        self.assertEqual(False, make_square([3, 3, 3, 3, 4]))
