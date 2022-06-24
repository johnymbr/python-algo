import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/4sum/
# Time complexity is O(n^k-1). We have k - 2 loops and
# two-sum algorithm that has O(n) time complexity.
# For four sum problem, time complexity is O(n^3)
# We use recursion until k == 2, when k == 2 we use two-sum with two pointers.
def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()  # O(n log n)
    res = []
    quad = []

    def k_sum(k: int, start: int, target: int):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                quad.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
                quad.pop()
        else:  # when k == 2, then we use two sum with two pointers.
            l, r = start, len(nums) - 1
            while l < r:  # O(n)
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

    k_sum(4, 0, target)
    return res


class FourSum(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], four_sum([1, 0, -1, 0, -2, 2], 0))

    def test_02(self):
        self.assertEqual([[2, 2, 2, 2]], four_sum([2, 2, 2, 2, 2], 8))
