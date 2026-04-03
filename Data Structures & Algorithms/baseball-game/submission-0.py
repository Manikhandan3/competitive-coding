class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for c in operations:
            if c == 'D':
                stack.append(2*stack[-1])
            elif c == '+':
                stack.append(stack[-1]+stack[-2])
            elif c == 'C':
                stack.pop()
            else :
                stack.append(int(c))
        res = 0
        for s in stack:
            res += s
        return res