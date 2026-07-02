class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        ans = []

        def backtrack(open ,close):
            if open == close == n:
                res.append(''.join(ans))
                return 
            
            if open < n:
                ans.append('(')
                backtrack(open+1,close)
                ans.pop()
            if open > close:
                ans.append(')')
                backtrack(open,close+1)
                ans.pop()
        backtrack(0,0)
        return res