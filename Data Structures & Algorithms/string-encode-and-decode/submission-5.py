class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        sizes = []
        l, r = 0, 0

        while s[r] != '#':
            if s[r] == ',':
                sizes.append(int(s[l:r]))
                r += 1
                l = r
            else:
                r += 1

        l += 1
        for size in sizes:
            res.append(s[l:l+size])
            l += size
        return res 
