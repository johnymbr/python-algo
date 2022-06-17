import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/3sum/
# time complexity: O(n^2)
# first operation is sort array nums
# loop through list nums, and for each num,
# make a two sum.
def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        # call two_sum
        aux = two_sum_ii(l=i + 1, r=len(nums) - 1, nums=nums, target=nums[i])
        if len(aux) > 0:
            res += aux

    return res


def two_sum_ii(l: int, r: int, nums: List[int], target: int) -> List[List[int]]:
    res = []
    while l < r:
        if target + nums[l] + nums[r] < 0:
            l += 1
        elif target + nums[l] + nums[r] > 0:
            r -= 1
        else:
            res.append([target, nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l - 1] and l < r:
                l += 1

    return res


class ThreeSum(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], three_sum([-1, 0, 1, 2, -1, -4]))

    def test_02(self):
        self.assertEqual([], three_sum([]))

    def test_03(self):
        self.assertEqual([], three_sum([0]))
