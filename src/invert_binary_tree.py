import unittest
from typing import Optional

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/invert-binary-tree/
# TC: O(n)
# SC: O(n)
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.right, root.left = root.left, root.right

    if root.left:
        invert_tree(root.left)

    if root.right:
        invert_tree(root.right)

    return root


def convert(root: TreeNode) -> [int]:
    res = []
    q = [root]
    while q:
        tmp = q.pop(0)
        res.append(tmp.val)

        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)

    return res


class InvertBinaryTree(unittest.TestCase):
    def test_01(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        self.assertEqual([4, 7, 2, 9, 6, 3, 1], convert(invert_tree(root)))

    def test_02(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual([2, 3, 1], convert(invert_tree(root)))
