import unittest


# Leetcode link: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# TC: O(n)
# SC: O(n)
# We use a set with vowels and an approach with two pointers left and right.
# We transform a str to list, to handle swaps.
def reverse_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    l = 0
    r = len(s) - 1

    res = list(s)
    while l < r:
        if s[l] in vowels and s[r] in vowels:
            aux = s[l]
            res[l] = s[r]
            res[r] = aux
            l += 1
            r -= 1
        else:
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1

    return "".join(res)


class ReverseVowelsString(unittest.TestCase):
    def test_01(self):
        self.assertEqual("holle", reverse_vowels("hello"))

    def test_02(self):
        self.assertEqual("leotcede", reverse_vowels("leetcode"))
