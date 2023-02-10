import unittest
from copy import copy
from typing import List


def distinct_names(ideas: List[str]) -> int:
    initial_groups = [set() for _ in range(26)]
    for idea in ideas:
        initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])

    count = 0
    for i in range(25):
        for j in range(i + 1, 26):
            num_mutual = len(initial_groups[i] & initial_groups[j])

            count += 2 * (len(initial_groups[i]) - num_mutual) * (len(initial_groups[j]) - num_mutual)

    return count


class NameACompany(unittest.TestCase):
    def test_01(self):
        self.assertEqual(6, distinct_names(["coffee", "donuts", "time", "toffee"]))

    def test_02(self):
        self.assertEqual(0, distinct_names(["lack", "back"]))

    def test_03(self):
        self.assertEqual(2, distinct_names(["aaa","baa","caa","bbb","cbb","dbb"]))
