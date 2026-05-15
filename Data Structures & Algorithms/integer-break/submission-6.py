class Solution:
    def integerBreak(self, n: int) -> int:
        cache = [1] * (n+1)

        for t in range(1, n + 1):
            for i in range(1, t + 1):
                if i == n:
                    break
                cache[t] = max(cache[t], i * cache[t - i])

        return cache[n]

        