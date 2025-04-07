class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublelInkedList:

    def __init__(self):
        self.head = None


    def DoubleLinkedList(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

        



