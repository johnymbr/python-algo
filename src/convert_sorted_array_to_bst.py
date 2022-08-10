import unittest
from typing import List, Optional

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# TC: O(n)
# SC: O(log n) -> representing the height of tree.
def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    def helper(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)

        return root

    return helper(0, len(nums) - 1)


def convert(root: TreeNode) -> [int]:
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


class SortedArrayToBST(unittest.TestCase):
    def test_01(self):
        self.assertEqual([0, -10, 5, -3, 9], convert(sorted_array_to_bst([-10, -3, 0, 5, 9])))

    def test_02(self):
        self.assertEqual([1, 3], convert(sorted_array_to_bst([1, 3])))
