import unittest


# LeetCode Link: https://leetcode.com/problems/zigzag-conversion/
# another solution for zigzag conversion.
# in this case using increment.
def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    res = ""
    for r in range(num_rows):
        increment = 2 * (num_rows - 1)
        for i in range(r, len(s), increment):
            res += s[i]
            if r > 0 and r < num_rows - 1 and i + increment - 2 * r < len(s):
                res += s[i + increment - 2 * r]

    return res


class ZigzagConversionSecAnswer(unittest.TestCase):
    def test_01(self):
        self.assertEqual("PAHNAPLSIIGYIR", convert("PAYPALISHIRING", 3))

    def test_02(self):
        self.assertEqual("PINALSIGYAHRPI", convert("PAYPALISHIRING", 4))
