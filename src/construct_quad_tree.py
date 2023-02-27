import queue
import unittest
from typing import List

from src.quad_tree_node import TreeNode


def construct(grid: List[List[int]]) -> TreeNode:
    def check(row_s, row_e, col_s, col_e) -> TreeNode:
        first_value = None
        for r in range(row_s, row_e, 1):
            for c in range(col_s, col_e, 1):
                if first_value is None:
                    first_value = grid[r][c]
                elif grid[r][c] != first_value:
                    tl = check(row_s, row_s + (row_e - row_s) // 2, col_s, col_s + (col_e - col_s) // 2)
                    tr = check(row_s, row_s + (row_e - row_s) // 2, col_s + (col_e - col_s) // 2, col_e)
                    bl = check(row_s + (row_e - row_s) // 2, row_e, col_s, col_s + (col_e - col_s) // 2)
                    br = check(row_s + (row_e - row_s) // 2, row_e, col_s + (col_e - col_s) // 2, col_e)

                    if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
                        if tl.val == tr.val == bl.val == br.val:
                            return TreeNode(val=tl.val, isLeaf=True, topLeft=tl, topRight=tr, bottomLeft=bl,
                                            bottomRight=br)
                    return TreeNode(val=1, isLeaf=False, topLeft=tl, topRight=tr, bottomLeft=bl,
                                    bottomRight=br)

        return TreeNode(val=first_value, isLeaf=True)

    return check(0, len(grid), 0, len(grid))


def transform(root: TreeNode) -> List[List[int]]:
    answer = [None] * (64 * 64)
    q = queue.Queue()
    q.put((0, root))

    last_index = None
    while not q.empty():
        position, node = q.get()
        answer.insert(position, [1 if node.isLeaf else 0, node.val])
        last_index = position

        if node.topLeft: q.put((4 * position + 1, node.topLeft))
        if node.topRight: q.put((4 * position + 2, node.topRight))
        if node.bottomLeft: q.put((4 * position + 3, node.bottomLeft))
        if node.bottomRight: q.put((4 * position + 4, node.bottomRight))

    return answer[:last_index + 1] if last_index else answer


class ConstructQuadTree(unittest.TestCase):
    def test_01(self):
        self.assertEqual([[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]], transform(construct([[0, 1], [1, 0]])))

    def test_02(self):
        self.assertEqual(
            [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]], transform(
                construct([[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
                           [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
                           [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]])))
