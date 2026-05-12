class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(len(word)):
            for j in range(1,len(strs)):
                if len(strs[j]) <= i or word[i] != strs[j][i]:
                    return word[:i]
        return word