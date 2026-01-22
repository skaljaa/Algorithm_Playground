class PriorityQueue:
    def __init__(self):
        self.queue = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def shiftUp(self, i):
        while i > 0 and self.queue[self.parent(i)] < self.queue[i]:
            p = self.parent(i)
            self.queue[p], self.queue[i] = self.queue[i], self.queue[p]
            i = p

    def shiftDown(self, i):
        maxIndex = i
        l = self.leftChild(i)
        r = self.rightChild(i)

        if l < len(self.queue) and self.queue[l] > self.queue[maxIndex]:
            maxIndex = l
        if r < len(self.queue) and self.queue[r] > self.queue[maxIndex]:
            maxIndex = r

        if i != maxIndex:
            self.queue[i], self.queue[maxIndex] = self.queue[maxIndex], self.queue[i]
            self.shiftDown(maxIndex)

    def insert(self, value):
        self.queue.append(value)
        self.shiftUp(len(self.queue) - 1)

    def pop(self):
        if not self.queue:
            return None
        result = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        if self.queue:
            self.shiftDown(0)
        return result

    def getMax(self):
        return self.queue[0] if self.queue else None
