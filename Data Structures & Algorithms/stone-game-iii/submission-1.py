class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        cache = [[None] * 2 for _ in range(n+1)]
        cache[n][1], cache[n][0] = 0, 0

        for i in range(n-1,-1,-1):
            for player in range(2):
                cache[i][player] = float('-inf') if player == 0 else float('inf')
                score = 0
                for j in range(i, min(i+3,n)):
                    if player == 0:
                        score += stoneValue[j]
                        cache[i][0] = max(cache[i][0], score + cache[j+1][1])
                    else:
                        score -= stoneValue[j]
                        cache[i][1] = min(cache[i][1], score + cache[j+1][0])
        res = cache[0][0]
        print(cache)
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"



        # def dfs(i, player):
        #     if i == n:
        #         return 0
            
        #     res = float('-inf') if player == 1 else float('inf')
        #     score = 0
        #     for j in range(i,min(n,i+3)):
        #         if player == 1:
        #             score += stoneValue[j]
        #             res = max(res, score + dfs(j+1,0)) 
        #         else:
        #             score -= stoneValue[j]
        #             res = min(res, score + dfs(j+1,1))

        #     cache[i][player] = res
        #     return res

        # res = dfs(0,1)
        # if res == 0:
        #     return "Tie"
        # return "Alice" if res > 0 else "Bob"