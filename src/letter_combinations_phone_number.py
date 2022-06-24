import unittest
from typing import List


def letter_combinations(digits: str) -> List[str]:
    res = []
    map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(pos: int, curStr: str):
        if len(curStr) == len(digits):
            if curStr != "":
                res.append(curStr)
            return

        for i in map[digits[pos]]:
            backtrack(pos + 1, curStr + i)

    backtrack(0, "")

    return res


class LetterCombinationsPhoneNumber(unittest.TestCase):
    def test_01(self):
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], letter_combinations(digits="23"))

    def test_02(self):
        self.assertEqual([], letter_combinations(digits=""))

    def test_03(self):
        self.assertEqual(["a", "b", "c"], letter_combinations(digits="2"))
