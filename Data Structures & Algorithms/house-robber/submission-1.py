class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * (len(nums)+3)
        
        for i in range(len(cache)-4,-1,-1):
            cache[i] = nums[i] + max(cache[i+2],cache[i+3])
        
        return max(cache[1],cache[0])
        