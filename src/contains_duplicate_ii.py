import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/contains-duplicate-ii/
# TC: O(n)
# SC: O(n)
# We use a map to store values already checked and his index too.
def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    my_map = {}
    for i in range(len(nums)):
        if not nums[i] in my_map:
            my_map[nums[i]] = i
        else:
            old_idx = my_map[nums[i]]
            if abs(old_idx - i) <= k:
                return True

            my_map[nums[i]] = i

    return False


class ContainsDuplicateII(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, contains_nearby_duplicate([1, 2, 3, 1], 3))

    def test_02(self):
        self.assertEqual(True, contains_nearby_duplicate([1, 0, 1, 1], 1))

    def test_03(self):
        self.assertEqual(False, contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
