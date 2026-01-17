class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self,x:int):
        
        self.items.append(x)
    
    def pop(self) -> int | str:
        if self.is_empty():
            raise  IndexError("empty stack")
        removed = self.items.pop()
        print(f"popped {removed}")
        return removed
    
    def is_empty(self) -> bool:
        
        return len(self.items) == 0
    
    def peek(self) -> int | str:
        if self.is_empty():
            raise  IndexError("empty stack")
        return self.items[-1]
            
        
    