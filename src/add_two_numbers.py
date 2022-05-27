import unittest
from typing import Optional

from src.list_node import ListNode


# LeetCode Link: https://leetcode.com/problems/add-two-numbers/
# Solving this using carry, follow each linked list,
# sum values, and calculate the first digit and carry for the next loop.
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode(val=0)
    curr_node = dummy_node
    carry = 0
    while l1 is not None or l2 is not None:
        vl1 = 0
        vl2 = 0
        if l1 is not None:
            vl1 = l1.val
            l1 = l1.next

        if l2 is not None:
            vl2 = l2.val
            l2 = l2.next

        sum = vl1 + vl2 + carry
        digit = sum % 10
        carry = int(sum / 10)

        curr_node.next = ListNode(val=digit)
        curr_node = curr_node.next

    if carry > 0:
        curr_node.next = ListNode(val=carry)

    return dummy_node.next


class AddTwoNumbersTest(unittest.TestCase):
    def test_01(self):
        l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
        l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
        result = add_two_numbers(l1, l2)
        self.assertEqual(result.val, 7)

    def test_02(self):
        l1 = ListNode(val=0)
        l2 = ListNode(val=0)
        result = add_two_numbers(l1, l2)
        self.assertEqual(result.val, 0)

    def test_03(self):
        l1 = ListNode(val=9,
                      next=ListNode(val=9,
                                    next=ListNode(val=9,
                                                  next=ListNode(val=9,
                                                                next=ListNode(val=9,
                                                                              next=ListNode(val=9,
                                                                                            next=ListNode(val=9)))))))
        l2 = ListNode(val=9,
                      next=ListNode(val=9,
                                    next=ListNode(val=9,
                                                  next=ListNode(val=9))))
        result = add_two_numbers(l1, l2)
        self.assertEqual(result.val, 8)


if __name__ == "__main__":
    unittest.main()
