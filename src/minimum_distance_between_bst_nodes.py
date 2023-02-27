import queue
from typing import Optional

from src.tree_node import TreeNode


def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    max_diff = 2**31
    def helper(root, p_dist) -> int:

        left_diff = p_dist
        if root.left:
            left_diff = min(left_diff, helper(root.left, p_dist + (root.val - root.left.val)))

        right_diff = p_dist
        if root.right:
            right_diff = min(right_diff, helper(root.right, p_dist + (root.val - root.right.val)))

        return min(abs(left_diff), abs(right_diff))