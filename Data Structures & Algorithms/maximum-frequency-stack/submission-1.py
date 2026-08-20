class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(list)
        self.maxF = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.maxF = max(self.maxF,self.count[val])
        self.freq[self.count[val]].append(val)

    def pop(self) -> int:
        value = self.freq[self.maxF].pop()
        self.count[value] -= 1
        if not self.freq[self.maxF]:
            self.maxF -= 1
        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()