import unittest


# LeetCode link: https://leetcode.com/problems/divide-two-integers/
# Time complexity O(n)
# We use bit manipulation to increment "multiplier".
# While dividend is less than or equal divisor, subtract temp from dividend.
# At each loop temp is doubled using bit manipulation.
def divide(dividend: int, divisor: int) -> int:
    d = abs(dividend)
    dv = abs(divisor)

    res = 0

    while d >= dv:
        temp = dv
        mul = 1
        while d >= temp:
            d -= temp
            res += mul
            mul <<= 1
            temp <<= 1

    if (dividend < 0) != (divisor < 0):
        res = -res

    return min(2 ** 31 - 1, max(-2 ** 31, res))


class DivideTwoIntegers(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, divide(10, 3))

    def test_02(self):
        self.assertEqual(-2, divide(7, -3))

    def test_03(self):
        self.assertEqual(0, divide(0, 1))

    def test_04(self):
        self.assertEqual(1, divide(1, 1))

    def test_05(self):
        self.assertEqual(2147483647, divide(-2147483648, -1))
