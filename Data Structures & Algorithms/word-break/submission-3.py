class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [-1] * len(s)
        def dfs(i):

            if i == len(s):
                return True
            
            if cache[i] != -1:
                return True if cache[i] == 1 else False

            for w in wordDict:
                if ((i + len(w)) <= len(s) and
                     s[i : i + len(w)] == w
                ):
                    cache[i] = 1
                    if dfs(i + len(w)):
                        return True
            cache[i] = 0
            return False

        return dfs(0)