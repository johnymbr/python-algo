import unittest
from typing import Optional

from src.list_node import ListNode


def is_palindrome(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head

    # find middle point
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse last half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


class PalindromeLinkedList(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertEqual(True, is_palindrome(head))

    def test_02(self):
        head = ListNode(1, ListNode(2))
        self.assertEqual(False, is_palindrome(head))
