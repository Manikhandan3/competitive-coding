class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = min(heights[l],heights[r])*(r-l)
        while l < r:
            area = 0
            if heights[l] > heights[r]:
                r -= 1
                area = min(heights[l],heights[r])*(r-l)
            else:
                l += 1
                area = min(heights[l],heights[r])*(r-l)
            res = max(res,area)
        return res