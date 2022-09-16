import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/bag-of-tokens/
# TC: O(n log n)
# SC: O(1)
# We need to sort our tokens. To increase score, is better face up the lower tokens and face down the higher tokens.
# We use 2 points, left and right. Until left less than right, if power greater than or equal token[left],
# decrease power, increase score and left. else, increase power with token[right], decrease score and right pointer.
# after loop, if token[right] is less or equal power, increase score one last time.
def bag_of_tokens_score(tokens: List[int], power: int) -> int:
    tokens.sort()  # O(n log n)

    left, right = 0, len(tokens) - 1
    score = 0

    if not tokens or tokens[0] > power:
        return score

    while left < right:
        if tokens[left] <= power:
            power -= tokens[left]
            score += 1
            left += 1
        else:
            power += tokens[right]
            score -= 1
            right -= 1

    if tokens[right] <= power:
        score += 1

    return score


class BagOfTokens(unittest.TestCase):
    def test_01(self):
        self.assertEqual(0, bag_of_tokens_score([100], 50))

    def test_02(self):
        self.assertEqual(1, bag_of_tokens_score([100, 200], power=150))

    def test_03(self):
        self.assertEqual(2, bag_of_tokens_score([100, 200, 300, 400], power=200))
