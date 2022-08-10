import unittest
from typing import Optional

from src.list_node import ListNode


# LeetCode link: https://leetcode.com/problems/reverse-linked-list/
# TC: O(n)
# SC: O(1)
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    tail = None
    while head:
        h_next = head.next
        tmp = tail
        tail = head
        tail.next = tmp
        head = h_next

    return tail


def convert(head: ListNode) -> [int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res


class ReverseLinkedList(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual([5, 4, 3, 2, 1], convert(reverse_list(head)))

    def test_02(self):
        head = ListNode(1, ListNode(2))
        self.assertEqual([2, 1], convert(reverse_list(head)))
