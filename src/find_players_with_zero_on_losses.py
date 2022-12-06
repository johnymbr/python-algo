import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
# TC: O(n log n)
# SC: O(n)
# We use dicts to store the count of losses.
# after processing matches, we check the elements of dict, if the value were 0, we include this element on zero_l array
# if the value were 1, we include this element on one_l array.
def find_winners(matches: List[List[int]]) -> List[List[int]]:
    count_losses = {}

    for match in matches:
        w, l = match[0], match[1]
        count_losses[w] = count_losses.get(w, 0)
        count_losses[l] = count_losses.get(l, 0) + 1

    zero_l = []
    one_l = []
    for k, v in count_losses.items():
        if v == 0:
            zero_l.append(k)
        elif v == 1:
            one_l.append(k)

    return [sorted(zero_l), sorted(one_l)]


class FindPlayersWithZeroOrOneLosses(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[1, 2, 10], [4, 5, 7, 8]].sort(), find_winners(
            [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]).sort())

    def test_02(self):
        self.assertEqual([[1, 2, 5, 6], []].sort(), find_winners([[2, 3], [1, 3], [5, 4], [6, 4]]).sort())
