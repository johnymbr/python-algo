import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/pascals-triangle-ii/
# Time complexity: O(rowIndex + column)
# Space complexity: O(rowIndex)
def get_row(rowIndex: int) -> List[int]:
    ret = []
    for r in range(rowIndex + 1):
        aux = []
        for c in range(r + 1):
            if c == 0 or c == r:
                aux.append(1)
            else:
                aux.append(ret[c - 1] + ret[c])

        ret = aux

    return ret


class PascalsTriangleII(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 3, 3, 1], get_row(3))

    def test_02(self):
        self.assertEqual([1], get_row(0))

    def test_03(self):
        self.assertEqual([1, 1], get_row(1))
