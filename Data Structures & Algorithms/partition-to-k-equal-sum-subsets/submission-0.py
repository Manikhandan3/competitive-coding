class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_length = sum(nums)
        if total_length % k != 0:
            return False

        length = total_length // k
        sides = [0] * k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True

            for side in range(k):
                if sides[side] + nums[i] <= length:
                    sides[side] += nums[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= nums[i]

                if sides[side] == 0:
                     break

            return False

        return dfs(0)