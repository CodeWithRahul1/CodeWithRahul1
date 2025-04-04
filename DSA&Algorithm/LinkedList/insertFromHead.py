class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def InserHead(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def PrintList(self):
        if self.head is None:
            return 'List Is empty'
        else:
            current_node = self.head
            res = ''
            while current_node is not None:
                res += str(current_node.data) + '-->'
                current_node = current_node.next

            return res

        
obj =  LinkedList()
# obj.InserHead(2)
print(obj.PrintList())


        