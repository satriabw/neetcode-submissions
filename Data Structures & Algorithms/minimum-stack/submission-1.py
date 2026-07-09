class MinStack:

    def __init__(self):
        self._min_stack = []
        self._stack = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        
        if len(self._min_stack) > 0:
            min_val = min(self._min_stack[-1], val)
            self._min_stack.append(min_val)
        else:
            self._min_stack.append(val)
        

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
