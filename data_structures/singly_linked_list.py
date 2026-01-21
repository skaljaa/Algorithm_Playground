class Node:
    def __init__(self,x) -> None:
        self.data = x
        self.next = None

class SinglyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
    
    def insert_beginning(self,x):
        node = Node(x)
        node.next = self.head
        self.head = node
    
    def insert_end(self,x):
        if self.head is None:
            node = Node(x)
            self.head = node
        else:
            current = self.head
            while  current.next is not None:
                current = current.next
            node = Node(x)
            current.next = node
            
    def delete(self,x):
        if self.head is None :
            raise IndexError("empty linked list")
        
        if self.head.data == x:
            self.head = self.head.next
            return "removed"
        previous = self.head
        current = self.head.next
        while current is not None:
            if current.data == x:
                previous.next = current.next
                return "removed"
            previous = current
            current = current.next
            
        if current is None:
            raise IndexError("not in the list")
        
        
    def search(self,x) -> bool:
        if self.head is None :
            raise IndexError("empty linked list")
        current = self.head
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        raise IndexError("not in the list")
    