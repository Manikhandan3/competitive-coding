class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0 = 0
        n1 = 0
        n2 = 0
        for num in nums:
            if num == 0:
                nums[n2] = 2
                nums[n1] = 1  
                nums[n0] = 0
                n2 += 1
                n1 += 1
                n0 += 1
            elif num == 1:
                nums[n2] = 2
                nums[n1] = 1  
                n2 += 1
                n1 += 1
            else:
                nums[n2] = 2
                n2 += 1
        
