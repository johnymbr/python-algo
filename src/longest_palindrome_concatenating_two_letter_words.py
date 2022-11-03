import unittest
from collections import Counter
from typing import List


# Leetcode link: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
# TC: O(n)
# SC: O(n)
# To solve this problem, we use a map.
# and we loop through keys of the map, if two letter are equals,
# we increase the answer with the count of this letter on the map if the count was even
# if the count was odd whe increase by count - 1
# we use a mid to indicate if there is mid
# if letters aren't equal, we check if reverse of the word is in map
# if yes, we increase using minimum between two words.
def longest_palindrome(words: List[str]) -> int:
    counter = Counter(words)

    res = mid = 0
    for w in counter.keys():

        if w[0] == w[1]:
            res += counter[w] if counter[w] % 2 == 0 else counter[w] - 1
            mid |= counter[w] % 2

        elif w[::-1] in counter:
            res += min(counter[w], counter[w[::-1]])

    return (res + mid) * 2


class LongestPalindromeConcatenating(unittest.TestCase):
    def test_01(self):
        self.assertEqual(6, longest_palindrome(["lc", "cl", "gg"]))

    def test_02(self):
        self.assertEqual(8, longest_palindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))

    def test_03(self):
        self.assertEqual(2, longest_palindrome(["cc", "ll", "xx"]))
