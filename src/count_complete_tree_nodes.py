import unittest
from typing import Optional

from src.tree_node import TreeNode


# Leetcode link: https://leetcode.com/problems/count-complete-tree-nodes/description/
# TC: O(logN * logN)
# SC: O(logN)
# We check every tree and calculate if left and right nodes have the same value,
# if not, we check next tree.
def count_nodes(root: Optional[TreeNode], l=1, r=1) -> int:
    if not root:
        return 0

    left = right = root

    while left := left.left:
        l += 1
    while right := right.right:
        r += 1

    if l == r:
        return 2 ** l - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)


class CountCompleteTreeNodes(unittest.TestCase):
    def test_01(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        self.assertEqual(6, count_nodes(root))

    def test_02(self):
        self.assertEqual(0, count_nodes(None))

    def test_03(self):
        self.assertEqual(1, count_nodes(TreeNode(1)))
