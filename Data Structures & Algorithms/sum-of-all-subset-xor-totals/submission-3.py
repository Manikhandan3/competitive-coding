class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, subset):
            nonlocal res

            if i >= len(nums):
                xorr = 0
                for num in subset:
                    xorr ^= num
                res += xorr
                return

            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res