import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/find-and-replace-pattern/
# TC O(n * k)
# SC O(n * k)
# We loop through the list of words and for each word, we build
# a map for character of pattern and word.
# if map is different between the current value and currently char, we return false
# otherwise we return true.
def find_and_replace_pattern(words: List[str], pattern: str) -> List[str]:
    res = []

    def matches(word: str) -> bool:
        word_map = [None] * 26
        pattern_map = [None] * 26

        for i in range(len(word)):
            w_idx = ord(word[i]) - ord('a')
            p_idx = ord(pattern[i]) - ord('a')
            if not word_map[w_idx]:
                word_map[w_idx] = pattern[i]
            if not pattern_map[p_idx]:
                pattern_map[p_idx] = word[i]

            if word_map[w_idx] != pattern[i] or pattern_map[p_idx] != word[i]:
                return False

        return True

    for w in words:
        if matches(w):
            res.append(w)

    return res


class FindAndReplacePattern(unittest.TestCase):
    def test_01(self):
        self.assertEqual(["mee", "aqq"], find_and_replace_pattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))

    def test_02(self):
        self.assertEqual(["a", "b", "c"], find_and_replace_pattern(["a", "b", "c"], "a"))
