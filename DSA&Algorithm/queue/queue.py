class Queue:

    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue)==0:
            return 'Queue is empty'
        
        self.queue.pop(0)

    def inqueue(self, item):
        return self.queue.append(item)
    
q = Queue()
print(q.dequeue())
q.inqueue(2)
q.inqueue(3)
print(q.queue)