import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/maximum-units-on-a-truck/
# Time complexity for sorting is O(n log n), so time complexity for solution is O(n log n).
# Space complexity is O(n) for sorting and the rest of solution is O(1).
def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)  # O(n log n)

    max_units = 0
    for boxes, units in boxTypes:  # O(n)
        if truckSize > 0:
            qty_boxes = min(boxes, truckSize)
            truckSize -= qty_boxes
            max_units += qty_boxes * units
        else:
            break

    return max_units


class MaximumUnitsOnATruck(unittest.TestCase):
    def test_01(self):
        self.assertEqual(8, maximum_units([[1, 3], [2, 2], [3, 1]], 4))

    def test_02(self):
        self.assertEqual(91, maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
