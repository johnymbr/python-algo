import unittest


# LeetCode link: https://leetcode.com/problems/string-to-integer-atoi/
# looping over string, remove the leading whitepaces, retrieve sign
# and retrieve all digits.
def my_atoi(s: str) -> int:
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)

    res = 0
    sign = 1
    n = len(s)

    index = 0
    while index < n and s[index] == ' ':
        index += 1

    if index < n and s[index] == '+':
        sign = 1
        index += 1
    elif index < n and s[index] == '-':
        sign = -1
        index += 1

    while index < n and s[index].isdigit():
        aux = int(s[index])

        if res > INT_MAX // 10 or (res == INT_MAX // 10 and aux > INT_MAX % 10):
            return INT_MAX if sign > 0 else INT_MIN

        res = res * 10 + aux
        index += 1

    return sign * res


class StringToInteger(unittest.TestCase):
    def test_01(self):
        self.assertEqual(42, my_atoi('42'))

    def test_02(self):
        self.assertEqual(-42, my_atoi('   -42'))

    def test_03(self):
        self.assertEqual(4193, my_atoi('4193 with words'))

    def test_04(self):
        self.assertEqual(0, my_atoi('n+42'))

    def test_05(self):
        self.assertEqual(-2147483648, my_atoi('-91283472332'))
