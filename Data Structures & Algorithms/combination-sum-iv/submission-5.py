class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        cache = [0] * (target+1)
        cache[0] = 1

        for t in range(1,target+1):
            for num in nums:
                if t >= num:
                    cache[t] += cache[t-num]
        return cache[target]

        # def dfs(total):
        #     if cache[total]!=-1:
        #         return cache[total]
            
        #     res = 0
        #     for i in range(len(nums)):
        #         if total < nums[i]:
        #             break
        #         res += dfs(total - nums[i])
        #         cache[total] = res
        #     return res
        
        # return dfs(target)