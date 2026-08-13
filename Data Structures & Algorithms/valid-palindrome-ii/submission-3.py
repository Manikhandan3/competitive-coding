class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPal(word: str) -> bool:
            l, r = 0, len(word)-1
            while l < r:
                if word[l] != word[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        if isPal(s): 
            return True
        l, r = 0, len(s) - 1
        while s[l] == s[r]:
            l += 1
            r -= 1
        return isPal(s[l:r]) or isPal(s[l+1:r+1])



        
        