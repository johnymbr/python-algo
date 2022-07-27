import unittest
from typing import Optional, List

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# TC O(n)
# SC O(n)
# We use dfs with stack. As we use stack, so in the worst case the stack would have size of n.
def flatten(root: Optional[TreeNode]) -> None:
    if not root:
        return None

    last = None
    my_stack = [root]
    while my_stack:
        tmp = my_stack.pop()

        if tmp.right:
            my_stack.append(tmp.right)
        if tmp.left:
            my_stack.append(tmp.left)

        tmp.right, tmp.left = None, None
        if last:
            last.right = tmp

        last = tmp


def convert_to_list(root: TreeNode) -> List:
    res = []
    while root:
        res.append(root.val)
        if root.right:
            res.append(root.left)
        root = root.right

    return res


class FlattenBTreeLinkedList(unittest.TestCase):
    def test_01(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, right=TreeNode(6)))
        flatten(root)
        self.assertEqual([1, None, 2, None, 3, None, 4, None, 5, None, 6], convert_to_list(root))

    def test_02(self):
        root = None
        flatten(root)
        self.assertEqual([], convert_to_list(root))

    def test_03(self):
        root = TreeNode(0)
        flatten(root)
        self.assertEqual([0], convert_to_list(root))
