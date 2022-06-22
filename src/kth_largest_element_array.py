import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# The simple solution is sort nums array and return len(nums) - k index. O(n log n).
# Another approach is using QuickSelect algorithm. Average case is O(n), and Worst case is O(n^2)
def find_kth_largest(nums: List[int], k: int) -> int:
    # another way is: nums.sort()[len(nums) - k]
    k = len(nums) - k
    return quick_select(nums=nums, k=k, l=0, r=len(nums) - 1)


def quick_select(nums: List[int], k: int, l: int, r: int) -> int:
    pivot, p = nums[r], l

    for i in range(l, r):
        if nums[i] < pivot:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1

    nums[p], nums[r] = nums[r], nums[p]

    if p > k:
        return quick_select(nums, k, l, p - 1)
    elif p < k:
        return quick_select(nums, k, p + 1, r)

    return nums[p]


class KthLargestElementArray(unittest.TestCase):
    def test_01(self):
        self.assertEqual(5, find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2))

    def test_02(self):
        self.assertEqual(4, find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
