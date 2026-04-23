class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(sentence,i,j):
            if j == len(s):
                if i == j:
                    res.append(sentence[:-1])
                return

            if s[i:j+1] in wordDict:
                sentence += s[i:j+1]
                sentence += " "
                dfs(sentence, j+1, j+1)
                sentence = sentence[:-(j-i+2)]
            
            dfs(sentence,i,j+1)
        
        dfs("",0,0)
        return res
