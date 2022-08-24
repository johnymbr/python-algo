from typing import Optional

from src.list_node import ListNode


def delete_node(node: Optional[ListNode]):
    node.val = node.next.val
    node.next = node.next.next