class Solution:
    def isValid(self, s: str) -> bool:
        b = {}
        b['}'] = '{'
        b[')'] = '('
        b[']'] = '['
        stack = []
        for c in s:
            if c in b:
                if stack and stack[-1] == b[c]:
                    stack.pop()
                else:
                    return False
            else :
                stack.append(c)
        return True if not stack else False

