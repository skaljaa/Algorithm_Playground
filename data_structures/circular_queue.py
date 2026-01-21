class CircularQueue:
    def __init__(self,x):
        self.queue = [None]*x
        self.capacity = x
        self.front = -1
        self.rear = -1
    
    def enqueue(self, x):
        if self.is_full():
            raise IndexError("queue is full")
        
        # First element case
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            # Move rear forward with wrap-around
            self.rear = (self.rear + 1) % self.capacity
        
        # Place item at rear
        self.queue[self.rear] = x
    
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty queue")
        item = self.queue[self.front]
        if self.rear == self.front:
            self.rear = -1
            self.front =  -1
        else:
            self.front = (self.front+1)%self.capacity
        
        return item
    def peek(self):
        if self.isempty():
            raise IndexError("empty queue")
        return self.queue[self.front]
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front