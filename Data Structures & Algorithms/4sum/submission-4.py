class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def kSum(index: int, k: int, subset: List[int], t: int):
            if k <= 2:
                l = index
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == t:
                        subset.append(nums[l])
                        subset.append(nums[r])
                        res.append(subset.copy())
                        subset.pop()
                        subset.pop()
                        l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif nums[l] + nums[r] > t:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    else:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                return 
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                kSum(i+1, k-1, subset, t-nums[i])
                subset.pop()

        nums.sort()
        kSum(0,4,[],target)
        return res