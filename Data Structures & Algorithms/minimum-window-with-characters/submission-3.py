class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = defaultdict(int)
        for c in t:
            count[c] += 1
        need = len(count)
        have = 0
        l = 0
        minL = float('inf')
        res = [-1,-1]
        window = defaultdict(int)
        for r in range(len(s)): 
            window[s[r]] += 1
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < minL:
                    minL = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        return "" if minL == float('inf') else s[res[0]:res[1]+1]

