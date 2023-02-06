import unittest
from typing import List


def best_team_score(scores: List[int], ages: List[int]) -> int:
    memo = []

    def check_conflict(first_tuple, second_tuple):
        ft_score, ft_age = first_tuple
        st_score, st_age = second_tuple

        if (st_age < ft_age and st_score > ft_score) or (st_age > ft_age and st_score < ft_score):
            return True

        return False

    hs = 0
    for i in range(len(ages)):
        score = scores[i]
        age = ages[i]




class BestTeamWithNoConflict(unittest.TestCase):
    def test_01(self):
        self.assertEqual(34, best_team_score([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]))

    def test_02(self):
        self.assertEqual(16, best_team_score([4, 5, 6, 5], [2, 1, 2, 1]))

    def test_03(self):
        self.assertEqual(6, best_team_score([1, 2, 3, 5], [8, 9, 10, 1]))
