import unittest


# LeetCode link: https://leetcode.com/problems/number-of-1-bits/
# TC: O(1) because the maximum length is 32 bits.
# SC: O(1)
# While n is > 0, sum the mod operation between n and 2
# Then n is equal n shifted on left by 1.
def hamming_weight(n: int) -> int:
    res = 0

    while n:
        res += n % 2
        n = n >> 1
    return res


# While n is > 0, sum res plus 1.
# Then whe use and (&) operator between n and n - 1.
def hamming_weight_ii(n: int) -> int:
    res = 0
    while n:
        res += 1
        n &= n - 1

    return res


class NumberOfOneBits(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, hamming_weight(0b00000000000000000000000000001011))

    def test_02(self):
        self.assertEqual(3, hamming_weight_ii(0b00000000000000000000000000001011))
