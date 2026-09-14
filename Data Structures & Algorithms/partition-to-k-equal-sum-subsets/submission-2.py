class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        length = sum(nums)
        if length % k:
            return False
        length = length // k
        sides = [0] * k
        nums.sort(reverse=True)
        if nums[0] > length:
            return False

        def backtrack(i):
            if i == len(nums):
                temp = sides[0]
                for s in sides:
                    if s != temp:
                        return False
                return True

            for side in range(k):
                if sides[side] + nums[i] > length:
                    continue
                sides[side] += nums[i]
                if backtrack(i+1):
                    return True
                sides[side] -= nums[i]
                if sides[side] == 0:
                    break
            return False
        
        return backtrack(0)