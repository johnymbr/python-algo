import unittest
from typing import List


# Leetcode link: https://leetcode.com/problems/verifying-an-alien-dictionary/description/
# TC O(MxN): Length of words times length of each individual word.
# SC O(1): We use only a dictionary, but with a constant length (26).
def is_alien_sorted(words: List[str], order: str) -> bool:
    alphabet = {}
    for i in range(len(order)):
        alphabet[order[i]] = i

    def check_words(first, second) -> bool:
        for j in range(len(first)):
            fc = first[j]

            if j > len(second) - 1:
                return False

            sc = second[j]
            if alphabet[fc] < alphabet[sc]:
                return True
            elif alphabet[fc] > alphabet[sc]:
                return False

        return True

    n = len(words)
    for i in range(n):
        curr = words[i]

        if i < (n - 1) and not check_words(curr, words[i + 1]):
            return False

    return True


class VerifyingAlienDictionary(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, is_alien_sorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))

    def test_02(self):
        self.assertEqual(False, is_alien_sorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))

    def test_03(self):
        self.assertEqual(False, is_alien_sorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
