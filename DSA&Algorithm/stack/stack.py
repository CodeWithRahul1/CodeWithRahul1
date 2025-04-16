class Stack:

    def __init__(self):
        self.stack = []

    def append_item(self, item):
        return self.stack.append(item)
    
    def pop_item(self):
        if len(self.stack) == 0:
            return 'Stack is empty'
        self.stack.pop()

    
s = Stack()
print(s.pop_item())
s.append_item(2)
s.append_item(3)
s.append_item(4)
s.pop_item()
print(s.stack)
