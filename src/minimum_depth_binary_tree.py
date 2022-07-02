import unittest
from typing import Optional

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Time complexity: O(n)
# Space complexity: O(n)
# Starts calling helper(root), then we check if root is null, return 0, if root.left and root.right are null, return 1
# If root.left is null, return 1 + helper of root.right, if root.right is null, return 1 + helper of root.left
# If root.left and root.right are valid, then return 1 + min of root.left and root.right
def min_depth(root: Optional[TreeNode]) -> int:

    def helper(root: TreeNode):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + helper(root.right)
        elif not root.right:
            return 1 + helper(root.left)

        return 1 + min(helper(root.left), helper(root.right))

    return helper(root)


class MinimumDepthBinaryTree(unittest.TestCase):
    def test_01(self):
        root = TreeNode(3, TreeNode(9), TreeNode(9, TreeNode(15), TreeNode(7)))
        self.assertEqual(2, min_depth(root))

    def test_02(self):
        root = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))
        self.assertEqual(5, min_depth(root))

    def test_03(self):
        # [-9, -3, 2, null, 4, 4, 0, -6, null, -5]
        root = TreeNode(-9, TreeNode(-3, right=TreeNode(4, left=TreeNode(-6))),
                        TreeNode(2, TreeNode(4, left=TreeNode(-5)), TreeNode(0)))
        self.assertEqual(3, min_depth(root))
