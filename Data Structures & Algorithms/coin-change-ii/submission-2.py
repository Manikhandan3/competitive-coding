class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = [[-1] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            memo[i][0] = 1
        
        def dfs(i,total):
            if i == len(coins):
                return 0
            
            if total < 0:
                return 0

            if memo[i][total] != -1:
                return memo[i][total]
            

            res = dfs(i+1, total)
            res += dfs(i, total - coins[i])
            memo[i][total] = res
            return res
        
        return dfs(0,amount)
