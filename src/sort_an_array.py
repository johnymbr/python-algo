import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/sort-an-array/description/
# TC: O(n logn)
# SC: O(n)
# To solve this problem I used merge sort algorithm.
def sort_array(nums: List[int]) -> List[int]:
    def merge_sort(l, r) -> List[int]:
        if l == r:
            return nums[l:l + 1]

        mid = l + (r - l) // 2
        left_array = merge_sort(l, mid)
        right_array = merge_sort(mid + 1, r)

        return merge(left_array, right_array)

    def merge(left_array, right_array) -> List[int]:
        l_idx = r_idx = 0
        l_length = len(left_array)
        r_length = len(right_array)

        res = []
        while l_idx < l_length and r_idx < r_length:
            if left_array[l_idx] < right_array[r_idx]:
                res.append(left_array[l_idx])
                l_idx += 1
            else:
                res.append(right_array[r_idx])
                r_idx += 1

        if l_idx < l_length:
            res += left_array[l_idx:]

        if r_idx < r_length:
            res += right_array[r_idx:]

        return res

    return merge_sort(0, len(nums) - 1)


class SortAnArray(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 2, 3, 5], sort_array([5, 2, 3, 1]))

    def test_02(self):
        self.assertEqual([0, 0, 1, 1, 2, 5], sort_array([5, 1, 1, 2, 0, 0]))
