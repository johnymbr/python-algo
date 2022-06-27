import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Using window. l starts from 0 and r is len(cardPoints) - k.
# Sum right last k positions and after that, every iteration,
# sum l and subtract r.
def max_score(cardPoints: List[int], k: int) -> int:
    l, r = 0, len(cardPoints) - k
    score = sum(cardPoints[r:])  # O(n)
    res = score
    while r < len(cardPoints):  # O(n)
        score = score + cardPoints[l] - cardPoints[r]
        res = max(res, score)
        l += 1
        r += 1

    return res


class MaximumPointsFromCards(unittest.TestCase):
    def test_01(self):
        self.assertEqual(12, max_score([1, 2, 3, 4, 5, 6, 1], 3))

    def test_02(self):
        self.assertEqual(4, max_score([2, 2, 2], 2))

    def test_03(self):
        self.assertEqual(55, max_score([9, 7, 7, 9, 7, 7, 9], 7))
