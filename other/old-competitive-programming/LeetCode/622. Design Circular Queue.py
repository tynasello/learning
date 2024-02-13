class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [0 for i in range(k)]
        self.cap = k
        self.size = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.cq[self.rear] = value
            self.rear = (self.rear+1) % self.cap
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front+1) % self.cap
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        return self.cq[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.cq[self.rear-1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.cap == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
