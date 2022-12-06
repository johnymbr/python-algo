import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/unique-number-of-occurrences/description/
# TC: O(n)
# SC: O(n)
def unique_occurrences(arr: List[int]) -> bool:
    occurs = set()
    arr.sort()

    prev = arr[0]
    count = 1
    for num in arr[1:]:
        if num == prev:
            count += 1
        else:
            if count in occurs:
                return False
            occurs.add(count)
            count = 1

        prev = num

    if count in occurs:
        return False

    return True


class UniqueNumberOfOccurrences(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, unique_occurrences([1, 2, 2, 1, 1, 3]))

    def test_02(self):
        self.assertEqual(False, unique_occurrences([1, 2]))

    def test_03(self):
        self.assertEqual(True, unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
