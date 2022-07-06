import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/majority-element/
# Time complexity: O(n log n)
# Space complexity: O(n) because the sorting operation
# This isn't a good solution, once after sorting we can only return the len(nums)//2 element.
def majority_element(nums: List[int]) -> int:
    nums.sort()  # O(n log n)

    count = 1
    previous = nums[0]
    majority_count = len(nums) // 2
    for val in nums[1:]:
        if val == previous:
            count += 1
        else:
            count = 1

        previous = val
        if count > majority_count:
            return val

    return previous


# Same time and space complexity for the first solution, but without boilerplate
def majority_element_sorting(nums: List[int]) -> int:
    nums.sort()  # O(n log n)
    return nums[len(nums) // 2]


# Time complexity O(n)
# Space complexity O(1)
# This solution uses boyer moore algorithm.
# we change the major(candidate) element once the count is 0.
def majority_element_boyer_moore(nums: List[int]) -> int:
    count = 0
    major = nums[0]

    for num in nums:
        if count == 0:
            major = num

        count += (1 if num == major else -1)

    return major


class MajorityElement(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, majority_element([3, 2, 3]))

    def test_02(self):
        self.assertEqual(2, majority_element([2, 2, 1, 1, 1, 2, 2]))

    def test_03(self):
        self.assertEqual(3, majority_element_sorting([3, 2, 3]))

    def test_04(self):
        self.assertEqual(2, majority_element_sorting([2, 2, 1, 1, 1, 2, 2]))

    def test_05(self):
        self.assertEqual(3, majority_element_iii([3, 2, 3]))

    def test_06(self):
        self.assertEqual(2, majority_element_iii([2, 2, 1, 1, 1, 2, 2]))
