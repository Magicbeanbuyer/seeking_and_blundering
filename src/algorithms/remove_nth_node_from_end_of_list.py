from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"data: {self.val} pointer: {self.next}"


class Solution:
    @staticmethod
    def measure_list_length(head: ListNode) -> int:
        """The method measured the lengh of a list"""

        i = 0
        temp_node = head
        while temp_node.next:
            i += 1
            temp_node = temp_node.next

        return i + 1

    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        list_length = self.measure_list_length(head)
        nth_node_index = list_length - n
        if nth_node_index == 0:
            return head.next

        i = 1
        node_a = head
        while i < nth_node_index:
            node_a = node_a.next
            i += 1

        node_a.next = node_a.next.next
        return head
