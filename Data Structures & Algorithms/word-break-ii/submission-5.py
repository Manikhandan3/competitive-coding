class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        subset = []

        def dfs(i):
            if i == len(s):
                res.append(" ".join(subset))
                return 
            
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    subset.append(word)
                    dfs(i + len(word))
                    subset.pop()
        
        dfs(0)
        return res