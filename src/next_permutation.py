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


class NextPermutation(unittest.TestCase):
    def test_01(self):
        self.assertEqual([1, 3, 2], next_permutation_brute_force([1, 2, 3]))
