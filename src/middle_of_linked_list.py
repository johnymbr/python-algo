import unittest
from typing import Optional

from src.list_node import ListNode


# Leetcode link: https://leetcode.com/problems/middle-of-the-linked-list/description/
# TC: O(n)
# SC: O(1)
# We use the approach slow and fast pointer to solve this problem.
# The slow pointer moves one by one and fast pointer moves two nodes.
# When the fast pointer reaches the end of the list( f == null or f.next == null), then
# slow pointer is in the middle of the list.
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    s = f = head

    while f and f.next:
        s = s.next
        f = f.next.next

    return s


class MiddleOfLinkedList(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(3, middle_node(head).val)

    def test_02(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        self.assertEqual(4, middle_node(head).val)
