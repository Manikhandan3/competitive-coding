class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        j = 1
        while j < len(path):
            s = ""
            while j < len(path) and path[j] != '/':
                s += path[j]
                j += 1
            if stack and s == "..":
                stack.pop()
            elif not s or s == "." or s == "..":
                j += 1
            else:
                stack.append(s)
        res = ""
        for s in stack:
            res += "/" + s
        return "/" if not res else res
            

            