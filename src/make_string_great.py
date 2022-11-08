import unittest


# Leetcode link: https://leetcode.com/problems/make-the-string-great/description/
# TC: O(n)
# SC: O(1)
def make_good(s: str) -> str:
    end = 0

    for i in range(len(s)):
        if end > 0 and abs(ord(s[i]) - ord(s[end - 1])) == 32:
            end -= 1
        else:
            s = s[:end] + s[i] + s[end + 1:]
            end += 1

    return s[0:end]


# Leetcode link: https://leetcode.com/problems/make-the-string-great/description/
# TC: O(n)
# SC: O(n)
def make_good_stack(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if not stack or abs(ord(s[i]) - ord(stack[-1])) != 32:
            stack.append(s[i])
        else:
            stack.pop()

    return "".join(stack)


class MakeStringGreat(unittest.TestCase):
    def test_01(self):
        self.assertEqual("leetcode", make_good("leEeetcode"))

    def test_02(self):
        self.assertEqual("", make_good("abBAcC"))

    def test_03(self):
        self.assertEqual("leetcode", make_good_stack("leEeetcode"))

    def test_04(self):
        self.assertEqual("", make_good_stack("abBAcC"))
