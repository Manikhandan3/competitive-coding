class MinStack:

    def __init__(self):
        self.s = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(0)
            self.min = val
        else:  
            self.s.append(val-self.min)
            self.min = min(val,self.min)
    

    def pop(self) -> None:
        if not self.s:
            return
        top = self.s.pop()
        if top < 0:
            self.min = self.min - top

    def top(self) -> int:
        top = self.s[-1]

        if top > 0:
            return self.min + top
        return self.min

    def getMin(self) -> int:
        return self.min
