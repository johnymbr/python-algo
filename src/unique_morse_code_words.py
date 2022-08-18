import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/unique-morse-code-words/
# TC: O(n + len(word))
# SC: O(n)
# We loop through words, for each word we transform to morse
# and put morse_str into map.
# We return the len of the map.
def unique_morse_representation(words: List[str]) -> int:
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    morse_map = {}

    for w in words:
        morse_str = ""
        for c in w:
            morse_str += morse[ord(c) - ord('a')]

        morse_map[morse_str] = True

    return len(morse_map.items())


class UniqueMorseCodeWords(unittest.TestCase):
    def test_01(self):
        self.assertEqual(2, unique_morse_representation(["gin", "zen", "gig", "msg"]))

    def test_02(self):
        self.assertEqual(1, unique_morse_representation(["a"]))
