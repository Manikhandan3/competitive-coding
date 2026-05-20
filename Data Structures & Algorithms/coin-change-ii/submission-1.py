class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = [[0] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            memo[i][0] = 1
        
        for i in range(len(coins)-1,-1,-1):
            for t in range(1,amount+1):
                res = 0
                for j in range(i,len(coins)):
                    if t - coins[j] >= 0:
                        res += memo[j][t - coins[j]]
                memo[i][t] = res
        return memo[0][amount]
        # def dfs(i,total):
        #     if memo[i][total] != -1:
        #         return memo[i][total]
        #     res = 0
        #     for j in range(i,len(coins)):
        #         if total - coins[j] >= 0:
        #             res += dfs(j,total - coins[j])
        #     memo[i][total] = res
        #     return res
        
        # return dfs(0,amount)
