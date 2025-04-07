class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None

    def InsertOnValue(self, target, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        Current_head = self.head
        while Current_head is not None:
            if Current_head.data == target:
                new_node.next = Current_head.next
                Current_head.next = new_node
                return
            Current_head = Current_head.next

        return 'Value is not present'
    
    def Print(self):

        current_node = self.head
        res = ''
        while current_node is  not None:
            res = str(current_node.data) + '-->'
            current_node = current_node.next
        return res


                      

        
        

obj = LinkedList()
obj.InsertOnValue(1, 1)
obj.InsertOnValue(1, 2)
print(obj.Print())
            