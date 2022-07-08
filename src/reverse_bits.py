import unittest


# LeetCode link: https://leetcode.com/problems/reverse-bits/
# Time complexity: O(1)
# Space complexity: O(1)
# I used bit manipulation, >> to shift the bit and & to operation
# and | to operation or and << to shift again but for the start of res.
def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))

    return res


class ReverseBits(unittest.TestCase):
    def test_01(self):
        self.assertEqual(964176192, reverse_bits(0b00000010100101000001111010011100))

    def test_02(self):
        self.assertEqual(3221225471, reverse_bits(0b11111111111111111111111111111101))
