import unittest


def convert(s: str, num_rows: int) -> str:
    res = [""] * num_rows
    curr_row = 0
    going_down = True

    for i in range(len(s)):
        res[curr_row] = res[curr_row] + s[i]
        if (not going_down and curr_row == 0) or curr_row == num_rows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1

    return "".join(res)


class ZigZagConversion(unittest.TestCase):
    def test_01(self):
        self.assertEqual("PAHNAPLSIIGYIR", convert("PAYPALISHIRING", 3))

    def test_02(self):
        self.assertEqual("PINALSIGYAHRPI", convert("PAYPALISHIRING", 4))

    def test_03(self):
        self.assertEqual("A", convert("A", 1))
