import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/add-to-array-form-of-integer/description/
# TC: O(max(nums, log k)
# SC: O(1)
def add_to_array_form(nums: List[int], k: int) -> List[int]:
    carry = 0
    for i in range(len(nums) - 1, -1, -1):
        if k:
            a = nums[i]
            b = k % 10
            k = k // 10

            sum = a + b + carry
            if sum > 9:
                nums[i] = sum % 10
                carry = 1
            else:
                nums[i] = sum
                carry = 0
        elif carry:
            sum = nums[i] + carry
            if sum > 9:
                nums[i] = sum % 10
                carry = 1
            else:
                nums[i] = sum
                carry = 0
        else:
            break

    while k:
        aux = k % 10
        k = k // 10
        sum = aux + carry
        if sum > 9:
            nums = [sum % 10] + nums
            carry = 1
        else:
            nums = [sum] + nums
            carry = 0

    if carry:
        nums = [carry] + nums

    return nums


class AddToArrayFormOfInteger(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 2, 3, 4], add_to_array_form([1, 2, 0, 0], 34))

    def test_02(self):
        self.assertEqual([4, 5, 5], add_to_array_form([2, 7, 4], 181))

    def test_03(self):
        self.assertEqual([1, 0, 2, 1], add_to_array_form([2, 1, 5], 806))

    def test_04(self):
        self.assertEqual([2, 0, 2, 1], add_to_array_form([2, 1, 5], 1806))
