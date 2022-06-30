import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/contains-duplicate/
# Time complexity is O(n log n) because of sorting operation.
# After the sorting operation, we loop through the list, and after the first element,
# we check the previous element is equal than the current element. Time complexity for this operation is O(n).
def contains_duplicate_sort(nums: List[int]) -> bool:
    nums.sort()  # O(n log n)

    for i in range(len(nums)):  # O(n)
        if i == 0:
            continue

        if nums[i] == nums[i - 1]:
            return True
    return False


# Time complexity is O(n) because we need to loop through the list.
# We use a hashset and for each element we check if this element is already on hashset,
# if yes, this is a duplicate, and we need to return True.
# if no, we add this element to hashset.
# In this solution we use a Space complexity of O(n).
def contains_duplicate_hashset(nums: List[int]) -> bool:
    hashset = set()

    for i in range(len(nums)):
        if nums[i] in hashset:
            return True

        hashset.add(nums[i])

    return False


class ContainsDuplicate(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, contains_duplicate_sort([1, 2, 3, 1]))

    def test_02(self):
        self.assertEqual(False, contains_duplicate_sort([1, 2, 3, 4]))

    def test_03(self):
        self.assertEqual(True, contains_duplicate_sort([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_04(self):
        self.assertEqual(True, contains_duplicate_hashset([1, 2, 3, 1]))

    def test_05(self):
        self.assertEqual(False, contains_duplicate_hashset([1, 2, 3, 4]))

    def test_06(self):
        self.assertEqual(True, contains_duplicate_hashset([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
