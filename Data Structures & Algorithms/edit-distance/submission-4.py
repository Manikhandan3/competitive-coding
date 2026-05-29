class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * (len(word2)+1) for _ in range(len(word1)+1)]
        # for i in range(len(word1)) 

        # for i in range(len(word1)-1,-1,-1):
        #     for j in range(len(word2)-1,-1,-1):
        #         if word1[i] == word2[j]:
        #             dp[i][j] = dp[i+1][j+1]
        #         else:
        #             dp[i][j] = min(1 + dp[i+1][j],1 + dp[i][j+1], 1 + dp[i+1][j+1])
        # return dp[0][0]

        def dfs(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i 
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = dfs(i+1,j+1)
                return dp[i][j]
            dp[i][j] = min(1 + dfs(i+1,j),1 + dfs(i,j+1), 1 + dfs(i+1,j+1))
            return dp[i][j]
        
        return dfs(0,0)