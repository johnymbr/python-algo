import unittest
from typing import Optional

from src.list_node import ListNode


# LeetCode link: https://leetcode.com/problems/remove-linked-list-elements/
# TC: O(n)
# SC: O(1)
def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(-1, next=head)

    previous = dummy
    while head:
        if head.val == val:
            previous.next = head.next
        else:
            previous = head

        head = head.next

    return dummy.next


def convert(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res


class RemoveLinkedListElement(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
        self.assertEqual([1, 2, 3, 4, 5], convert(remove_elements(head, 6)))

    def test_02(self):
        self.assertEqual([], convert(remove_elements(None, 1)))

    def test_03(self):
        head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
        self.assertEqual([], convert(remove_elements(head, 7)))
