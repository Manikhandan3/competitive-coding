class Solution:
    def isValid(self, s: str) -> bool:
        preMap = {}
        preMap['}'] = '{'
        preMap[']'] = '['
        preMap[')'] = '('
        st = []
        for c in s:
            if c in preMap:
                if not st or st[-1] != preMap[c]:
                    return False
                st.pop()
            else:
                st.append(c)
        return True if len(st) == 0 else False