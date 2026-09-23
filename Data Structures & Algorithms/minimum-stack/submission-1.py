class MinStack:

    def __init__(self):
        self._stack=[]
        self._minStack = []
        
    def push(self, val: int) -> None:
        self._stack.append(val)

        if not self._minStack:
            self._minStack.append(val)
        else:
            self._minStack.append(min(val,self._minStack[-1]))
        
    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
            self._minStack.pop()

    def top(self) -> int:
        if self._stack:
            return self._stack[-1]
        
    def getMin(self) -> int:
        return self._minStack[-1]