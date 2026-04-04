class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)+1):
            while stack and (i == len(heights) or heights[i]<=heights[stack[-1]]):
                h = heights[stack.pop()]
                l = i if not stack else  i - 1 - stack[-1]
                res = max(res, h*l)
            stack.append(i)
        return res
