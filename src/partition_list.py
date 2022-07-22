import unittest
from typing import Optional

from src.list_node import ListNode


# LeetCode link: https://leetcode.com/problems/partition-list/
# TC O(n)
# SC O(1)
# To solve this problem, we create two dummy list, and
# if head is less than x, we put in left list, if not, we put in right list.
# after the loop we connect left to right list and set right last next node to none
def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    left, right = ListNode(), ListNode()
    l_tail, r_tail = left, right

    while head:
        if head.val < x:
            l_tail.next = head
            l_tail = l_tail.next
        else:
            r_tail.next = head
            r_tail = r_tail.next

        head = head.next

    l_tail.next = right.next
    r_tail.next = None

    return left.next


def convert_to_list(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res


class PartitionList(unittest.TestCase):
    def test_01(self):
        head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        self.assertEqual([1, 2, 2, 4, 3, 5], convert_to_list(partition(head, 3)))

    def test_02(self):
        head = ListNode(2, ListNode(1))
        self.assertEqual([1, 2], convert_to_list(partition(head, 2)))
