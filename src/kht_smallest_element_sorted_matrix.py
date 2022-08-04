import unittest
from typing import List


# TC: O(n log n)
def kth_smallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    mtx_min = matrix[0][0]
    mtx_max = matrix[n - 1][n - 1]

    while mtx_min < mtx_max:
        mid = (mtx_min + mtx_max) // 2

        row = 0
        col = n - 1
        count = 0
        while row < n and col >= 0:
            if matrix[row][col] <= mid:
                count += col + 1
                row += 1
            else:
                col -= 1

        if count < k:
            mtx_min = mid + 1
        else:
            mtx_max = mid

    return mtx_max


class KthSmallestElementSortedMatrix(unittest.TestCase):
    def test_01(self):
        self.assertEqual(13, kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))

    def test_02(self):
        self.assertEqual(-5, kth_smallest([[-5]], 1))
