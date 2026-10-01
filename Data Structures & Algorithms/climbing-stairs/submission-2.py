class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        cache[0] = 1

        def dfs(i):
            if i < 0:
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]

        return dfs(n)