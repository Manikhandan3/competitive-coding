class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # def dfs(i,j,parent):
        #     if i == len(s):
        #         if j == len(p):
        #             return True
        #         elif j < len(p) - 1 and p[j+1] == '*':
        #             return dfs(i,j+2,parent)
        #         elif j == len(p) - 1 and p[j] == '*':
        #             return True
            
        #     if i == len(s) or j == len(p):
        #         return False
            
        #     if s[i] == p[j] or p[j] == '.':
        #         if j < len(p) - 1 and p[j+1] == '*':
        #             return dfs(i,j+2,parent) or dfs(i+1,j+1,p[j]) 
        #         return dfs(i+1,j+1,p[j]) 
        #     elif p[j] == '*':
        #         if parent == '.':
        #             return dfs(i,j+1,parent) or dfs(i+1,j,parent) or dfs(i+1,j+1,parent)
        #         else:
        #             if s[i] == parent:
        #                 return dfs(i,j+1,parent) or dfs(i+1,j,parent) or dfs(i+1,j+1,parent)
        #             else:
        #                 return dfs(i,j+1,parent)
        #     elif j < len(p) - 1 and p[j+1] == '*':
        #         return dfs(i,j+2,parent)
        #     else:
        #         return False
        
        # return dfs(0,0,'*')
        dp = [[-1] * len(p) for _ in range(len(s))]
        def dfs(i,j):
            if i == len(s):
                if j == len(p):
                    return True
                elif j < len(p) - 1 and p[j+1] == '*':
                    return dfs(i,j+2)
                elif j == len(p) - 1 and p[j] == '*':
                    return True
            
            if i == len(s) or j == len(p):
                return False
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == p[j] or p[j] == '.':
                if j < len(p) - 1 and p[j+1] == '*':
                    dp[i][j] = dfs(i,j+2) or dfs(i+1,j+1)
                    return dp[i][j]
                dp[i][j] = dfs(i+1,j+1) 
                return dp[i][j]
            elif p[j] == '*':
                if p[j-1] == '.':
                    dp[i][j] = dfs(i,j+1) or dfs(i+1,j) or dfs(i+1,j+1)
                    return dp[i][j]
                else:
                    if s[i] == p[j-1]:
                        dp[i][j] = dfs(i,j+1) or dfs(i+1,j) or dfs(i+1,j+1)
                        return dp[i][j]
                    else:
                        dp[i][j] = dfs(i,j+1)
                        return dfs(i,j+1)
            elif j < len(p) - 1 and p[j+1] == '*':
                dp[i][j] = dfs(i,j+2)
                return dp[i][j]
            else:
                dp[i][j] = False
                return dp[i][j] 
        
        return dfs(0,0)