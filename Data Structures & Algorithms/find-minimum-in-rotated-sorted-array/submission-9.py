class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float('inf')
        while l <= r:
            m = (l+r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            if nums[m] >= nums[l] and nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m 
        return res