import unittest


# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Solving this using slide window.
# While the character exists in the set, remove the left position and increment left position
# After this, add character of the current position on set and retrieve max from rest and set length.
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        res = max(res, len(char_set))

    return res


class LongestSubstringWithoutRepeatingCharTest(unittest.TestCase):
    def test_01(self):
        self.assertEqual(3, length_of_longest_substring("abcabcbb"))
