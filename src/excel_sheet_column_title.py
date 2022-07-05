import unittest


# LeetCode link: https://leetcode.com/problems/excel-sheet-column-title/
# Time complexity: O(n)
# First calculate modulus over columnNumber - 1 to find the last character.
# After this, concatenate this character with res string
# After this, the new columnNumber will be columnNumber - 1 divided by 26.
# Iterate over this until columnNumber is greater than zero.
def convert_to_title(columnNumber: int) -> str:
    res = ""
    while columnNumber > 0:  # O(n)
        c = chr(ord('A') + ((columnNumber - 1) % 26))
        res = c + res
        columnNumber = (columnNumber - 1) // 26

    return res


class ExcelSheetColumnTitle(unittest.TestCase):
    def test_01(self):
        self.assertEqual("A", convert_to_title(1))

    def test_02(self):
        self.assertEqual("AB", convert_to_title(28))

    def test_03(self):
        self.assertEqual("ZY", convert_to_title(701))
