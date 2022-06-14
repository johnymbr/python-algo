import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/container-with-most-water/
# Solution using two pointers approach
def max_area(height: List[int]) -> int:
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

        res = max(res, area)

    return res


class ContainerWithMostWater(unittest.TestCase):
    def test_01(self):
        self.assertEqual(49, max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_02(self):
        self.assertEqual(1, max_area([1, 1]))
