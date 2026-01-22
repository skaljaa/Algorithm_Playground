class HashTable:
    
    def __init__(self, size = 10):
        self.size = 10
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key)%self.size
    
    def put(self,key,value):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] == value
        self.table[idx].append([key,value])
        
    def get(self,key):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None
                
    def remove(self,key):
        idx = self._hash(key)
        self.table[idx] = [p for p in self.table[idx] if p[0] != key]