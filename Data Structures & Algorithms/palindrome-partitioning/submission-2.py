class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []
        subset = []

        def backtrack(i,j):
            if i == len(s):
                res.append(subset.copy())
                return
            
            if j == len(s):
                return 
            
            if isPalindrome(i,j):
                subset.append(s[i:j+1])
                backtrack(j+1,j+1)
                subset.pop()
            
            backtrack(i,j+1)
        
        backtrack(0,0)
        return res
        