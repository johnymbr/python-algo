import unittest
from typing import Optional

from src.list_node import ListNode


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(-1, head)

    left_p = dummy
    cur = head
    for i in range(left - 1):
        left_p, cur = cur, cur.next

    p = None
    for i in range(right - left + 1):
        tmp_next = cur.next
        cur.next = p
        p, cur = cur, tmp_next

    left_p.next.next = cur
    left_p.next = p

    return dummy.next


def convert_to_list(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res


class ReverseLinkedListII(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual([1, 4, 3, 2, 5], convert_to_list(reverse_between(head, 2, 4)))

    def test_02(self):
        head = ListNode(5)
        self.assertEqual([5], convert_to_list(reverse_between(head, 1, 1)))

    def test_03(self):
        heap = ListNode(3, ListNode(5))
        self.assertEqual([5, 3], convert_to_list(reverse_between(heap, 1, 2)))
