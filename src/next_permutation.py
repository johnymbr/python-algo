import heapq
import unittest
from typing import List


# Time O(n!)
def next_permutation_brute_force(nums: List[int]) -> List[int]:
    permutations = []

    def backtrack(first=0):
        if first == len(nums):
            permutations.append(nums[:])

        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    permutations = []
    backtrack()

    heapq.heapify(permutations)

    if nums == permutations[-1]:
        return permutations[0]

    while permutations:
        permutation = heapq.heappop(permutations)
        if nums == permutation:
            next_perm = heapq.heappop(permutations)
            return next_perm


# LeetCode link: https://leetcode.com/problems/next-permutation/
# TC: O(n)
# TC: O(1)
def next_permutation_single_pass(nums: List[int]) -> List[int]:
    i = len(nums) - 2

    def swap(x: int, y: int):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp

    def reverse(start: int):
        end = len(nums) - 1
        while start < end:
            swap(start, end)
            start += 1
            end -= 1

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        swap(i, j)

    reverse(i + 1)

    return nums


class NextPermutation(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 3, 2], next_permutation_brute_force([1, 2, 3]))

    def test_02(self):
        self.assertEqual([1, 3, 2], next_permutation_single_pass([1, 2, 3]))

    def test_03(self):
        self.assertEqual([1, 5, 8, 5, 1, 3, 4, 6, 7], next_permutation_single_pass([1, 5, 8, 4, 7, 6, 5, 3, 1]))

    def test_04(self):
        self.assertEqual([5, 1, 1], next_permutation_single_pass([1, 5, 1]))
