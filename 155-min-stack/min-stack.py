class MinStack:

    def __init__(self):
        self.mainStk = []
        self.minStk = []
        

    def push(self, val: int) -> None:
        self.mainStk.append(val)
        if len(self.minStk) == 0 or val < self.minStk[-1]:
            self.minStk.append(val)
        else:
            self.minStk.append(self.minStk[-1])

    def pop(self) -> None:
        topItem = self.mainStk.pop(-1)
        self.minStk.pop(-1)
        return topItem
        
    def top(self) -> int:
        return self.mainStk[-1]
        

    def getMin(self) -> int:
        return self.minStk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()