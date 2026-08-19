class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        st = []
        for d in s:
            if not d or d == '.':
                continue
            if d == "..":
                if st:
                    st.pop()
            else:
                st.append(d)
        return '/' if len(st) == 0 else "/"+"/".join(st)