class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                r -= 1
            if l > r: break
            m = (l+r)//2
            if nums[m] == target : return True
            if nums[m] >= nums[l]:
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
        return False