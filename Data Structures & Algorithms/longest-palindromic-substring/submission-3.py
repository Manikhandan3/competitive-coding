class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0] * 2
        count = 0
        for i in range(1,len(s)):
            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > count:
                    count = r - l
                    res = [l,r]
                l -= 1
                r += 1
            
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > count:
                    count = r - l
                    res = [l,r]
                l -= 1
                r += 1
        
        return s[res[0]:res[1]+1]
            
