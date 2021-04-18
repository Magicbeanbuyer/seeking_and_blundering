import pytest
from src.algorithms.remove_nth_node_from_end_of_list import ListNode, Solution

length = 6
node_list = [ListNode(i) for i in range(length)]
for i in range(length):
    try:
        node_list[i].next = node_list[i + 1]
        print(node_list[i])
    except IndexError:
        print(f"last {node_list[i]}")


def test_measure_list_length():
    assert Solution.measure_list_length(node_list[0]) == length
