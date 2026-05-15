class Solution:
    def integerBreak(self, n: int) -> int:
        cache = [1] * (n+1)

        # for t in range(1, n+1):
        #     for i in (1,t+1):
        #         if i == n:
        #             break
        #         cache[t] = max(cache[t],  i*cache[t-i])
        # return cache[n]


        def dfs(target):
            if target == 0:
                return 1

            if cache[target] != 1:
                return cache[target]
            
            res = 1
            for i in range(1,target+1):
                if i == n:
                    break
                res = max(res, i*dfs(target-i)) 
            cache[target] = res
            return res
    
        return dfs(n)

