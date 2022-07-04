import unittest
from typing import Optional, List

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Time complexity: O(n)
# Space complexity: O(n)
# Loop through stack, if curr node left and right are none, put cur val on res.
# If right isn't none put on stack and set right none. Do the same with left.
# If change the tree isn't possible, so we can use a loop to put in pre-order
# and then another loop to make the answer as post-order.
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    if not root:
        return res

    stack = [root]
    while len(stack) > 0:
        cur_node = stack[-1]
        if not cur_node.left and not cur_node.right:
            cur_node = stack.pop()
            res.append(cur_node.val)
        else:
            if cur_node.right:
                stack.append(cur_node.right)
                cur_node.right = None
            if cur_node.left:
                stack.append(cur_node.left)
                cur_node.left = None

    return res


def postorder_traversal_ii(root: Optional[TreeNode]) -> List[int]:
    res = []

    if not root:
        return res

    stack = [root]
    temp_stack = []
    while stack:
        cur = stack.pop()
        temp_stack.append(cur.val)

        if cur.left:
            stack.append(cur.left)

        if cur.right:
            stack.append(cur.right)

    while temp_stack:
        res.append(temp_stack.pop())

    return res


class BinaryTreePostOrderTraversal(unittest.TestCase):
    def test_01(self):
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        self.assertEqual([3, 2, 1], postorder_traversal(root))

    def test_02(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, right=TreeNode(6)))
        self.assertEqual([4, 5, 2, 6, 3, 1], postorder_traversal(root))

    def test_03(self):
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        self.assertEqual([3, 2, 1], postorder_traversal_ii(root))

    def test_04(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, right=TreeNode(6)))
        self.assertEqual([4, 5, 2, 6, 3, 1], postorder_traversal_ii(root))
