class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 
        r = len(nums)-1
        while l<=r :
            while l<=r and nums[r] == val:
                r-=1;
            if l<=r and nums[l] == val:
                nums[l] = nums[r]
                l+=1
                r-=1
            else:
                l+=1
        return r+1
            
            
            
