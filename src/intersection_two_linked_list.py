import unittest
from typing import Optional

from src.list_node import ListNode


# LeetCode Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# l1 starts at headA and l2 starts at headB
# loop will continue until l1 isn't equal l2,
# when l1 comes to end, it starts at headB and when l2 comes to end, it starts at headA
def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1, l2 = headA, headB

    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA

    return l1


class IntersectionTwoLinkedList(unittest.TestCase):
    def test_01(self):
        intersected = ListNode(val=8, next=ListNode(val=4, next=ListNode(val=5)))
        head_a = ListNode(val=4, next=ListNode(val=1, next=intersected))
        head_b = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=1, next=intersected)))
        self.assertEqual(8, get_intersection_node(head_a, head_b).val)

    def test_02(self):
        intersected = ListNode(val=2, next=ListNode(val=4))
        head_a = ListNode(val=1, next=ListNode(val=9, next=ListNode(val=1, next=intersected)))
        head_b = ListNode(val=3, next=intersected)
        self.assertEqual(2, get_intersection_node(head_a, head_b).val)

    def test_03(self):
        head_a = ListNode(val=2, next=ListNode(val=6, next=ListNode(val=4)))
        head_b = ListNode(val=1, next=ListNode(val=5))
        self.assertEqual(None, get_intersection_node(head_a, head_b))
