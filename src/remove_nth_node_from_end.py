import math
import unittest
from typing import Optional

from src.list_node import ListNode


# LeetCode link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# To solve this problem, I used two pointers and dummy node approach. The left pointer starts
# in dummy node and the right pointer must be on head + n nodes.
# After this, a loop starts until right pointer is not null, and left and right pointer go to next node.
# When loop stops, I change the next field of left node to next position of next (left.next = left.next.next).
# In the end, the method returns dummy next node.
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    l = dummy
    r = head
    while n > 0 and r:
        r = r.next
        n -= 1

    while r:
        l = l.next
        r = r.next

    l.next = l.next.next

    return dummy.next


class RemoveNthNodeFromEnd(unittest.TestCase):
    def runOverNodes(self, head: ListNode):
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res

    def test_01(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual([1, 2, 3, 5], self.runOverNodes(remove_nth_from_end(head, 2)))

    def test_02(self):
        head = ListNode(1)
        self.assertEqual([], self.runOverNodes(remove_nth_from_end(head, 1)))

    def test_03(self):
        head = ListNode(1, ListNode(2))
        self.assertEqual([1], self.runOverNodes(remove_nth_from_end(head, 1)))

    def test_04(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        self.assertEqual([1, 2, 3, 4, 6], self.runOverNodes(remove_nth_from_end(head, 2)))

    def test_05(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        self.assertEqual([1, 2, 3, 4, 5], self.runOverNodes(remove_nth_from_end(head, 1)))

    def test_06(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual([2, 3], self.runOverNodes(remove_nth_from_end(head, 3)))

    def test_07(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual([1, 3], self.runOverNodes(remove_nth_from_end(head, 2)))

    def test_08(self):
        head = ListNode(1,
                        ListNode(2,
                                 ListNode(3,
                                          ListNode(4,
                                                   ListNode(5,
                                                            ListNode(6,
                                                                     ListNode(7, ListNode(8,
                                                                                          ListNode(9,
                                                                                                   ListNode(
                                                                                                       10))))))))))
        self.assertEqual([1, 2, 3, 5, 6, 7, 8, 9, 10], self.runOverNodes(remove_nth_from_end(head, 7)))
