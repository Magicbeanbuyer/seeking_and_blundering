class LinkedList:
    def __init__(self, data: int, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"value: {self.data}, pointer: {self.next_node}"


n1 = LinkedList(1)
# print(n1)
n2 = LinkedList(2)
n1.next_node = n2
# print(n1)
n3 = LinkedList(3)
n2.next_node = n3
# print(n1)
print(f"{n1}\n{n2}\n{n3}")


def delete_node(node: LinkedList):
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node


delete_node(n2)

print(f"{n1}\n{n2}\n{n3}")

del n3

print(f"{n1}\n{n2}")
