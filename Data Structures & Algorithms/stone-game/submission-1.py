class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l,r,player):
            if l > r:
                return 0
            
            if (l,r,player) in dp:
                return dp[(l,r,player)]
            
            res = 0
            if player == 0:
                res = max(piles[l] + dfs(l+1,r,1), piles[r] + dfs(l,r-1,1))
            else:
                res = min(-piles[l] + dfs(l+1,r,0), -piles[r] + dfs(l,r-1,0))
            dp[(l,r,player)] = res
            return res
        
        return dfs(0,len(piles)-1,0) > 0 
