import unittest


# LeetCode link: https://leetcode.com/problems/first-unique-character-in-a-string/
# TC: O(n)
# SC: O(1), because English letters has only 26 characters
def first_uniq_char(s: str) -> int:
    count = [0] * 26

    for i in range(len(s)):
        pos = ord(s[i]) - ord('a')
        count[pos] = count[pos] + 1

    for i in range(len(s)):
        if count[ord(s[i]) - ord('a')] == 1:
            return i

    return -1


class FirstUniqueCharacterString(unittest.TestCase):
    def test_01(self):
        self.assertEqual(0, first_uniq_char("leetcode"))

    def test_02(self):
        self.assertEqual(2, first_uniq_char("loveleetcode"))

    def test_03(self):
        self.assertEqual(-1, first_uniq_char("aabb"))
