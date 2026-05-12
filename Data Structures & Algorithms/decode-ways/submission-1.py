class Solution:
    def numDecodings(self, s: str) -> int:

        cache = [-1] * (len(s)+1)
        cache[len(s)] = 1

        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                cache[i] = 0
            else:
                cache[i] = cache[i+1]

            if i < len(s)-1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456'):
                    cache[i] = cache[i] + cache[i+2]
            
        return cache[0]


        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]

        #     res = dfs(i + 1)
        #     if i < len(s) - 1:
        #         if (s[i] == '1' or
        #            (s[i] == '2' and s[i + 1] < '7')):
        #             res += dfs(i + 2)
            
        #     cache[i] = res
        #     return res

        # return dfs(0)