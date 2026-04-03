class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.s2 or self.s2[-1]>=val:
            self.s2.append(val)
    

    def pop(self) -> None:
        if self.s1.pop() == self.s2[-1]:
            self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]
