class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}
        for i in range(len(nums)):
            if target - nums[i] in preMap:
                return [preMap[target-nums[i]],i]
            preMap[nums[i]] = i