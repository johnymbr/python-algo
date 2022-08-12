import unittest
from typing import Optional

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/validate-binary-search-tree/
# TC: O(n)
# SC: O(n)
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def helper(node: TreeNode, left: int, right: int) -> bool:
        if not node:
            return True

        if not (right > node.val > left):
            return False

        return helper(node.left, left, node.val) and helper(node.right, node.val, right)

    return helper(root, float("-inf"), float("inf"))


class ValidateBinarySearchTree(unittest.TestCase):
    def test_01(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(True, is_valid_bst(root))

    def test_02(self):
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(False, is_valid_bst(root))
