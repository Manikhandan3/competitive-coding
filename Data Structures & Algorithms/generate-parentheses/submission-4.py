class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open ,close, ans):
            if open == close == n:
                res.append(''.join(ans))
                return 
            
            if open < n:
                ans.append('(')
                backtrack(open+1,close,ans)
                ans.pop()
            if open > close:
                ans.append(')')
                backtrack(open,close+1,ans)
                ans.pop()
        backtrack(0,0,[])
        return res