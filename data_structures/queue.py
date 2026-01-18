class Queue:
    
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self,x:int):
        self.items.append(x)
        print(f"{x} enqueued")
    
    def is_empty(self) -> bool :
        return len(self.items) == 0
        
    def dequeue(self) -> int:
        if not self.is_empty():
            x = self.items.pop(0)
            print(f"{x} dequeued")
            return x
        else:
            raise IndexError("Empty queue")
    def peek(self) -> int:
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Empty queue")
        