import unittest


# Leetcode link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
# TC: O(n)
# SC: O(n)
# We use a stack to store the chars and we check if
# the current char is the same as last char in stack.
# if yes, we pop from stack, else we append this char to stack.
def remove_duplicates(s: str) -> str:
    stack = []

    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()

    return "".join(stack)


class RemoveAllAdjacentDuplicatesInString(unittest.TestCase):
    def test_01(self):
        self.assertEqual("ca", remove_duplicates("abbaca"))

    def test_02(self):
        self.assertEqual("ay", remove_duplicates("azxxzy"))
