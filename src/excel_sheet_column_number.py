import unittest


# LeetCode link: https://leetcode.com/problems/excel-sheet-column-number/
# Time complexity: O(n)
# Space complexity: O(1)
# Count store the length of title, for each char, res plus 26**count multiple number of character.
def title_to_number(columnTitle: str) -> int:
    res = 0
    count = len(columnTitle) - 1
    for c in columnTitle:
        res += 26 ** count * (ord(c) % 32)
        count -= 1

    return res


# Time complexity: O(n)
# Space complexity: O(1)
# For each char, res is equal to res multiplied by 26 plus (ord(c) minus ord('A') plus one).
def title_to_number_sec(columnTitle: str) -> int:
    res = 0
    for c in columnTitle:
        res = 26 * res + (ord(c) - ord('A') + 1)

    return res


class ExcelSheetColumnNumber(unittest.TestCase):
    def test_01(self):
        self.assertEqual(1, title_to_number("A"))

    def test_02(self):
        self.assertEqual(28, title_to_number("AB"))

    def test_03(self):
        self.assertEqual(701, title_to_number("ZY"))

    def test_04(self):
        self.assertEqual(1, title_to_number_sec("A"))

    def test_05(self):
        self.assertEqual(28, title_to_number_sec("AB"))

    def test_06(self):
        self.assertEqual(701, title_to_number_sec("ZY"))
