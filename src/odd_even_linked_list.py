import unittest
from typing import Optional

from src.list_node import ListNode


# Leetcode link: https://leetcode.com/problems/odd-even-linked-list/description/
# TC: O(n)
# SC: O(1)
# We loop through the list and use 4 pointers to store the last odd node, the head and last even nodes.
# We use a counter to check if the actual node is odd
# and after the loop we join the last odd node with the head of even nodes.
def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    p_odd = ListNode(-1)
    dummy_even = ListNode(-1)
    p_even = dummy_even

    count = 1
    aux = head
    while aux:
        if count % 2 != 0:
            p_odd.next = aux
            p_odd = aux
        else:
            p_even.next = aux
            p_even = aux

        aux = aux.next
        count += 1

    p_odd.next = dummy_even.next
    p_even.next = None
    return head


def convert(head: ListNode):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next

    return ans


class OddEvenLinkedList(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual([1,3,5,2,4], convert(odd_even_list(head)))

    def test_02(self):
        head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
        self.assertEqual([2,3,6,7,1,5,4], convert(odd_even_list(head)))