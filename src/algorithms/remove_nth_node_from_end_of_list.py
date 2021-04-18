from pprint import pprint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"node value: {self.val}"


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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth_node_i = n - (i - 1)
        pass


if __name__ == "__main__":
    linked_list_dict = {f"n{i}": ListNode(i) for i in range(6)}
    pprint(linked_list_dict)
