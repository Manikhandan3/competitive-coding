class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        cache = [float('inf')] * (amount+1)
        cache[0] = 0

        for i in range(1,amount+1):
            for c in coins:
                if i - c >= 0 and cache[i - c] != float('inf'):
                    cache[i] = min(cache[i], 1 + cache[i-c])
        
        return -1 if cache[amount] == float('inf') else cache[amount]


        # def dfs(amount):
        #     if amount == 0:
        #         return 0
            
        #     if cache[amount] != -1:
        #         return cache[amount]

        #     res = float('inf')
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     cache[amount] = res
        #     return res

        # minCoins = dfs(amount)
        # return -1 if minCoins == float('inf') else minCoins