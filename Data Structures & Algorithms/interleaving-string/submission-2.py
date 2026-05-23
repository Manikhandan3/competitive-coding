class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = {}
        dp[(l1,l2,0)], dp[(l1,l2,1)] = True, True

        def dfs(i,j,t):
            if (i,j,t) in dp:
                return dp[(i,j,t)]
            
            if i == l1 and t == 0:
                return False
            
            if j == l2 and t == 1:
                return False
            
            if t == 0 and s1[i] == s3[i+j]:
                dp[(i,j,t)] = dfs(i+1,j,1) or dfs(i+1,j,0)
                return dp[(i,j,t)]
            
            if t == 1 and s2[j] == s3[i+j]:
                dp[(i,j,t)] = dfs(i,j+1,0) or dfs(i,j+1,1)
                return dp[(i,j,t)]

            dp[(i,j,t)] = False
            return dp[(i,j,t)]
        
        return dfs(0,0,0) or dfs(0,0,1)