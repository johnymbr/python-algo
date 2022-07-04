import unittest
from typing import Optional, List

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Time complexity: O(n)
# Using a stack to traverse the tree iteratively.
# At each loop, we pop the stack, put val on the variable res
# and append the stack with right and left node of current node.
# preorder: root -> left -> right
def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    if not root:
        return res

    # preorder root -> left -> right
    stack = [root]
    while len(stack) > 0:
        cur_node = stack.pop()
        res.append(cur_node.val)
        if cur_node.right:
            stack.append(cur_node.right)
        if cur_node.left:
            stack.append(cur_node.left)

    return res


class BinaryTreePreOrderTraversal(unittest.TestCase):
    def test_01(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, right=TreeNode(6)))
        self.assertEqual([1, 2, 4, 5, 3, 6], preorder_traversal(root))

    def test_02(self):
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        self.assertEqual([1, 2, 3], preorder_traversal(root))

    def test_03(self):
        root = TreeNode(1)
        self.assertEqual([1], preorder_traversal(root))
