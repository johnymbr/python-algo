import unittest


def int_to_roman(num: int) -> str:
    symbols = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
               ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

    res = ""
    for symbol, val in reversed(symbols):
        if num // val:
            count = num // val
            res += (symbol * count)
            num = num % val

    return res


class IntegerToRoman(unittest.TestCase):
    def test_01(self):
        self.assertEqual("III", int_to_roman(3))

    def test_02(self):
        self.assertEqual("LVIII", int_to_roman(58))

    def test_03(self):
        self.assertEqual("MCMXCIV", int_to_roman(1994))
