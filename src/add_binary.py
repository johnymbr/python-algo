import unittest


# Leetcode link: https://leetcode.com/problems/add-binary/description/
# TC: O(n)
# SC: O(1)
def add_binary(a: str, b: str) -> str:
    sum = ''

    a_int = int(a)
    b_int = int(b)

    if not a_int and not b_int:
        return '0'

    rest = 0
    while a_int or b_int:
        a_aux = 0
        if a_int:
            a_aux = a_int % 10
            a_int = a_int // 10

        b_aux = 0
        if b_int:
            b_aux = b_int % 10
            b_int = b_int // 10

        sum_aux = (a_aux + b_aux + rest) % 2
        rest = (a_aux + b_aux + rest) // 2

        sum = str(sum_aux) + sum

    return str(rest) + sum if rest else sum


class AddBinary(unittest.TestCase):
    def test_01(self):
        self.assertEqual('100', add_binary('11', '1'))

    def test_02(self):
        self.assertEqual('10101', add_binary('1010', '1011'))