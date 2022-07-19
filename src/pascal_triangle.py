import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/pascals-triangle/
# TC O(n^2)
# SC O(n^2)
def generate(numRows: int) -> List[List[int]]:
    res = []

    # loop for rows
    for r in range(numRows):
        row = []
        for c in range(r + 1):
            if c == 0 or c == r:
                row.append(1)
            else:
                row.append(res[r - 1][c] + res[r - 1][c - 1])
        res.append(row)

    return res


class PascalTriangle(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], generate(5))

    def test_02(self):
        self.assertEqual([[1]], generate(1))
