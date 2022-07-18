import collections
import unittest
from typing import Optional, List

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/binary-tree-right-side-view/
# Time complexity: O(n)
# This solution uses dfs to run through binary tree, firstly
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    levels = -1

    def helper(root: TreeNode, level: int):
        nonlocal levels
        if levels < level:
            result.append(root.val)
            levels += 1

        if root.right:
            helper(root.right, level + 1)
        if root.left:
            helper(root.left, level + 1)

    helper(root, 0)

    return result


def right_side_view_ii(root: Optional[TreeNode]) -> List[int]:
    result = []
    nodes_queue = collections.deque([root])

    while nodes_queue:
        right_node = None
        q_len = len(nodes_queue)
        for i in range(q_len):
            node = nodes_queue.popleft()
            if node:
                right_node = node
                nodes_queue.append(right_node.left)
                nodes_queue.append(right_node.right)

        if right_node:
            result.append(right_node.val)

    return result


class BinaryTreeRightSideView(unittest.TestCase):
    def test_01(self):
        root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3, right=TreeNode(4)))
        self.assertEqual([1, 3, 4], right_side_view(root))

    def test_02(self):
        root = TreeNode(1, right=TreeNode(3))
        self.assertEqual([1, 3], right_side_view(root))

    def test_03(self):
        root = TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3))
        self.assertEqual([1, 3, 4], right_side_view(root))

    def test_04(self):
        root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3, right=TreeNode(4)))
        self.assertEqual([1, 3, 4], right_side_view_ii(root))

    def test_05(self):
        root = TreeNode(1, right=TreeNode(3))
        self.assertEqual([1, 3], right_side_view_ii(root))

    def test_06(self):
        root = TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3))
        self.assertEqual([1, 3, 4], right_side_view_ii(root))

    def test_07(self):
        root = TreeNode(1, left=TreeNode(2))
        self.assertEqual([1, 2], right_side_view_ii(root))
