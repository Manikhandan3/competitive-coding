class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        cache = set()
        cache.add(0)

        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for t in cache:
                if  (t + nums[i]) == half:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            cache = nextDp
        return False

        # def dfs(i,s):
        #     if s in cache:
        #         return True
            
        #     if s < 0:
        #         return False
            
        #     if i == len(nums):
        #         return False
            
        #     if dfs(i+1,s-nums[i]):
        #         cache.add(s - nums[i])
        #         return True
            
        #     if dfs(i+1,s):
        #         cache.add(s)
        #         return True
            
        #     return False
        
        # return dfs(0,half)