class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        sizes = []
        res = ""
        c = 0
        while c < len(s):
            while s[c] >= '0' and s[c] <= '9':
                res += s[c]
                c += 1
            if res : 
                sizes.append(int(res))
                res = ""
            if s[c]!=']':
                stack.append(s[c])
                c += 1
            else:
                while stack[-1]!='[':
                    res += stack.pop()
                stack.pop()
                stack.append(res*sizes.pop())
                res = ""
                c += 1
        while stack:
            res += stack.pop()
        return res[::-1]

            