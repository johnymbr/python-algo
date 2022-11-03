import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/toeplitz-matrix/
# TC: O(M*N)
# SC: O(1)
# We do a loop through the matrix, from second row, and for each column we evaluate if top-left value
# of this column has the same value of current value.
def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    for row_idx in range(1, len(matrix)):
        for col_idx in range(1, len(matrix[row_idx])):
            if col_idx > 0 and matrix[row_idx - 1][col_idx - 1] != matrix[row_idx][col_idx]:
                return False

    return True


class ToeplitzMatrixTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))

    def test_02(self):
        self.assertEqual(False, is_toeplitz_matrix([[1, 2], [2, 2]]))
