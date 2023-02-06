import unittest
from typing import Optional

from src.tree_node import TreeNode


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    sum = 0

    if low <= root.val <= high:
        sum += root.val

    if root.val > low and root.left:
        sum += range_sum_bst(root.left, low, high)

    if root.val < high and root.right:
        sum += range_sum_bst(root.right, low, high)

    return sum


class RangeSumOfBST(unittest.TestCase):
    def test_01(self):
        root = TreeNode(10, TreeNode(5, TreeNode(5), TreeNode(7)), TreeNode(15, right=TreeNode(18)))
        self.assertEqual(32, range_sum_bst(root, 7, 15))

    def test_02(self):
        root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))), TreeNode(15, TreeNode(13), TreeNode(18)))
        self.assertEqual(23, range_sum_bst(root, 6, 10))