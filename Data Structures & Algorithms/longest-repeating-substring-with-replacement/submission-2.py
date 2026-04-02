class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        m = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            m = max(m,count[s[r]])
            if r-l+1-m > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res

