class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for l in range(n-1,-1,-1):
            for r in range(l,n):
                even = (r - l) % 2 == 0
                left = piles[l] if even else 0
                right = piles[r] if even else 0
                if l == r:
                    dp[l][r] = left
                else:
                    dp[l][r] = max(dp[l + 1][r] + left, dp[l][r - 1] + right)
        
        # def dfs(l, r):
        #     if l > r:
        #         return 0
        #     if (l, r) in dp:
        #         return dp[(l, r)]
        #     even = (r - l) % 2 == 1
        #     left = piles[l] if even else 0
        #     right = piles[r] if even else 0
        #     dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
        #     return dp[(l, r)]

        total = sum(piles)
        # alice_score = dfs(0, len(piles) - 1)
        return dp[0][n-1] > total - dp[0][n-1]