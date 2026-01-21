class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
    def insert_beginning(self,data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            self.head = node
            return
        self.head = node
    
    def insert_end(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            node = Node(data)
            node.prev = current
            current.next = node
    def delete(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                # Handle head case
                if current.prev is None:
                    self.head = current.next
                    if current.next is not None:
                        current.next.prev = None
                    return "removed"
                
                # Handle tail case
                if current.next is None:
                    current.prev.next = None
                    return "removed"
                
                # Handle middle case
                current.prev.next = current.next
                current.next.prev = current.prev
                return "removed"
            
            current = current.next
        raise IndexError("not in the list")
        
    def traverse_forward(self):
        current  = self.head 
        while current is not None:
            print(f"{current.data} -> ")
            current = current.next
    def traverse_backwards(self):
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(f"{current.data} -> ")
            current = current.prev