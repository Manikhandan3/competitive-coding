class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        res = 0
        for i in range(len(heights)+1):
            while st and ( i == len(heights) or heights[i] <= heights[st[-1]]):
                h = heights[st.pop()]
                l = i if not st else i - st[-1] -1
                res = max(res, h*l)
            st.append(i)
        return res