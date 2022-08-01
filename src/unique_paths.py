import unittest


# LeetCode link: https://leetcode.com/problems/unique-paths/
# TC O(m * n)
# SC O(n)
# To solve this problem, we use dynamic programming.
# We start with the last row, all the elements are 1.
# We iterate over m - 1 and create a new row, initiating with value 1 too.
# We iterate over n - 2, from back to front, and each position is equal new_row[j+1] + row[j]
# Then row is equal new_row.
def unique_paths(m: int, n: int) -> int:
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]

        row = new_row

    return row[0]


class UniquePaths(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, unique_paths(3, 2))

    def test_02(self):
        self.assertEqual(28, unique_paths(3, 7))

    def test_03(self):
        self.assertEqual(193536720, unique_paths(23, 12))
