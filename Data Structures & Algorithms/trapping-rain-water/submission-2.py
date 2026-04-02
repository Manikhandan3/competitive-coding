class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[len(height)-1]
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            if maxL > maxR:
                r -= 1
                maxR = max(maxR,height[r])
                res += maxR - height[r]
            else :
                l += 1
                maxL = max(maxL,height[l])
                res += maxL - height[l]
        return res
        