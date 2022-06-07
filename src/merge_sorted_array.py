import unittest
from typing import List


# LeetCode Link: https://leetcode.com/problems/merge-sorted-array/
# length of nums1 is equal m + n, and the end of nums1 was filled by 0's.
# as nums1 has the total length, we can start the merge from the end to begin.
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1

        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


class MergeSortedArray(unittest.TestCase):
    def test_01(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)

    def test_02(self):
        nums1 = [1]
        merge(nums1=nums1, m=1, nums2=[], n=0)
        self.assertEqual([1], nums1)

    def test_03(self):
        nums1 = [2, 3, 5, 0, 0]
        merge(nums1=nums1, m=3, nums2=[0, 1], n=2)
        self.assertEqual([0, 1, 2, 3, 5], nums1)
