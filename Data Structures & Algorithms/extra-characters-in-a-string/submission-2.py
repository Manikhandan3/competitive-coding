class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        res = len(s)
        dictionary = set(dictionary)

        def dfs(i, count):
            nonlocal res

            if i == len(s):
                res = min(res, len(s) - count)
                return 

            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    if i-count < res:
                        dfs(j+1,count+j-i+1)
            
            dfs(i+1,count)
        
        dfs(0,0)
        return res
                
