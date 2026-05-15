class Solution:
    def numSquares(self, n: int) -> int:
        
        cache = [n] * (n+1)
        cache[0] = 0

        for t in range(1,n+1):
            for i in range(t):
                if i*i <= t:
                    cache[t] = min(cache[t], 1 + cache[t-i*i])
        return cache[n]
        # def dfs(target):
        #     if target in memo:
        #         return memo[target]
        #     res = target
        #     for i in range(1,target):
        #         if (i*i) > target:
        #             break
        #         res = min(res,1+dfs(target-(i*i)))
        #     cache[target] = res
        #     return res
            
        # return dfs(n)