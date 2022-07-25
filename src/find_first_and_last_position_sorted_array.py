import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Using binary search with recursion to solve this problem.
# TC O(log n)
# SC O(log n)
def search_range(nums: List[int], target: int) -> List[int]:
    res = [len(nums), -1]

    def helper(left: int, right: int):
        if left > right:
            return

        mid = (left + right) // 2

        if nums[mid] == target:
            if res[0] > mid:
                res[0] = mid
            if res[1] < mid:
                res[1] = mid
            helper(left, mid - 1)
            helper(mid + 1, right)
        elif nums[mid] < target:
            helper(mid + 1, right)
        else:
            helper(left, mid - 1)

    helper(0, len(nums) - 1)

    return res if res[1] != -1 else [-1, -1]


# LeetCode link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Using binary search to solve this problem.
# TC O(log n)
# SC O(1)
def search_range_without_recursion(nums: List[int], target: int) -> List[int]:

    def helper(go_left: bool):
        left, right = 0, len(nums) - 1
        i = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                i = mid
                if go_left:
                    right = mid - 1
                else:
                    left = mid + 1

        return i

    left_p = helper(True)
    right_p = helper(False)

    return [left_p, right_p]


class FindFirstAndLasPosition(unittest.TestCase):
    def test_01(self):
        self.assertEqual([3, 4], search_range([5, 7, 7, 8, 8, 10], 8))

    def test_02(self):
        self.assertEqual([-1, -1], search_range([5, 7, 7, 8, 8, 10], 6))

    def test_03(self):
        self.assertEqual([-1, -1], search_range([], 0))

    def test_04(self):
        self.assertEqual([3, 4], search_range_without_recursion([5, 7, 7, 8, 8, 10], 8))

    def test_05(self):
        self.assertEqual([-1, -1], search_range_without_recursion([5, 7, 7, 8, 8, 10], 6))

    def test_06(self):
        self.assertEqual([-1, -1], search_range_without_recursion([], 0))
