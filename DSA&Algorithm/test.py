class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None


    def InsertFromBegning(self, value):
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    
    def PrintLinst(self):
        if self.head is None:
            return 'List is Empty'

        current_node = self.head
        res = ''

        while current_node is not None:

            res += str(current_node.data) + '-->'
            current_node = current_node.next 
        return res
    


obj = LinkedList()
obj.InsertFromBegning(3)
obj.InsertFromBegning(4)
obj.InsertFromBegning(5)
obj.InsertFromBegning(6)
print(obj.PrintLinst())




        