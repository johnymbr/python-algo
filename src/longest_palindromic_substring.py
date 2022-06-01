import unittest


# Check if a string is a palindrome, using two pointer
# Time complexity: O(n)
def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


# LeetCode Link: https://leetcode.com/problems/longest-palindromic-substring/
# Run through the string, and validate an odd string and an even string
# for every substring, calls expand_around_center function
# Time complexity: O(n^2)
def longest_palindrome(s: str) -> str:
    # run through s, checking if this curr substring is a palindrome or not
    start = 0
    end = 0

    for i in range(len(s)):  # O(n)
        len_1 = expand_around_center(s, i, i)  # O(n)
        len_2 = expand_around_center(s, i, i + 1)  # O(n)
        _len = max(len_1, len_2)

        if _len > end - start:
            start = int(i - (_len - 1) // 2)
            end = int(i + _len // 2)

    return s[start:end + 1]


class LongestPalindromicSubstring(unittest.TestCase):
    def test_01(self):
        self.assertEqual("aba", longest_palindrome("babad"))

    def test_02(self):
        self.assertEqual("bb", longest_palindrome("cbbd"))
