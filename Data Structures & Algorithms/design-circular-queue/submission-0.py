class MyCircularQueue:

    def __init__(self, k: int):
        self._queue = [0] * k
        self._front = None
        self._rear = None
        self._k = k

        self._size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # Empty array
        if self.isEmpty():
            self._queue[0] = value
            self._front = 0
            self._rear = 0

        else:
            rear = (self._rear + 1) % self._k
            self._queue[rear] =  value
            self._rear = rear
        
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        front = (self._front + 1) % self._k
        val = self._queue[self._front]
        self._front = front
        self._size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self._queue[self._front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self._queue[self._rear]
        

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()