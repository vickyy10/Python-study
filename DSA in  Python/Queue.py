

# creating queue using class 
# FIFO


class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):

        if self.is_empty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def display(self):
        return self.queue
    
queue=Queue()


queue.enqueue('Task 1')
queue.enqueue('Task 2')
queue.enqueue('Task 3')

print("Initial Queue:")
print(queue.display())


print(f"\nDequeued: {queue.dequeue()}")
print("Queue after dequeue:")
print(queue.display())
