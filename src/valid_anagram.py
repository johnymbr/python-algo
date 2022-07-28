import unittest


# LeetCode link: https://leetcode.com/problems/valid-anagram/
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_dict = {}
    for c in s:
        char_dict[c] = char_dict.get(c, 0) + 1

    for c in t:
        char_dict[c] = char_dict.get(c, 0) - 1
        if char_dict[c] < 0:
            return False
        elif char_dict[c] == 0:
            char_dict.pop(c)

    return len(char_dict) == 0


class ValidAnagram(unittest.TestCase):
    def test_01(self):
        self.assertEqual(True, is_anagram("anagram", "nagaram"))

    def test_02(self):
        self.assertEqual(False, is_anagram("rat", "cat"))

    def test_03(self):
        self.assertEqual(False, is_anagram("ac", "bb"))
