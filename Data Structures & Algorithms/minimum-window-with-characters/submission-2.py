class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or t == "":
            return ""
        count = {}
        for c in t:
            count[c] = count.get(c,0) + 1
        window = {}
        need = len(count)
        have = 0 
        l = 0
        reslen = float('infinity')
        res = [-1,-1]
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in count and count[s[r]]==window[s[r]]:
                have += 1
            while need == have:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r - l + 1
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float('infinity') else ""