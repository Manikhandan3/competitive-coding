class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True 

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i < len(s1) and s1[i] == s3[i+j]:
                    dp[i][j] = dp[i + 1][j]
                if not dp[i][j] and j < len(s2) and s2[j] == s3[i+j]:
                    dp[i][j] = dp[i][j + 1]
        return dp[0][0]

        # def dfs(i, j, k):
        #     if k == len(s3):
        #         return (i == len(s1)) and (j == len(s2))
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     res = 0
        #     if i < len(s1) and s1[i] == s3[k]:
        #         res = dfs(i + 1, j, k + 1)
        #     if not res and j < len(s2) and s2[j] == s3[k]:
        #         res = dfs(i, j + 1, k + 1)

        #     dp[i][j] = res
        #     return res

        # return False if dfs(0, 0, 0) == 0 else True