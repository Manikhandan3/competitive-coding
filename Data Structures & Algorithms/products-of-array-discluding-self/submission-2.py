class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        p = 1
        for num in nums:
            if num == 0:
                count += 1
            else:
                p *= num
        if count > 1:
            return [0]*len(nums)
        
        res = [0]*len(nums)
        for i,c in enumerate(nums):
            if count: res[i] = 0 if c else p
            else: res[i] = p//c
        return res

