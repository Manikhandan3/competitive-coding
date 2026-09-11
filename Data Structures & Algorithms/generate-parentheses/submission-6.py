class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtrack(open, close):
            if open == close == n:
                res.append("".join(subset))
                return
            
            if open <= n:
                subset.append('(')
                backtrack(open+1,close)
                subset.pop()
            
            if open > close:
                subset.append(')')
                backtrack(open,close+1)
                subset.pop()
            
        backtrack(0,0)
        return res