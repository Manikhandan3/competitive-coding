class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)

        nums.sort()
        backtrack(0, [])
        return res