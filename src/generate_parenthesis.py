import unittest
from typing import List


# LeetCode link: https://leetcode.com/problems/generate-parentheses/
# Time complexity O(4^n/sqroot(n))
# To solve this problem we use backtracking.
def generate_parenthesis(n: int) -> List[str]:
    ans = []

    def backtrack(tmp=[], l=0, r=0):
        if len(tmp) == 2 * n:
            ans.append("".join(tmp))
            return

        if l < n:
            tmp.append('(')
            backtrack(tmp, l + 1, r)
            tmp.pop()

        if r < l:
            tmp.append(')')
            backtrack(tmp, l, r + 1)
            tmp.pop()

    backtrack()
    return ans


class GenerateParenthesis(unittest.TestCase):
    def test_01(self):
        self.assertEqual(["((()))", "(()())", "(())()", "()(())", "()()()"], generate_parenthesis(3))
