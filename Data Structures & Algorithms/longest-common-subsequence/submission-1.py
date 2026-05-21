class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == len(text1) or j == len(text2):
                    dp[i][j] = 0 
        
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            for k in range(j,len(text2)):
                if text1[i] == text2[k]:
                    res = max(res, 1 + dfs(i+1,k+1))
            res = max(dfs(i+1,j),res)
            dp[i][j] = res
            return res
        
        return dfs(0,0)