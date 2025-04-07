class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None
        

    def Append(self, value):

        new_node = Node(value)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        else:
            Current_node = self.head
            while Current_node.next is not None:
                Current_node = Current_node.next
            
            Current_node.next = new_node

        
    def Print(self):
        if self.head is None:
            return "List is empty"
        current_node = self.head
        res = ''
        while current_node is not None:
            res = str(current_node.data) + '-->'
            current_node = current_node.next
        return res
    

obj = LinkedList()

obj.Append(5)
print(obj.Print())


