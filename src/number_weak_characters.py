import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# This first solution uses brute force.
# TC: O(n^2)
# SC: O(1)
def number_of_weak_characters(properties: List[List[int]]) -> int:
    output = 0

    # brute force O(n^2)
    for i in range(len(properties)):
        for j in range(i + 1, len(properties)):
            if (properties[j][0] > properties[i][0] and properties[j][1] > properties[i][1]) \
                    or (properties[j][0] < properties[i][0] and properties[j][1] < properties[i][1]):
                output += 1

    return output


# This second solution uses the sort trick.
# We sort attack in descending order and defending property in ascending order
# Then we loop through array, and check if defense is less than max defense,
# if true, increase number of weak characters.
# O(n log n)
# SC: O(1)
def number_of_weak_characters_ii(properties: List[List[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    number = 0
    max_d = 0

    for a, d in properties:
        if d < max_d:
            number += 1

        max_d = max(max_d, d)

    return number


class NumberOfWeakCharactersInTheGame(unittest.TestCase):
    def test_01(self):
        self.assertEqual(0, number_of_weak_characters([[5, 5], [6, 3], [3, 6]]))

    def test_02(self):
        self.assertEqual(1, number_of_weak_characters([[2, 2], [3, 3]]))

    def test_03(self):
        self.assertEqual(1, number_of_weak_characters([[1, 5], [10, 4], [4, 3]]))

    def test_04(self):
        self.assertEqual(0, number_of_weak_characters_ii([[5, 5], [6, 3], [3, 6]]))

    def test_05(self):
        self.assertEqual(1, number_of_weak_characters_ii([[2, 2], [3, 3]]))

    def test_06(self):
        self.assertEqual(1, number_of_weak_characters_ii([[1, 5], [10, 4], [4, 3]]))
