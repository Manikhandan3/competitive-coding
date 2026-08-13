class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = (len(nums) + 1) * -1
            else:
                nums[i] *= -1
        
        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                cur = abs(nums[i])-1
                nums[cur] = nums[cur]*-1 if nums[cur] < 0 else nums[cur]

        for i in range(len(nums)):
            if nums[i] < 0:
                return i + 1
        
        return len(nums) + 1
        

