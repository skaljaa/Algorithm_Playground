class DoubleHashTable:
    
    def __init__(self,size=11):
        
        self.size = size
        self.table = [None]*size
        self.DELETED = object()
        
    def _h1(self,key):
        return hash(key)%self.size
    
    def _h2(self,key):
        return 1+(hash(key)%(self.size-1))
    
    def set(self,key,value):
        for i in range(self.size):
            idx = (self._h1(key) + i * self._h2(key)) % self.size
            if self.table[idx] is None:
                self.table[idx] = (key,value)
                return
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        raise RuntimeError("Hash table full")
    
    def get(self,key):
        for i in range(self.size):
            idx = (self._h1(key) + i * self._h2(key)) % self.size
            if self.table[idx] is None:
                return None
            if self.table[idx] != self.DELETED and self.table[idx][0] == key:
                return self.table[idx][1]
        return None
    
    def remove(self, key):
        for i in range(self.size):
            idx = (self._h1(key) + i * self._h2(key)) % self.size
            if self.table[idx] is None:
                return
            if self.table[idx] != self.DELETED and self.table[idx][0] == key:
                self.table[idx] = self.DELETED
                return