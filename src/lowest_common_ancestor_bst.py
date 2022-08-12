import unittest

from src.tree_node import TreeNode


# LeetCode link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# TC: O(log n)
# SC: O(log n)
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val < root.val < q.val or q.val < root.val < p.val:
        return root

    if p.val == root.val or q.val == root.val:
        return root

    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    else:
        return lowest_common_ancestor(root.right, p, q)


# LeetCode link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# TC: O(log n)
# SC: O(1)
def lowest_common_ancestor_while(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur


class LowestCommonAncestorBST(unittest.TestCase):
    def test_01(self):
        p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
        q = TreeNode(8, TreeNode(7), TreeNode(9))
        root = TreeNode(6, p, q)
        self.assertEqual(6, lowest_common_ancestor(root, p, q).val)

    def test_02(self):
        q = TreeNode(4, TreeNode(3), TreeNode(5))
        p = TreeNode(2, TreeNode(0), q)
        root = TreeNode(6, p, TreeNode(8, TreeNode(7), TreeNode(9)))
        self.assertEqual(2, lowest_common_ancestor(root, p, q).val)

    def test_03(self):
        q = TreeNode(1)
        p = TreeNode(2, left=q)
        root = p
        self.assertEqual(2, lowest_common_ancestor(root, p, q).val)

    def test_04(self):
        p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
        q = TreeNode(8, TreeNode(7), TreeNode(9))
        root = TreeNode(6, p, q)
        self.assertEqual(6, lowest_common_ancestor_while(root, p, q).val)

    def test_05(self):
        q = TreeNode(4, TreeNode(3), TreeNode(5))
        p = TreeNode(2, TreeNode(0), q)
        root = TreeNode(6, p, TreeNode(8, TreeNode(7), TreeNode(9)))
        self.assertEqual(2, lowest_common_ancestor_while(root, p, q).val)

    def test_05(self):
        q = TreeNode(1)
        p = TreeNode(2, left=q)
        root = p
        self.assertEqual(2, lowest_common_ancestor_while(root, p, q).val)
