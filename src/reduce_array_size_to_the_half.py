import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/reduce-array-size-to-the-half/
# TC: O(n log n)
# SC: O(n)
# We use a map to store each number and the frequency of this number.
# After that, we sort this map by value (frequency)
def min_set_size(arr: List[int]) -> int:
    cmap = {}
    N = len(arr)
    n = 0
    output = 0

    for i in arr:
        cmap[i] = cmap.get(i, 0) + 1

    for k, v in sorted(cmap.items(), key=lambda item: -item[1]):
        n += v
        output += 1

        if n >= (N // 2):
            break

    return output


class ReduceArraySizeToTheHalf(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2, min_set_size([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))

    def test_02(self):
        self.assertEqual(1, min_set_size([7, 7, 7, 7, 7, 7]))
